# M02 — Captura, integración y preparación de datos

[← Página anterior](../M01-ia-industrial-arquitectura/M01-02-visualizacion-supervision.md) · [Siguiente página →](M02-01-telemetria.md)

> [!NOTE]
> **Cómo funciona este módulo.** Primero la **teoría**, luego la **demostración guiada**, y después **practicas tú** en los laboratorios.

## Qué aprenderás

- Publicar y consumir telemetría de la estación.
- Leer el mismo hecho por MQTT, OPC-UA y Modbus simulado.
- Dejar un dataset limpio, con unidades y sin huecos escondidos.

## Teoría

El modelo solo ve lo que la integración le entrega. Si la hora está mal, la unidad cambia a mitad de turno o faltan piezas, el entrenamiento aprende ese desastre.

### De dónde sale el dato

En la planta real sería un sensor cableado a un PLC. Aquí el PLC y el sensor son simulados, con la misma forma: un valor, una unidad, una hora y un nombre de variable.

### Tres formas de llevarse el dato

| Protocolo | Idea | Cuándo encaja |
|-----------|------|----------------|
| MQTT | Alguien publica un mensaje en un tema; quien se ha suscrito lo recibe | Eventos y telemetría ligera |
| OPC-UA | Un servidor expone variables con nombre y tipo; un cliente las lee o se suscribe | Integrar con equipos que ya hablan OPC-UA |
| Modbus TCP | Registros numerados en una dirección IP | Equipos sencillos que exponen holding registers |

No son tres verdades distintas. Son tres puertas al mismo hecho de proceso. El laboratorio lo demuestra leyendo la misma estación por las tres.

### Calidad mínima antes de analizar

- Hora presente y ordenable.
- Unidad explícita (°C no mezclados con décimas).
- Identificador de pieza o de ciclo.
- Huecos visibles, no rellenados en silencio.
- Valores imposibles apartados (una temperatura de 9999 es un fallo de sensor, no un pico de proceso).

## Demostración guiada

El recorrido enseña la misma estación publicada por MQTT. Un cliente suscrito al tema recibe ciclos sin preguntar uno a uno.

A continuación se abre un servidor OPC-UA simulado y un esclavo Modbus con los mismos números en otros nombres: nodo OPC y registro Modbus. El valor coincide. Cambia el modo de acceso, no la física.

Al final, una tabla pasa de «filas tal cual llegaron» a un dataset con tipos, huecos marcados y unidades homogéneas.

## Ahora practica tú

| Lab | Título | Qué harás |
|-----|--------|-----------|
| M02-01 | [Captura de telemetría industrial](M02-01-telemetria.md) | Publicar lecturas y consumirlas como eventos. |
| M02-02 | [Integración mediante protocolos industriales](M02-02-protocolos.md) | Leer la estación por MQTT, OPC-UA y Modbus. |
| M02-03 | [Preparación de información para analítica](M02-03-preparacion-datos.md) | Limpiar y normalizar hasta tener un dataset usable. |

→ Empieza por **[M02-01 — Captura de telemetría industrial](M02-01-telemetria.md)**.
