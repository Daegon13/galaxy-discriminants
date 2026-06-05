# Project Masterplan

## Resumen ejecutivo

Este proyecto propone desarrollar un prototipo reproducible de física computacional y astrofísica de datos para estudiar curvas de rotación galáctica desde una perspectiva comparativa entre familias de modelos físicos. El objetivo no es proponer una nueva teoría de gravedad ni resolver el problema de la materia oscura, sino construir una herramienta computacional que permita identificar qué galaxias son más informativas para discriminar entre modelos competidores.

La pregunta central del proyecto es: dado un conjunto de curvas de rotación galáctica y varios modelos candidatos, ¿qué galaxias son más útiles para distinguir entre MOND/RAR, halos de materia oscura y modelos híbridos? Esta pregunta se abordará mediante una arquitectura modular, reproducible y testeable que permita cargar datos, ajustar modelos, calcular métricas de comparación y producir rankings de utilidad discriminante.

El enfoque inicial será incremental. La primera versión trabajará con datos sintéticos/mock claramente marcados. Las versiones posteriores podrán incorporar datasets públicos, como SPARC, siempre que se verifique previamente su disponibilidad, formato, licencia y documentación. El proyecto prioriza claridad metodológica, trazabilidad, control de unidades, validación con tests y documentación científica honesta.

Decisión tomada: el proyecto se implementará como paquete Python científico reproducible, usando Python 3.12, `uv`, estructura `src/`, `pytest`, `ruff` y documentación Markdown mantenida junto al código.

## Problema científico-computacional

Una “galaxia discriminante” es una galaxia cuya curva de rotación y estructura observacional permiten distinguir con mayor fuerza entre modelos físicos competidores. No se trata necesariamente de la galaxia mejor ajustada por un modelo, sino de aquella donde las predicciones, penalizaciones estadísticas, incertidumbres y sensibilidad a supuestos hacen que la comparación sea más informativa.

Es importante diferenciar los siguientes casos:

| Caso | Descripción | Implicación |
|---|---|---|
| Modelo que mejor ajusta una galaxia | Un modelo obtiene menor error o mejor métrica estadística para una galaxia específica | No implica automáticamente alto poder discriminante |
| Modelos con predicciones parecidas | Varios modelos producen curvas similares dentro de las incertidumbres observacionales | La galaxia tiene bajo poder discriminante con los datos actuales |
| Modelos con predicciones muy distintas | Las curvas predichas divergen en regiones observadas con buena precisión | La galaxia puede tener alto poder discriminante |
| Datos insuficientes para decidir | Las barras de error, falta de cobertura radial o degeneración de parámetros impiden una comparación fuerte | La galaxia puede requerir mejor observación |
| Galaxia prioritaria para observación futura | Nuevas mediciones en zonas específicas podrían reducir incertidumbre entre modelos | Caso relevante para extensión futura basada en valor esperado de nueva observación |

Supuesto: el poder discriminante depende tanto de la física del modelo como de la calidad, cobertura y estructura de los datos disponibles.

Riesgo: una galaxia puede parecer discriminante por errores sistemáticos, mala calibración, unidades inconsistentes, priors demasiado restrictivos o implementación incorrecta del modelo.

## Objetivos

### Objetivo principal

Construir una herramienta computacional reproducible que permita rankear galaxias según su utilidad para discriminar entre familias de modelos de curvas de rotación galáctica.

### Objetivos secundarios

- Diseñar una arquitectura modular para representar galaxias, datos observacionales, modelos físicos, ajustes y métricas.
- Implementar una primera versión con datos sintéticos/mock para validar el pipeline sin depender de datasets reales.
- Incorporar modelos físicos iniciales de forma progresiva:
  - modelo bariónico/newtoniano base;
  - MOND/RAR simple;
  - halo NFW;
  - halo Burkert.
- Implementar métricas de comparación entre modelos:
  - error de ajuste;
  - AIC/BIC;
  - diferencia entre predicciones;
  - robustez ante incertidumbres;
  - sensibilidad a priors.
- Generar visualizaciones básicas:
  - curva observada vs predicha;
  - residuos;
  - comparación entre modelos;
  - ranking de galaxias discriminantes.
- Mantener documentación científica y técnica defendible.
- Preparar el proyecto para una posible tesis, prototipo académico o paper técnico futuro.

### Objetivos fuera de alcance

- Resolver el problema de la materia oscura.
- Proponer una nueva teoría de gravedad.
- Ejecutar simulaciones cosmológicas completas.
- Implementar simulaciones N-body avanzadas en la primera etapa.
- Hacer inferencia cosmológica global.
- Automatizar conclusiones científicas sin revisión humana.
- Usar IA como decoración sin una función científica clara.
- Descargar o asumir datasets reales sin verificar disponibilidad, formato y licencia.
- Construir un dashboard web en el MVP.

## Hipótesis de trabajo

- Algunas galaxias tienen mayor poder discriminante que otras para comparar modelos de curvas de rotación.
- El ranking discriminante puede depender de incertidumbres observacionales, cobertura radial, priors y criterios estadísticos.
- Una galaxia con buen ajuste en varios modelos puede tener bajo poder discriminante si las predicciones son muy similares.
- Una galaxia con ajuste moderado puede ser científicamente útil si los modelos difieren de forma sistemática en regiones observadas.
- Un framework reproducible puede ayudar a comparar modelos de forma más justa y auditable.
- Los datos sintéticos permiten validar el pipeline antes de introducir complejidad observacional real.
- La incorporación de datasets reales debe hacerse después de validar estructura, unidades, tests y supuestos mínimos.

Pendiente de verificación: revisar literatura existente sobre selección de galaxias discriminantes, comparación entre MOND/RAR y halos, y metodologías similares.

## Alcance MVP

El MVP corresponde a una primera versión técnica y científica mínima. Su objetivo es demostrar que el pipeline funciona de extremo a extremo con datos sintéticos, sin pretender resultados científicos reales.

### Debe incluir

- Proyecto Python reproducible con:
  - Python 3.12;
  - `uv`;
  - `pyproject.toml`;
  - estructura `src/`;
  - `pytest`;
  - `ruff`;
  - `uv.lock`.
- Datos sintéticos/mock claramente marcados.
- Una representación básica de galaxias mock:
  - nombre;
  - radios;
  - velocidades observadas;
  - incertidumbres;
  - componentes simuladas si aplica.
- Modelos mínimos o placeholders controlados.
- Visualización básica de curva de rotación.
- Pipeline CLI o script ejecutable simple.
- Tests mínimos:
  - carga de datos mock;
  - forma esperada de arrays;
  - salida básica de modelo;
  - generación de resultados.
- README inicial con comandos de instalación, ejecución y tests.
- Documentación de límites del MVP.

### No debe incluir todavía

- Descarga de SPARC.
- Análisis científico real.
- Implementación completa de MOND/NFW/Burkert.
- Optimización sofisticada.
- MCMC.
- Dashboard web.
- IA.
- Reporte final de tesis.

Decisión tomada: el MVP debe validar arquitectura y reproducibilidad antes que profundidad física.

## Alcance científico inicial

El primer alcance científico real se planteará después del MVP, cuando el pipeline pueda trabajar con un dataset público inicial. SPARC es candidato natural por su relación con curvas de rotación, contribuciones bariónicas y estudios de dinámica galáctica, pero no debe asumirse su disponibilidad operativa sin verificación.

### Con un dataset público inicial se podría estudiar

- Comparación de ajuste entre modelos por galaxia.
- Identificación de galaxias donde los modelos producen predicciones similares.
- Identificación de galaxias donde los modelos divergen.
- Sensibilidad del ranking a incertidumbres observacionales.
- Sensibilidad del ranking a priors razonables.
- Relación entre poder discriminante y características observacionales:
  - rango radial;
  - número de puntos;
  - incertidumbre promedio;
  - forma de la curva;
  - dominancia bariónica;
  - régimen de baja aceleración.

### Pendientes de verificación

- Disponibilidad exacta de SPARC.
- Formato de archivos.
- Licencia de uso.
- Variables disponibles.
- Convenciones de unidades.
- Tratamiento de masa-luz.
- Papers base a revisar.
- Existencia de catálogos ampliados como BIG-SPARC u otros equivalentes.
- Existencia de herramientas previas similares.

## Modelos físicos iniciales

### Modelo newtoniano/bariónico base

| Campo | Descripción |
|---|---|
| Descripción breve | Modelo que calcula la contribución esperada de la materia bariónica visible a la curva de rotación. Puede incluir disco, gas y bulbo si los datos lo permiten. |
| Parámetros | Factores masa-luz, escala o normalización bariónica según disponibilidad del dataset. |
| Entrada esperada | Radios, componentes bariónicas o contribuciones precomputadas. |
| Salida esperada | Velocidad circular predicha para cada radio. |
| Riesgos | Confundir contribuciones observadas con derivaciones propias; errores de unidades; degeneración masa-luz. |
| Limitaciones | No explica por sí solo curvas planas extendidas en muchas galaxias; sirve como base comparativa. |

Decisión tomada: el modelo bariónico será tratado como baseline, no como explicación completa.

### MOND/RAR simple

| Campo | Descripción |
|---|---|
| Descripción breve | Modelo fenomenológico basado en una modificación efectiva de la relación entre aceleración bariónica y aceleración observada. |
| Parámetros | Aceleración característica, función de interpolación simple, posibles normalizaciones. |
| Entrada esperada | Aceleración o velocidad bariónica estimada en cada radio. |
| Salida esperada | Velocidad circular o aceleración efectiva predicha. |
| Riesgos | Implementar una formulación incorrecta; mezclar versiones distintas de MOND/RAR; no documentar función de interpolación. |
| Limitaciones | Requiere cuidado matemático y revisión de literatura; no debe usarse como caja negra. |

Pendiente de verificación: elegir una formulación inicial defendible y documentada antes de v0.2.

### Halo NFW

| Campo | Descripción |
|---|---|
| Descripción breve | Modelo de halo de materia oscura con perfil de densidad NFW. Es un perfil usado ampliamente en el contexto de estructuras cosmológicas. |
| Parámetros | Masa o densidad característica, radio de escala, concentración o parametrización equivalente. |
| Entrada esperada | Radios y parámetros del halo. |
| Salida esperada | Velocidad circular asociada al halo en cada radio. |
| Riesgos | Parametrizaciones no equivalentes; degeneración de parámetros; rangos físicos inadecuados. |
| Limitaciones | Puede no ajustar bien núcleos de baja densidad en algunas galaxias; requiere priors razonables. |

Pendiente de verificación: definir parametrización exacta y unidades antes de implementación científica.

### Halo Burkert

| Campo | Descripción |
|---|---|
| Descripción breve | Modelo de halo con núcleo central, usado frecuentemente para representar perfiles menos cuspidados. |
| Parámetros | Densidad central, radio de núcleo o escala equivalente. |
| Entrada esperada | Radios y parámetros del halo. |
| Salida esperada | Velocidad circular asociada al halo. |
| Riesgos | Errores en expresión analítica; comparación injusta si priors difieren demasiado de NFW. |
| Limitaciones | Es fenomenológico y no representa por sí solo una solución cosmológica completa. |

Pendiente de verificación: revisar fórmula, unidades y parametrización antes de v0.2.

### Einasto

Extensión futura: incorporar perfil Einasto si el pipeline ya permite agregar modelos con bajo costo técnico. No debe implementarse en el MVP.

### Modelo híbrido simplificado

Extensión futura: incorporar un modelo híbrido que combine contribución bariónica, componente tipo halo y/o modificación efectiva. Requiere especial cuidado para no introducir parámetros excesivos que vuelvan injusta la comparación.

Riesgo: un modelo híbrido con demasiados grados de libertad puede ganar por flexibilidad, no por valor físico.

## Métricas discriminantes

El proyecto debe separar métricas de ajuste de métricas de discriminación. Un modelo puede ajustar bien y aun así no aportar una diferencia clara frente a otros.

### Métricas de ajuste

- Error cuadrático ponderado.
- Chi-cuadrado o métrica equivalente.
- Residuos por radio.
- Error relativo promedio.
- Métricas por región radial.

### Métricas penalizadas

- AIC.
- BIC.
- Penalización por número de parámetros.
- Comparación entre modelos con distinta flexibilidad.

Riesgo: AIC/BIC requieren supuestos estadísticos que deben documentarse.

### Métricas de diferencia entre predicciones

- Distancia entre curvas predichas por dos modelos.
- Diferencia normalizada por incertidumbre observacional.
- Diferencia máxima por región radial.
- Diferencia integrada en el rango observado.
- Separación entre modelos en regiones de baja aceleración.

Ejemplo conceptual:

```text
score_pairwise(model_a, model_b, galaxy) =
    average_over_radius(
        abs(v_model_a - v_model_b) / sigma_observed
    )
```

Este pseudocódigo no define aún la métrica final. Solo ilustra el tipo de comparación deseada.

### Robustez ante incertidumbres

- Repetición con ruido sintético.
- Perturbación de datos dentro de barras de error.
- Comparación de estabilidad del ranking.
- Intervalos de confianza del score discriminante.

### Sensibilidad a priors

- Comparar rankings bajo distintos rangos de parámetros.
- Detectar galaxias cuyo ranking cambia mucho al modificar priors.
- Marcar resultados inestables.

### Valor esperado de nueva observación

Extensión futura: estimar qué medición adicional reduciría más la ambigüedad entre modelos. Esto permitiría identificar galaxias prioritarias para observación futura.

### Clasificación de galaxias por utilidad discriminante

| Categoría | Definición operativa inicial |
|---|---|
| Alta utilidad | Modelos divergen de forma clara en regiones observadas y las métricas son robustas |
| Utilidad media | Hay diferencias, pero dependen de priors, errores o región radial |
| Baja utilidad | Modelos producen predicciones similares dentro de incertidumbres |
| Datos insuficientes | La calidad/cobertura de datos no permite comparación confiable |
| Prioritaria para observación | Nuevos datos podrían aumentar mucho su poder discriminante |

## Arquitectura conceptual

El sistema se dividirá en módulos con responsabilidades separadas.

```text
galaxy_discriminants/
    data/
        loaders
        validators
        mock_generators
    models/
        base_interface
        baryonic
        mond_rar
        nfw
        burkert
    fitting/
        optimizers
        priors
        result_objects
    metrics/
        fit_metrics
        model_comparison
        discriminant_scores
        robustness
    ranking/
        galaxy_ranking
        classification
    visualization/
        rotation_curves
        residuals
        ranking_plots
    reporting/
        export_tables
        run_summaries
    cli/
        commands
    config/
        schemas
```

### Principios de arquitectura

- Separar datos, modelos, fitting, métricas y visualización.
- Evitar lógica científica escondida dentro de scripts sueltos.
- Mantener interfaces comunes para modelos.
- Hacer que cada resultado sea exportable y auditable.
- Evitar dependencias pesadas en etapas tempranas.
- Priorizar tests y documentación desde v0.1.

## Pipeline científico

El flujo conceptual del proyecto será:

1. Carga de datos.
2. Validación de estructura, unidades y campos requeridos.
3. Preprocesamiento mínimo.
4. Cálculo o lectura de contribuciones relevantes.
5. Ajuste de modelos.
6. Evaluación de métricas de ajuste.
7. Evaluación de métricas discriminantes.
8. Ranking de galaxias.
9. Visualización.
10. Reporte.
11. Exportación de resultados.

Pseudocódigo conceptual:

```text
dataset = load_dataset(config)
validated_dataset = validate_dataset(dataset)

for galaxy in validated_dataset:
    observations = preprocess(galaxy)

    for model in selected_models:
        fit_result = fit_model(model, observations)
        store_fit_result(galaxy, model, fit_result)

    comparison = compare_models(galaxy, fit_results)
    score = compute_discriminant_score(galaxy, comparison)
    store_score(galaxy, score)

ranking = rank_galaxies(all_scores)
export_results(ranking, fit_results)
generate_report(ranking)
```

Este pseudocódigo no debe ser tratado como implementación final.

## Validación

### Tests unitarios

- Validar creación de objetos de datos.
- Validar formas de arrays.
- Validar que modelos devuelvan salidas con dimensiones correctas.
- Validar que métricas simples respondan valores esperados en casos controlados.
- Validar exportación de resultados.

### Tests con datos sintéticos

- Generar galaxias mock con curvas conocidas.
- Probar que el pipeline detecta diferencias artificiales entre modelos.
- Probar que el ranking sea reproducible con semilla fija.
- Probar que errores de entrada se detectan de forma clara.

### Control de unidades

- Documentar unidades esperadas:
  - radio;
  - velocidad;
  - aceleración;
  - masa si aplica.
- Validar que el sistema rechace datos incompletos.
- Evitar conversiones implícitas no documentadas.

### Recuperación de parámetros

En etapas posteriores, usar datos sintéticos generados con parámetros conocidos para verificar si el fitting puede recuperarlos dentro de tolerancias razonables.

### Sensibilidad a ruido

Agregar perturbaciones controladas a datos mock y estudiar si el ranking se mantiene estable.

### Reproducibilidad

- Fijar semillas donde corresponda.
- Exportar configuración usada por corrida.
- Registrar versión del paquete.
- Registrar fecha y comandos ejecutados.
- Mantener `uv.lock`.
- Evitar dependencias no registradas.

### Logging

- Registrar pasos principales del pipeline.
- Registrar advertencias sobre datos.
- Registrar modelos usados.
- Registrar fallos de ajuste sin interrumpir todo el dataset cuando sea posible.

## Riesgos científicos

| Riesgo | Descripción | Mitigación |
|---|---|---|
| Comparación injusta entre modelos | Modelos con más parámetros pueden ajustar mejor por flexibilidad | Usar AIC/BIC y documentar grados de libertad |
| Priors mal elegidos | Priors pueden forzar conclusiones | Reportar sensibilidad a priors |
| Datos insuficientes | Algunas galaxias no permiten distinguir modelos | Clasificar como datos insuficientes |
| Errores de unidades | Unidades inconsistentes pueden invalidar resultados | Validación explícita y tests |
| Implementación física incorrecta | Fórmulas o parametrizaciones pueden estar mal aplicadas | Revisar literatura y requerir tutoría si corresponde |
| Sobreinterpretación | Un ranking computacional no prueba una teoría | Documentar límites explícitamente |
| Sesgo por dataset | Un catálogo puede no representar toda la población galáctica | Marcar alcance del dataset y evitar generalizaciones |

## Riesgos técnicos

| Riesgo | Descripción | Mitigación |
|---|---|---|
| Codex avanza fuera de alcance | Puede implementar demasiado o mezclar etapas | Prompts quirúrgicos por patch |
| Scripts sueltos difíciles de mantener | El proyecto puede degradarse rápido | Paquete Python con módulos separados |
| Falta de tests | Cambios futuros pueden romper lógica | Tests desde v0.1 |
| Dependencias pesadas prematuras | Aumentan complejidad sin aportar al MVP | Mantener stack mínimo |
| Datos reales mal versionados | Datasets grandes o licenciados pueden terminar en Git | Separar `data/raw`, usar `.gitignore` |
| Resultados no reproducibles | Corridas no trazables | Configuración, semillas y exports |
| Visualizaciones ambiguas | Gráficos pueden sugerir conclusiones falsas | Etiquetas claras y documentación |

## Extensiones futuras

- Incorporación de BIG-SPARC u otros catálogos, si se verifican disponibilidad y licencia.
- IA explicable para detectar patrones en galaxias altamente discriminantes.
- Validación cruzada avanzada.
- Modelos híbridos simplificados.
- Perfil Einasto.
- Dashboard web para exploración interactiva.
- Auditoría cruzada con información de Gaia u otros catálogos, si es científicamente pertinente.
- Generación de reportes estilo LaTeX.
- Exportación de notebooks reproducibles.
- Módulo de recomendación de observaciones futuras.
- Comparación con frameworks o papers existentes.
- Integración con pipelines de publicación académica.

## Criterio de éxito del proyecto

El proyecto será exitoso si produce una herramienta clara, reproducible y extensible que permita:

- cargar curvas de rotación;
- comparar modelos bajo una interfaz común;
- calcular métricas de ajuste y discriminación;
- rankear galaxias por utilidad discriminante;
- documentar supuestos y límites;
- reproducir resultados con comandos simples;
- evitar afirmaciones científicas exageradas.

No se considerará éxito afirmar que un modelo físico es “verdadero” o “falso” sin una validación científica completa.
