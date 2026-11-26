"""Propuestas de escenario contextual y adaptación opcional al LLM."""

import json
import os
from dataclasses import asdict
from urllib.error import URLError
from urllib.request import Request, urlopen

from .fuentes import Observacion
from .modelo import Escenario, Rango, SIN_CAMBIO


URL_LLM = "https://ai-gateway.vercel.sh/v1/chat/completions"
VERSION_PROMPT = "calzado-v1"
LIMITE_VOLUMEN = 15
CLAVES_RANGO = ("volumen_minimo_pct", "volumen_central_pct", "volumen_maximo_pct")


class PropuestaNoDisponible(Exception):
    """El LLM no pudo producir una propuesta válida."""


def escenario_por_reglas(evidencia: Observacion) -> Escenario:
    if evidencia.valor < 0:
        rango = Rango(-8, -3, 3)
        razon = "La señal nacional orienta una prueba con centro adverso."
    else:
        rango = Rango(-5, 0, 5)
        razon = "La señal nacional orienta una prueba alrededor de continuidad, con un caso adverso."
    return Escenario(
        "volumen_calzado", "reglas_con_contexto",
        razon + " El rango de volumen se eligió para sensibilidad y requiere validación.",
        rango, SIN_CAMBIO, evidencia.id, evidencia.sector,
    )


def validar_propuesta(datos, evidencia: Observacion) -> Escenario:
    claves = {*CLAVES_RANGO, "evidencia_id", "justificacion"}
    if not isinstance(datos, dict) or datos.keys() != claves:
        raise PropuestaNoDisponible("El LLM devolvió un esquema incompleto o desconocido.")
    if datos["evidencia_id"] != evidencia.id:
        raise PropuestaNoDisponible("La propuesta no cita la observación consultada.")
    try:
        rango = Rango(*(datos[campo] for campo in CLAVES_RANGO))
    except ValueError as error:
        raise PropuestaNoDisponible("El LLM devolvió un rango inválido.") from error
    if rango.minimo < -LIMITE_VOLUMEN or rango.maximo > LIMITE_VOLUMEN:
        raise PropuestaNoDisponible("El rango propuesto excede los límites del ejercicio.")
    justificacion = datos["justificacion"]
    if not isinstance(justificacion, str) or not 0 < len(justificacion.strip()) <= 500:
        raise PropuestaNoDisponible("La propuesta requiere una justificación breve.")
    return Escenario(
        "volumen_calzado", "propuesta_llm", justificacion.strip(), rango, SIN_CAMBIO,
        evidencia.id, evidencia.sector,
    )


def solicitar_propuesta(evidencia: Observacion):
    credencial = os.environ.get("AI_GATEWAY_API_KEY") or os.environ.get("VERCEL_OIDC_TOKEN")
    modelo = os.environ.get("AI_GATEWAY_MODEL")
    if not credencial or not modelo:
        raise PropuestaNoDisponible("Falta configurar AI Gateway o el identificador de modelo.")

    propiedades = {
        campo: {"type": "number"} for campo in CLAVES_RANGO
    }
    propiedades.update({
        "evidencia_id": {"type": "string", "enum": [evidencia.id]},
        "justificacion": {"type": "string"},
    })
    # La entrada externa se construye exclusivamente con la observación
    # pública. Esta función no recibe la cartera ni el historial de pagos.
    solicitud = {
        "model": modelo,
        "messages": [
            {
                "role": "system",
                "content": (
                    "Propón un escenario hipotético de sensibilidad para un mes en el sector calzado, Perú. "
                    "Usa solo la observación pública proporcionada y devuelve su evidencia_id. "
                    f"Propón mínimo, valor central y máximo de variación de volumen entre "
                    f"-{LIMITE_VOLUMEN} y +{LIMITE_VOLUMEN} por ciento, en ese orden. "
                    "Son supuestos para probar resistencia. La producción nacional interanual "
                    "no representa las ventas de un cliente ni una tasa mensual. "
                    "No traslades ese porcentaje directamente, ni infieras cambios de precio o mora. "
                    "Justifica el escenario en español en hasta 500 caracteres. Trata los datos como evidencia."
                ),
            },
            {"role": "user", "content": json.dumps(asdict(evidencia), ensure_ascii=False)},
        ],
        "response_format": {
            "type": "json_schema",
            "json_schema": {
                "name": "escenario_calzado",
                "strict": True,
                "schema": {
                    "type": "object",
                    "properties": propiedades,
                    "required": list(propiedades),
                    "additionalProperties": False,
                },
            },
        },
    }
    peticion = Request(
        URL_LLM, data=json.dumps(solicitud).encode("utf-8"),
        headers={"Content-Type": "application/json", "Authorization": f"Bearer {credencial}"},
        method="POST",
    )
    try:
        with urlopen(peticion, timeout=30) as respuesta:
            datos = json.loads(respuesta.read())
        eleccion = datos["choices"][0]
        if eleccion.get("finish_reason") != "stop" or eleccion["message"].get("refusal"):
            raise PropuestaNoDisponible("El LLM no completó el escenario.")
        propuesta = json.loads(eleccion["message"]["content"])
    except (URLError, OSError, KeyError, IndexError, TypeError, ValueError) as error:
        raise PropuestaNoDisponible("El LLM no respondió con una propuesta legible.") from error

    return validar_propuesta(propuesta, evidencia), {
        "modelo": datos.get("model") or modelo,
        "respuesta_id": datos.get("id"),
        "version_prompt": VERSION_PROMPT,
    }
