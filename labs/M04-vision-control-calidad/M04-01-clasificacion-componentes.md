# M04-01 — Clasificación automática de componentes

[← Página anterior](README.md) · [Siguiente página →](M04-02-deteccion-defectos.md)

> Práctica del módulo. La teoría y la demostración están en el [README del módulo](README.md).
>
> Lanza los comandos desde la carpeta `infra/` del repositorio. Un paso que cuadra termina con una línea que empieza por `OK`.

### Objetivo

Entrenas un clasificador que separa componente correcto y defectuoso, y lo pruebas con imágenes que no vio.

### Prerrequisitos

- Solo `lab`. Genera 80 PNG pequeñas en `infra/data/imagenes/`.
- Sin cámara y sin GPU.

### En qué consiste

Las imágenes son sintéticas: una pieza gris y, en las malas, un rayón blanco. Hay 40 y 40. El 30 % final no entra al entrenamiento. El modelo es una regresión logística sobre la imagen reducida a 16×16.

### 1 — Contar y entrenar

**Acción:** `docker compose --profile lab run --rm --no-deps lab m04-01`

**Por qué:** Si una clase no existe, no hay nada que aprender. Aquí están equilibradas a propósito para que el límite lo veas en el laboratorio siguiente, no en un dataset vacío.

**Resultado esperado:** `OK m04-01:` con un acierto en prueba de al menos 0,85. Queda `modelo_vision.joblib`.

### 2 — Abrir una de cada

**Acción:** Abre un PNG de `imagenes/buenas` y otro de `imagenes/defectuosas`.

**Por qué:** Tienes que ver qué está aprendiendo el modelo: el rayón, no un fondo distinto.

**Resultado esperado:** La defectuosa tiene una línea clara. La buena, no.

## Comprueba tu entendimiento

**Imágenes nuevas**

El acierto que imprime el comando, ¿de qué imágenes es?

→ Del 30 % apartado, no del entrenamiento.

## Reto

### 1 — Atajo

Si todas las malas tuvieran otro fondo, el modelo podría ignorar el rayón.

<details>
<summary>Ver solución</summary>

En este generador el fondo es el mismo. El rayón es la diferencia.

</details>

## Errores frecuentes

| Síntoma | Causa probable | Cómo arreglarlo |
|---------|----------------|-----------------|
| acierto bajo | las imágenes no se generaron | borra `infra/data/imagenes` y repite |
| no abre el PNG | estás en el contenedor, no en el disco del host | la carpeta montada es `infra/data/imagenes` |
