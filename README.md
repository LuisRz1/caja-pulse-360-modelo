# Base del modelo de CAJA PULSE 360

Simulador mensual de resistencia económica para el caso de calzado. Recibe una estructura económica fechada y el crédito. Prueba el caso A/B de la presentación, genera distribuciones con 1.000 muestras por defecto y documenta qué escenario, fuente y semilla utilizó.

## Ejecutar

Desde la carpeta de este proyecto, con Python 3.9 a 3.12.

```sh
python -m pip install -r requirements.txt
python -m caja_pulse
python -m caja_pulse --modo publico --salida corrida-publica.json
python -m unittest discover -s tests -v
```

El modo `local` funciona sin conexión. El modo `publico` añade un escenario con la última observación válida de BCRPData. El archivo `ejemplo-contexto-publico.json` conserva el resultado de una consulta en vivo con los perfiles ficticios.

## Datos de entrada

El archivo `perfiles-sinteticos.json` contiene tres perfiles ficticios. Puedes pasar otro archivo con `--perfiles archivo.json`.

| Dato | Origen esperado |
| --- | --- |
| Identificador, sector y zona | Ficha del crédito o expediente del negocio. El identificador del ejemplo es ficticio. |
| Cuota vigente | Registro interno del crédito, al corte. |
| Factor de capacidad de pago | Regla de Riesgos por producto. El 65 % del ejemplo es ilustrativo. |
| Ventas, costos y fecha de evaluación | Última evaluación económica disponible. El ejemplo trata sus costos como variables. |
| Otros gastos y obligaciones | Gastos fijos y deudas distintas de la cuota evaluada. |
| Producción de calzado | [BCRPData, serie PN01927AM](https://estadisticas.bcrp.gob.pe/estadisticas/series/mensuales/resultados/PN01927AM). Es una variación interanual de alcance nacional. |

Un campo económico faltante se representa con `null`. El cliente C conserva su umbral calculable y el resultado señala que faltan ventas para simularlo. Una evaluación posterior al corte queda fuera del cálculo. Si falta el FCP, se puede comparar utilidad con cuota cuando hay estructura económica, y queda pendiente el umbral preventivo.

## Escenarios con datos públicos y LLM opcional

1. El programa consulta BCRPData, selecciona el periodo mensual válido más reciente y guarda el valor, la unidad, el periodo, la cobertura y la fecha de consulta. Para esta demo, exige una antigüedad máxima de 90 días desde el cierre del periodo. Los datos de otras zonas o sectores requieren su propia fuente y regla de pertinencia.
2. En modo `llm`, Vercel AI Gateway recibe esa observación pública. El modelo devuelve el identificador de la evidencia, un rango de volumen hipotético y una justificación. El programa verifica el identificador, el orden y que el rango quede entre −15 % y +15 %, límites de sensibilidad ilustrativos. La justificación se conserva como texto propuesto y debe revisarse.
3. NumPy genera los escenarios por sector con la misma semilla para comparar los perfiles. Si la fuente falla, quedan disponibles los escenarios de demostración. Si falla el LLM, se usa una regla de sensibilidad explícita y el informe indica su origen.

Para usar `python -m caja_pulse --modo llm`, configura `AI_GATEWAY_API_KEY` y `AI_GATEWAY_MODEL` en el entorno de ejecución. Usa un identificador del catálogo que admita salidas estructuradas. El código también acepta `VERCEL_OIDC_TOKEN` si el entorno lo suministra. El adaptador se probó con una respuesta controlada. La ejecución de ejemplo solo usa BCRPData y reglas. [Salidas estructuradas en Vercel AI Gateway](https://vercel.com/docs/ai-gateway/sdks-and-apis/openai-chat-completions/structured-outputs)

## Cálculo y siguiente integración

La utilidad disponible se calcula como ventas ajustadas por volumen, menos costos variables ajustados por volumen y precio de insumos, menos otros gastos y obligaciones. El umbral preventivo es cuota ÷ FCP. La insuficiencia de pago en el escenario comienza cuando la utilidad cae por debajo de la cuota. Una utilidad igual a la cuota deja margen cero.

Las proporciones indican cuántas muestras cruzaron un umbral bajo los supuestos declarados. Su interpretación se limita al ejercicio de sensibilidad. Para repetir una corrida conserva el archivo de perfiles, la observación, el escenario, la versión de NumPy y la semilla.

La siguiente integración puede sumar cronogramas y pagos para calcular ICCO, y evaluaciones comparables para respaldar imputaciones KNN. Antes de evaluar un piloto, Riesgos debe definir población, evento e intervalo de alerta, validar el FCP y medir qué proporción de alertas justificaría una revisión.
