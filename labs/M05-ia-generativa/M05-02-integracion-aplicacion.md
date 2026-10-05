# M05-02 — Integración desde aplicaciones

[← Página anterior](M05-01-modelo-local.md) · [Siguiente página →](M05-03-asistente-documentacion.md)

> Práctica del módulo. La teoría y la demostración están en el [README del módulo](README.md).
>
> Lanza los comandos desde la carpeta `infra/` del repositorio. Un paso que cuadra termina con una línea que empieza por `OK`.

### Objetivo

Una aplicación pide texto al servicio local y, si el servicio no está, el fallo se entiende.

### Prerrequisitos

- El contenedor `llm` en marcha y `/salud` en ok.

### En qué consiste

El comando hace de aplicación: envía un mensaje a `http://llm:8088/v1/chat/completions` y enseña la respuesta. Después intenta un host que no existe y tiene que fallar con un error de red, no con un texto inventado.

### 1 — Llamar y mostrar

**Acción:** `docker compose --profile lab run --rm --no-deps lab m05-02`

**Por qué:** Integrar es usar el contrato HTTP, no abrir la consola del modelo.

**Resultado esperado:** `OK m05-02:` ves la respuesta y una línea `servicio caído:` con el tipo de error de red.

## Comprueba tu entendimiento

**Mismo servicio**

Compara el puerto de esta llamada con el de M05-01.

→ Los dos usan el 8088. Cambia quién pide, no el modelo.

## Reto

### 1 — Tiempo máximo

Si quitas el servicio a media frase, la aplicación no puede quedarse colgada.

<details>
<summary>Ver solución</summary>

El cliente de este laboratorio corta a los 180 s. En un puesto real el límite debe ser más corto y verse en pantalla.

</details>

## Errores frecuentes

| Síntoma | Causa probable | Cómo arreglarlo |
|---------|----------------|-----------------|
| Connection refused al llm | `docker compose up -d llm` todavía no está sano | espera a `/salud` |
| no aparece servicio caído | el host inventado resolvió por error | el nombre del comando es `servicio-inexistente`; no lo cambies por localhost |
