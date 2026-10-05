# M03 — Machine learning para predicción y detección de incidencias

[← Página anterior](../M02-captura-integracion-datos/M02-03-preparacion-datos.md) · [Siguiente página →](M03-01-prediccion-defectos.md)

> [!NOTE]
> **Cómo funciona este módulo.** Primero la **teoría**, luego la **demostración guiada**, y después **practicas tú** en los laboratorios.

## Qué aprenderás

- Entrenar un modelo que relacione condiciones de proceso con un defecto posterior.
- Detectar ciclos raros sin esperar a la etiqueta de calidad.
- Comparar modelos con métricas que importan cuando el defecto es escaso.

## Teoría

Aquí el modelo aprende de ejemplos. No programa umbrales a mano: los ajusta con históricos de la línea simulada.

### Tres tareas distintas

| Tarea | Pregunta | Qué necesitas |
|-------|----------|----------------|
| Clasificación | ¿Esta pieza acabará como defecto? | Histórico con la etiqueta de calidad |
| Regresión | ¿Qué valor numérico tendrá esta señal? | Histórico del valor a estimar |
| Anomalía | ¿Este ciclo no se parece a los normales? | Sobre todo ciclos buenos; el fallo puede no estar etiquetado |

No se sustituyen. Un detector de anomalías avisa de «esto es raro». Un clasificador avisa de «esto se parece a los defectos que ya vimos».

### Cómo saber si sirve

Si el defecto es raro, acertar siempre «pieza buena» da un porcentaje alto y no detecta nada. Hay que mirar cuántos defectos reales encontró el modelo y cuántas alarmas falsas generó.

También hay que separar datos de entrenamiento y datos de prueba por tiempo o por lote. Si la misma pieza entra en los dos sitios, el resultado miente.

## Demostración guiada

Se parte del dataset de piezas ya preparado. Se entrena un clasificador sencillo que usa las señales de proceso anteriores al control de calidad.

Después se recorre un histórico de ciclos sanos y se marca lo que se aleja, sin usar la etiqueta de defecto.

Al comparar dos modelos sobre el mismo corte temporal se ve que un porcentaje global casi igual puede esconder un modelo que no encuentra defectos y otro que sí, a costa de más falsas alarmas.

## Ahora practica tú

| Lab | Título | Qué harás |
|-----|--------|-----------|
| M03-01 | [Predicción de defectos de fabricación](M03-01-prediccion-defectos.md) | Entrenar y evaluar un clasificador de defecto. |
| M03-02 | [Detección temprana de anomalías](M03-02-anomalias.md) | Marcar ciclos raros y convertirlos en aviso. |
| M03-03 | [Comparación de modelos predictivos](M03-03-comparacion-modelos.md) | Elegir entre enfoques con los mismos datos. |

→ Empieza por **[M03-01 — Predicción de defectos de fabricación](M03-01-prediccion-defectos.md)**.
