# Codex Task Prompt — v0.2b-1 Modelo bariónico/newtoniano mínimo

## Rol

Actúa como ingeniero de software científico trabajando sobre el repositorio `galaxy-discriminants`.

Tu tarea es implementar únicamente el patch:

`v0.2b-1 — Modelo bariónico/newtoniano mínimo`

Este patch debe agregar un primer modelo físico controlado: un modelo bariónico/newtoniano mínimo basado en contribuciones de velocidad precomputadas.

No debes implementar todavía MOND/RAR, NFW, Burkert, fitting, ranking discriminante ni datasets reales.

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

Este patch debe continuar sobre esa base sin romper compatibilidad.

## Instrucciones generales

Antes de modificar archivos:

1. Lee `AGENTS.md`.
2. Lee `PROJECT_MASTERPLAN.md`.
3. Lee `PATCH_ROADMAP.md`.
4. Lee `DECISIONS_LOG.md`.
5. Lee `docs/model_assumptions.md`.
6. Inspecciona `src/galaxy_discriminants/models/base.py`.
7. Inspecciona `src/galaxy_discriminants/validation.py`.
8. Inspecciona `src/galaxy_discriminants/models/placeholders.py`.
9. Inspecciona `src/galaxy_discriminants/pipeline.py`.
10. Revisa los tests existentes.

No asumas que el repo está vacío.

No borres ni reescribas la implementación v0.1/v0.2a.

No cambies la arquitectura sin justificarlo.

## Alcance exacto de v0.2b-1

Implementar un modelo bariónico/newtoniano mínimo que combine contribuciones de velocidad precomputadas.

El modelo debe representar una operación básica:

```text
v_bar(r) = sqrt(v_component_1(r)^2 + v_component_2(r)^2 + ...)
```

Este modelo no debe derivar velocidades desde masa, luminosidad, fotometría, potencial gravitatorio ni datos reales.

Debe aceptar componentes ya precomputadas, por ejemplo:

* gas;
* disk;
* bulge;
* stellar_disk;
* stellar_bulge;
* u otros nombres explícitos.

La elección exacta de nombres debe ser flexible, pero las unidades deben estar documentadas como km/s.

## Qué debes implementar

### 1. Modelo bariónico mínimo

Crear un archivo nuevo sugerido:

```text
src/galaxy_discriminants/models/baryonic.py
```

Implementar una clase similar a:

```text
BaryonicRotationModel
```

Requisitos:

* Debe implementar `RotationCurveModel`.
* Debe devolver `ModelPrediction`.
* Debe tener `name` legible.
* Debe marcarse como modelo físico inicial o físico simplificado según la semántica existente de `is_physical`.
* Debe recibir contribuciones bariónicas de velocidad precomputadas.
* Debe combinar componentes mediante suma cuadrática.
* Debe validar radios y velocidades.
* Debe rechazar arrays con shapes incompatibles.
* Debe rechazar radios inválidos.
* Debe rechazar velocidades no finitas.
* Debe rechazar velocidades negativas salvo que exista una justificación documentada. Para este patch, preferir no aceptar velocidades negativas.
* Debe documentar que no deriva masas ni fotometría.

Una API posible, no obligatoria:

```text
model = BaryonicRotationModel(
    components={
        "gas": gas_velocity_kms,
        "disk": disk_velocity_kms,
        "bulge": bulge_velocity_kms,
    }
)

prediction = model.predict(radius_kpc)
```

Otra API aceptable:

```text
model = BaryonicRotationModel.from_components(...)
```

Elige la opción más simple y coherente con la arquitectura actual. Explica la decisión en el summary.

### 2. Escalado opcional de componentes

Puedes implementar factores de escala simples para componentes si se mantiene claro y testeable.

Ejemplo conceptual:

```text
v_bar = sqrt(
    gas_scale * v_gas^2 +
    disk_scale * v_disk^2 +
    bulge_scale * v_bulge^2
)
```

Reglas:

* Los factores deben ser positivos.
* El valor por defecto debe ser 1.0.
* Deben estar documentados como factores numéricos simplificados.
* No deben presentarse como ajuste físico real ni como masa-luz calibrada.
* No implementar fitting de estos factores.

Si esto complica demasiado el patch, puedes omitir escalado y dejarlo como extensión futura. Explica la decisión.

### 3. Datos mock bariónicos

Extender los datos mock o agregar una utilidad separada para crear contribuciones bariónicas sintéticas.

Opciones aceptables:

* agregar campos opcionales a `MockGalaxy`;
* crear una función nueva que genere componentes bariónicas sintéticas;
* crear tests con arrays manuales sin modificar demasiado `MockGalaxy`.

Requisitos:

* No romper el pipeline v0.1.
* No hacer que todos los datos mock dependan obligatoriamente de componentes bariónicas.
* Marcar todo como sintético/mock.
* No asociar estos datos con SPARC ni galaxias reales.

Preferencia: mantener los componentes bariónicos como utilidad separada o como campos opcionales para evitar sobrecargar `MockGalaxy`.

### 4. Exportación pública

Actualizar:

```text
src/galaxy_discriminants/models/__init__.py
```

para exportar el nuevo modelo bariónico si corresponde.

No eliminar exports existentes.

### 5. Documentación

Actualizar:

```text
docs/model_assumptions.md
```

Debe incluir una sección para el modelo bariónico/newtoniano mínimo.

Debe aclarar:

* usa radios en kpc;
* usa velocidades en km/s;
* combina contribuciones precomputadas mediante suma cuadrática;
* no deriva masas;
* no deriva luminosidades;
* no calcula potenciales gravitatorios;
* no usa datos reales;
* no representa todavía una comparación científica completa;
* factores de escala, si existen, no son fitting físico en este patch.

Actualizar `README.md` solo si hace falta para reflejar que v0.2b-1 existe como modelo inicial, sin prometer resultados científicos.

### 6. Tests

Agregar tests nuevos para el modelo bariónico.

Archivo sugerido:

```text
tests/test_baryonic_model.py
```

Debe cubrir:

* predicción con un solo componente;
* predicción con varios componentes;
* resultado esperado de suma cuadrática;
* shapes correctos;
* nombre del modelo;
* indicador `is_physical`;
* unidades de `ModelPrediction`;
* rechazo de radios inválidos;
* rechazo de velocidades negativas;
* rechazo de shapes incompatibles;
* rechazo de componentes vacías;
* compatibilidad con arrays numpy;
* que el pipeline v0.1 siga funcionando.

Ejemplo matemático simple para test:

```text
gas = [3, 4]
disk = [4, 3]

v_bar = sqrt(gas^2 + disk^2) = [5, 5]
```

Si implementas factores de escala, agregar tests específicos.

### 7. Mantener compatibilidad

El pipeline existente debe seguir funcionando:

```powershell
uv run python -m galaxy_discriminants.pipeline
```

No es obligatorio integrar el modelo bariónico al pipeline mock principal en este patch, salvo que pueda hacerse sin aumentar complejidad.

Preferencia: mantener pipeline v0.1 estable y testear el nuevo modelo por separado.

## Restricciones científicas

No implementar todavía:

* MOND/RAR real;
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

No afirmar que el modelo bariónico explica curvas reales.

No afirmar que este modelo compara teorías físicas.

No inventar fórmulas avanzadas ni referencias.

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

* [ ] Existe `BaryonicRotationModel` o equivalente.
* [ ] El modelo implementa `RotationCurveModel`.
* [ ] El modelo devuelve `ModelPrediction`.
* [ ] La predicción combina componentes mediante suma cuadrática.
* [ ] Las unidades internas siguen siendo kpc y km/s.
* [ ] Hay tests para uno y varios componentes.
* [ ] Hay tests para validaciones de errores.
* [ ] El pipeline v0.1 sigue funcionando.
* [ ] MOND/RAR, NFW y Burkert siguen siendo stubs no implementados.
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

Explica cómo funciona el modelo bariónico/newtoniano mínimo.

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

* API del modelo bariónico;
* tratamiento de componentes;
* si implementaste o no factores de escala;
* validaciones agregadas;
* documentación actualizada.

### Riesgos o pendientes

Indica qué queda pendiente para próximos patches.

### Próximo paso sugerido

Sugerir uno de estos pasos, pero no implementarlo:

* `v0.2b-2 — MOND/RAR simple`;
* o `v0.2b-2 — preparación de aceleraciones bariónicas para MOND/RAR`.

## Importante

No avances más allá de v0.2b-1.

Este patch debe implementar solo el modelo bariónico/newtoniano mínimo sobre contribuciones precomputadas, sin introducir todavía modelos alternativos ni fitting.
