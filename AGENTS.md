# AGENTS.md — CAJA PULSE 360 | CAJATHÓN 2026

## 1. Propósito y reglas para cualquier agente

Este archivo es la referencia consolidada del equipo para preparar y presentar la Concept Solution de CAJA PULSE 360 y orientar un eventual desarrollo presencial. Priorizar las decisiones de este documento frente a versiones anteriores de la propuesta. Escribir en español claro, profesional y concreto, adaptado a microfinanzas peruanas. No añadir funcionalidades que comprometan la factibilidad de una hackatón. No presentar supuestos, datos sintéticos, proyecciones o beneficios esperados como hechos comprobados. No afirmar que Caja Trujillo carece de herramientas similares sin confirmación de sus Owners. No enviar ni publicar el formulario sin autorización del equipo.

## 2. Contexto oficial y etapa actual

- Competencia: CAJATHÓN 2026, Caja Trujillo, Perú.
- Eje 3: Riesgo, fraude y recuperaciones inteligentes.
- Desafío: **Anticipar el deterioro de pago antes del atraso**.
- Pregunta de innovación: ¿Cómo podríamos identificar anticipadamente señales de deterioro en la capacidad de pago de los clientes y facilitar acciones preventivas antes de que se produzcan incumplimientos crediticios?
- Resultado esperado: fortalecer la gestión preventiva, reducir potenciales incumplimientos, mejorar la calidad de cartera y preservar la salud financiera de los microempresarios.
- Insumos referenciales del reto: historial de pagos, comportamiento crediticio, evolución de saldos, actividad económica, variables de riesgo, eventos de incumplimiento, series históricas y datos sintéticos. No constituyen compromiso de entrega.
- Restricciones: protección de datos personales, evitar sesgos, considerar incertidumbre, alertas sustentadas, minimizar falsos positivos, revisión humana y ausencia de decisiones crediticias perjudiciales automáticas.
- Complejidad tecnológica: IA, agentes inteligentes, analítica predictiva, optimización o automatización avanzada cuando aporten valor real. Un dashboard, chatbot genérico, formulario o automatización básica por sí solo no es suficiente. Se debe demostrar desarrollo funcional e integración tecnológica en la etapa de prototipo.

### Comunicado N.º 5 (aportado por el equipo)

1. Inmersión: comprender problema, procesos, restricciones y resultados; Owners aclaran dudas, no entregan datos ni recursos en esta etapa.
2. Concept Solution: presentar propuesta y especificar datos, reglas de negocio y recursos requeridos para la etapa presencial.
3. Preparación presencial: Caja evalúa requerimientos y comunica a finalistas los recursos disponibles, incluidos posibles datos anonimizados o sintéticos. No hay garantía de entrega.
4. El formulario confirma que material visual es opcional y **no se requiere prototipo funcional en esta etapa**.

## 3. Información de los Owners del reto de Negocios (24/11/2026)

Es contexto auxiliar, no trasladar automáticamente sus restricciones al reto de Riesgos.

- Negocios se dirige a créditos nuevos, admisión, ampliación y recuperación de cliente. El cronograma se fija antes del desembolso; en créditos vigentes solo cambia mediante reprogramación o refinanciación según corresponda. El objetivo de Negocios es construir el plan desde el inicio, no redistribuir cuotas vigentes.
- El core actual genera cuotas homogéneas de periodicidad única; incluso cronogramas estacionales tienen cuotas homogéneas. Evaluación usa ingreso estándar promedio. El asesor carece de herramientas para estimar el ciclo por sector y zona.
- Usuario principal de Negocios: asesor de negocios; Riesgos valida y comité o nivel de aprobación revisa. Demo independiente del core, posible web/app/WhatsApp; API de lenguaje externo permitida para demo de Negocios. Seguridad institucional futura por TI.
- Factor máximo Cuota/Utilidad Neta configurable por producto, menor a 1. Ejemplos ilustrativos 0,65 inclusión y 0,85 pequeña empresa. Asesor puede aplicar factor inferior. Utilidad neta descuenta otras deudas y carga familiar cuando corresponde; para persona jurídica totalmente formal se toma de estados financieros auditados según respuesta del Owner.
- Cronogramas nuevos pueden variar montos y periodos según ciclo; en cima se amortiza máximo capital después de seguros e intereses, en valle se priorizan seguros e intereses. Gracia/solo intereses con cautela por costo.
- TEA fija, TED base 360 y días exactos sobre saldo de capital; seguros simples base 360 según saldo o valor asegurable. Desgravamen opcional; multirriesgo/vivienda opcionales y excluyentes, vivienda obligatoria en hipotecarios según respuesta. TEA editable dentro del máximo BCRP aplicable; TCEA cambia con estructura, plazo y seguros. Pagos se aplican a seguros, interés y capital; pendientes conservan concepto y no se capitalizan como principal; siguiente periodo prioriza pendientes.
- Para Negocios indicaron que no entregarán ni clonarán bases reales, incluso anonimizadas. Permiten perfiles sintéticos. Historial de pagos no es fuente adecuada para estimar ciclo económico del negocio por sí solo. Esta respuesta no confirma disponibilidad de datos para Riesgos.
- Factores internos: ventas, costos, gastos operativos/tributarios, evidencias transaccionales, modelo de negocio y carga familiar. Externos: sector, zona, ciclo, estacionalidad, clima, competencia y factores sociales/económicos. Fuentes sugeridas INEI, BCRP, MIDAGRI, SENAMHI, SUNAT, SBS, Cámara de Comercio y calendarios comerciales.
- Negocios espera ciclo gráfico, cronograma, ratio Cuota/Utilidad por etapa, supuestos y comparación con cuota fija en escenarios sintéticos adversos. No medirá mora real. No construir generador de cronogramas para nuestro MVP de Riesgos.

## 4. Decisión de producto

Nombre: **CAJA PULSE 360 — Motor inteligente de vulnerabilidad económica y prevención del deterioro crediticio**.

Usuarios principales: área de Riesgos y asesores de negocios responsables de seguimiento. Foco: créditos vigentes, preferentemente al día (confirmar alcance con Owners). El usuario no ejecuta los módulos por separado. Dos vistas: panel de cartera y ficha individual con simulador integrado. Tres componentes internos automatizados.

Problema central: el cliente puede pagar puntualmente usando ahorros, deuda o capital de trabajo mientras su negocio se deteriora. No hay acceso obligatorio a ventas diarias actuales, Yape, Plin, cuentas externas ni registros contables continuos. Tampoco depender de formularios periódicos o de que el cliente cambie sus hábitos. Incluso ingresos y gastos iniciales podrían faltar, como ocurre en el ejemplo aportado por el equipo sobre Cooperativa León XIII; no asumir que esa frecuencia de faltantes es la misma en Caja Trujillo.

Objetivo: estimar vulnerabilidad y resistencia bajo escenarios, contextualizar señales observables y recomendar verificaciones preventivas, no adivinar ventas reales ni producir un score de incumplimiento calibrado sin datos suficientes.

### Componentes internos

1. **Perfil económico y contextual**: unir evaluación inicial, cronograma, pagos, crédito, sector, zona e indicadores externos; validar faltantes y antigüedad; calcular indicadores de pagos; KNN para encontrar comparables e imputar información económica referencial cuando haya suficientes registros confiables.
2. **Simulador inteligente de vulnerabilidad**: Monte Carlo y sensibilidad financiera; proyectar escenarios de ventas, costos, gastos, otras obligaciones y estacionalidad; calcular umbrales y puntos de quiebre; distinguir escenarios hipotéticos de evidencias individuales.
3. **Motor de decisiones preventivas**: reglas y ponderaciones configurables para priorizar atención por vulnerabilidad, evidencia externa, señales crediticias y saldo; confianza separada de prioridad; recomendar seguimiento, contacto o verificación focalizada. Nunca modificar automáticamente condiciones, aprobar/rechazar créditos, reclasificar o restringir al cliente.

### Vistas

- Panel de cartera: clientes evaluados, prioridades, exposición por saldo, sector/zona, filtros, factores económicos, lista de revisión.
- Ficha individual: datos observados y faltantes, antigüedad, indicadores de pago, comparables, simulador, umbrales, evidencia, incertidumbre y acción sugerida. Seleccionar cliente debe bastar para ver análisis automático.

## 5. Metodología financiera y aporte del compañero

### Factor de capacidad de pago (FCP)

FCP = límite Cuota / Utilidad Neta definido por producto; ejemplos 0,65 y 0,85 son ilustrativos. Usar como referencia preventiva en créditos vigentes solo sujeto a validación de Riesgos. Cuota máxima = utilidad × FCP. Utilidad mínima referencial = cuota / FCP. No equivale a utilidad real ni implica que el crédito fue concedido exactamente en el límite. Utilidad disponible antes de la cuota evaluada debe descontar las otras obligaciones, sin duplicar el gasto financiero.

Dos umbrales: vulnerabilidad cuando utilidad simulada < cuota/FCP; insuficiencia cuando utilidad simulada < cuota. Para utilidad no positiva no calcular ratio engañoso ni dividir por cero. Caída tolerable de utilidad = 1 - (cuota/FCP)/utilidad inicial, si es positiva. Incremento tolerable de costos = (utilidad inicial - cuota/FCP)/costos iniciales, con ventas, volumen y demás gastos constantes. Si ya supera el umbral, indicar que no existe margen positivo.

### Índice de cobertura de cuota observada (ICCO)

Aporte del compañero: usar fluctuaciones del monto pagado respecto a cuota establecida. En Cooperativa León XIII existen campos de ingresos/gastos en registro de crédito e ingreso mensual estimado del socio, pero según ejemplo del equipo a menudo faltan. No usar datos privados de esa entidad; solo reproducir características mediante datos ficticios.

ICCO_t = monto pagado en periodo / cuota programada en periodo. Desviación = ICCO - 1. Cobertura acumulada = suma pagos / suma cuotas. Volatilidad = desviación estándar poblacional de ICCO; añadir tendencia, pagos fraccionados, regularizaciones, adelantos, amortizaciones extraordinarias, fechas respecto al vencimiento y persistencia.

Ejemplo simplificado: desembolso S/12.000, 12 meses, cuota S/1.000 (ignora intereses/seguros solo para ilustrar).

| Mes | Cuota | Pago | ICCO | Desviación | Brecha acumulada |
|---|---:|---:|---:|---:|---:|
| Ene | 1000 | 700 | 0,70 | -30% | -300 |
| Feb | 1000 | 1300 | 1,30 | +30% | 0 |
| Mar | 1000 | 1000 | 1,00 | 0% | 0 |
| Abr | 1000 | 1300 | 1,30 | +30% | 300 |
| May | 1000 | 700 | 0,70 | -30% | 0 |

Cobertura acumulada 100%, volatilidad poblacional 26,83%, meses bajo cuota 40%. Brecha acumulada no es saldo vencido contractual. Febrero podría regularizar S/300 pendientes; abril podría ser adelanto o amortización. No confundir flujo de pagos con ingresos, puntualidad o capacidad económica. Requiere reglas de aplicación y fechas. Un pago inferior a la cuota no implica atraso si hay adelantos o aún no vence.

Combinar cuota/FCP × ICCO equivale algebraicamente a pago/FCP y no aporta evidencia económica independiente. Con FCP 0,65, los valores 1076,92; 2000; 1538,46; 2000; 1076,92 serían un proxy hipotético bajo proporción constante no validada, **no estimación de ingresos reales**. Mantener ICCO como variable complementaria, no convertirlo directamente en ventas ni utilidad.

### Datos faltantes y KNN

- Datos completos: simulación individualizada con evaluación inicial fechada.
- Parciales: imputar valores referenciales mediante comparables, cuando haya suficientes registros.
- Sin evaluación utilizable: cuota/FCP como umbral, historial de pagos y comparables si existen.
- Sin comparables ni historial suficiente: escenarios sectoriales y umbrales, abstenerse de afirmar deterioro individual. Si tampoco existe estructura económica válida, no calcular un punto de quiebre individual ficticio.

KNN: seleccionar vecinos por sector, zona, antigüedad, monto, cuota, plazo, destino, endeudamiento y señales crediticias disponibles; normalizar numéricas, codificar categóricas, evitar variables futuras; ponderar por distancia si corresponde, exigir suficiente similitud y registros completos, medir error con ocultamiento de valores conocidos. No imputar si no hay soporte; distinguir faltante de cero; mantener origen y fecha de cada valor. Ejemplo de cinco vecinos con ventas 8000,9000,7500,8500,10000 y utilidades 1800,2100,1600,1900,2400: medias simples S/8600 y S/1960; rangos observados S/7500–10000 y S/1600–2400, no intervalos de confianza. La imputación aproxima un perfil referencial, no ventas actuales verificadas.

### Caso de demostración

| Variable | Cliente A | Cliente B |
|---|---:|---:|
| Ventas iniciales | 12000 | 12000 |
| Costos | 7000 | 8000 |
| Otros gastos y obligaciones | 2000 | 2000 |
| Utilidad inicial | 3000 | 2000 |
| Cuota | 1200 | 1200 |
| FCP | 0,65 | 0,65 |
| Días de atraso | 0 | 0 |
| Ratio inicial | 40% | 60% |
| Costos bajo shock +10% | 7700 | 8800 |
| Utilidad bajo shock | 2300 | 1200 |
| Ratio bajo shock | 52,17% | 100% |
| Incremento de costos tolerable | 16,48% | 1,92% |

Umbral referencial común S/1846,15. Ambos al día, B más vulnerable bajo el mismo supuesto; verificar costos y capital de trabajo. No demuestra deterioro real. Usar este caso en pitch y material visual.

### Simulación y priorización

Monte Carlo: generar por ejemplo 1000 escenarios por cliente a partir de rangos sectoriales explícitos, considerar estacionalidad normal y shock adicional; ajustar costos variables y fijos coherentemente, evitar doble conteo, reproducir con semilla. Indicador de vulnerabilidad = proporción de escenarios que superan umbral, **no PD real**. No afirmar predicción temporal si no hay series/horizonte definidos. Puntuación ilustrativa opcional: 40% vulnerabilidad, 25% exposición externa, 20% señales crediticias, 15% saldo normalizado; evitar duplicar shock en dos componentes, calibrar o declarar pesos arbitrarios. Confianza independiente (disponibilidad, antigüedad, comparabilidad). Revisión humana. Sin evidencia individual, exposición sectorial solo justifica verificación proporcional, no deterioro confirmado.

## 6. MVP y recursos

Stack: Python, Pandas, NumPy, Scikit-learn (KNN), Streamlit, Plotly, CSV o SQLite; GitHub para colaboración. Licencias permisivas habituales: Python PSF, Pandas/NumPy/Scikit-learn BSD, Streamlit Apache 2.0, Plotly MIT, SQLite dominio público; verificar licencias/versiones exactas al implementar. No exigir LLM ni API pagada. Aplicación independiente del core.

Cartera sintética aproximada de 1000 clientes: 250 calzado, 350 comercio, 250 agricultura, 150 transporte; cifras de diseño no oficiales. Historial de 6 meses como punto de partida, ampliar si es necesario para evaluar estacionalidad. Archivos sugeridos clientes.csv, creditos.csv, pagos.csv, indicadores_economicos.csv y verdad sintética de validación separada. No usar la verdad oculta como entrada. Usar fuentes públicas seleccionadas: INEI/BCRP (precios/actividad), MIDAGRI (agro), SENAMHI (clima), OSINERGMIN (combustible), SBS (agregados), calendarios y Cámara de Comercio. Confirmar granularidad y disponibilidad antes de usar; no afirmar que indicadores sectoriales equivalen a ventas individuales.

Validación: comparar con reglas crediticias usando mismos datos y horizonte; pruebas con escenarios independientes, separación temporal y sin fuga de información; medir precisión, sensibilidad, falsos positivos, anticipación respecto al evento simulado, error de imputación, consistencia financiera, robustez a faltantes, eficiencia de priorización. No atribuir reducción de mora real. Datos sintéticos demuestran funcionamiento, no generalización ni eficacia clínica/financiera real.

Fuera del MVP: core, acceso Yape/Plin/bancos, ventas reales automáticas, integración masiva en tiempo real, despliegue institucional, modificación contractual, comunicaciones automáticas, modelos causales, PD calibrada real y generación de cronogramas flexibles. Negocios es solo extensión futura para probar sostenibilidad de cronogramas nuevos.

Plan orientativo (no confirmado): 48 horas/4 integrantes; datos y ML, finanzas/riesgos, desarrollo web, negocio/validación. Priorizar simulador, datos faltantes y ficha/panel antes de funciones opcionales. No presentar tiempos o número de integrantes como requisitos oficiales.

## 7. FORMULARIO OFICIAL — respuestas listas para copiar

Los siguientes textos corresponden a la última versión del formulario. No copiar títulos ni comentarios de límites dentro de los campos. Revisar contador del portal antes de enviar. Paso 1 no se mostró completo: seleccionar el desafío de Riesgos indicado arriba y usar nombre CAJA PULSE 360; no inventar otros campos.

### 2.1 ¿En qué consiste su solución y cómo aborda la problemática del desafío? (máx. 2000 caracteres)

CAJA PULSE 360 es una plataforma inteligente de gestión preventiva del riesgo crediticio, dirigida al área de Riesgos y a los asesores de negocios de Caja Trujillo, que busca identificar señales de deterioro y vulnerabilidad económica en microempresarios antes de que presenten atrasos.

La problemática radica en que un cliente puede continuar pagando puntualmente sus cuotas mientras su capacidad económica se deteriora. Esta situación resulta difícil de identificar en el contexto microfinanciero peruano, debido a la informalidad, la ausencia de registros contables actualizados y la limitada disponibilidad de información sobre ventas, ingresos y movimientos financieros externos.

Nuestra solución integrará información de la evaluación crediticia inicial, comportamiento histórico de pagos, endeudamiento, características del negocio e indicadores económicos sectoriales y territoriales. Cuando existan datos económicos faltantes, utilizará técnicas de aprendizaje automático para construir perfiles referenciales a partir de clientes comparables, siempre que exista información suficiente.

Mediante simulaciones probabilísticas y análisis de sensibilidad financiera, determinará cuánto deterioro económico podría soportar cada cliente ante disminuciones de ingresos, incrementos de costos, nuevas obligaciones o fluctuaciones estacionales.

Asimismo, analizará la estabilidad, tendencia y cobertura de sus pagos para identificar señales financieras complementarias, sin asumir que estas representan directamente sus ingresos.

El sistema distinguirá la vulnerabilidad potencial del deterioro sustentado, incorporará la incertidumbre de las estimaciones y recomendará intervenciones preventivas priorizadas y explicables.

La solución no dependerá del registro periódico de ventas, formularios recurrentes ni acceso a Yape o Plin. Sus recomendaciones estarán sujetas a revisión humana, evitando decisiones crediticias automáticas y contribuyendo a preservar la salud financiera de los microempresarios y la calidad de la cartera.

### 2.2 ¿Cómo funcionaría su solución? (límite no visible; objetivo <2000 caracteres)

CAJA PULSE 360 funcionará mediante tres componentes internos integrados y automatizados.

1. Perfil económico y contextual: procesará la evaluación económica inicial, cronogramas, historial de pagos, endeudamiento, actividad económica, ubicación e indicadores externos. Identificará información faltante y, cuando existan suficientes registros comparables, utilizará KNN para estimar valores económicos referenciales. También calculará indicadores de cobertura de cuotas, volatilidad, tendencias y regularizaciones, diferenciando los pagos ordinarios de los extraordinarios cuando la información lo permita.

2. Simulador inteligente de vulnerabilidad: ejecutará simulaciones Monte Carlo considerando variaciones de ingresos, costos, gastos, endeudamiento y estacionalidad. Utilizará la relación Cuota/Utilidad Neta y el factor referencial de capacidad de pago por producto para determinar el punto de quiebre financiero y la proporción de escenarios en los que el cliente podría comprometer su capacidad de pago. Si no existen datos económicos suficientes, trabajará con escenarios sectoriales y umbrales referenciales, comunicando sus limitaciones.

3. Motor de decisiones preventivas: combinará vulnerabilidad económica, señales crediticias, exposición a factores externos y saldo pendiente para priorizar casos y recomendar acciones específicas. La calidad de la información se evaluará independientemente para evitar penalizar a clientes con datos incompletos.

El usuario interactuará con dos vistas: un panel general de cartera y una ficha individual del cliente que incluirá un simulador interactivo, factores explicativos y recomendaciones preventivas.

El procesamiento se realizará automáticamente. El asesor únicamente deberá seleccionar al cliente, revisar los resultados y validar las acciones sugeridas. La plataforma distinguirá datos observados, estimaciones y escenarios hipotéticos, sin modificar automáticamente las condiciones contractuales.

### 2.3 ¿Qué diferencia su solución de otras alternativas existentes? (máx. 1000 caracteres)

A diferencia de los enfoques de alerta temprana centrados principalmente en el comportamiento crediticio, CAJA PULSE 360 incorpora una perspectiva de resiliencia económica que permite identificar clientes vulnerables incluso cuando pagan puntualmente.

Su diferenciación radica en integrar aprendizaje automático para estimar información económica faltante, análisis de fluctuaciones de pagos, contextualización sectorial y territorial, simulaciones Monte Carlo y cálculo individualizado del punto de quiebre financiero.

No se limita a identificar quién podría incumplir, sino que explica qué factores podrían comprometer su capacidad de pago, cuánto deterioro podría soportar y qué información convendría verificar.

La solución funciona sin acceso obligatorio a ventas actualizadas, Yape, Plin o registros contables formales. Además, distingue vulnerabilidad potencial de deterioro sustentado, gestiona la incertidumbre y recomienda intervenciones preventivas focalizadas, explicables y sujetas a revisión humana.

### 2.4 Material visual complementario (opcional)

Hasta 3 archivos PDF, PNG o JPG, máximo 10 MB cada uno. Propuestos, aún no creados como adjuntos independientes:

1. Diagrama de arquitectura: entradas internas (evaluación, créditos, pagos, endeudamiento) y externas (sector, zona, precios, estacionalidad) → perfil económico (KNN, datos faltantes, estabilidad de pagos) → simulador (Monte Carlo, capacidad de pago, quiebre) → motor preventivo (priorización, incertidumbre, recomendaciones) → aplicación web (panel + ficha) → validación humana.
2. Caso gráfico A/B: barras utilidad inicial 3000/2000, bajo estrés 2300/1200 y cuota 1200/1200; incremento tolerable 16,48%/1,92%; shock +10%, FCP 65%, datos sintéticos.
3. Mockups de dos vistas: panel con cartera, prioridades, exposición y sectores; ficha CL-0021 con calzado, 0 días, utilidad inicial 2000, cuota 1200, ventas actuales desconocidas, quiebre 1,92%, simulador y recomendación. Ejemplos visuales no funcionales; cifras ficticias del panel 1000 clientes, 87 prioritarios, S/12,5M exposición.

### 2.5 Enlace complementario (opcional)

Dejar vacío salvo que se disponga de enlace accesible a Figma/Miro u otra herramienta. Si muestra desarrollos funcionales preexistentes que se reutilizarán, declararlos en paso 4.

### 3.1 ¿Qué impacto generaría su solución y cómo contribuiría al resultado esperado del desafío? (máx. 2000 caracteres)

CAJA PULSE 360 contribuirá a fortalecer la gestión preventiva del riesgo crediticio de Caja Trujillo mediante la identificación de clientes económicamente vulnerables antes de que presenten atrasos, facilitando intervenciones oportunas y mejorando la asignación de recursos operativos.

Para la entidad, permitirá identificar exposiciones económicas relevantes, priorizar clientes según su vulnerabilidad y saldo pendiente, reducir alertas innecesarias y contribuir potencialmente a disminuir incumplimientos, costos de recuperación y pérdidas crediticias.

Para los asesores, proporcionará recomendaciones explicables y verificaciones focalizadas, evitando realizar evaluaciones económicas completas cuando únicamente sea necesario actualizar determinadas variables.

Para los microempresarios, facilitará una atención preventiva que considere sus características económicas y fluctuaciones comerciales, evitando evaluaciones desfavorables sustentadas únicamente en información insuficiente.

Como ejemplo, dos clientes con cuotas de S/1.200, utilidades iniciales de S/3.000 y S/2.000, y costos de S/7.000 y S/8.000, respectivamente, pueden presentar distintos niveles de resistencia. Ante un incremento hipotético del 10% en sus costos, sus ratios Cuota/Utilidad serían 52,17% y 100%. Con un factor referencial de 65%, el segundo cliente requeriría una revisión prioritaria, aunque ambos mantengan sus créditos al día.

La contribución se evaluará mediante indicadores de anticipación del deterioro simulado, precisión, sensibilidad, falsos positivos, robustez ante datos faltantes y eficiencia en la priorización de intervenciones. Se compararán los resultados con un modelo de referencia basado en reglas crediticias, utilizando los mismos escenarios de prueba.

La reducción efectiva de la morosidad y las pérdidas crediticias constituirá un beneficio esperado que deberá validarse posteriormente con información real. No se atribuirán mejoras financieras reales a resultados obtenidos exclusivamente con datos sintéticos.

### 4.1 ¿Cuál será el enfoque tecnológico de su solución? (máx. 2000 caracteres)

La solución se desarrollará mediante una arquitectura modular en Python, integrando procesamiento de datos, aprendizaje automático, simulación probabilística y automatización de recomendaciones preventivas dentro de una aplicación web independiente.

Pandas permitirá preparar, integrar y validar información económica, crediticia y sectorial, incluyendo la identificación de registros incompletos y el cálculo de indicadores de cobertura, volatilidad, tendencia y regularización de pagos.

Scikit-learn se utilizará para implementar K-Nearest Neighbors (KNN), identificando clientes comparables mediante características económicas y crediticias disponibles. Cuando existan suficientes registros confiables, permitirá estimar valores económicos faltantes mediante vecinos ponderados por similitud. Se establecerán criterios mínimos de comparabilidad para evitar imputaciones injustificadas.

NumPy permitirá ejecutar simulaciones Monte Carlo, generando múltiples escenarios de ingresos, costos, gastos y obligaciones financieras. El motor calculará distribuciones de utilidad, umbrales de capacidad de pago, puntos de quiebre y sensibilidad ante factores adversos.

Un motor de reglas y ponderaciones configurables combinará vulnerabilidad, señales crediticias, exposición económica y saldo pendiente para priorizar intervenciones. La incertidumbre y calidad de información serán evaluadas independientemente.

Streamlit y Plotly permitirán desarrollar una interfaz web interactiva con un panel de cartera, fichas individuales y simulaciones económicas. Los datos se almacenarán mediante archivos CSV o SQLite.

Se utilizarán tecnologías de código abierto con licencias permisivas, como BSD, MIT y Apache 2.0, respetando sus condiciones de uso y atribución. No se requerirán APIs de pago, modelos generativos externos ni integraciones directas con el core de Caja Trujillo.

Este enfoque permite concentrar el desarrollo en el motor analítico, garantizar la reproducibilidad de los cálculos y construir un prototipo funcional dentro de las restricciones de una hackatón.

### 4.2 Punto de partida

Seleccionar **Desarrollo desde cero**, siempre que no se reutilicen componentes funcionales previamente desarrollados. Uso de librerías, modelos, APIs, frameworks o herramientas comerciales por sí solo no constituye desarrollo preexistente según formulario. Si el equipo reutiliza un desarrollo funcional, cambiar selección y declarar correctamente.

### 4.3 ¿Identifican alguna limitación o riesgo técnico relevante? (máx. 800 caracteres)

Los principales riesgos técnicos son la ausencia de información económica inicial o actualizada, la escasez de clientes comparables, la limitada granularidad de indicadores externos y la dificultad para distinguir fluctuaciones de pagos de cambios reales en los ingresos.

Se mitigarán mediante datos sintéticos, criterios mínimos de similitud para KNN, escenarios probabilísticos, análisis de sensibilidad y mecanismos de abstención cuando la evidencia sea insuficiente.

Las simulaciones no se interpretarán como ingresos reales ni probabilidades de incumplimiento validadas. Se realizarán pruebas con datos faltantes y escenarios adversos independientes, incorporando revisión humana y evitando integraciones obligatorias con sistemas internos o plataformas financieras externas.

### 5.1 ¿Qué construirán durante el hackathon? (máx. 2000 caracteres)

Durante la hackatón desarrollaremos un producto mínimo viable de CAJA PULSE 360 mediante una aplicación web funcional, utilizando información autorizada por Caja Trujillo o, en su defecto, una cartera de aproximadamente 1.000 clientes sintéticos pertenecientes a cuatro sectores económicos: calzado, comercio minorista, agricultura y transporte.

Construiremos tres componentes internos:

1. Procesamiento y perfil económico: integración de información crediticia, evaluaciones económicas, indicadores externos y cálculo de variables derivadas del historial de pagos. Implementaremos KNN para identificar clientes comparables y estimar información económica faltante cuando exista suficiente evidencia.

2. Motor de simulación económica: generación automatizada de escenarios mediante Monte Carlo, cálculo de utilidad referencial, capacidad de pago, punto de quiebre financiero, sensibilidad ante factores adversos y proporción de escenarios que superan los umbrales referenciales.

3. Motor de priorización preventiva: clasificación de prioridades mediante reglas configurables que consideren vulnerabilidad económica, señales crediticias, exposición externa y saldo pendiente, proporcionando recomendaciones explicables y diferenciando la incertidumbre de la información.

El prototipo contará con dos vistas: un panel general de cartera para identificar clientes y sectores prioritarios, y una ficha individual con resultados económicos, indicadores crediticios, comparación de perfiles, simulador interactivo y recomendaciones preventivas.

La funcionalidad crítica será evaluar la resistencia económica de un cliente sin conocer sus ventas actuales, identificar los factores que podrían comprometer su capacidad de pago y recomendar una acción preventiva sustentada.

Se priorizará la integración funcional de estos componentes, los cálculos financieros reproducibles y las pruebas controladas, evitando desarrollar funcionalidades adicionales que comprometan la entrega del prototipo.

### 5.2 ¿Qué resultado funcional esperan demostrar al finalizar el hackathon? (máx. 1500 caracteres)

Demostraremos una aplicación capaz de procesar una cartera crediticia, identificar clientes vulnerables y generar recomendaciones preventivas sin requerir información actualizada de sus ventas.

El caso principal comparará dos microempresarios del mismo sector, ambos con créditos al día y cuotas similares, pero con diferentes estructuras económicas. Ante un incremento hipotético de costos, el sistema ejecutará simulaciones, calculará sus respectivos puntos de quiebre y explicará por qué uno requiere mayor atención preventiva.

Posteriormente, se eliminarán variables económicas del cliente para demostrar cómo la solución identifica información faltante, utiliza perfiles comparables mediante KNN cuando corresponde y comunica incertidumbre cuando no existe evidencia suficiente.

También se analizarán patrones de pagos estables, fluctuantes y progresivamente decrecientes, diferenciando regularizaciones y pagos extraordinarios cuando los datos lo permitan.

La validación utilizará escenarios sintéticos independientes, cuya situación económica subyacente permanecerá oculta para el motor. Se comparará la solución con reglas convencionales de alerta crediticia mediante indicadores de anticipación, precisión, sensibilidad, falsos positivos y eficiencia de priorización.

Esperamos demostrar la capacidad de identificar diferencias de vulnerabilidad antes del atraso, explicar los resultados y recomendar verificaciones preventivas específicas, sin afirmar una reducción comprobada de la mora real.

### 5.3 ¿Qué funcionalidades o capacidades quedarán fuera del alcance? (máx. 800 caracteres)

Quedarán fuera del alcance la integración directa con el sistema core de Caja Trujillo, el acceso a Yape, Plin y cuentas bancarias externas, la captura automática de ventas reales, las conexiones masivas en tiempo real con fuentes externas y el despliegue en infraestructura institucional.

Tampoco se implementarán modificaciones automáticas de cronogramas, refinanciamientos, decisiones de aprobación crediticia ni comunicaciones automáticas con clientes.

La calibración de probabilidades reales de incumplimiento, la medición del impacto efectivo sobre la mora y los modelos causales de efectividad de intervenciones requerirán información histórica y validaciones posteriores.

La generación de cronogramas adaptados al ciclo económico para créditos nuevos se considerará una futura ampliación.

### 6.1 ¿Qué tipo de requerimiento de datos e insumos tiene su propuesta?

Seleccionar únicamente **Requerimiento deseable de datos e insumos**. No marcar indispensable ni no requerimos. Podemos construir y demostrar técnicamente con datos propios; los recursos de Caja ayudarían a validar representatividad y reglas, no garantizan validación real. Priorizar generación autónoma. Si aparecen campos adicionales al seleccionar, adaptar el texto siguiente; su estructura y límites aún no se conocen.

Solicitamos, según disponibilidad y autorización de Caja Trujillo, información sintética, estructuras de datos, diccionarios o reglas de negocio representativas de los siguientes elementos:

- Evaluaciones económicas iniciales: ingresos, costos, gastos, carga familiar, obligaciones financieras, utilidad neta y fecha de evaluación.
- Características del cliente: actividad económica, ubicación del negocio, antigüedad y destino del financiamiento.
- Características crediticias: producto, monto, plazo, cuota, cronograma, saldo pendiente y factor de capacidad de pago.
- Historial de pagos: fechas, montos, cuotas programadas, pagos parciales, regularizaciones, adelantos y amortizaciones extraordinarias.
- Evolución del endeudamiento y eventos de incumplimiento, cuando estén disponibles.
- Evaluaciones económicas posteriores, si existen, para contrastar cambios económicos con patrones de pago.
- Reglas de negocio sobre capacidad de pago, deterioro crediticio, monitoreo e intervenciones preventivas permitidas.
- Descripción general de los mecanismos actuales de alerta temprana y periodicidad de la información disponible.

Estos insumos permitirán adaptar los perfiles sintéticos a la realidad microfinanciera de Caja Trujillo y mejorar la validación del prototipo.

Su entrega no constituye una dependencia indispensable. En caso de no disponer de ellos, desarrollaremos la solución mediante datos sintéticos propios, supuestos explícitos e indicadores económicos públicos.

## 8. Preguntas pendientes para Owners (consolidadas; no multiplicar cuestionarios)

1. ¿El reto se enfoca en créditos vigentes al día, incluidos clientes recuperados con antecedentes de mora?
2. ¿Qué herramientas o reglas de alerta temprana usan actualmente y qué limitaciones presentan?
3. ¿Conservan históricamente ventas, costos, gastos, carga familiar, obligaciones y utilidad inicial; qué proporción aproximada de registros es utilizable? ¿Existe ingreso mensual estimado en ficha del cliente?
4. ¿Se actualizan evaluaciones económicas durante el crédito o en renovaciones/ampliaciones, y con qué frecuencia y variables?
5. ¿El historial distingue cuotas corrientes, pagos parciales, regularizaciones, adelantos, amortizaciones extraordinarias y fechas efectivas? ¿Qué otras señales internas, como ahorros o solicitudes, son observables?
6. ¿Qué detalle y periodicidad de endeudamiento externo pueden consultar durante el crédito?
7. ¿Se registran actividad/CIIU, ubicación del negocio, antigüedad y destino del crédito de forma estructurada?
8. ¿Es válido usar Cuota/Utilidad Neta como referencia preventiva en créditos vigentes? ¿Se conserva factor máximo por producto y factor aplicado al cliente?
9. ¿Qué intervenciones preventivas están permitidas antes del atraso y qué protocolos las limitan?
10. ¿Qué evento debe anticiparse y con qué horizonte: deterioro económico, primer atraso o mora de determinada duración?
11. ¿Qué estructuras, reglas, datos sintéticos o anonimizados autorizados podrían estar disponibles para finalistas y con qué granularidad, periodicidad e historia?
12. ¿Se espera identificar vulnerabilidad, predecir incumplimiento, recomendar acciones o combinar capacidades? ¿Qué criterios de evaluación y validación sintética aceptan?

Preguntas internas al compañero: (1) ¿Pretendía estimar ventas, utilidad o disponibilidad para pagar? (2) ¿Los S/1300 de febrero regularizan los S/300 de enero o son pago adicional independiente? (3) ¿Contempló calibrar con clientes con datos económicos completos o solo usar pagos?

## 9. Criterios finales y pendientes de envío

- Alinear cada respuesta al campo del formulario, no repetir todo en cada sección.
- Verificar caracteres y selección 4.2 con equipo. Confirmar campos no visibles de pasos 1 y 6 y límite 2.2.
- Material visual opcional aún pendiente de crear como archivos independientes; no confundir mockups con un prototipo construido.
- Confirmar FCP en Riesgos, definición de deterioro, disponibilidad de datos y acciones permitidas con Owners.
- No inventar fechas límite, puntajes de selección, duración del evento ni resultados cuantitativos reales.
- Principio central: identificar exposición y resistencia con información incompleta, explicar qué sabemos y qué no sabemos, y orientar revisión humana antes del atraso. No sustituir evidencia económica con pagos observados.
