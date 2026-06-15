# Decisions Log

## Propósito

Este archivo registra decisiones técnicas, científicas y metodológicas del proyecto. Su objetivo es mantener trazabilidad y evitar cambios de alcance no documentados.

Cada decisión debe indicar motivo, alternativas consideradas, estado y consecuencias.

## Tabla de decisiones

| ID | Fecha | Decisión | Motivo | Alternativas consideradas | Estado | Consecuencias |
|---|---|---|---|---|---|---|
| D-001 | 2026-06-05 | Usar enfoque incremental por patches | Reducir riesgo, controlar alcance y facilitar auditoría después de cada intervención de Codex | Implementar todo el proyecto en una sola etapa | Decisión tomada | Cada versión tendrá criterios de aceptación y límites explícitos |
| D-002 | 2026-06-05 | Separar chat estratégico de Codex | Mantener diseño, auditoría y ejecución en roles separados | Usar Codex para decidir arquitectura y programar simultáneamente | Decisión tomada | Este chat define prompts y audita; Codex implementa patches concretos |
| D-003 | 2026-06-05 | No empezar con simulación N-body | Sería demasiado grande para una primera tesis/prototipo y desviaría el foco | Simulación cosmológica o dinámica avanzada desde el inicio | Decisión tomada | El proyecto se concentra en curvas de rotación y comparación de modelos |
| D-004 | 2026-06-05 | No prometer nueva teoría de gravedad ni resolver materia oscura | Mantener honestidad científica y defendibilidad académica | Presentar el proyecto como descubrimiento teórico | Decisión tomada | El proyecto se formula como herramienta computacional reproducible |
| D-005 | 2026-06-05 | Empezar con datos mock antes de datasets reales | Validar arquitectura, tests y pipeline sin depender de disponibilidad externa | Descargar SPARC desde el primer patch | Decisión tomada | v0.1 usa datos sintéticos claramente marcados |
| D-006 | 2026-06-05 | Priorizar selección de galaxias discriminantes sobre ajuste global promedio | La pregunta central es qué galaxias distinguen mejor modelos, no solo qué modelo ajusta mejor en promedio | Hacer ranking global de modelos únicamente | Decisión tomada | Las métricas deben separar ajuste de poder discriminante |
| D-007 | 2026-06-05 | Preparar arquitectura extensible hacia SPARC/BIG-SPARC | Permitir incorporación futura de catálogos reales sin reescribir el proyecto | Diseñar solo para datos mock | Decisión tomada | Los loaders y validadores deberán aislar formatos de datos |
| D-008 | 2026-06-05 | Mantener documentación científica honesta | Evitar sobreinterpretación, claims débiles o confusión entre supuestos y resultados | Documentar solo uso técnico | Decisión tomada | Los Markdown deben distinguir hechos, supuestos, riesgos y pendientes |
| D-009 | 2026-06-05 | Usar Python 3.12 | Priorizar estabilidad y compatibilidad científica | Usar Python global 3.13 | Decisión tomada | El proyecto fija `.python-version` y debe ejecutarse con Python 3.12.x |
| D-010 | 2026-06-05 | Usar `uv` como gestor de proyecto y dependencias | Mejorar reproducibilidad, lockfile y comandos consistentes | `pip`, `venv`, Poetry o Conda | Decisión tomada | El flujo estándar será `uv sync`, `uv run pytest`, `uv run ruff check .` |
| D-011 | 2026-06-05 | Usar estructura `src/` | Evitar imports accidentales desde la raíz y mejorar calidad de paquete | Código en scripts sueltos o paquete plano | Decisión tomada | El código principal vive en `src/galaxy_discriminants/` |
| D-012 | 2026-06-05 | Usar `pytest` para tests | Estándar simple y suficiente para validar pipeline científico inicial | Tests manuales o notebooks | Decisión tomada | Cada patch debe mantener o mejorar cobertura mínima |
| D-013 | 2026-06-05 | Usar `ruff` para lint/formato | Mantener consistencia de estilo y detectar errores simples | Flake8, Black, isort separados | Decisión tomada | Todo patch debe pasar `uv run ruff check .` |
| D-014 | 2026-06-05 | Mantener datasets reales fuera del primer patch | Evitar problemas de licencia, formato y peso del repositorio | Descargar datos reales inmediatamente | Decisión tomada | `data/raw` queda preparado pero no usado en v0.1 |
| D-015 | 2026-06-05 | No implementar IA en el MVP | Evitar complejidad decorativa sin aporte científico inicial | Agregar ML/IA desde el inicio | Decisión tomada | IA explicable queda como extensión futura |
| D-016 | 2026-06-05 | Separar métricas de ajuste y métricas discriminantes | Un buen ajuste no implica alto poder para distinguir modelos | Usar solo chi-cuadrado o error promedio | Decisión tomada | El diseño futuro debe incluir scores discriminantes independientes |
| D-017 | 2026-06-05 | Tratar SPARC como candidato pendiente de verificación | No asumir rutas, APIs, licencia ni formato | Basar el proyecto desde el inicio en SPARC | Decisión tomada | Antes de v0.5 se debe verificar disponibilidad y formato |
| D-018 | 2026-06-05 | No usar framework web en v0.1 | El objetivo inicial es científico/reproducible, no interfaz | Streamlit, Dash, Next.js o dashboard temprano | Decisión tomada | Dashboard queda como extensión futura |
| D-019 | 2026-06-05 | Auditar cada summary de Codex antes de continuar | Prevenir deriva de alcance y errores acumulados | Aceptar automáticamente cada patch | Decisión tomada | El usuario pegará summary y este chat decidirá siguiente prompt |
| D-020 | 2026-06-05 | Documentar riesgos científicos y técnicos desde el inicio | Hacer el proyecto defendible y honesto | Documentar solo resultados positivos | Decisión tomada | Los reportes deben incluir limitaciones explícitas |
| D-021 | 2026-06-10 | Seleccionar una relación empírica RAR como primera formulación MOND/RAR implementable | Trabaja directamente con `g_bar`, encaja con la capa de aceleraciones y permite tests controlados de sus límites | MOND con función de interpolación simple; MOND con función de interpolación estándar | Decisión tomada | `docs/mond_rar_design.md` fija la ecuación, el dominio, las unidades, las entradas, las salidas y los tests previstos para v0.2b-4 |
| D-022 | 2026-06-10 | Mantener MOND/RAR sin implementación ejecutable durante v0.2b-3 | Separar la selección y revisión de la formulación de su codificación para evitar semántica científica improvisada | Convertir inmediatamente `MondRARPlaceholderModel` en modelo físico | Decisión tomada | El stub MOND/RAR y los stubs NFW/Burkert permanecen sin física hasta un patch posterior explícito |
| D-023 | 2026-06-10 | Tratar `g_dagger = 1.2e-10 m/s²` solo como valor inicial de trabajo | Permitir diseñar el contrato y los tests sin declarar prematuramente una constante científica definitiva | Añadirlo ya como constante fija en código; omitir un default inicial | Decisión tomada | El valor queda documentado, pendiente de verificación científica y sujeto a cambio tras revisar literatura y datasets |
| D-024 | 2026-06-10 | Mantener las funciones de interpolación MOND simple y estándar como alternativas futuras | Reconocer opciones relevantes sin implementar ecuaciones o convenciones no verificadas | Implementarlas junto con la primera RAR; descartarlas definitivamente | Decisión tomada | Sus definiciones exactas, convenciones y aplicabilidad deberán verificarse antes de otro patch |

## Pendientes de verificación

### Datasets

- Pendiente de verificación: disponibilidad exacta de SPARC.
- Pendiente de verificación: formato actual de archivos de SPARC.
- Pendiente de verificación: licencia de uso de SPARC.
- Pendiente de verificación: condiciones de redistribución de datos.
- Pendiente de verificación: variables disponibles para curvas de rotación y componentes bariónicas.
- Pendiente de verificación: convenciones de unidades.
- Pendiente de verificación: existencia, disponibilidad y licencia de BIG-SPARC u otros catálogos ampliados.

### Literatura científica

- Pendiente de verificación: papers base sobre SPARC.
- Pendiente de verificación: papers base sobre MOND/RAR aplicados a curvas de rotación.
- Pendiente de verificación: formulación inicial defendible para MOND/RAR.
- Pendiente de verificación: parametrización exacta de NFW a usar.
- Pendiente de verificación: parametrización exacta de Burkert a usar.
- Pendiente de verificación: criterios estadísticos apropiados para comparación entre modelos.
- Pendiente de verificación: metodologías existentes de selección de objetos discriminantes.

### Software y frameworks similares

- Pendiente de verificación: existencia de herramientas abiertas similares.
- Pendiente de verificación: paquetes Python científicos útiles para curvas de rotación galáctica.
- Pendiente de verificación: convenciones comunes de datos en astrofísica para este problema.
- Pendiente de verificación: si conviene usar `astropy` en una etapa futura.
- Pendiente de verificación: si conviene usar notebooks como capa exploratoria, sin reemplazar el paquete.

### Requisitos matemáticos

- Pendiente de verificación: nivel mínimo necesario de dinámica galáctica.
- Pendiente de verificación: tratamiento correcto de incertidumbres observacionales.
- Pendiente de verificación: uso adecuado de AIC/BIC en modelos no lineales.
- Pendiente de verificación: degeneración de parámetros en halos.
- Pendiente de verificación: priors físicamente razonables.
- Pendiente de verificación: necesidad de tutoría científica externa.

### Tutoría y revisión

- Pendiente de verificación: posible tutor académico o científico.
- Pendiente de verificación: revisión externa de fórmulas físicas.
- Pendiente de verificación: revisión de resultados antes de afirmar conclusiones.
- Pendiente de verificación: estándares mínimos para convertir el prototipo en tesis.

## Reglas para nuevas decisiones

Cuando aparezca una decisión relevante, agregar una fila con:

- ID incremental.
- Fecha.
- Decisión.
- Motivo.
- Alternativas consideradas.
- Estado.
- Consecuencias.

Estados sugeridos:

- Propuesta.
- Decisión tomada.
- Revertida.
- Pendiente.
- En revisión.

## Regla de honestidad científica

Toda afirmación científica debe clasificarse como:

- hecho verificado;
- supuesto;
- resultado computacional;
- interpretación;
- pendiente de verificación.

Decisión tomada: si una afirmación no puede verificarse todavía, debe marcarse explícitamente como pendiente de verificación.
