# M02-01 — Captura de telemetría industrial

[← Página anterior](README.md) · [Siguiente página →](M02-02-protocolos.md)

> Práctica del módulo. La teoría y la demostración están en el [README del módulo](README.md).
>
> Lanza los comandos desde la carpeta `infra/` del repositorio. Un paso que cuadra termina con una línea que empieza por `OK`.

### Objetivo

Publicas la telemetría de EST-01 y la consumes como eventos, incluido el hueco cuando el origen se detiene.

### Prerrequisitos

- `mosquitto` y `sensor` en marcha. El panel puede estar parado: aquí no hace falta.
- RAM de este paso: ~0,3 GB.

### En qué consiste

El sensor publica JSON en el tema `linea/est01/ciclo` cada segundo: pieza, hora, temperatura, vibración y corriente. Tú te suscribes. No se entrena nada.

### 1 — Consumir un ciclo

**Acción:** `docker compose --profile lab run --rm --no-deps lab m02-01`

**Por qué:** Suscribirse es enterarse del evento, no leer un archivo a posteriori.

**Resultado esperado:** `OK m02-01:` y el JSON con `pieza_id`, `temperatura_c`, `vibracion_mm_s` y `ts`.

### 2 — Abrir el hueco

**Acción:** `docker compose stop sensor` y, enseguida, `docker compose --profile lab run --rm --no-deps lab m02-01-pausa`.

**Por qué:** Una parada del origen no debe inventar lecturas. El hueco se ve porque no llega nada.

**Resultado esperado:** `OK m02-01-pausa:` ningún ciclo en 3 segundos.

### 3 — Reanudar

**Acción:** `docker compose start sensor` y otra vez `lab m02-01`.

**Por qué:** Al volver el origen llegan ciclos nuevos. Los perdidos durante la pausa no reaparecen.

**Resultado esperado:** `OK m02-01:` con una pieza posterior a la última que viste antes de parar.

## Comprueba tu entendimiento

**Tema**

Di el tema del que sale el JSON.

→ `linea/est01/ciclo`.

## Reto

### 1 — Dos orígenes

Si lanzaras un segundo publicador contra el mismo tema, ¿qué vería el consumidor?

<details>
<summary>Ver solución</summary>

Dos voces en el mismo tema, sin saber cuál es la estación. Por eso el ciclo lleva `estacion` y `pieza_id`.

</details>

## Errores frecuentes

| Síntoma | Causa probable | Cómo arreglarlo |
|---------|----------------|-----------------|
| siguen llegando ciclos con el sensor parado | no llegaste a pararlo, o hay otro sensor | `docker compose ps` y deja un solo sensor |
| no hay telemetría | mosquitto o sensor caídos | `docker compose up -d mosquitto sensor` |
