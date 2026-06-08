# Codex Task Prompt — v0.2a Infraestructura de modelos físicos

## Rol

Actúa como ingeniero de software científico trabajando sobre el repositorio `galaxy-discriminants`.

Tu tarea es implementar únicamente el patch:

`v0.2a — Infraestructura de modelos físicos`

No debes implementar todavía fórmulas físicas reales de MOND/RAR, NFW o Burkert. Este patch prepara la arquitectura para que esos modelos puedan implementarse en un patch posterior.

## Contexto del proyecto

El proyecto busca construir una herramienta computacional reproducible para estudiar curvas de rotación galáctica y seleccionar galaxias con mayor utilidad discriminante entre familias de modelos.

La versión `v0.1` ya implementó:

* generación reproducible de datos mock;
* `MockGalaxy`;
* modelo placeholder de velocidad constante;
* pipeline mock ejecutable;
* exportación CSV/JSON/PNG en `outputs/`;
* visualización básica;
* tests;
* README actualizado.

La versión `v0.2a` debe fortalecer la infraestructura para futuros modelos físicos sin introducir física real todavía.

## Instrucciones generales

Antes de modificar archivos:

1. Lee `AGENTS.md`.
2. Lee `PROJECT_MASTERPLAN.md`.
3. Lee `PATCH_ROADMAP.md`.
4. Lee `DECISIONS_LOG.md`.
5. Inspecciona el código existente.
6. Revisa `pyproject.toml`.
7. Revisa los tests actuales.

No asumas que el repo está vacío.

No borres ni reescribas la implementación v0.1.

## Alcance exacto de v0.2a

Implementar infraestructura para modelos físicos futuros.

Este patch debe incluir:

* mejora de la interfaz común de modelos;
* estructuras de datos para predicciones de curvas de rotación;
* documentación explícita de unidades esperadas;
* validaciones básicas de radios y velocidades;
* placeholders nominales para familias futuras, si ayudan a preparar arquitectura;
* tests de interfaz y validación;
* documentación técnica de supuestos de modelos.

Este patch no debe implementar fórmulas físicas reales todavía.

## Objetivos técnicos

### 1. Mejorar interfaz común de modelos

Revisar `src/galaxy_discriminants/models/base.py`.

Crear o mejorar una abstracción común para modelos de curvas de rotación.

La interfaz debe permitir que modelos futuros:

* tengan un nombre legible;
* declaren si son físicos o placeholder;
* reciban radios en kpc;
* devuelvan velocidades en km/s;
* puedan ser usados de forma común por el pipeline futuro.

Una posible dirección, no obligatoria:

```text
RotationCurveModel:
    name: str
    is_physical: bool
    predict(radius_kpc) -> ModelPrediction
```

No es obligatorio usar exactamente esta API si hay una alternativa mejor, pero la decisión debe explicarse en el summary.

### 2. Crear estructura para predicciones

Agregar una estructura clara para resultados de predicción.

Debe incluir, como mínimo:

* nombre del modelo;
* radios usados;
* velocidades predichas;
* unidades;
* indicador de si la predicción proviene de un placeholder o modelo físico.

Ejemplo conceptual:

```text
ModelPrediction:
    model_name
    radius_kpc
    velocity_kms
    is_physical_model
    notes
```

Debe ser simple y testeable.

### 3. Validación de entradas

Agregar funciones de validación para arrays científicos básicos.

Validar al menos:

* radios no vacíos;
* radios finitos;
* radios positivos;
* radios idealmente crecientes cuando corresponda;
* velocidades finitas;
* shapes compatibles entre radio y velocidad.

Ubicación sugerida:

```text
src/galaxy_discriminants/validation.py
```

o

```text
src/galaxy_discriminants/models/validation.py
```

Elegir una ubicación clara y justificarla en el summary.

### 4. Documentación de unidades

Crear documentación breve sobre unidades internas.

Archivo sugerido:

```text
docs/model_assumptions.md
```

Debe explicar:

* radios en kpc;
* velocidades en km/s;
* datos mock no científicos;
* modelos físicos futuros pendientes de verificación;
* MOND/RAR, NFW y Burkert todavía no implementados;
* fórmulas y parametrizaciones pendientes de revisión científica.

No inventes citas, papers ni fórmulas.

### 5. Placeholders nominales, si corresponde

Puedes crear clases placeholder nominales para modelos futuros solo si ayudan a fijar arquitectura.

Por ejemplo:

```text
BaryonicPlaceholderModel
MondRARPlaceholderModel
NFWPlaceholderModel
BurkertPlaceholderModel
```

Pero si las creas:

* deben estar marcadas claramente como placeholders;
* no deben simular física real;
* no deben sugerir resultados científicos;
* deben lanzar `NotImplementedError` o devolver predicciones triviales claramente no científicas, según lo que sea más coherente con la arquitectura.

Preferencia: evitar predicciones falsas de modelos físicos. Es aceptable crear stubs que lancen `NotImplementedError`.

### 6. Mantener compatibilidad con v0.1

El pipeline existente debe seguir funcionando:

```powershell
uv run python -m galaxy_discriminants.pipeline
```

Los outputs de v0.1 deben seguir generándose.

El modelo `ConstantVelocityModel` puede adaptarse a la nueva interfaz, pero debe seguir siendo no científico.

### 7. Tests

Agregar o actualizar tests para:

* interfaz común de modelos;
* estructura `ModelPrediction`;
* validación de radios;
* validación de shapes incompatibles;
* comportamiento del placeholder existente;
* compatibilidad del pipeline v0.1.

Tests sugeridos:

```text
tests/test_model_interface.py
tests/test_validation.py
tests/test_placeholder_models.py
tests/test_pipeline.py
```

Puedes ajustar nombres si mantiene claridad.

## Restricciones científicas

No implementar todavía:

* MOND/RAR real;
* NFW real;
* Burkert real;
* Einasto;
* modelos híbridos;
* fitting;
* AIC/BIC;
* ranking discriminante;
* análisis científico real;
* dataset SPARC;
* BIG-SPARC;
* MCMC;
* simulaciones N-body;
* IA/ML.

No afirmar que ningún modelo es correcto, incorrecto, mejor o peor.

No inventar fórmulas ni referencias.

Si algo requiere verificación científica, marcarlo como:

`Pendiente de verificación`.

## Restricciones técnicas

* Mantener Python 3.12.
* Mantener `uv`.
* No eliminar `uv.lock`.
* No cambiar el nombre del paquete.
* No agregar dependencias salvo necesidad estricta.
* Si agregas una dependencia, justificarla.
* No convertir el proyecto en app web.
* No versionar outputs generados.
* No tocar datasets reales.
* No hacer refactors grandes fuera del alcance.

## Criterios de aceptación

El patch es aceptable si:

* [ ] El pipeline v0.1 sigue funcionando.
* [ ] Existe una interfaz de modelos más clara y extensible.
* [ ] Existe una estructura de predicción testeada.
* [ ] Existen validaciones básicas de arrays científicos.
* [ ] Las unidades internas están documentadas.
* [ ] MOND/RAR, NFW y Burkert siguen sin implementación física real.
* [ ] Los tests pasan.
* [ ] Ruff pasa.
* [ ] Mypy pasa si ya estaba configurado.
* [ ] El README no promete resultados científicos reales.
* [ ] `docs/model_assumptions.md` documenta supuestos y pendientes.

## Comandos que debes ejecutar

Ejecuta como mínimo:

```powershell
uv sync
uv run python --version
uv run pytest
uv run ruff format --check .
uv run ruff check .
uv run mypy src tests
uv run python -m galaxy_discriminants.pipeline
git diff --check
git status --short --branch
```

## Summary obligatorio al finalizar

Al terminar, responde con un summary que incluya:

### Archivos modificados

Lista de archivos creados o modificados.

### Qué implementaste

Explica la infraestructura agregada para modelos físicos futuros.

### Qué NO implementaste

Confirma explícitamente que no implementaste:

* MOND/RAR real;
* NFW real;
* Burkert real;
* SPARC;
* fitting;
* ranking discriminante;
* análisis científico real.

### Tests ejecutados

Indica comandos y resultado.

### Decisiones tomadas

Explica decisiones de arquitectura:

* ubicación de validaciones;
* forma de `ModelPrediction`;
* diseño de la interfaz común;
* tratamiento de placeholders.

### Riesgos o pendientes

Indica qué queda pendiente para v0.2b.

### Próximo paso sugerido

Sugerir `v0.2b — Modelos físicos iniciales`, pero no implementarlo.

## Importante

No avances más allá de v0.2a.

Este patch debe preparar el terreno para implementar modelos físicos reales en una etapa posterior, sin introducir todavía fórmulas científicas que no hayan sido verificadas.
