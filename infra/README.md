# Entorno de la línea EST-01

Los laboratorios ocurren en una **estación de mecanizado simulada** (EST-01). No hay PLC, cámara ni nube del cliente: cada señal nace en un contenedor y se puede volver a generar.

Trabaja siempre desde esta carpeta (`infra/`).

```bash
docker compose up -d mosquitto sensor archivador
docker compose --profile lab run --rm --no-deps lab m01-01
```

## Qué proceso es cada contenedor

| Servicio | Proceso | Puerto en tu máquina | Qué emula |
|----------|---------|----------------------|-----------|
| `mosquitto` | Broker MQTT | 1883 | El transporte de eventos de la estación |
| `sensor` | Publica un ciclo por segundo y escribe `/data/estado.json` | — | El origen: husillo, vibración y corriente |
| `archivador` | Se suscribe a `linea/est01/ciclo` y guarda SQLite | — | El histórico del turno |
| `opcua` | Servidor OPC-UA que lee el mismo estado | 4840 | Un equipo que ya habla OPC-UA |
| `modbus` | Esclavo Modbus TCP. La temperatura va en décimas en el registro 0. El registro 10 es el paro de seguridad y **nadie lo escribe** | 1502 (en planta el puerto habitual es 502) | Un automatismo sencillo |
| `panel` | Streamlit sobre el SQLite | 8501 | El panel del turno |
| `llm` | Modelo generativo en local (Qwen2.5 0.5B, GGUF Q4) | 8088 | Asistencia, sin salir a una API |
| `api` | FastAPI con el clasificador entrenado en M03 | 8000 | El servicio de inferencia en operación |
| `lab` | No se queda arrancado. `docker compose run` ejecuta un paso | — | Tus comandos de laboratorio |

El estado vivo está en `infra/data/` (no se versiona). El modelo generativo está en `infra/modelos/` (el fichero `.gguf` tampoco se versiona).

## De dónde sale el dato

| Dato | Origen | Cómo se crea |
|------|--------|----------------|
| Ciclo en vivo | `sensor` | Secuencia determinista, un mensaje/s en `linea/est01/ciclo` |
| Misma señal por OPC-UA y Modbus | `opcua` y `modbus` leen `estado.json` | No hay un segundo proceso físico |
| Histórico para entrenar | `python -m linea.cli m02-03` | 800 piezas sintéticas, con huecos, temperaturas en décimas y algún 9999 |
| Imágenes de calidad | `m04-01` | 64×64 generadas con Pillow: pieza gris y, si hay defecto, un rayón blanco |
| Procedimiento del asistente | `linea/docs/procedimiento-est01.md` | Texto fijo del laboratorio. El par de apriete es 12 N·m |
| Modelo de lenguaje | descarga única | Ver M05 |

Nada de esto es telemetría de una planta real.

## Cómo levantar los emuladores

No hace falta tenerlos todos a la vez.

```bash
# Dato en vivo: MQTT, origen y archivo
docker compose up -d mosquitto sensor archivador

# Las otras dos puertas al mismo valor
docker compose up -d opcua modbus

# Panel
docker compose up -d panel

# Generativo (antes, el fichero del modelo; ver M05)
docker compose up -d llm

# Servicio del clasificador (después de M03-03)
docker compose up -d api

docker compose ps
docker compose logs -f sensor
docker compose stop sensor    # provoca el hueco de telemetría
docker compose start sensor
```

Un paso de laboratorio:

```bash
docker compose --profile lab run --rm --no-deps lab m01-01
```

El comando imprime una línea `OK m01-01: ...` cuando el paso cuadra.

## Requisitos del curso

Medidos para que quepan en un puesto justo y en un Codespace pequeño. Los techos son los `mem_limit` del `docker-compose.yml`.

| | Mínimo para M01–M04 y M06–M08 | Para poder hacer también M05 |
|--|-------------------------------|------------------------------|
| CPU | 2 núcleos | 2 núcleos (mejor 4: la respuesta del modelo es por CPU) |
| RAM libre | 4 GB | 8 GB |
| Disco libre | 4 GB (imagen + datos) | + 1 GB para el GGUF (~470 MB) y la carga |
| Docker | Engine 24+ y Compose v2 | igual |
| Red | Solo el primer `docker compose build` y el `pull` de Mosquitto | Más la descarga del GGUF, una vez |
| Puertos libres | 1883, 4840, 1502, 8501 | + 8088 y, desde M07, 8000 |

En un Codespace de 2 núcleos y 8 GB entra el curso si **no** dejas el panel y el modelo generativo arrancados a la vez. Para M05 para el panel (`docker compose stop panel`).

Después de construir la imagen y, si toca M05, de tener el GGUF en disco, los laboratorios siguen sin internet: no llaman a una API externa.

## Requisitos por laboratorio

| Lab | Contenedores que tienen que estar arriba | RAM de esos contenedores | Disco extra | Red |
|-----|------------------------------------------|--------------------------|-------------|-----|
| M01-01 | mosquitto, sensor, archivador | ~0,5 GB | el histórico crece unos KB/s | no |
| M01-02 | los anteriores + panel | ~1 GB | igual | no |
| M02-01 | mosquitto, sensor | ~0,3 GB | — | no |
| M02-02 | los anteriores + opcua + modbus | ~0,7 GB | — | no |
| M02-03 | solo `lab` (genera CSV) | ~0,4 GB en el run | < 5 MB | no |
| M03-01 a M03-03 | `lab` y el CSV de M02-03 | ~0,5 GB | el `.joblib` | no |
| M04-01 a M04-03 | `lab` | ~0,5 GB | ~80 PNG pequeñas | no |
| M05-01 a M05-04 | `llm` (+ sensor en M05-04) | hasta 2 GB | ~470 MB del GGUF | solo la primera descarga |
| M06-01 | `lab` con el modelo de M03 | ~0,4 GB | — | no |
| M06-02 | `lab` + mosquitto + modbus + sensor | ~0,7 GB | — | no |
| M07-01, M07-02 | `api` + el `.joblib` | ~0,8 GB | el registro jsonl | no |
| M08-01 | modbus (registro de paro) | ~0,2 GB | — | no |
| M08-02 | `api` | ~0,8 GB | el jsonl de predicciones | no |

Para el panel: <http://localhost:8501>. Para el servicio de inferencia: <http://localhost:8000/salud>. Para el modelo generativo: <http://localhost:8088/salud>.
