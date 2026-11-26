import json
import unittest
from datetime import datetime
from unittest.mock import patch

from caja_pulse.__main__ import PERFILES_DEMO, generar_informe
from caja_pulse.escenarios import PropuestaNoDisponible, solicitar_propuesta, validar_propuesta
from caja_pulse.fuentes import PERU, FuenteNoDisponible, interpretar_produccion_calzado
from caja_pulse.modelo import Perfil


AHORA = datetime(2026, 11, 25, 12, tzinfo=PERU)
FUENTE = {
    "config": {"series": [{"name": "Producción manufacturera - Calzado"}]},
    "periods": [
        {"name": "Sep.2026", "values": ["11.59"]},
        {"name": "Oct.2026", "values": ["n.d."]},
        {"name": "Dic.2026", "values": ["4.00"]},
    ],
}
EVIDENCIA = interpretar_produccion_calzado(FUENTE, AHORA, "https://example.test/consulta")
PROPUESTA = {
    "evidencia_id": EVIDENCIA.id,
    "volumen_minimo_pct": -6,
    "volumen_central_pct": 0,
    "volumen_maximo_pct": 4,
    "justificacion": "Ensayar continuidad y una caída como sensibilidad.",
}


class ModeloTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.perfiles = [Perfil(**registro) for registro in json.loads(PERFILES_DEMO.read_text("utf-8"))]

    def informe(self, modo="local"):
        return generar_informe(self.perfiles, modo, AHORA, 2026, 1000)

    def test_caso_ab_y_abstencion(self):
        a, b, c = self.informe()["escenarios"][0]["resultados"]
        self.assertEqual(a["utilidad_escenario_central_pen"], 2300)
        self.assertEqual(b["utilidad_escenario_central_pen"], 1200)
        self.assertEqual(b["proporcion_escenarios_bajo_cuota"], 0)
        self.assertEqual(b["proporcion_escenarios_bajo_umbral"], 1)
        self.assertEqual(b["aumento_tolerable_insumos_pct"], 1.92)
        self.assertEqual(c["estado"], "sin_simulacion_individual")
        self.assertEqual(c["campos_faltantes"], ["ventas"])
        self.assertNotIn("utilidad_escenario_central_pen", c)

    def test_monte_carlo_reproducible(self):
        uno, dos = self.informe(), self.informe()
        self.assertEqual(uno, dos)
        a, b, _ = uno["escenarios"][1]["resultados"]
        self.assertGreater(b["proporcion_escenarios_bajo_umbral"], a["proporcion_escenarios_bajo_umbral"])

    def test_periodo_valido_y_fuente_vencida(self):
        self.assertEqual(EVIDENCIA.periodo, "2026-09")
        self.assertEqual(EVIDENCIA.valor, 11.59)
        with self.assertRaises(FuenteNoDisponible):
            interpretar_produccion_calzado(FUENTE, datetime(2027, 6, 1, tzinfo=PERU), "https://example.test/consulta")

    def test_valida_cita_orden_y_limites_del_llm(self):
        self.assertEqual(validar_propuesta(PROPUESTA, EVIDENCIA).origen, "propuesta_llm")
        for cambios in (
            {"evidencia_id": "fuente-inventada"},
            {"volumen_central_pct": 9},
            {"volumen_minimo_pct": -16},
            {"volumen_minimo_pct": float("nan")},
            {"precio_insumos_pct": 4},
        ):
            with self.subTest(cambios=cambios), self.assertRaises(PropuestaNoDisponible):
                validar_propuesta({**PROPUESTA, **cambios}, EVIDENCIA)

    @patch("caja_pulse.__main__.obtener_produccion_calzado", return_value=EVIDENCIA)
    @patch("caja_pulse.__main__.solicitar_propuesta", side_effect=PropuestaNoDisponible("Sin credenciales."))
    def test_fallback_de_llm(self, llm, fuente):
        informe = self.informe("llm")
        self.assertEqual(informe["escenarios"][-1]["origen"], "reglas_con_contexto")
        self.assertIsNone(informe["llm"])
        self.assertIn("Sin credenciales", informe["avisos"][0])
        llm.assert_called_once_with(EVIDENCIA)
        fuente.assert_called_once_with(AHORA)

    @patch("caja_pulse.__main__.obtener_produccion_calzado", side_effect=FuenteNoDisponible("Sin señal actual."))
    @patch("caja_pulse.__main__.solicitar_propuesta")
    def test_sin_fuente_se_conservan_solo_los_escenarios_demo(self, llm, fuente):
        informe = self.informe("llm")
        self.assertEqual(len(informe["escenarios"]), 2)
        self.assertIsNone(informe["fuente_publica"])
        llm.assert_not_called()
        fuente.assert_called_once_with(AHORA)

    @patch.dict("os.environ", {"AI_GATEWAY_API_KEY": "credencial-de-prueba", "AI_GATEWAY_MODEL": "test/demo"}, clear=True)
    @patch("caja_pulse.escenarios.urlopen")
    def test_adaptador_solo_envia_datos_publicos(self, urlopen):
        respuesta = {"id": "test", "choices": [{"finish_reason": "stop", "message": {"content": json.dumps(PROPUESTA)}}]}
        urlopen.return_value.__enter__.return_value.read.return_value = json.dumps(respuesta).encode()
        escenario, registro = solicitar_propuesta(EVIDENCIA)
        solicitud = json.loads(urlopen.call_args.args[0].data)
        contenido = json.loads(solicitud["messages"][1]["content"])
        self.assertEqual(contenido["id"], EVIDENCIA.id)
        self.assertTrue({"cuota", "ventas", "perfil_id"}.isdisjoint(contenido))
        self.assertEqual(registro["respuesta_id"], "test")
        self.assertEqual(escenario.evidencia_id, EVIDENCIA.id)


if __name__ == "__main__":
    unittest.main()
