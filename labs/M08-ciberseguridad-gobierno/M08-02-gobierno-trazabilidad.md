# M08-02 — Gobierno y trazabilidad

[← Página anterior](M08-01-evaluacion-riesgos.md) · [Siguiente página →](../../README.md)

> Práctica del módulo. La teoría y la demostración están en el [README del módulo](README.md).
>
> Lanza los comandos desde la carpeta `infra/` del repositorio. Un paso que cuadra termina con una línea que empieza por `OK`.

### Objetivo

Reconstruyes entrada, dictamen y versión de una pieza, y compruebas que cambiar el fichero VERSION no reescribe el pasado.

### Prerrequisitos

- `api` en marcha, arrancada después de existir `VERSION`.
- No reinicies `api` durante el paso.

### En qué consiste

Se predicen AUD0007 y AUD0008. Entre medias se cambia `VERSION` en disco a `defecto-0.2` sin reiniciar. Las dos líneas del jsonl tienen que seguir en la versión que el proceso cargó al arrancar. El uso queda clasificado como asistencia: recomienda seguir o revisar, no escribe el paro.

### 1 — Reconstruir y no reescribir la historia

**Acción:** `docker compose --profile lab run --rm --no-deps lab m08-02`

**Por qué:** Una auditoría que cambia cuando sustituyes el fichero no sirve.

**Resultado esperado:** `OK m08-02:` las dos piezas con la versión de arranque. El comando restaura `VERSION` al terminar.

## Comprueba tu entendimiento

**Otra versión**

Busca AUD0007 en `predicciones.jsonl` después del comando.

→ Su `version` no es `defecto-0.2`.

## Reto

### 1 — Qué tipo de sistema es

Lee la frase que imprime el comando antes del OK.

<details>
<summary>Ver solución</summary>

Asistencia: no escribe el paro. No es un rechazo automático de la pieza.

</details>

## Errores frecuentes

| Síntoma | Causa probable | Cómo arreglarlo |
|---------|----------------|-----------------|
| no hay rastro | api no está guardando | `docker compose logs api` y repite M07-01 |
| el rastro cambió de versión | reiniciaste api entre las dos llamadas | vuelve a dejar una sola instancia y repite |
