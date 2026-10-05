# M06-01 — Inferencia en entornos edge

[← Página anterior](README.md) · [Siguiente página →](M06-02-integracion-ot.md)

> Práctica del módulo. La teoría y la demostración están en el [README del módulo](README.md).
>
> Lanza los comandos desde la carpeta `infra/` del repositorio. Un paso que cuadra termina con una línea que empieza por `OK`.

### Objetivo

Dictaminas una pieza con el modelo cargado desde disco y mides el tiempo por pieza.

### Prerrequisitos

- `modelo_defecto.joblib` de M03-03.
- Puedes parar `llm` (`docker compose stop llm`) para liberar RAM. Este paso no lo usa.
- Unos 0,4 GB.

### En qué consiste

El borde, en este laboratorio, es el mismo puesto: no hay URL. Se carga el joblib y se predicen 20 piezas seguidas para no medir solo la primera, que es la carga.

### 1 — Medir en caliente

**Acción:** `docker compose --profile lab run --rm --no-deps lab m06-01`

**Por qué:** La latencia que importa es la de la pieza siguiente, no la del arranque.

**Resultado esperado:** `OK m06-01:` milisegundos por pieza (tiene que quedar por debajo de 200) y el nombre del fichero local.

## Comprueba tu entendimiento

**Sin nube**

¿Qué dirección usa este comando para predecir?

→ Ninguna. Lee `modelo_defecto.joblib` del disco.

## Reto

### 1 — Pieza lenta

Si una pieza tardara más que el ciclo de la estación, ¿se acepta sola?

<details>
<summary>Ver solución</summary>

No. Llegar tarde es no llegar: iría a revisión. Aquí el tiempo medio cabe de sobra en un ciclo de un segundo.

</details>

## Errores frecuentes

| Síntoma | Causa probable | Cómo arreglarlo |
|---------|----------------|-----------------|
| falta el modelo | no terminó M03-03 | lanza `m03-03` |
| demasiado lenta | el puesto está saturado por el llm | `docker compose stop llm` y repite |
