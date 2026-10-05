# M07-02 — Monitorización y seguimiento operacional

[← Página anterior](M07-01-servicio-inferencia.md) · [Siguiente página →](../M08-ciberseguridad-gobierno/README.md)

> Práctica del módulo. La teoría y la demostración están en el [README del módulo](README.md).
>
> Lanza los comandos desde la carpeta `infra/` del repositorio. Un paso que cuadra termina con una línea que empieza por `OK`.

### Objetivo

Comparas la tasa de avisos de un lote normal con la de ese lote 8 °C más caliente.

### Prerrequisitos

- El mismo `modelo_defecto.joblib`.
- No hace falta GPU.

### En qué consiste

Es la misma función que sirve `api`, aplicada en lote para ver la deriva. Subir la temperatura imita un proceso que ya no es el del entrenamiento. Si la tasa de `revisar` no se mueve, no estás viendo la degradación.

### 1 — Medir base y desplazamiento

**Acción:** `docker compose --profile lab run --rm --no-deps lab m07-02`

**Por qué:** Sin una línea base, el número de después no dice nada.

**Resultado esperado:** `OK m07-02:` `tasa_desplazada` al menos 0,10 por encima de `tasa_base`. El resumen queda en `infra/data/seguimiento.json`.

## Comprueba tu entendimiento

**Dos fallos distintos**

Si paras `api` a mitad de un lote de llamadas, ¿reentrenas?

→ No. Eso es una caída del servicio. La deriva de este laboratorio es el servicio vivo con datos distintos.

## Reto

### 1 — Volver a la base

El lote original, sin los 8 °C, tiene que parecerse otra vez a `tasa_base`.

<details>
<summary>Ver solución</summary>

Si no, ya no estás puntuando el modelo que crees.

</details>

## Errores frecuentes

| Síntoma | Causa probable | Cómo arreglarlo |
|---------|----------------|-----------------|
| no se ve la deriva | el CSV no es el limpio de este curso | repite `m02-03` y `m03-03` |
| no está el joblib | saltaste M03 | `m03-03` |
