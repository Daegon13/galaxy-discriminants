# galaxy-discriminants

Base computacional reproducible para desarrollar, en etapas posteriores, herramientas que comparen familias de modelos de curvas de rotación galáctica. La versión **v0.1** valida únicamente la arquitectura y el flujo de ejecución.

> [!WARNING]
> Todos los datos de v0.1 son **mock/sintéticos** y el predictor es un placeholder no científico. Los resultados no representan galaxias, catálogos ni conclusiones físicas reales.

## Requisitos e instalación

- Python 3.12
- [`uv`](https://docs.astral.sh/uv/)

Desde la raíz del repositorio:

```powershell
uv sync
uv run python --version
```

## Ejecutar el pipeline mock

```powershell
uv run python -m galaxy_discriminants.pipeline
```

La ejecución usa una semilla fija y crea en `outputs/`:

- `mock_rotation_curve.csv`: datos sintéticos y predicción placeholder;
- `mock_pipeline_summary.json`: metadatos y un diagnóstico RMSE básico;
- `mock_rotation_curve.png`: gráfico etiquetado explícitamente como mock/sintético.

Los artefactos generados dentro de `outputs/` no se versionan.

## Tests y lint

```powershell
uv run pytest
uv run ruff check .
```

## Estructura principal

```text
src/galaxy_discriminants/
├── data/                  # generación reproducible de datos sintéticos
├── models/                # interfaz y modelo placeholder no científico
├── visualization/         # gráfico básico de la curva mock
└── pipeline.py            # pipeline ejecutable de v0.1
tests/                     # tests unitarios y de integración mínima
data/mock/                 # espacio reservado para datos mock versionables
outputs/                   # artefactos locales generados por el pipeline
```

## Alcance y límites actuales

v0.1 incluye generación determinista de una curva sintética, una interfaz mínima de modelo, un predictor de velocidad constante, exportación CSV/JSON, visualización con Matplotlib y tests. El RMSE exportado sirve sólo para comprobar el flujo de software; no es un resultado científico ni un ranking discriminante.

Esta versión **no** incluye datos reales ni SPARC, implementaciones físicas de MOND/RAR, NFW o Burkert, inferencia estadística, ranking real de galaxias ni conclusiones científicas.

## Próximos pasos

El siguiente patch sugerido es **v0.2**, sujeto a revisión y aprobación separadas. Puede introducir los primeros componentes científicos acotados sin alterar la separación entre datos, modelos, visualización y pipeline establecida aquí.
