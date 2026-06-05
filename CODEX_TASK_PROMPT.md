# Codex Task Prompt — v0.1 Skeleton reproducible con datos mock

## Rol

Actúa como ingeniero de software científico trabajando sobre un repositorio Python ya inicializado. Tu tarea es implementar únicamente el patch `v0.1 — Skeleton reproducible con datos mock`.

No debes avanzar a modelos físicos reales ni análisis científico completo.

## Contexto del proyecto

El proyecto se llama `galaxy-discriminants`.

Objetivo general:

Construir una herramienta computacional reproducible para identificar qué galaxias tienen mayor poder discriminante al comparar familias de modelos de curvas de rotación galáctica, incluyendo modelos bariónicos/newtonianos, MOND/RAR, halos de materia oscura y posibles modelos híbridos futuros.

La primera versión no debe producir resultados científicos reales. Debe crear una base técnica profesional que permita correr un pipeline mínimo con datos sintéticos/mock.

## Estado actual esperado del repositorio

El repositorio ya fue inicializado con:

- Python 3.12.
- `uv`.
- `pyproject.toml`.
- `uv.lock`.
- estructura `src/`.
- paquete `galaxy_discriminants`.
- `ruff`.
- `pytest`.
- carpetas base:
  - `data/mock`;
  - `data/raw`;
  - `data/processed`;
  - `outputs`;
  - `reports`.
- documentación base:
  - `PROJECT_MASTERPLAN.md`;
  - `PATCH_ROADMAP.md`;
  - `CODEX_TASK_PROMPT.md`;
  - `DECISIONS_LOG.md`;
  - `README.md`.

Comandos ya verificados antes de este patch:

```powershell
uv sync
uv run python --version
uv run ruff check .
```

Python esperado:

```text
Python 3.12.x
```

## Instrucciones generales

Antes de modificar archivos:

1. Inspecciona el repositorio actual.
2. Revisa `pyproject.toml`.
3. Revisa la estructura existente.
4. No asumas que el repo está vacío.
5. No reinicialices Git.
6. No borres `uv.lock`.
7. No cambies la versión de Python salvo que haya una razón clara.
8. No conviertas el proyecto en app web.
9. No agregues frameworks web.
10. No descargues datasets reales.

## Alcance exacto de v0.1

Implementar un skeleton reproducible con datos mock.

Debe incluir:

- estructura mínima de módulos;
- datos sintéticos/mock claramente marcados;
- modelo placeholder o mínimo no científico;
- pipeline simple ejecutable;
- visualización básica;
- tests mínimos;
- README inicial actualizado;
- comandos de ejecución documentados.

## Qué debes implementar

### 1. Estructura de módulos

Crear o completar una estructura similar a:

```text
src/galaxy_discriminants/
    __init__.py
    data/
        __init__.py
        mock.py
    models/
        __init__.py
        base.py
        placeholders.py
    visualization/
        __init__.py
        rotation_curves.py
    pipeline.py
```

Puedes ajustar nombres si hay una razón técnica, pero mantén una arquitectura simple y clara.

### 2. Datos mock

Crear una forma reproducible de generar galaxias sintéticas.

Requisitos:

- Los datos deben estar claramente identificados como mock/sintéticos.
- Deben incluir:
  - nombre de galaxia mock;
  - radios;
  - velocidades observadas simuladas;
  - incertidumbres;
  - opcional: velocidad verdadera usada para generar el mock.
- Debe usarse una semilla fija o parametrizable.
- No debe descargarse ningún dataset externo.
- No debe mencionarse que estos datos representan SPARC ni ningún catálogo real.

Ejemplo conceptual, no obligatorio:

```text
MockGalaxy:
    name
    radius_kpc
    velocity_kms
    velocity_error_kms
```

### 3. Modelo placeholder o mínimo

Crear una interfaz simple de modelo.

Requisitos:

- Debe existir una clase, protocolo o función base que represente un modelo de curva de rotación.
- Debe existir al menos un modelo placeholder que devuelva una curva predicha simple.
- El modelo placeholder debe estar documentado como no científico.
- No implementar todavía MOND/RAR real.
- No implementar todavía NFW real.
- No implementar todavía Burkert real.

### 4. Pipeline simple

Crear un pipeline mínimo que:

1. Genere o cargue datos mock.
2. Ejecute un modelo placeholder.
3. Calcule una salida básica.
4. Genere una visualización simple o prepare datos para ella.
5. Exporte algún resultado mínimo a `outputs/`.

Puede ser una función pública como:

```text
run_mock_pipeline()
```

o un módulo ejecutable con:

```powershell
uv run python -m galaxy_discriminants.pipeline
```

Preferencia: dejar una forma simple y documentada de ejecución desde terminal.

### 5. Visualización básica

Crear una función de visualización para una curva de rotación mock.

Requisitos:

- Usar `matplotlib`.
- Mostrar datos observados simulados con errores si es razonable.
- Mostrar curva predicha placeholder.
- Guardar imagen en `outputs/`.
- El gráfico debe estar claramente etiquetado como mock/synthetic.
- No debe sugerir resultados científicos reales.

### 6. Tests mínimos

Agregar tests con `pytest`.

Debe cubrir al menos:

- generación de datos mock;
- formas/dimensiones esperadas;
- incertidumbres positivas;
- salida del modelo placeholder;
- ejecución del pipeline mínimo;
- creación de archivo de salida si aplica.

Archivos esperados:

```text
tests/test_mock_data.py
tests/test_placeholder_models.py
tests/test_pipeline.py
```

Puedes ajustar nombres si mantienes claridad.

### 7. README inicial

Actualizar `README.md` con:

- descripción sobria del proyecto;
- advertencia de que v0.1 usa datos mock;
- instalación;
- ejecución;
- tests;
- lint;
- estructura del proyecto;
- límites actuales;
- próximos pasos.

Debe incluir comandos:

```powershell
uv sync
uv run python --version
uv run pytest
uv run ruff check .
```

Y si implementas módulo ejecutable:

```powershell
uv run python -m galaxy_discriminants.pipeline
```

## Restricciones científicas

No hacer ninguna de estas cosas:

- No afirmar que el proyecto resuelve materia oscura.
- No afirmar que MOND, RAR, NFW o Burkert ganan.
- No implementar conclusiones científicas.
- No descargar SPARC.
- No inventar rutas, APIs ni disponibilidad de datasets.
- No usar datos reales.
- No agregar IA.
- No agregar N-body.
- No agregar simulaciones cosmológicas.
- No implementar MCMC.
- No avanzar a v0.2 sin aprobación.

## Restricciones técnicas

- Mantener Python 3.12.
- Mantener `uv`.
- Mantener estructura `src/`.
- Mantener imports limpios.
- Evitar dependencias nuevas salvo que sean estrictamente necesarias.
- Si agregas una dependencia, justifícala en el summary.
- No romper `ruff`.
- No crear archivos grandes.
- No commitear datasets reales.
- No modificar documentación estratégica salvo README, a menos que sea estrictamente necesario.
- No borrar los archivos Markdown existentes.

## Criterios de aceptación

El patch se considera aceptable si:

- [ ] `uv sync` pasa.
- [ ] `uv run python --version` usa Python 3.12.
- [ ] `uv run pytest` pasa.
- [ ] `uv run ruff check .` pasa.
- [ ] Existe pipeline mock ejecutable.
- [ ] Se genera al menos una salida en `outputs/` o una salida verificable.
- [ ] Los datos mock están claramente marcados.
- [ ] El README explica cómo ejecutar el proyecto.
- [ ] No se descargaron datasets reales.
- [ ] No se implementaron modelos físicos reales fuera de alcance.

## Comandos que debes ejecutar

Ejecuta como mínimo:

```powershell
uv sync
uv run pytest
uv run ruff check .
```

Si implementas formato automático con Ruff, puedes usar:

```powershell
uv run ruff format .
uv run ruff check . --fix
```

Pero no ocultes cambios grandes bajo auto-fix sin explicar.

## Summary obligatorio al finalizar

Al terminar, responde con un summary que incluya:

### Archivos modificados

Lista de archivos creados o modificados.

### Qué implementaste

Explicación breve del skeleton v0.1.

### Qué NO implementaste

Confirmar explícitamente que no implementaste:

- SPARC;
- MOND/RAR real;
- NFW real;
- Burkert real;
- ranking discriminante real;
- análisis científico real.

### Tests ejecutados

Indicar comandos y resultado.

### Decisiones tomadas

Indicar cualquier decisión técnica relevante.

### Riesgos o pendientes

Indicar posibles mejoras, deuda técnica o próximos pasos.

### Próximo paso sugerido

Sugerir que el siguiente patch sea v0.2, pero no implementarlo.

## Importante

No avances más allá de v0.1.

El objetivo de este patch es que el repositorio quede técnicamente sólido, reproducible y listo para implementar modelos físicos iniciales en una etapa posterior.
