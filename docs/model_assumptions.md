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

## Pendiente de verificación

- Las fórmulas, parametrizaciones, constantes y convenciones necesarias para modelos bariónicos/Newtonianos, MOND/RAR, NFW y Burkert.
- La semántica y validación de parámetros específicos de cada familia física.
- Las convenciones de unidades al incorporar fuentes externas y las transformaciones necesarias hacia las unidades internas.
- La disponibilidad, formato, licencia y condiciones de uso de SPARC y BIG-SPARC.

MOND/RAR, NFW y Burkert no tienen implementación física en v0.2a. Sus clases nominales son *stubs*: validan los radios y lanzan `NotImplementedError` en lugar de producir predicciones falsas.

## Riesgos

- Un arreglo numéricamente válido no garantiza que sus valores sean científicamente apropiados para una galaxia o modelo concreto.
- Marcar una implementación futura como física solo describe la naturaleza declarada de su código; no constituye validación científica.
- Las reglas generales de esta fase pueden requerir extensión cuando existan parámetros, componentes bariónicos o datos observacionales reales.

## Extensión futura

`v0.2b — Modelos físicos iniciales` podrá implementar modelos revisados científicamente sobre esta interfaz. Ese trabajo deberá documentar y probar cada fórmula y parametrización antes de cambiar los stubs nominales por implementaciones físicas.
