"""Simula la resistencia mensual y señala dónde falta evidencia individual."""

from dataclasses import dataclass
from datetime import date
from math import isfinite
from typing import Optional

import numpy as np


def numero_valido(valor) -> bool:
    return type(valor) in (float, int) and isfinite(valor)


@dataclass(frozen=True)
class Perfil:
    id: str
    sector: str
    zona: str
    cuota: float
    fcp: Optional[float]
    fecha_evaluacion: Optional[str]
    ventas: Optional[float]
    costos_variables: Optional[float]
    otros_gastos_obligaciones: Optional[float]

    def __post_init__(self):
        if not all(isinstance(x, str) and x.strip() for x in (self.id, self.sector, self.zona)):
            raise ValueError("El perfil requiere identificador, sector y zona.")
        if not numero_valido(self.cuota) or self.cuota <= 0:
            raise ValueError("La cuota debe ser un importe positivo.")
        if self.fcp is not None and (not numero_valido(self.fcp) or not 0 < self.fcp < 1):
            raise ValueError("El FCP debe estar entre 0 y 1, o ser nulo si falta.")
        if self.fecha_evaluacion is not None:
            date.fromisoformat(self.fecha_evaluacion)
        for campo in ("ventas", "costos_variables", "otros_gastos_obligaciones"):
            valor = getattr(self, campo)
            if valor is not None and (not numero_valido(valor) or valor < 0):
                raise ValueError(f"{campo} debe ser un importe no negativo o nulo.")

    @property
    def umbral(self):
        return self.cuota / self.fcp if self.fcp is not None else None


@dataclass(frozen=True)
class Rango:
    minimo: float
    central: float
    maximo: float

    def __post_init__(self):
        if not all(numero_valido(x) for x in (self.minimo, self.central, self.maximo)):
            raise ValueError("El rango requiere tres números finitos.")
        if not -100 <= self.minimo <= self.central <= self.maximo:
            raise ValueError("El rango requiere mínimo ≤ central ≤ máximo y mínimo ≥ −100 %.")

    def muestra(self, rng, cantidad):
        if self.minimo == self.maximo:
            return np.full(cantidad, self.central / 100)
        return rng.triangular(self.minimo, self.central, self.maximo, cantidad) / 100


SIN_CAMBIO = Rango(0, 0, 0)


@dataclass(frozen=True)
class Escenario:
    id: str
    origen: str
    justificacion: str
    volumen_pct: Rango
    precio_insumos_pct: Rango
    evidencia_id: Optional[str] = None
    sector: Optional[str] = None
    horizonte_meses: int = 1


CASO_AB = Escenario(
    "caso_ab", "supuesto_demo", "Aumento fijo del 10 % del costo por unidad de insumos.",
    SIN_CAMBIO, Rango(10, 10, 10), sector="calzado",
)
ESTRES_INSUMOS = Escenario(
    "estres_insumos", "supuesto_demo",
    "Rango ilustrativo de costos de insumos para probar sensibilidad.",
    SIN_CAMBIO, Rango(0, 10, 20), sector="calzado",
)


def evaluar_cartera(perfiles, escenario: Escenario, corte: date, semilla: int, muestras: int):
    """Usa las mismas muestras sectoriales para todos los perfiles comparados."""
    rng = np.random.default_rng(semilla)
    volumen = escenario.volumen_pct.muestra(rng, muestras)
    precio_insumos = escenario.precio_insumos_pct.muestra(rng, muestras)
    return [
        evaluar_perfil(perfil, escenario, corte, volumen, precio_insumos)
        for perfil in perfiles if escenario.sector is None or perfil.sector == escenario.sector
    ]


def evaluar_perfil(perfil, escenario, corte, volumen, precio_insumos):
    umbral = perfil.umbral
    resultado = {
        "perfil_id": perfil.id,
        "cuota_pen": perfil.cuota,
        "umbral_preventivo_pen": round(umbral, 2) if umbral is not None else None,
        "fecha_evaluacion": perfil.fecha_evaluacion,
    }
    campos = ("ventas", "costos_variables", "otros_gastos_obligaciones", "fecha_evaluacion")
    faltantes = [nombre for nombre in campos if getattr(perfil, nombre) is None]
    if faltantes or date.fromisoformat(perfil.fecha_evaluacion) > corte:
        return {
            **resultado,
            "estado": "sin_simulacion_individual",
            "campos_faltantes": faltantes,
            "motivo": "Evaluación parcial." if faltantes else "La evaluación es posterior al corte.",
            "revision_sugerida": "Verificar si existe una evaluación utilizable o comparables autorizados.",
        }

    inicial = perfil.ventas - perfil.costos_variables - perfil.otros_gastos_obligaciones
    # El volumen repercute tanto en ventas como en costos variables. El precio
    # de insumos se aplica sobre el costo de las unidades efectivamente vendidas.
    utilidad = np.round(
        (1 + volumen) * (perfil.ventas - perfil.costos_variables * (1 + precio_insumos))
        - perfil.otros_gastos_obligaciones, 2,
    )
    central = round(
        (1 + escenario.volumen_pct.central / 100)
        * (perfil.ventas - perfil.costos_variables * (1 + escenario.precio_insumos_pct.central / 100))
        - perfil.otros_gastos_obligaciones, 2,
    )
    p10, p50, p90 = np.quantile(utilidad, [0.1, 0.5, 0.9]).round(2).tolist()
    margen = None
    if umbral is not None and perfil.costos_variables > 0:
        margen = round(max(0, 100 * (inicial - umbral) / perfil.costos_variables), 2)
    return {
        **resultado,
        "estado": "simulado",
        "utilidad_base_pen": round(inicial, 2),
        "utilidad_escenario_central_pen": central,
        "cuota_sobre_utilidad_central_pct": round(100 * perfil.cuota / central, 2) if central > 0 else None,
        "aumento_tolerable_insumos_pct": margen,
        "utilidad_percentiles_pen": {"p10": p10, "p50": p50, "p90": p90},
        "proporcion_escenarios_bajo_umbral": float(np.mean(utilidad < umbral)) if umbral is not None else None,
        "proporcion_escenarios_bajo_cuota": float(np.mean(utilidad < perfil.cuota)),
        "revision_sugerida": sugerir_revision(perfil, escenario, central, umbral),
    }


def sugerir_revision(perfil, escenario, central, umbral):
    if central <= perfil.cuota or (umbral is not None and central < umbral):
        variable = "volumen habitual de ventas" if escenario.evidencia_id else "costo de insumos"
        return f"Revisar el {variable} y el capital de trabajo con el asesor."
    return "Revisar la vigencia de la evaluación en el seguimiento habitual."
