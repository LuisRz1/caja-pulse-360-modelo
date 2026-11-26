"""Entrada local para ejecutar la comparación y guardar sus resultados."""

import argparse
import json
import sys
from dataclasses import asdict
from datetime import datetime
from pathlib import Path

import numpy as np

from .escenarios import PropuestaNoDisponible, escenario_por_reglas, solicitar_propuesta
from .fuentes import PERU, FuenteNoDisponible, obtener_produccion_calzado
from .modelo import CASO_AB, ESTRES_INSUMOS, Perfil, evaluar_cartera


PERFILES_DEMO = Path(__file__).resolve().parent.parent / "perfiles-sinteticos.json"


def generar_informe(perfiles, modo, ahora, semilla, muestras):
    escenarios = [CASO_AB, ESTRES_INSUMOS]
    evidencia = None
    metadatos_llm = None
    avisos = []
    if modo != "local":
        try:
            evidencia = obtener_produccion_calzado(ahora)
        except FuenteNoDisponible as error:
            avisos.append(str(error))
        if evidencia is not None:
            contextual = escenario_por_reglas(evidencia)
            if modo == "llm":
                try:
                    contextual, metadatos_llm = solicitar_propuesta(evidencia)
                except PropuestaNoDisponible as error:
                    avisos.append(f"{error} Se usó el escenario contextual por reglas.")
            escenarios.append(contextual)

    corte = ahora.astimezone(PERU).date()
    return {
        "version_informe": 1,
        "modo_solicitado": modo,
        "fecha_corte": corte.isoformat(),
        "muestras_por_escenario": muestras,
        "semilla": semilla,
        "numpy": np.__version__,
        "nota": "Resultados condicionados a supuestos de sensibilidad. Requieren revisión humana.",
        "fuente_publica": asdict(evidencia) if evidencia is not None else None,
        "llm": metadatos_llm,
        "avisos": avisos,
        "escenarios": [
            {
                **asdict(escenario),
                "resultados": evaluar_cartera(perfiles, escenario, corte, semilla, muestras),
            }
            for escenario in escenarios
        ],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--modo", choices=("local", "publico", "llm"), default="local")
    parser.add_argument("--muestras", type=int, default=1000)
    parser.add_argument("--semilla", type=int, default=2026)
    parser.add_argument("--perfiles", type=Path, default=PERFILES_DEMO)
    parser.add_argument("--salida", type=Path, help="Guardar el informe JSON en UTF-8.")
    args = parser.parse_args()
    if not 1 <= args.muestras <= 100_000 or args.semilla < 0:
        parser.error("Usa de 1 a 100.000 muestras y una semilla no negativa.")
    try:
        datos = json.loads(args.perfiles.read_text(encoding="utf-8-sig"))
        if not isinstance(datos, list) or not datos:
            raise ValueError("El archivo debe contener una lista de perfiles.")
        perfiles = [Perfil(**registro) for registro in datos]
        if len({perfil.id for perfil in perfiles}) != len(perfiles):
            raise ValueError("Cada perfil requiere un identificador único.")
    except (OSError, TypeError, ValueError) as error:
        parser.error(f"Perfiles inválidos. {error}")

    informe = generar_informe(perfiles, args.modo, datetime.now(PERU), args.semilla, args.muestras)
    texto = json.dumps(informe, indent=2, ensure_ascii=False, allow_nan=False) + "\n"
    if args.salida:
        args.salida.write_text(texto, encoding="utf-8")
    else:
        sys.stdout.reconfigure(encoding="utf-8")
        print(texto, end="")


if __name__ == "__main__":
    main()
