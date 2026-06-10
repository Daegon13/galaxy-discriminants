# Codex Task Prompt — v0.2b-3 Selección documentada de formulación MOND/RAR

## Rol

Actúa como ingeniero de software científico trabajando sobre el repositorio `galaxy-discriminants`.

Tu tarea es implementar únicamente el patch:

`v0.2b-3 — Selección documentada de formulación MOND/RAR`

Este patch es principalmente documental y de diseño científico-técnico.

No debes implementar todavía un modelo MOND/RAR ejecutable como `RotationCurveModel`.

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
* validaciones reutilizables;
* stubs nominales para MOND/RAR, NFW y Burkert;
* documentación de unidades y supuestos;
* compatibilidad del pipeline v0.1;
* tests ampliados.

### v0.2b-1

Ya implementó:

* `BaryonicRotationModel`;
* combinación de componentes bariónicas precomputadas mediante suma cuadrática;
* validación de componentes;
* tests del modelo bariónico;
* documentación de límites y supuestos.

### v0.2b-2

Ya implementó:

* constantes de unidades en `units.py`;
* conversiones entre velocidad circular y aceleración;
* validación de aceleraciones;
* tests de conversión, round-trip y no mutación;
* documentación de la capa de aceleraciones.

Este patch debe preparar la implementación futura de MOND/RAR de forma científica y auditable.

## Instrucciones generales

Antes de modificar archivos:

1. Lee `AGENTS.md`.
2. Lee `PROJECT_MASTERPLAN.md`.
3. Lee `PATCH_ROADMAP.md`.
4. Lee `DECISIONS_LOG.md`.
5. Lee `docs/model_assumptions.md`.
6. Inspecciona `src/galaxy_discriminants/units.py`.
7. Inspecciona `src/galaxy_discriminants/acceleration.py`.
8. Inspecciona `src/galaxy_discriminants/models/baryonic.py`.
9. Inspecciona `src/galaxy_discriminants/models/placeholders.py`.
10. Revisa los tests existentes.

No asumas que el repo está vacío.

No borres ni reescribas implementaciones anteriores.

No cambies arquitectura sin justificarlo.

## Alcance exacto de v0.2b-3

Crear documentación y registro de decisión para la primera formulación MOND/RAR que se implementará en un patch posterior.

Este patch debe responder:

1. Qué formulación se implementará primero.
2. Qué entradas tendrá.
3. Qué salidas tendrá.
4. Qué constante de aceleración se usará como default inicial.
5. Qué unidades se usarán.
6. Qué límites científicos tiene.
7. Qué tests deberá tener el patch de implementación.
8. Qué queda pendiente de verificación.

## Qué debes implementar

### 1. Crear documento de diseño MOND/RAR

Crear un archivo:

```text
docs/mond_rar_design.md
```

Debe estar en español técnico claro.

Debe incluir:

```text
# MOND/RAR Design Notes
```

Secciones mínimas:

* Propósito del documento.
* Contexto dentro del proyecto.
* Definiciones:

  * `g_bar`;
  * `g_obs`;
  * `g_dagger` o constante característica;
  * radio en kpc;
  * velocidad en km/s;
  * aceleración en m/s².
* Formulación seleccionada para primera implementación.
* Formulaciones consideradas.
* Motivo de selección.
* Entradas esperadas.
* Salidas esperadas.
* Tests esperados para la implementación futura.
* Riesgos.
* Pendientes de verificación.
* Qué NO se implementa todavía.

### 2. Seleccionar primera formulación

Seleccionar como primera formulación implementable una relación empírica RAR simple:

```text
g_model = g_bar / (1 - exp(-sqrt(g_bar / g_dagger)))
```

Donde:

```text
g_bar > 0
g_dagger > 0
```

Decisión tomada:

* Esta será tratada como una formulación empírica RAR inicial.
* No debe presentarse como prueba de MOND.
* No debe presentarse como verificación científica.
* No debe presentarse como modelo final.
* Se usará solo como primera relación aceleración-bariónica para pruebas controladas.

Debe quedar documentado que esta formulación reproduce comportamientos esperados de transición:

* régimen de alta aceleración: comportamiento cercano a `g_model ≈ g_bar`;
* régimen de baja aceleración: comportamiento cercano a `g_model ≈ sqrt(g_bar * g_dagger)`.

No implementar esta fórmula en código todavía. Solo documentarla.

### 3. Constante característica

Documentar como default inicial pendiente de revisión:

```text
g_dagger = 1.2e-10 m/s²
```

Reglas:

* Debe marcarse explícitamente como valor inicial de trabajo.
* Debe marcarse como pendiente de verificación científica.
* Debe quedar claro que puede cambiar cuando se revisen papers/datasets.
* No convertirlo todavía en constante de código si eso implica semántica científica prematura.

Puedes agregar una sección en `docs/model_assumptions.md` que apunte a `docs/mond_rar_design.md`.

### 4. Formulaciones consideradas

Documentar al menos estas opciones:

#### Opción A — RAR empírica seleccionada

```text
g_model = g_bar / (1 - exp(-sqrt(g_bar / g_dagger)))
```

Ventajas:

* Trabaja directamente con `g_bar`.
* Encaja bien con la capa `acceleration.py`.
* Puede convertirse luego a velocidad circular con la función inversa ya implementada.
* Es simple de testear.

Riesgos:

* Es una relación empírica.
* Requiere cuidado en `g_bar = 0`.
* Requiere documentar el valor de `g_dagger`.

#### Opción B — MOND con función de interpolación simple

Documentar como alternativa futura.

No implementarla todavía.

#### Opción C — MOND con función estándar

Documentar como alternativa futura.

No implementarla todavía.

### 5. Tests esperados para implementación futura

Documentar los tests que deberá tener `v0.2b-4`.

Debe incluir:

* validación de `g_bar`;
* validación de `g_dagger`;
* comportamiento en alta aceleración;
* comportamiento en baja aceleración;
* conversión de aceleración modelada a velocidad;
* compatibilidad con `BaryonicRotationModel`;
* rechazo de aceleraciones negativas;
* rechazo de valores no finitos;
* estabilidad numérica cerca de cero;
* no mutación de entradas;
* mantenimiento de stubs NFW/Burkert sin cambios.

### 6. Actualizar documentación existente

Actualizar:

```text
docs/model_assumptions.md
```

Agregar una sección breve que indique:

* se agregó `docs/mond_rar_design.md`;
* la primera formulación seleccionada será RAR empírica;
* MOND/RAR aún no está implementado como modelo;
* `g_dagger` queda como valor inicial pendiente de verificación científica.

Actualizar:

```text
README.md
```

solo si hace falta reflejar que el proyecto está en estado `v0.2b-3`.

### 7. Actualizar Decisions Log

Actualizar:

```text
DECISIONS_LOG.md
```

Agregar una o más decisiones nuevas:

* seleccionar RAR empírica como primera formulación implementable;
* mantener MOND/RAR sin implementación hasta el siguiente patch;
* tratar `g_dagger = 1.2e-10 m/s²` como valor inicial pendiente de verificación;
* documentar alternativas MOND simple/standard como extensiones futuras.

No borrar decisiones previas.

## Restricciones científicas

No implementar todavía:

* clase MOND/RAR real;
* función ejecutable RAR;
* función de interpolación MOND;
* constante definitiva en código;
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

No afirmar que esta formulación prueba MOND.

No afirmar que esta formulación descarta materia oscura.

No afirmar que el proyecto explica galaxias reales.

No inventar referencias, DOIs, enlaces ni citas bibliográficas.

Si no puedes verificar una fuente, marca:

```text
Pendiente de verificación
```

## Restricciones técnicas

* Mantener Python 3.12.
* Mantener `uv`.
* No eliminar `uv.lock`.
* No cambiar el nombre del paquete.
* No agregar dependencias.
* No convertir el proyecto en app web.
* No versionar outputs generados.
* No tocar datasets reales.
* No hacer refactors grandes fuera del alcance.
* No romper los stubs existentes de MOND/RAR, NFW y Burkert.
* No convertir placeholders en modelos reales.

## Criterios de aceptación

El patch es aceptable si:

* [ ] Existe `docs/mond_rar_design.md`.
* [ ] La formulación RAR empírica queda documentada.
* [ ] Las alternativas MOND simple y standard quedan mencionadas como futuras.
* [ ] `g_dagger = 1.2e-10 m/s²` queda marcado como valor inicial pendiente de verificación.
* [ ] `docs/model_assumptions.md` enlaza o resume la decisión.
* [ ] `DECISIONS_LOG.md` registra la decisión.
* [ ] README se actualiza solo si corresponde.
* [ ] MOND/RAR sigue sin implementación ejecutable.
* [ ] NFW y Burkert siguen sin implementación física.
* [ ] No se agregan dependencias.
* [ ] Tests existentes siguen pasando.
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

Explica la documentación y decisiones agregadas para MOND/RAR.

### Qué NO implementaste

Confirma explícitamente que no implementaste:

* MOND/RAR ejecutable;
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

Explica:

* formulación seleccionada;
* alternativas consideradas;
* tratamiento de `g_dagger`;
* por qué no se implementó todavía el modelo.

### Riesgos o pendientes

Indica qué queda pendiente para `v0.2b-4`.

### Próximo paso sugerido

Sugerir:

```text
v0.2b-4 — Implementación de modelo RAR/MOND simple
```

pero no implementarlo.

## Importante

No avances más allá de v0.2b-3.

Este patch debe cerrar la decisión científica mínima para poder implementar MOND/RAR en el siguiente paso sin improvisar fórmulas en código.
