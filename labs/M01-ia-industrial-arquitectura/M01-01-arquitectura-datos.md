# M01-01 — Arquitectura básica de datos

[← Página anterior](README.md) · [Siguiente página →](M01-02-visualizacion-supervision.md)

> Práctica del módulo. La teoría y la demostración están en el [README del módulo](README.md).
>
> Lanza los comandos desde la carpeta `infra/` del repositorio. Un paso que cuadra termina con una línea que empieza por `OK`.

### Objetivo

Dejas una lectura de EST-01 recorriendo origen, transporte y almacén, con la misma pieza en los tres sitios.

### Prerrequisitos

- Docker en marcha. Imagen ya construida (`docker compose build` en `infra/`).
- RAM: unos 0,5 GB para mosquitto, sensor y archivador.
- [Qué es cada contenedor](../../infra/README.md).

### En qué consiste

EST-01 es una estación de mecanizado simulada. `sensor` inventa el ciclo y lo publica en MQTT. `mosquitto` lo transporta. `archivador` lo guarda en SQLite. No hay modelo.

### 1 — Levantar origen, transporte y almacén

**Acción:** En `infra/`: `docker compose up -d mosquitto sensor archivador` y luego `docker compose ps`.

**Por qué:** Cada contenedor es una pieza de la arquitectura. Si no está en `ps`, ese tramo no existe.

**Resultado esperado:** Los tres servicios figuran como running. `sensor` es el origen, `mosquitto` el transporte, `archivador` el almacén.

### 2 — Ver el ciclo cruzar

**Acción:** `docker compose --profile lab run --rm --no-deps lab m01-01`

**Por qué:** El comando lee un mensaje del tema `linea/est01/ciclo` y cuenta filas en el SQLite. Así compruebas que no se pierde la pieza.

**Resultado esperado:** Una línea `OK m01-01:` con un identificador de pieza y un total archivado mayor que cero.

### 3 — Mirar el proceso, no solo el OK

**Acción:** `docker compose logs --tail=5 sensor` y `docker compose logs --tail=5 archivador`.

**Por qué:** El OK resume. Los logs enseñan quién publicó y quién guardó.

**Resultado esperado:** El sensor imprime `Pxxxx` y una temperatura. El archivador imprime la misma pieza un instante después.

## Comprueba tu entendimiento

**La misma pieza**

En la salida de `m01-01`, quédate con el `pieza_id` del JSON.

→ Ese identificador aparece en el mensaje MQTT y el archivador ya lleva al menos un ciclo.

## Reto

### 1 — Para el origen

Haz `docker compose stop sensor`, espera dos segundos y vuelve a lanzar `lab m01-01`.

<details>
<summary>Ver solución</summary>

Sin `sensor` no hay ciclos nuevos. `docker compose start sensor` devuelve el flujo. El almacén conserva lo ya guardado.

</details>

## Errores frecuentes

| Síntoma | Causa probable | Cómo arreglarlo |
|---------|----------------|-----------------|
| FALLO: el archivador no tiene ciclos | sensor o mosquitto no han arrancado | Mira `docker compose ps` y los logs de sensor |
| el run no encuentra el servicio lab | falta `--profile lab` | Copia el comando del paso 2 tal cual |
