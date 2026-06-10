# Supuestos de la infraestructura de modelos

## Decisiones tomadas

- La unidad interna de radio para interfaces y predicciones es el kilopársec (`kpc`).
- La unidad interna de velocidad es el kilómetro por segundo (`km/s`).
- Una predicción contiene nombre del modelo, radios, velocidades, unidades, notas y un indicador explícito de si la implementación es física.
- Los radios de una predicción deben ser un arreglo unidimensional, no vacío, finito, positivo y estrictamente creciente.
- Las velocidades deben ser un arreglo unidimensional, no vacío, finito, no negativo y con el mismo *shape* que los radios.
- Los arreglos almacenados en una predicción validada son copias de solo lectura.

## Supuestos

- En esta fase, una curva de rotación se representa mediante velocidades escalares no negativas muestreadas en radios ordenados.
- El modelo de velocidad constante existe únicamente para probar el software y conservar el pipeline mock de v0.1. No representa una hipótesis física sobre galaxias.
- Todos los datos generados por el pipeline actual son mock/sintéticos y no permiten inferencias sobre galaxias reales.

## Modelo bariónico/newtoniano mínimo (v0.2b-1)

### Decisión tomada

- `BaryonicRotationModel` recibe un mapeo flexible de nombres explícitos a contribuciones de velocidad precomputadas. Nombres como `gas`, `disk`, `bulge`, `stellar_disk` o `stellar_bulge` son convenciones del consumidor y no activan comportamientos especiales.
- Los radios entregados a `predict` usan `kpc`; cada componente y la predicción resultante usan `km/s`.
- Todas las componentes deben ser arreglos unidimensionales, no vacíos, finitos, no negativos y con el mismo *shape* que los radios.
- La velocidad bariónica se combina por suma cuadrática: `v_bar(r) = sqrt(sum(v_component(r)^2))`.
- El modelo se marca como físico simplificado porque implementa esa combinación controlada, no porque constituya una validación científica completa.

### Supuesto

Las contribuciones de velocidad ya existen sobre la misma grilla radial y son compatibles entre sí. En este patch se usan únicamente valores manuales o sintéticos/mock; no se asocian con SPARC, BIG-SPARC ni galaxias reales.

### Límites

- El modelo no deriva masas, factores masa-luz, luminosidades ni fotometría.
- El modelo no calcula potenciales gravitatorios ni obtiene velocidades a partir de distribuciones de materia.
- El modelo no incluye factores de escala, fitting, optimización ni calibración física.
- La operación implementada no representa todavía una comparación científica completa ni permite concluir que el baseline explique curvas de rotación reales.

### Pendiente de verificación

La procedencia, interpretación, normalización y compatibilidad científica de componentes bariónicas provenientes de datasets reales, junto con cualquier parametrización física adicional.

### Extensión futura

Los factores de escala o masa-luz podrán evaluarse en otro patch, con semántica física documentada y sin convertirlos implícitamente en fitting no auditado.

## Capa de aceleraciones (v0.2b-2)

### Decisión tomada

- Las unidades internas de esta capa son `kpc` para radio, `km/s` para velocidad circular y `m/s²` para aceleración.
- Las conversiones de unidad se centralizan en `galaxy_discriminants.units`, sin introducir `astropy` ni otra dependencia nueva.
- La aceleración circular se calcula punto a punto mediante `g = v² / r`, convirtiendo antes la velocidad a `m/s` y el radio a metros.
- La conversión inversa usa `v = sqrt(g * r)` y devuelve la velocidad en `km/s`.
- Las utilidades aceptan radios positivos no necesariamente ordenados porque realizan una conversión punto a punto y no construyen por sí mismas una predicción de curva de rotación. Las predicciones de modelos mantienen el requisito existente de radios estrictamente crecientes.
- La conversión desde una predicción bariónica se mantiene como composición externa: se pasan `prediction.radius_kpc` y `prediction.velocity_kms` a la utilidad correspondiente. No se agrega responsabilidad adicional a `BaryonicRotationModel`.

### Supuesto

Las velocidades de entrada representan velocidades circulares no negativas y los radios asociados están expresados en las unidades internas documentadas. La validez numérica y dimensional de los arreglos no garantiza por sí sola que una entrada sea científicamente apropiada.

### Preparación para MOND/RAR

Esta capa permite obtener una aceleración bariónica a partir de una curva de velocidad bariónica y volver de aceleración a velocidad circular. Es una infraestructura matemática necesaria para expresar una relación MOND/RAR futura en el espacio de aceleraciones, pero no implementa ni valida todavía un modelo físico MOND/RAR.

### Pendiente de verificación

- La función de interpolación o relación funcional MOND/RAR que se usará en un patch futuro.
- El valor, las unidades y la convención de la constante de aceleración característica que requiera esa implementación futura.
- La revisión científica de cualquier parametrización MOND/RAR antes de marcarla como implementación física.

### Límites y riesgos

- Estas conversiones son relaciones cinemáticas y de unidades; no ajustan parámetros ni explican curvas de rotación reales.
- No se incorporan incertidumbres, covarianzas, factores masa-luz ni datos observacionales.
- Valores extremos finitos podrían exceder el rango numérico de `float64`; el rango científicamente admisible deberá definirse cuando existan modelos y datos reales verificados.

## Pendiente de verificación

- Las fórmulas, parametrizaciones, constantes y convenciones adicionales necesarias para derivar componentes bariónicas y para implementar MOND/RAR, NFW y Burkert.
- La semántica y validación de parámetros específicos de cada familia física.
- Las convenciones de unidades al incorporar fuentes externas y las transformaciones necesarias hacia las unidades internas.
- La disponibilidad, formato, licencia y condiciones de uso de SPARC y BIG-SPARC.

MOND/RAR, NFW y Burkert no tienen implementación física en v0.2b-2. Sus clases nominales son *stubs*: validan los radios y lanzan `NotImplementedError` en lugar de producir predicciones falsas.

## Riesgos

- Un arreglo numéricamente válido no garantiza que sus valores sean científicamente apropiados para una galaxia o modelo concreto.
- Marcar una implementación futura como física solo describe la naturaleza declarada de su código; no constituye validación científica.
- Las reglas generales de esta fase pueden requerir extensión cuando existan parámetros, componentes bariónicos o datos observacionales reales.

## Extensión futura

`v0.2b-3` podrá seleccionar y documentar una formulación MOND/RAR simple después de revisión científica. NFW y Burkert deben permanecer como stubs hasta sus patches correspondientes.
