# Galaxy Discriminants

Herramienta/prototipo de física computacional para estudiar curvas de rotación galáctica y seleccionar galaxias con mayor utilidad discriminante entre familias de modelos.

## Estado del proyecto

Estado actual: fase inicial de tesis/prototipo.

El repositorio ya fue inicializado como paquete Python reproducible con:

- Python 3.12
- `uv`
- estructura `src/`
- `pytest`
- `ruff`
- `pyproject.toml`
- `uv.lock`

La implementación actual corresponde a `v0.2b-2 — Utilidades de aceleración bariónica y preparación MOND/RAR`. Conserva el pipeline mock y el baseline bariónico previo, y agrega conversiones validadas entre radio, velocidad circular y aceleración sin implementar todavía un modelo físico MOND/RAR.

## Objetivo

Construir un framework computacional reproducible para responder la pregunta:

> Dado un conjunto de curvas de rotación galáctica y varios modelos competidores, ¿qué galaxias son más útiles para discriminar entre MOND/RAR, halos de materia oscura y modelos híbridos?

El objetivo no es resolver el problema de la materia oscura ni proponer una nueva teoría de gravedad. El objetivo es construir una herramienta clara, testeable y extensible para comparar modelos y rankear galaxias por utilidad discriminante.

## Alcance científico

El proyecto apunta a comparar familias de modelos como:

- modelo bariónico/newtoniano base;
- MOND/RAR con función de interpolación simple;
- halo NFW;
- halo Burkert;
- modelos futuros como Einasto o híbridos simplificados.

SPARC y otros catálogos reales se tratan como candidatos futuros. Su disponibilidad, formato, licencia y condiciones de uso están pendientes de verificación.

## Alcance actual

En `v0.2b-2`, el proyecto incluye:

- datos mock claramente marcados y reproducibles;
- pipeline ejecutable, exportación y visualización de v0.1;
- interfaz común para modelos de curvas de rotación;
- predicciones validadas con radios en `kpc` y velocidades en `km/s`;
- validaciones básicas para arreglos científicos;
- un modelo bariónico/newtoniano mínimo que combina componentes precomputadas en suma cuadrática;
- constantes explícitas de conversión y utilidades validadas entre `kpc`, `km/s` y `m/s²`;
- stubs nominales de MOND/RAR, NFW y Burkert que lanzan `NotImplementedError`;
- tests de interfaz, validación, placeholders y compatibilidad del pipeline.

En `v0.2b-2`, el proyecto todavía no incluye:

- descarga o uso de datasets reales como SPARC o BIG-SPARC;
- análisis científico real;
- fórmulas físicas reales de MOND/RAR, NFW o Burkert;
- fitting, AIC/BIC o ranking discriminante;
- MCMC, simulaciones N-body, dashboard web o IA/ML.

## Instalación

Desde la raíz del repositorio:

```powershell
uv sync
```

Verificar versión de Python:

```powershell
uv run python --version
```

Resultado esperado:

```text
Python 3.12.x
```

## Comandos de desarrollo

Ejecutar tests:

```powershell
uv run pytest
```

Ejecutar lint:

```powershell
uv run ruff check .
```

Formatear código:

```powershell
uv run ruff format .
```

## Ejecución del pipeline

El pipeline mock compatible con v0.1 se ejecuta con:

```powershell
uv run python -m galaxy_discriminants.pipeline
```

Las salidas generadas se guardan en `outputs/` y no se versionan. Son artefactos sintéticos para comprobar el software, no resultados científicos.

## Estructura esperada del repositorio

```text
galaxy-discriminants/
├── AGENTS.md
├── README.md
├── PROJECT_MASTERPLAN.md
├── PATCH_ROADMAP.md
├── CODEX_TASK_PROMPT.md
├── DECISIONS_LOG.md
├── pyproject.toml
├── uv.lock
├── .python-version
├── src/
│   └── galaxy_discriminants/
├── tests/
├── data/
│   ├── mock/
│   ├── raw/
│   └── processed/
├── outputs/
└── reports/
```

## Documentación principal

- `PROJECT_MASTERPLAN.md`: visión científica, técnica y metodológica.
- `docs/model_assumptions.md`: supuestos de unidades, validación e infraestructura de modelos.
- `PATCH_ROADMAP.md`: roadmap por versiones incrementales.
- `CODEX_TASK_PROMPT.md`: prompt activo para Codex.
- `DECISIONS_LOG.md`: decisiones tomadas y pendientes de verificación.
- `AGENTS.md`: instrucciones permanentes para Codex/agentes.

## Flujo de trabajo

1. Este chat estratégico define el alcance.
2. `CODEX_TASK_PROMPT.md` contiene el patch activo.
3. Codex implementa solo ese patch.
4. El summary de Codex se audita antes de avanzar.
5. El siguiente patch se genera únicamente después de revisar resultados.

## Reglas científicas

Toda afirmación científica debe distinguir entre:

- hecho verificado;
- supuesto;
- pendiente de verificación;
- resultado computacional;
- interpretación;
- extensión futura.

Los datos mock no permiten conclusiones científicas sobre MOND, materia oscura, halos, SPARC ni galaxias reales.

## Reglas de datos

No subir datasets reales al repositorio sin aprobación explícita.

Uso previsto de carpetas:

- `data/mock/`: datos sintéticos.
- `data/raw/`: datos externos sin procesar.
- `data/processed/`: datos procesados.
- `outputs/`: salidas generadas.
- `reports/`: reportes generados.

## Roadmap resumido

| Versión | Objetivo |
|---|---|
| v0.1 | Skeleton reproducible con datos mock |
| v0.2 | Modelos físicos iniciales |
| v0.3 | Ajuste y métricas básicas |
| v0.4 | Ranking discriminante |
| v0.5 | Dataset real inicial |
| v0.6 | Sensibilidad e incertidumbres |
| v1.0 | Prototipo tesis |

Ver `PATCH_ROADMAP.md` para detalle completo.

## Criterio de éxito

El proyecto será exitoso si permite:

- cargar o generar curvas de rotación;
- comparar modelos bajo una interfaz común;
- calcular métricas de ajuste y discriminación;
- rankear galaxias por utilidad discriminante;
- documentar supuestos y límites;
- reproducir resultados con comandos simples;
- evitar afirmaciones científicas exageradas.

No se considerará éxito afirmar que un modelo físico es verdadero o falso sin validación científica completa.
