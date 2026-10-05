# M08-01 — Evaluación de riesgos

[← Página anterior](README.md) · [Siguiente página →](M08-02-gobierno-trazabilidad.md)

> Práctica del módulo. La teoría y la demostración están en el [README del módulo](README.md).
>
> Lanza los comandos desde la carpeta `infra/` del repositorio. Un paso que cuadra termina con una línea que empieza por `OK`.

### Objetivo

Listas las superficies de la arquitectura y dejas una medida para el dato, otra para el modelo y otra para el acceso.

### Prerrequisitos

- `modbus` en marcha, para leer el registro de paro.
- El inventario es el de `infra/README.md`.

### En qué consiste

Cada contenedor que publicaste es una superficie. El cruce con OT es el tema de dictamen; el registro 10 no entra en ese cruce. Las medidas de este laboratorio son concretas: el dato no sale del volumen, el modelo lleva versión, los puertos se publican solo en el puesto.

### 1 — Inventariar y mirar el paro

**Acción:** `docker compose --profile lab run --rm --no-deps lab m08-01`

**Por qué:** No se protege lo que no está escrito.

**Resultado esperado:** `OK m08-01:` lista de servicios y `paro de seguridad en 0`. Tres medidas: dato, modelo y acceso.

## Comprueba tu entendimiento

**Tres medidas**

Comprueba que no son la misma frase.

→ Una habla del volumen local, otra de la versión, otra de los puertos.

## Reto

### 1 — El agente

¿Qué medida tomaste al no crear una herramienta de escritura?

<details>
<summary>Ver solución</summary>

No dar la herramienta. M05-04 ya la rechazó.

</details>

## Errores frecuentes

| Síntoma | Causa probable | Cómo arreglarlo |
|---------|----------------|-----------------|
| modbus no disponible | el esclavo está parado | `docker compose up -d modbus` |
| paro distinto de 0 | alguien escribió el registro | reinicia el contenedor modbus |
