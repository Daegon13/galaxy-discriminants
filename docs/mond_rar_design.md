# MOND/RAR Design Notes

## Propósito del documento

Este documento fija la decisión científico-técnica mínima para la primera relación aceleración-bariónica que podrá implementarse en `v0.2b-4`. Su objetivo es evitar que la fórmula, las unidades, el valor inicial de la constante característica o los criterios de validación se improvisen dentro del código.

**Decisión tomada:** la primera implementación será una relación empírica RAR simple y controlada. Esta selección no constituye una prueba de MOND, una verificación científica, un modelo final ni una explicación de galaxias reales.

## Contexto dentro del proyecto

El proyecto ya dispone de:

- `BaryonicRotationModel`, que combina contribuciones de velocidad bariónica precomputadas en `km/s` sobre radios en `kpc`;
- utilidades para convertir entre velocidad circular y aceleración mediante `galaxy_discriminants.acceleration`;
- una interfaz común `RotationCurveModel` y un stub nominal `MondRARPlaceholderModel`;
- datos mock/sintéticos para pruebas de software.

La formulación aquí seleccionada encaja entre la predicción bariónica y la conversión de una aceleración modelada de vuelta a velocidad circular. Este patch solo documenta ese diseño: no modifica el stub MOND/RAR ni agrega una función ejecutable.

## Definiciones y unidades

- `g_bar`: aceleración centrípeta atribuida al baseline bariónico en cada radio. Se expresará en `m/s²` y se obtendrá, cuando corresponda, a partir de la velocidad bariónica mediante `g_bar = v_bar² / r`.
- `g_obs`: aceleración centrípeta inferida de una velocidad circular observada. Se expresa en `m/s²`. En datos reales sería una cantidad observacional y no debe confundirse con una predicción; esos datos no se incorporan en este patch.
- `g_model`: aceleración producida por la relación RAR seleccionada a partir de `g_bar`. Se expresará en `m/s²`. Se usa este nombre para no presentar la salida calculada como si fuera `g_obs` medido.
- `g_dagger`: constante característica positiva de aceleración de la relación. Se expresará en `m/s²`.
- Radio: el radio de la curva se expresará en kilopársecs (`kpc`), de acuerdo con la interfaz actual del proyecto.
- Velocidad: la velocidad circular se expresará en kilómetros por segundo (`km/s`).
- Aceleración: las aceleraciones internas de esta relación se expresarán en metros por segundo al cuadrado (`m/s²`).

Las conversiones entre estas unidades deben reutilizar la infraestructura existente; no se duplicarán factores de conversión dentro del futuro modelo.

## Formulación seleccionada para la primera implementación

**Decisión tomada:** se selecciona como primera formulación implementable la relación empírica RAR

```text
g_model = g_bar / (1 - exp(-sqrt(g_bar / g_dagger)))
```

con dominio nominal

```text
g_bar > 0
g_dagger > 0
```

El valor inicial de trabajo previsto será:

```text
g_dagger = 1.2e-10 m/s²
```

**Pendiente de verificación científica:** este valor no se considera definitivo. Debe revisarse contra literatura y convenciones científicas antes de utilizar datos reales, publicar resultados o interpretar parámetros. Puede cambiar tras esa revisión y no se convierte en una constante de código en `v0.2b-3`.

La relación se tratará exclusivamente como una primera transformación empírica entre aceleración bariónica y aceleración modelada para pruebas controladas. No debe presentarse como prueba de MOND, como descarte de materia oscura, como verificación científica ni como modelo final.

### Comportamientos de transición esperados

La implementación futura deberá reproducir y testear los siguientes límites aproximados:

- régimen de alta aceleración, `g_bar / g_dagger` grande: `g_model ≈ g_bar`;
- régimen de baja aceleración, `g_bar / g_dagger` pequeño y positivo: `g_model ≈ sqrt(g_bar * g_dagger)`.

Estas expresiones describen límites matemáticos esperados de la formulación seleccionada. No son, por sí solas, validación frente a observaciones.

## Formulaciones consideradas

### Opción A — RAR empírica seleccionada

```text
g_model = g_bar / (1 - exp(-sqrt(g_bar / g_dagger)))
```

**Ventajas:**

- trabaja directamente con `g_bar`;
- encaja con la capa existente `acceleration.py`;
- permite convertir después `g_model` a velocidad circular mediante la función inversa ya implementada;
- tiene límites asintóticos claros y es simple de testear;
- mantiene separadas la combinación bariónica, la relación RAR y las conversiones de unidades.

**Riesgos:**

- es una relación empírica y no una validación de una teoría;
- la expresión directa requiere tratamiento explícito de `g_bar = 0` y estabilidad numérica cerca de cero;
- el resultado depende de la convención y el valor adoptado para `g_dagger`;
- una implementación numéricamente ingenua puede sufrir cancelación en el denominador cuando el argumento es pequeño.

### Opción B — MOND con función de interpolación simple

**Extensión futura:** considerar una formulación MOND basada en una función de interpolación denominada “simple”. Antes de implementarla será necesario verificar la ecuación exacta, la convención de aceleración, la relación entre variables, la rama o solución numérica requerida y su procedencia científica.

No se selecciona para `v0.2b-4` y no se implementa en este patch.

### Opción C — MOND con función estándar

**Extensión futura:** considerar una formulación MOND basada en una función de interpolación denominada “estándar”. También requiere verificar su definición exacta, convenciones, parámetros, solución y uso apropiado antes de codificarla.

No se selecciona para `v0.2b-4` y no se implementa en este patch.

## Motivo de selección

La opción A es la ruta incremental más pequeña compatible con la arquitectura actual. Permite partir de una predicción de `BaryonicRotationModel`, convertirla a `g_bar`, aplicar una relación escalar documentada y convertir `g_model` a velocidad circular sin introducir todavía fitting, datasets reales ni nuevas dependencias.

La selección prioriza auditabilidad y tests deterministas. No implica que la relación sea científicamente preferible a todas las alternativas ni que las formulaciones MOND “simple” o “estándar” hayan sido descartadas.

## Entradas esperadas para `v0.2b-4`

El diseño conceptual de la implementación futura requerirá:

1. radios validados, unidimensionales, finitos, positivos y expresados en `kpc`;
2. una predicción bariónica compatible sobre la misma grilla radial, con velocidades en `km/s`, o su `g_bar` derivada en `m/s²`;
3. `g_dagger` como escalar finito y estrictamente positivo, en `m/s²`, con `1.2e-10 m/s²` como valor inicial de trabajo pendiente de verificación;
4. arreglos con formas compatibles y sin valores negativos o no finitos.

**Pendiente de diseño para `v0.2b-4`:** concretar si la API pública recibe un `BaryonicRotationModel`, un `ModelPrediction` bariónico o una aceleración ya validada. La decisión deberá preservar la interfaz `RotationCurveModel`, evitar duplicar validaciones y mantener explícita la procedencia de `g_bar`.

El dominio matemático nominal de la fórmula exige `g_bar > 0`. El tratamiento contractual de entradas exactamente iguales a cero debe decidirse y testearse en `v0.2b-4`; no debe resolverse de forma implícita o mediante división no controlada.

## Salidas esperadas para `v0.2b-4`

La transformación física interna producirá:

- `g_model`, con el mismo *shape* que `g_bar`, valores finitos y no negativos en `m/s²`;
- una velocidad circular modelada en `km/s`, calculada con los mismos radios mediante la conversión inversa existente;
- una `ModelPrediction` compatible con la interfaz común, con radios en `kpc`, velocidades en `km/s`, nombre y notas que identifiquen la relación empírica y sus límites.

La salida no deberá denominarse observación ni sustituir `g_obs`: será una predicción del modelo bajo supuestos explícitos.

## Tests esperados para la implementación futura

`v0.2b-4` deberá incluir, como mínimo:

- validación de `g_bar`, su dimensionalidad, *shape*, finitud y dominio permitido;
- validación de que `g_dagger` sea escalar, finito y estrictamente positivo;
- rechazo explícito de aceleraciones negativas;
- rechazo de valores `NaN`, `+inf` y `-inf`;
- comportamiento cercano a `g_model ≈ g_bar` en alta aceleración con tolerancias justificadas;
- comportamiento cercano a `g_model ≈ sqrt(g_bar * g_dagger)` en baja aceleración con tolerancias justificadas;
- estabilidad numérica cerca de cero, incluida una decisión explícita y testeada para `g_bar = 0`;
- conversión de la aceleración modelada a velocidad circular con las utilidades existentes;
- compatibilidad de radios, formas y unidades con `BaryonicRotationModel` y `ModelPrediction`;
- comprobación de que no se mutan los arreglos ni las predicciones de entrada;
- determinismo y conservación del *shape*;
- mantenimiento sin cambios físicos de los stubs NFW y Burkert y de sus tests de `NotImplementedError`;
- preservación de la compatibilidad del pipeline mock existente.

Los tests asintóticos deberán usar cocientes suficientemente separados de la transición y tolerancias numéricas explícitas; no deberán presentarse como tests contra datos observacionales.

## Riesgos

- **Riesgo científico:** confundir una correlación empírica seleccionada para el prototipo con una prueba de MOND o una explicación de galaxias reales.
- **Riesgo de convención:** usar `g_dagger` con valor, unidades o interpretación distintos de la fuente científica que se revise posteriormente.
- **Riesgo numérico:** evaluar `1 - exp(-x)` de forma inestable para `x` pequeño. La futura implementación deberá elegir una evaluación estable y documentada.
- **Riesgo de dominio:** la fórmula nominal no está definida por sustitución directa en `g_bar = 0`, aunque tenga un límite. La política de validación o extensión continua debe ser explícita.
- **Riesgo arquitectónico:** acoplar innecesariamente la relación RAR al almacenamiento de componentes bariónicas o duplicar las conversiones existentes.
- **Riesgo observacional:** asumir que una aceleración calculada desde datos mock equivale a evidencia sobre galaxias reales.

## Pendientes de verificación

- **Pendiente de verificación científica:** fuente, contexto, convención y rango de aplicabilidad de la relación RAR seleccionada.
- **Pendiente de verificación científica:** valor definitivo, incertidumbre e interpretación de `g_dagger`; `1.2e-10 m/s²` es solo el valor inicial de trabajo.
- **Pendiente de verificación científica:** definiciones exactas de las funciones de interpolación MOND “simple” y “estándar” antes de considerarlas implementables.
- **Pendiente de verificación:** tratamiento de incertidumbres, covarianzas y dispersión intrínseca.
- **Pendiente de verificación:** compatibilidad con formatos, componentes y convenciones de datasets reales como SPARC o BIG-SPARC.
- **Pendiente de diseño:** API concreta, metadatos y política exacta para `g_bar = 0` en `v0.2b-4`.
- **Pendiente de validación:** comparación contra casos de referencia científicos revisados; los datos mock solo validarán comportamiento de software.

## Qué NO se implementa todavía

`v0.2b-3` no implementa:

- una clase MOND/RAR ejecutable ni una función ejecutable para la fórmula RAR;
- funciones de interpolación MOND simple o estándar;
- una constante científica definitiva en código;
- halos NFW, Burkert o Einasto reales;
- modelos híbridos;
- fitting, optimización, AIC, BIC o ranking discriminante;
- SPARC, BIG-SPARC ni ningún dataset real;
- análisis científico real, MCMC, simulaciones N-body o IA/ML.

El `MondRARPlaceholderModel` debe continuar como stub, y los placeholders NFW y Burkert deben permanecer sin implementación física.
