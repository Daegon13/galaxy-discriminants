# Codex Task Prompt — v0.2b-2 Utilidades de aceleración bariónica y preparación MOND/RAR

## Rol

Actúa como ingeniero de software científico trabajando sobre el repositorio `galaxy-discriminants`.

Tu tarea es implementar únicamente el patch:

`v0.2b-2 — Utilidades de aceleración bariónica y preparación MOND/RAR`

Este patch debe preparar la base matemática y técnica para implementar MOND/RAR en un patch posterior.

No debes implementar todavía un modelo MOND/RAR completo como `RotationCurveModel`.

No debes implementar halos NFW, Burkert, fitting, ranking discriminante ni datasets reales.

## Contexto del proyecto

El proyecto busca construir una herramienta computacional reproducible para estudiar curvas de rotación galáctica y seleccionar galaxias con mayor utilidad discriminante entre familias de modelos.

Versiones anteriores:

### v0.1

Ya implementó:

* generación reproducible de datos mock;
* `MockGalaxy`;
* modelo placeholder de velocidad constante;
* pipeline mock ejecutable;
* exportación CSV/JSON/PNG en `outputs/`;
* visualización básica;
* tests;
* README actualizado.

### v0.2a

Ya implementó:

* `ModelPrediction`;
* interfaz extensible `RotationCurveModel`;
* validaciones reutilizables en `galaxy_discriminants.validation`;
* stubs nominales para MOND/RAR, NFW y Burkert;
* documentación de unidades y supuestos en `docs/model_assumptions.md`;
* compatibilidad del pipeline v0.1;
* tests ampliados.

### v0.2b-1

Ya implementó:

* `BaryonicRotationModel`;
* combinación de componentes bariónicas precomputadas mediante suma cuadrática;
* validación de componentes;
* tests del modelo bariónico;
* documentación de límites y supuestos.

Este patch debe continuar sobre esa base sin romper compatibilidad.

## Instrucciones generales

Antes de modificar archivos:

1. Lee `AGENTS.md`.
2. Lee `PROJECT_MASTERPLAN.md`.
3. Lee `PATCH_ROADMAP.md`.
4. Lee `DECISIONS_LOG.md`.
5. Lee `docs/model_assumptions.md`.
6. Inspecciona `src/galaxy_discriminants/models/base.py`.
7. Inspecciona `src/galaxy_discriminants/models/baryonic.py`.
8. Inspecciona `src/galaxy_discriminants/validation.py`.
9. Inspecciona `src/galaxy_discriminants/models/placeholders.py`.
10. Revisa los tests existentes.

No asumas que el repo está vacío.

No borres ni reescribas la implementación anterior.

No cambies la arquitectura sin justificarlo.

## Alcance exacto de v0.2b-2

Implementar utilidades de conversión entre velocidades circulares, radios y aceleraciones.

Este patch debe permitir calcular:

```text
g = v^2 / r
```

usando entradas en:

* radio: kpc;
* velocidad: km/s;

y salida en:

* aceleración: m/s².

También debe permitir la conversión inversa:

```text
v = sqrt(g * r)
```

usando:

* aceleración: m/s²;
* radio: kpc;

y salida en:

* velocidad: km/s.

Este patch prepara el terreno para MOND/RAR, pero no implementa todavía el modelo MOND/RAR completo.

## Qué debes implementar

### 1. Constantes de unidades

Crear un módulo sugerido:

```text
src/galaxy_discriminants/units.py
```

Debe incluir constantes explícitas, por ejemplo:

```text
KILOMETER_IN_METERS
KPC_IN_METERS
```

Puedes agregar otras constantes si son necesarias.

Requisitos:

* Nombres claros.
* Sin dependencias nuevas.
* Documentar que las unidades internas del proyecto son kpc, km/s y m/s² para aceleraciones.
* No introducir `astropy` todavía.

### 2. Utilidades de aceleración

Crear un módulo sugerido:

```text
src/galaxy_discriminants/physics.py
```

o

```text
src/galaxy_discriminants/acceleration.py
```

Elegir una ubicación clara y justificarla en el summary.

Implementar funciones similares a:

```text
circular_velocity_to_acceleration_m_s2(radius_kpc, velocity_kms)

acceleration_to_circular_velocity_kms(radius_kpc, acceleration_m_s2)
```

Requisitos:

* Validar radios con las utilidades existentes.
* Validar velocidades con las utilidades existentes.
* Validar aceleraciones:

  * arrays unidimensionales;
  * no vacíos;
  * valores finitos;
  * valores no negativos.
* Validar compatibilidad de shapes.
* Aceptar arrays NumPy y listas convertibles a arrays.
* Devolver arrays NumPy.
* No mutar entradas.
* Mantener precisión numérica razonable.

### 3. Validación de aceleraciones

Extender `src/galaxy_discriminants/validation.py` con una función nueva, por ejemplo:

```text
validate_acceleration_m_s2(...)
```

Requisitos:

* Debe validar arrays unidimensionales.
* Debe rechazar arrays vacíos.
* Debe rechazar valores no finitos.
* Debe rechazar valores negativos.
* Debe devolver una copia validada o array seguro consistente con el estilo actual.
* Debe estar testeada.

No duplicar lógica innecesariamente.

### 4. Integración opcional con BaryonicRotationModel

Si es simple y no aumenta demasiado el alcance, agregar una utilidad o método que permita obtener aceleración bariónica a partir de la predicción del modelo bariónico.

Ejemplo aceptable:

```text
baryonic_prediction = model.predict(radius_kpc)
g_bar = circular_velocity_to_acceleration_m_s2(
    baryonic_prediction.radius_kpc,
    baryonic_prediction.velocity_kms,
)
```

No es obligatorio agregar un método al modelo. De hecho, puede ser preferible mantenerlo como función externa para conservar separación de responsabilidades.

No integrar esto al pipeline principal todavía salvo que sea extremadamente simple y no rompa nada.

### 5. Documentación

Actualizar:

```text
docs/model_assumptions.md
```

Debe explicar:

* unidades internas;
* conversión de velocidad circular a aceleración;
* conversión inversa;
* por qué esta capa prepara MOND/RAR;
* que no se implementa todavía MOND/RAR como modelo físico;
* que la elección de función de interpolación MOND/RAR sigue pendiente de verificación;
* que la constante de aceleración característica de MOND/RAR queda pendiente para el patch futuro.

Actualizar `README.md` solo si hace falta reflejar el estado `v0.2b-2`.

### 6. Tests

Agregar tests nuevos para las utilidades de aceleración.

Archivo sugerido:

```text
tests/test_acceleration.py
```

Debe cubrir:

* conversión velocidad → aceleración con valores simples;
* conversión aceleración → velocidad;
* round-trip aproximado:

  * velocidad → aceleración → velocidad;
* rechazo de radios inválidos;
* rechazo de velocidades negativas;
* rechazo de aceleraciones negativas;
* rechazo de valores no finitos;
* rechazo de shapes incompatibles;
* compatibilidad con listas y arrays NumPy;
* que las entradas no sean mutadas.

Ejemplo de test conceptual:

```text
radius_kpc = [1.0]
velocity_kms = [1.0]

g = (1000 m/s)^2 / (1 kpc en metros)
```

No hardcodear constantes de forma opaca. Usar las constantes definidas por el proyecto para construir el valor esperado.

### 7. Mantener compatibilidad

El pipeline existente debe seguir funcionando:

```powershell
uv run python -m galaxy_discriminants.pipeline
```

No modificar el pipeline salvo necesidad clara.

No romper `BaryonicRotationModel`.

No romper stubs existentes.

## Restricciones científicas

No implementar todavía:

* MOND/RAR real como modelo;
* función de interpolación MOND/RAR;
* constante MOND/RAR definitiva;
* NFW real;
* Burkert real;
* Einasto;
* modelos híbridos;
* fitting;
* optimización de parámetros;
* AIC/BIC;
* ranking discriminante;
* análisis científico real;
* dataset SPARC;
* BIG-SPARC;
* MCMC;
* simulaciones N-body;
* IA/ML.

No afirmar que estas utilidades validan MOND/RAR.

No afirmar que el proyecto explica curvas reales.

No inventar referencias ni fórmulas avanzadas.

Si algo requiere verificación científica, marcarlo como:

```text
Pendiente de verificación
```

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
* No romper los stubs existentes de MOND/RAR, NFW y Burkert.
* No convertir placeholders en modelos reales.

## Criterios de aceptación

El patch es aceptable si:

* [ ] Existen constantes de unidad explícitas.
* [ ] Existe conversión velocidad circular → aceleración.
* [ ] Existe conversión aceleración → velocidad circular.
* [ ] Existe validación de aceleraciones.
* [ ] Hay tests de conversión directa.
* [ ] Hay tests de conversión inversa.
* [ ] Hay tests de round-trip aproximado.
* [ ] Hay tests de errores por radios, velocidades, aceleraciones y shapes inválidos.
* [ ] El pipeline v0.1 sigue funcionando.
* [ ] `BaryonicRotationModel` sigue funcionando.
* [ ] MOND/RAR, NFW y Burkert siguen sin implementación física real.
* [ ] No se introduce fitting.
* [ ] No se introduce dataset real.
* [ ] No se agregan dependencias innecesarias.
* [ ] La documentación explica límites y supuestos.
* [ ] Tests pasan.
* [ ] Ruff pasa.
* [ ] Mypy pasa si ya estaba funcionando.

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

Si el entorno de Codex tiene problemas de red con `uv sync`, puedes usar temporalmente:

```powershell
uv run --no-sync pytest
uv run --no-sync ruff format --check .
uv run --no-sync ruff check .
uv run --no-sync mypy src tests
uv run --no-sync python -m galaxy_discriminants.pipeline
```

Pero debes reportar claramente que usaste `--no-sync` y explicar el motivo.

## Summary obligatorio al finalizar

Al terminar, responde con un summary que incluya:

### Archivos modificados

Lista de archivos creados o modificados.

### Qué implementaste

Explica cómo funcionan las utilidades de aceleración y conversiones de unidades.

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

Aclara si usaste comandos normales o `--no-sync`.

### Decisiones tomadas

Explica decisiones de arquitectura:

* ubicación de constantes;
* ubicación de utilidades de aceleración;
* diseño de validación de aceleraciones;
* si integraste o no estas utilidades con `BaryonicRotationModel`.

### Riesgos o pendientes

Indica qué queda pendiente para próximos patches.

### Próximo paso sugerido

Sugerir uno de estos pasos, pero no implementarlo:

* `v0.2b-3 — MOND/RAR simple`;
* o `v0.2b-3 — documentación y selección explícita de función MOND/RAR`.

## Importante

No avances más allá de v0.2b-2.

Este patch debe preparar la capa de aceleraciones necesaria para MOND/RAR sin implementar todavía MOND/RAR como modelo físico.
