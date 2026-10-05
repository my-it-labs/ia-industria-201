# M05-03 — Asistente técnico basado en documentación

[← Página anterior](M05-02-integracion-aplicacion.md) · [Siguiente página →](M05-04-agentes.md)

> Práctica del módulo. La teoría y la demostración están en el [README del módulo](README.md).
>
> Lanza los comandos desde la carpeta `infra/` del repositorio. Un paso que cuadra termina con una línea que empieza por `OK`.

### Objetivo

El asistente contesta el par de apriete citando el procedimiento, y calla cuando el documento no habla del tema.

### Prerrequisitos

- `llm` en marcha.
- El procedimiento está en la imagen: `linea/docs/procedimiento-est01.md`.

### En qué consiste

Se parten los párrafos del procedimiento y se elige el que más palabras comparte con la pregunta. Ese párrafo entra en el mensaje al modelo. El dato que tiene que salir es 12 N·m. Una pregunta sobre el color del tornillo no tiene párrafo: no se inventa.

### 1 — Preguntar lo que sí está

**Acción:** `docker compose --profile lab run --rm --no-deps lab m05-03`

**Por qué:** Sin el párrafo, el modelo solo tendría su memoria general.

**Resultado esperado:** Verás el fragmento del par de apriete y `OK m05-03:`. La respuesta contiene 12.

### 2 — Preguntar lo que no está

**Acción:** `docker compose --profile lab run --rm --no-deps lab m05-03-ausente`

**Por qué:** El fallo grave es inventar un paso que el procedimiento no tiene.

**Resultado esperado:** `OK m05-03-ausente:` el procedimiento no habla del color.

## Comprueba tu entendimiento

**Cita**

Señala en el fragmento impreso la frase del par.

→ Está en el procedimiento, no en la memoria del modelo.

## Reto

### 1 — Documento nuevo

Si añades un párrafo al markdown, ¿reentrenas el modelo?

<details>
<summary>Ver solución</summary>

No. Vuelves a recuperar. El modelo fundacional no se toca.

</details>

## Errores frecuentes

| Síntoma | Causa probable | Cómo arreglarlo |
|---------|----------------|-----------------|
| la respuesta no contiene el 12 | el modelo pequeño no copió el número | repite; el fragmento sí tiene que mostrar 12. Si el fragmento no lo tiene, el recuperador falló |
| el servicio corta | llm parado | `docker compose ps` |
