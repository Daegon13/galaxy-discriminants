# Patch Roadmap

## Principios del roadmap

El proyecto se desarrollará mediante versiones incrementales. Cada patch debe tener alcance limitado, criterios de aceptación claros y una separación explícita entre lo que se implementa ahora y lo que queda fuera.

Decisión tomada: Codex ejecutará un patch concreto por vez. Este chat estratégico auditará el summary de Codex antes de generar el siguiente prompt.

Supuesto: el repositorio ya fue inicializado como paquete Python reproducible con Python 3.12, `uv`, estructura `src/`, `pytest`, `ruff`, `pyproject.toml` y `uv.lock`.

## v0.1 — Skeleton reproducible con datos mock

### Objetivo

Crear una base técnica mínima, reproducible y testeable para ejecutar un pipeline simple con datos sintéticos/mock. Esta versión no busca resultados científicos reales.

### Alcance

- Consolidar estructura profesional de carpetas.
- Crear generador o archivo de datos mock claramente identificado.
- Crear modelos placeholder o mínimos sin pretensión científica.
- Crear visualización básica de una curva de rotación mock.
- Crear una función o comando simple para ejecutar el flujo mínimo.
- Agregar tests mínimos.
- Completar README inicial.
- Mantener compatibilidad con `uv`, Python 3.12, `pytest` y `ruff`.

### Archivos probables

```text
README.md
pyproject.toml
src/galaxy_discriminants/__init__.py
src/galaxy_discriminants/data/
src/galaxy_discriminants/data/mock.py
src/galaxy_discriminants/models/
src/galaxy_discriminants/models/base.py
src/galaxy_discriminants/models/placeholders.py
src/galaxy_discriminants/visualization/
src/galaxy_discriminants/visualization/rotation_curves.py
src/galaxy_discriminants/pipeline.py
tests/
tests/test_mock_data.py
tests/test_placeholder_models.py
tests/test_pipeline.py
data/mock/
outputs/
```

### Criterios de aceptación

- [ ] `uv sync` funciona.
- [ ] `uv run python --version` usa Python 3.12.
- [ ] `uv run pytest` pasa.
- [ ] `uv run ruff check .` pasa.
- [ ] El README explica instalación, ejecución y tests.
- [ ] Los datos mock están claramente marcados como sintéticos.
- [ ] No se descargan datasets reales.
- [ ] No se implementan conclusiones científicas.
- [ ] El pipeline mínimo genera una salida verificable.
- [ ] La visualización básica se puede generar sin configuración compleja.

### Qué NO debe hacerse todavía

- No implementar MOND/RAR real.
- No implementar NFW real.
- No implementar Burkert real.
- No descargar SPARC.
- No agregar dashboard web.
- No agregar IA.
- No implementar MCMC.
- No hacer claims científicos.

### Riesgos

| Riesgo | Mitigación |
|---|---|
| Codex implementa física real prematuramente | Indicar explícitamente placeholders o modelos mínimos |
| Se mezclan datos mock con datos reales | Usar nombres claros y documentación |
| La estructura queda demasiado compleja | Mantener módulos mínimos |
| Tests triviales sin utilidad | Validar shapes, reproducibilidad y salidas esperadas |

### Resultado esperado

Un repositorio que permita ejecutar un flujo mínimo reproducible con datos mock, tests y documentación inicial. Debe quedar listo para implementar modelos físicos iniciales en v0.2.

## v0.2 — Modelos físicos iniciales

### Objetivo

Implementar una primera interfaz común para modelos de curvas de rotación y agregar modelos físicos iniciales con documentación de supuestos.

### Alcance

- Definir interfaz común de modelos.
- Implementar modelo newtoniano/bariónico base.
- Implementar MOND/RAR simple.
- Implementar halo NFW.
- Implementar halo Burkert.
- Agregar tests unitarios para cada modelo.
- Documentar fórmulas, parámetros y unidades esperadas.
- Mantener datos mock como mecanismo de validación.

### Archivos probables

```text
src/galaxy_discriminants/models/base.py
src/galaxy_discriminants/models/baryonic.py
src/galaxy_discriminants/models/mond_rar.py
src/galaxy_discriminants/models/nfw.py
src/galaxy_discriminants/models/burkert.py
src/galaxy_discriminants/units.py
tests/test_models_baryonic.py
tests/test_models_mond_rar.py
tests/test_models_nfw.py
tests/test_models_burkert.py
docs/model_assumptions.md
```

### Criterios de aceptación

- [ ] Todos los modelos exponen una interfaz común.
- [ ] Cada modelo recibe radios y parámetros explícitos.
- [ ] Cada modelo devuelve velocidades o aceleraciones con dimensiones correctas.
- [ ] Las unidades esperadas están documentadas.
- [ ] Los tests cubren casos simples.
- [ ] Las fórmulas usadas están documentadas como pendientes de revisión científica si aún no fueron auditadas.
- [ ] No se mezclan modelos físicos con fitting avanzado todavía.

### Qué NO debe hacerse todavía

- No implementar fitting completo.
- No implementar ranking discriminante.
- No descargar datasets reales.
- No introducir modelos híbridos.
- No hacer optimización bayesiana.
- No afirmar que un modelo es mejor científicamente.

### Riesgos

| Riesgo | Mitigación |
|---|---|
| Fórmulas incorrectas | Marcar fórmulas para revisión y testear casos límite |
| Inconsistencia de unidades | Centralizar unidades esperadas |
| Interfaz rígida | Diseñar base extensible |
| Comparación injusta | No comparar todavía sin fitting y métricas |

### Resultado esperado

Una base de modelos iniciales consistente y testeada, lista para integrarse en un sistema de ajuste en v0.3.

## v0.3 — Ajuste y métricas básicas

### Objetivo

Implementar ajuste de parámetros y métricas básicas de error para comparar modelos por galaxia.

### Alcance

- Crear módulo de fitting.
- Definir objeto de resultado de ajuste.
- Implementar ajuste determinista simple con `scipy`.
- Calcular errores de ajuste.
- Calcular AIC/BIC.
- Exportar resultados por galaxia y modelo.
- Agregar tests con datos mock de parámetros conocidos.

### Archivos probables

```text
src/galaxy_discriminants/fitting/
src/galaxy_discriminants/fitting/fitters.py
src/galaxy_discriminants/fitting/results.py
src/galaxy_discriminants/metrics/
src/galaxy_discriminants/metrics/fit.py
src/galaxy_discriminants/io/
src/galaxy_discriminants/io/export.py
tests/test_fitting.py
tests/test_fit_metrics.py
tests/test_export_results.py
```

### Criterios de aceptación

- [ ] El fitting corre sobre datos mock.
- [ ] Los resultados incluyen parámetros, error y estado del ajuste.
- [ ] AIC/BIC se calculan con número de parámetros documentado.
- [ ] Los errores de ajuste son reproducibles.
- [ ] Los resultados se exportan a un formato tabular.
- [ ] Los tests pasan con `uv run pytest`.
- [ ] Ruff pasa sin errores.

### Qué NO debe hacerse todavía

- No implementar ranking discriminante completo.
- No hacer análisis sobre SPARC.
- No implementar MCMC.
- No optimizar rendimiento.
- No crear dashboard.

### Riesgos

| Riesgo | Mitigación |
|---|---|
| Fitting inestable | Usar casos mock controlados |
| Parámetros no identificables | Documentar degeneraciones |
| AIC/BIC mal aplicados | Documentar supuestos estadísticos |
| Resultados difíciles de auditar | Exportar objetos claros y tablas |

### Resultado esperado

El sistema puede ajustar modelos simples a galaxias mock y exportar métricas básicas por modelo.

## v0.4 — Ranking discriminante

### Objetivo

Implementar un score discriminante inicial para rankear galaxias según su utilidad para distinguir entre modelos.

### Alcance

- Crear módulo de comparación entre modelos.
- Implementar distancia entre predicciones.
- Normalizar diferencias por incertidumbre observacional.
- Combinar métricas de ajuste y diferencia entre modelos.
- Clasificar galaxias por utilidad discriminante.
- Visualizar ranking.
- Exportar ranking final.

### Archivos probables

```text
src/galaxy_discriminants/metrics/discrimination.py
src/galaxy_discriminants/ranking/
src/galaxy_discriminants/ranking/scoring.py
src/galaxy_discriminants/ranking/classification.py
src/galaxy_discriminants/visualization/ranking.py
tests/test_discrimination_metrics.py
tests/test_ranking.py
tests/test_classification.py
```

### Criterios de aceptación

- [ ] Existe un score discriminante documentado.
- [ ] El ranking se genera para un conjunto de galaxias mock.
- [ ] La clasificación distingue utilidad alta, media, baja y datos insuficientes.
- [ ] La métrica no depende solo del mejor ajuste.
- [ ] Las visualizaciones de ranking se generan.
- [ ] Los resultados son reproducibles.
- [ ] Tests y Ruff pasan.

### Qué NO debe hacerse todavía

- No usar dataset real sin adaptador validado.
- No presentar resultados como conclusión científica.
- No agregar IA explicable todavía.
- No implementar valor esperado de nueva observación salvo como documentación futura.

### Riesgos

| Riesgo | Mitigación |
|---|---|
| Score arbitrario | Documentar fórmula y límites |
| Ranking sensible a escala | Normalizar por incertidumbre |
| Clasificación engañosa | Incluir categoría “datos insuficientes” |
| Sobreinterpretación | Reportar límites explícitos |

### Resultado esperado

El proyecto puede generar un ranking discriminante inicial sobre datos mock y explicar por qué una galaxia fue clasificada de cierta manera.

## v0.5 — Dataset real inicial

### Objetivo

Incorporar un adaptador para un dataset real inicial, probablemente SPARC si se verifica su disponibilidad, formato y licencia.

### Alcance

- Documentar dataset elegido.
- Crear adaptador de carga.
- Separar `data/raw` y `data/processed`.
- Validar campos requeridos.
- Documentar unidades.
- Probar pipeline con un subconjunto pequeño.
- Mantener datos reales fuera del repo si la licencia o tamaño lo requieren.

### Archivos probables

```text
docs/datasets.md
src/galaxy_discriminants/data/loaders.py
src/galaxy_discriminants/data/validators.py
src/galaxy_discriminants/data/schemas.py
src/galaxy_discriminants/data/preprocessing.py
tests/test_dataset_loader.py
tests/test_dataset_validation.py
```

### Criterios de aceptación

- [ ] La disponibilidad del dataset fue verificada.
- [ ] La licencia fue revisada.
- [ ] El formato está documentado.
- [ ] El loader valida columnas/campos requeridos.
- [ ] Los datos raw no se suben accidentalmente si no corresponde.
- [ ] El pipeline puede correr sobre un subconjunto real.
- [ ] Las limitaciones del dataset están documentadas.

### Qué NO debe hacerse todavía

- No analizar todo el dataset sin validación.
- No publicar resultados sin revisión.
- No asumir que SPARC es automáticamente usable.
- No agregar BIG-SPARC todavía.
- No mezclar transformación de datos con fitting.

### Riesgos

| Riesgo | Mitigación |
|---|---|
| Dataset no accesible | Tener adaptador abstracto y mantener mock |
| Licencia restrictiva | No subir datos raw al repo |
| Formato ambiguo | Documentar parsing y validación |
| Unidades inconsistentes | Validación explícita |

### Resultado esperado

El proyecto puede leer un dataset real verificado o un subconjunto controlado, validarlo y prepararlo para el pipeline.

## v0.6 — Sensibilidad e incertidumbres

### Objetivo

Evaluar robustez del ranking discriminante ante ruido, incertidumbres observacionales y cambios de priors.

### Alcance

- Agregar ruido sintético controlado.
- Ejecutar múltiples corridas con semilla.
- Evaluar estabilidad del ranking.
- Medir sensibilidad a priors.
- Generar reportes por galaxia.
- Exportar intervalos o medidas de dispersión del score.

### Archivos probables

```text
src/galaxy_discriminants/uncertainty/
src/galaxy_discriminants/uncertainty/noise.py
src/galaxy_discriminants/uncertainty/priors.py
src/galaxy_discriminants/uncertainty/robustness.py
src/galaxy_discriminants/reporting/
src/galaxy_discriminants/reporting/galaxy_report.py
tests/test_noise.py
tests/test_prior_sensitivity.py
tests/test_robustness.py
```

### Criterios de aceptación

- [ ] Se pueden correr perturbaciones reproducibles.
- [ ] Se calcula estabilidad del ranking.
- [ ] Se reportan galaxias sensibles a priors.
- [ ] Se exportan reportes por galaxia.
- [ ] Se documentan límites del análisis.
- [ ] Tests y Ruff pasan.

### Qué NO debe hacerse todavía

- No implementar MCMC completo salvo decisión futura.
- No hacer claims fuertes con incertidumbre parcial.
- No agregar observación futura salvo como extensión conceptual.
- No introducir modelos nuevos sin necesidad.

### Riesgos

| Riesgo | Mitigación |
|---|---|
| Costo computacional alto | Mantener corridas pequeñas y configurables |
| Incertidumbre mal modelada | Documentar supuestos y empezar simple |
| Ranking inestable | Reportar inestabilidad como resultado |
| Priors arbitrarios | Comparar escenarios y no ocultarlos |

### Resultado esperado

El proyecto puede indicar no solo qué galaxias parecen discriminantes, sino también qué tan robusto es ese ranking.

## v1.0 — Prototipo tesis

### Objetivo

Consolidar un prototipo completo, documentado y reproducible, apto para presentación de tesis/proyecto académico inicial.

### Alcance

- Pipeline completo desde datos hasta reporte.
- Modelos iniciales implementados y documentados.
- Fitting y métricas.
- Ranking discriminante.
- Dataset real inicial si fue verificado.
- Sensibilidad e incertidumbres.
- Visualizaciones.
- Resultados reproducibles.
- Reporte técnico.
- Limitaciones explícitas.
- Guía de instalación y ejecución.

### Archivos probables

```text
README.md
docs/
reports/
outputs/
src/galaxy_discriminants/
tests/
notebooks/
```

### Criterios de aceptación

- [ ] El pipeline completo se ejecuta con un comando documentado.
- [ ] Los resultados son reproducibles.
- [ ] Los tests pasan.
- [ ] Ruff pasa.
- [ ] El reporte técnico explica metodología y límites.
- [ ] La documentación distingue hechos, supuestos y pendientes.
- [ ] El proyecto no promete descubrimientos que no demuestra.
- [ ] El repositorio está ordenado para revisión externa.

### Qué NO debe hacerse todavía

- No escalar a cosmología completa.
- No presentar resultados como prueba definitiva.
- No inflar el alcance con dashboard, IA o modelos avanzados si no son necesarios.
- No esconder limitaciones.

### Riesgos

| Riesgo | Mitigación |
|---|---|
| Alcance demasiado grande | Congelar funcionalidades para v1.0 |
| Falta de revisión científica | Buscar tutoría o revisión externa |
| Resultados frágiles | Reportar sensibilidad y límites |
| Complejidad técnica excesiva | Mantener pipeline simple y auditable |

### Resultado esperado

Un prototipo defendible como proyecto de física computacional, con foco en metodología reproducible para selección de galaxias discriminantes.

## Flujo de trabajo por patch

Cada patch debe seguir este ciclo:

1. Este chat estratégico define el prompt.
2. Codex implementa solo el patch pedido.
3. El usuario pega el summary de Codex.
4. Este chat audita:
   - alcance;
   - archivos modificados;
   - tests;
   - riesgos;
   - desviaciones;
   - próximos pasos.
5. Se genera el siguiente prompt.

## Regla de control de alcance

Si Codex implementa algo fuera del patch solicitado, se debe decidir explícitamente si:

- se acepta;
- se revierte;
- se mueve a un patch futuro;
- se documenta como deuda técnica.

Decisión tomada: no avanzar a la siguiente versión sin auditoría del summary.
