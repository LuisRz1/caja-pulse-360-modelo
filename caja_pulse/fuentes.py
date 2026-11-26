"""Indicadores públicos con periodo, cobertura y procedencia."""

import calendar
import json
import math
from dataclasses import dataclass
from datetime import date, datetime, timedelta, timezone
from urllib.error import URLError
from urllib.request import urlopen


PERU = timezone(timedelta(hours=-5), "PET")
BCRP = "https://estadisticas.bcrp.gob.pe/estadisticas/series"
SERIE_CALZADO = "PN01927AM"
MESES = ("Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic")


class FuenteNoDisponible(Exception):
    """La fuente no ofrece un dato apto para el escenario contextual."""


@dataclass(frozen=True)
class Observacion:
    id: str
    serie: str
    indicador: str
    periodo: str
    valor: float
    unidad: str
    cobertura: str
    sector: str
    fuente: str
    enlace: str
    consulta: str
    fecha_consulta: str


def obtener_produccion_calzado(ahora: datetime) -> Observacion:
    corte = ahora.astimezone(PERU).date()
    inicio = corte.replace(day=1) - timedelta(days=180)
    url = f"{BCRP}/api/{SERIE_CALZADO}/json/{inicio.year}-{inicio.month}/{corte.year}-{corte.month}/esp"
    try:
        with urlopen(url, timeout=15) as response:
            datos = json.loads(response.read())
        return interpretar_produccion_calzado(datos, ahora, url)
    except (URLError, OSError, KeyError, TypeError, ValueError) as error:
        raise FuenteNoDisponible("BCRPData no respondió con una observación válida.") from error


def interpretar_produccion_calzado(datos: dict, ahora: datetime, consulta: str) -> Observacion:
    fecha = ahora.astimezone(PERU)
    corte = fecha.date()
    serie = datos["config"]["series"]
    if len(serie) != 1 or not serie[0]["name"].endswith(" - Calzado"):
        raise FuenteNoDisponible("La respuesta no corresponde a la serie configurada de calzado.")

    disponibles = {}
    for registro in datos["periods"]:
        mes, anio = registro["name"].split(".")
        periodo = date(int(anio), MESES.index(mes) + 1, 1)
        fin = periodo.replace(day=calendar.monthrange(periodo.year, periodo.month)[1])
        if fin > corte:
            continue
        try:
            valor = float(registro["values"][0])
        except (ValueError, TypeError, IndexError):
            continue
        if math.isfinite(valor):
            disponibles[fin] = valor

    if not disponibles or (corte - max(disponibles)).days > 90:
        raise FuenteNoDisponible("La serie no tiene un dato mensual válido con antigüedad de hasta 90 días.")
    fin = max(disponibles)
    periodo = f"{fin:%Y-%m}"
    return Observacion(
        id=f"bcrp-{SERIE_CALZADO}-{periodo}",
        serie=SERIE_CALZADO,
        indicador="Producción manufacturera de calzado",
        periodo=periodo,
        valor=disponibles[fin],
        unidad="variación porcentual interanual",
        cobertura="Perú",
        sector="calzado",
        fuente="BCRPData",
        enlace=f"{BCRP}/mensuales/resultados/{SERIE_CALZADO}",
        consulta=consulta,
        fecha_consulta=fecha.isoformat(timespec="seconds"),
    )
