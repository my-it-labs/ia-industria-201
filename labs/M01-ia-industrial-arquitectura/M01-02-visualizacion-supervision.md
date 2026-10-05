# M01-02 — Visualización y supervisión de procesos

[← Página anterior](M01-01-arquitectura-datos.md) · [Siguiente página →](../M02-captura-integracion-datos/README.md)

> Práctica del módulo. La teoría y la demostración están en el [README del módulo](README.md).
>
> Lanza los comandos desde la carpeta `infra/` del repositorio. Un paso que cuadra termina con una línea que empieza por `OK`.

### Objetivo

Lees la estación en indicadores —nivel, serie y margen— y no en una lista cruda.

### Prerrequisitos

- M01-01 hecho: mosquitto, sensor y archivador en marcha.
- RAM adicional del panel: hasta 512 MB. Puerto 8501 libre.

### En qué consiste

El panel es otro contenedor (`panel`, Streamlit). Lee el mismo SQLite del archivador. El margen de 70 °C es una regla de operación, no un modelo.

### 1 — Arrancar el panel

**Acción:** `docker compose up -d panel` y abre http://localhost:8501.

**Por qué:** Supervisar es mirar un indicador. El contenedor `panel` es ese puesto.

**Resultado esperado:** Ves la pieza actual, la temperatura, la vibración y una serie. Si la temperatura pasa de 70 °C el panel lo marca.

### 2 — Comprobar el dato detrás del dibujo

**Acción:** `docker compose --profile lab run --rm --no-deps lab m01-02`

**Por qué:** Confirma que el panel responde y cuántas lecturas de la ventana están fuera del margen.

**Resultado esperado:** `OK m01-02:` con el código HTTP del panel, el número de lecturas y las que superan 70 °C.

## Comprueba tu entendimiento

**Margen visible**

En el panel, lee el número de lecturas fuera de margen que declara el recuadro.

→ Coincide con `fuera_de_margen` impreso por `m01-02`.

## Reto

### 1 — Quita el panel

`docker compose stop panel` y recarga http://localhost:8501.

<details>
<summary>Ver solución</summary>

La página deja de abrir. Los ciclos siguen archivándose: el panel no es el origen. `docker compose start panel` lo devuelve.

</details>

## Errores frecuentes

| Síntoma | Causa probable | Cómo arreglarlo |
|---------|----------------|-----------------|
| localhost:8501 no abre | el contenedor panel no está running o el puerto está ocupado | `docker compose ps` y `docker compose logs panel` |
| El panel dice que no hay histórico | el archivador acaba de crear la base y aún no entró un ciclo | Espera un segundo y recarga |
