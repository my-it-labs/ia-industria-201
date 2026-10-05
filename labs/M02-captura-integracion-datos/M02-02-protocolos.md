# M02-02 — Integración mediante protocolos industriales

[← Página anterior](M02-01-telemetria.md) · [Siguiente página →](M02-03-preparacion-datos.md)

> Práctica del módulo. La teoría y la demostración están en el [README del módulo](README.md).
>
> Lanza los comandos desde la carpeta `infra/` del repositorio. Un paso que cuadra termina con una línea que empieza por `OK`.

### Objetivo

Lees la misma temperatura de EST-01 por OPC-UA y por Modbus, y cuadra con el estado que ya publica MQTT.

### Prerrequisitos

- mosquitto, sensor, y ahora también `opcua` y `modbus`.
- Puertos 4840 y 1502 libres. RAM conjunta ~0,7 GB.

### En qué consiste

No hay tres sensores. `opcua` y `modbus` leen el fichero `estado.json` que escribe `sensor`. Modbus guarda la temperatura en décimas en el registro 0 (614 significa 61,4 °C). El puerto del laboratorio es 1502, no el 502 de planta.

### 1 — Abrir las otras dos puertas

**Acción:** `docker compose up -d opcua modbus` y `docker compose ps`.

**Por qué:** Hasta que esos procesos no escuchan, no hay interoperabilidad que enseñar.

**Resultado esperado:** `opcua` y `modbus` en running.

### 2 — Leer las tres a la vez

**Acción:** `docker compose --profile lab run --rm --no-deps lab m02-02`

**Por qué:** El comando lee el nodo OPC-UA `Estacion.Temperatura`, el registro Modbus 0 con escala /10, y el JSON de estado.

**Resultado esperado:** `OK m02-02:` y una línea `estado=… opcua=… modbus=…` con los tres valores a menos de 1,5 °C.

## Comprueba tu entendimiento

**La escala**

Si Modbus devolviera 614, ¿qué temperatura es?

→ 61,4 °C. Sin dividir entre 10 el número no es una temperatura de husillo.

## Reto

### 1 — Registro que no existe

El mapa solo rellena unos pocos registros. El 10 es el paro de seguridad y vale 0.

<details>
<summary>Ver solución</summary>

Leerlo da 0. No es «proceso parado»: es un registro que este laboratorio no usa para la temperatura.

</details>

## Errores frecuentes

| Síntoma | Causa probable | Cómo arreglarlo |
|---------|----------------|-----------------|
| OPC-UA: … | el servidor no arrancó o el endpoint no es opc.tcp://opcua:4840/linea/server | `docker compose logs opcua` |
| Modbus no coincide | se olvidó la escala /10 | el laboratorio ya la aplica; si ves el entero crudo, estás leyendo el registro a mano |
