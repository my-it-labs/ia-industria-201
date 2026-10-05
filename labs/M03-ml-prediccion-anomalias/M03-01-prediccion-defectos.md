# M03-01 — Predicción de defectos de fabricación

[← Página anterior](README.md) · [Siguiente página →](M03-02-anomalias.md)

> Práctica del módulo. La teoría y la demostración están en el [README del módulo](README.md).
>
> Lanza los comandos desde la carpeta `infra/` del repositorio. Un paso que cuadra termina con una línea que empieza por `OK`.

### Objetivo

Entrenas un clasificador que relaciona las señales de proceso con un defecto ya etiquetado, y lo mides por defectos encontrados.

### Prerrequisitos

- `infra/data/limpio.csv` (sale de M02-03). Si falta, este comando lo regenera.
- RAM del entrenamiento: ~0,5 GB. CPU, sin GPU.

### En qué consiste

Las piezas van ordenadas por identificador, que aquí es el tiempo. El 70 % primero entrena; el 30 % último solo se evalúa. El modelo es una regresión logística con las clases equilibradas. La etiqueta `defecto` imita un control de calidad posterior: no está entre las columnas que el modelo puede usar como entrada.

### 1 — Entrenar y evaluar el tramo nuevo

**Acción:** `docker compose --profile lab run --rm --no-deps lab m03-01`

**Por qué:** El porcentaje global miente cuando el defecto es la clase pequeña. El comando imprime recall y falsas alarmas.

**Resultado esperado:** `OK m03-01:` con `recall_defecto` de al menos 0,45. También verás tp, fp, fn y tn.

### 2 — Guardar el modelo de este enfoque

**Acción:** El propio comando deja `infra/data/modelo_logreg.joblib`.

**Por qué:** Sin fichero no hay nada que comparar en M03-03 ni que servir después.

**Resultado esperado:** El fichero existe al lado del CSV.

## Comprueba tu entendimiento

**Qué número mirar**

En el JSON, lee `recall` y `fn`.

→ `fn` son defectos reales que el modelo dejó pasar. `recall` es la fracción que sí encontró.

## Reto

### 1 — Columna que llega tarde

Si añadieras la propia columna `defecto` como entrada, el acierto sería perfecto.

<details>
<summary>Ver solución</summary>

Eso no predice: lee la etiqueta. Las entradas permitidas son solo temperatura, vibración, corriente y presión.

</details>

## Errores frecuentes

| Síntoma | Causa probable | Cómo arreglarlo |
|---------|----------------|-----------------|
| recall demasiado bajo | el CSV limpio está mal generado | repite M02-03 y luego M03-01 |
| no está limpio.csv | no corriste M02-03 | el comando lo crea si falta; si falla, lanza `m02-03` |
