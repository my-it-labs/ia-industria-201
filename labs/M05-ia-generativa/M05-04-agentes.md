# M05-04 — Automatización mediante agentes

[← Página anterior](M05-03-asistente-documentacion.md) · [Siguiente página →](../M06-edge-integracion-ot/README.md)

> Práctica del módulo. La teoría y la demostración están en el [README del módulo](README.md).
>
> Lanza los comandos desde la carpeta `infra/` del repositorio. Un paso que cuadra termina con una línea que empieza por `OK`.

### Objetivo

El agente lee la temperatura con una herramienta y se niega a escribir en el automatismo.

### Prerrequisitos

- `llm` y `sensor` en marcha (hace falta un estado vivo).
- RAM: el llm sigue siendo el coste grande.

### En qué consiste

La herramienta `leer_estacion` lee `estado.json`. La orquestación la llama cuando la pregunta es el valor de la estación, guarda la traza y pide al modelo una frase que incluya ese número, sin cambiarlo. No existe herramienta de escritura: pedir un cambio se rechaza antes de tocar el proceso.

### 1 — Pedir el valor y pedir un cambio

**Acción:** `docker compose --profile lab run --rm --no-deps lab m05-04`

**Por qué:** El número tiene que salir de la herramienta. Escribir en el proceso no está permitido.

**Resultado esperado:** `OK m05-04:` con la temperatura medida. La traza queda en `infra/data/traza_agente.jsonl`. La línea de escritura dice que no hay herramienta.

## Comprueba tu entendimiento

**La cifra no es inventada**

Compara el número de la frase con `infra/data/estado.json`.

→ Son el mismo.

## Reto

### 1 — Segunda herramienta

¿Añadirías una herramienta que escriba el registro de paro?

<details>
<summary>Ver solución</summary>

No. El agente de este curso solo lee. El paro no se toca.

</details>

## Errores frecuentes

| Síntoma | Causa probable | Cómo arreglarlo |
|---------|----------------|-----------------|
| la frase no incluye el valor | el modelo no copió el número de la herramienta | repite; el estado tiene que existir (`docker compose up -d sensor`) |
| no quedó traza | el comando no llegó a escribir el jsonl | mira el permiso de `infra/data` |
