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

## Pendiente de verificación

- Las fórmulas, parametrizaciones, constantes y convenciones adicionales necesarias para derivar componentes bariónicas y para implementar MOND/RAR, NFW y Burkert.
- La semántica y validación de parámetros específicos de cada familia física.
- Las convenciones de unidades al incorporar fuentes externas y las transformaciones necesarias hacia las unidades internas.
- La disponibilidad, formato, licencia y condiciones de uso de SPARC y BIG-SPARC.

MOND/RAR, NFW y Burkert no tienen implementación física en v0.2a. Sus clases nominales son *stubs*: validan los radios y lanzan `NotImplementedError` en lugar de producir predicciones falsas.

## Riesgos

- Un arreglo numéricamente válido no garantiza que sus valores sean científicamente apropiados para una galaxia o modelo concreto.
- Marcar una implementación futura como física solo describe la naturaleza declarada de su código; no constituye validación científica.
- Las reglas generales de esta fase pueden requerir extensión cuando existan parámetros, componentes bariónicos o datos observacionales reales.

## Extensión futura

`v0.2b-2` podrá preparar aceleraciones bariónicas o implementar un MOND/RAR simple después de revisión científica. NFW y Burkert deben permanecer como stubs hasta sus patches correspondientes.
