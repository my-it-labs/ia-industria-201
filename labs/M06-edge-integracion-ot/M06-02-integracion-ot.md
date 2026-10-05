# M06-02 — Integración con sistemas industriales

[← Página anterior](M06-01-inferencia-edge.md) · [Siguiente página →](../M07-mlops-observabilidad/README.md)

> Práctica del módulo. La teoría y la demostración están en el [README del módulo](README.md).
>
> Lanza los comandos desde la carpeta `infra/` del repositorio. Un paso que cuadra termina con una línea que empieza por `OK`.

### Objetivo

Publicas el dictamen como evento y compruebas que el registro de paro sigue en cero.

### Prerrequisitos

- mosquitto, sensor y modbus en marcha.
- El modelo de M03-03.

### En qué consiste

Cada dictamen va al tema `linea/est01/dictamen` con pieza, decisión (`seguir` o `revisar`) y probabilidad. El consumidor hace de automatismo: se entera por el evento. El registro Modbus 10 es el paro de seguridad y este flujo no lo escribe. La presión no viene en el ciclo vivo; el laboratorio usa la consigna nominal de 6 bar.

### 1 — Publicar y no tocar el paro

**Acción:** `docker compose --profile lab run --rm --no-deps lab m06-02`

**Por qué:** OT lee eventos. No lee el fichero del modelo ni obedece un modelo en el enclavamiento.

**Resultado esperado:** `OK m06-02:` pieza, decisión y `paro=0`.

## Comprueba tu entendimiento

**Evento completo**

En el JSON impreso, comprueba que `evento.pieza_id` es el de `estado.json`.

→ Son la misma pieza.

## Reto

### 1 — Confianza baja

Si la probabilidad pasa de 0,5 la decisión es `revisar` aunque preferirías seguir fabricando.

<details>
<summary>Ver solución</summary>

Dudar es una decisión de proceso. El umbral está en el código del comando, no en el PLC.

</details>

## Errores frecuentes

| Síntoma | Causa probable | Cómo arreglarlo |
|---------|----------------|-----------------|
| el automatismo no recibió el dictamen | mosquitto caído | `docker compose up -d mosquitto sensor modbus` |
| el registro de paro cambió | algo escribió el registro 10 | no debe ocurrir; reinicia `modbus` |
