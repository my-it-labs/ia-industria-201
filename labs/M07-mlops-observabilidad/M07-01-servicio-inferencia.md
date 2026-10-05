# M07-01 — Publicación de servicios de inferencia

[← Página anterior](README.md) · [Siguiente página →](M07-02-monitorizacion.md)

> Práctica del módulo. La teoría y la demostración están en el [README del módulo](README.md).
>
> Lanza los comandos desde la carpeta `infra/` del repositorio. Un paso que cuadra termina con una línea que empieza por `OK`.

### Objetivo

Publicas el clasificador como servicio y la respuesta dice qué versión contestó.

### Prerrequisitos

- M03-03 hecho (`modelo_defecto.joblib` y `VERSION`).
- `docker compose up -d api`. Puerto 8000. Techo 768 MB.
- http://localhost:8000/salud tiene que responder antes del comando.

### En qué consiste

Al arrancar, `api` carga el joblib y lee `VERSION` una vez. Cada `POST /predecir` guarda una línea en `predicciones.jsonl` con entrada, dictamen y esa versión. Una pieza sin señales se rechaza: el servicio no rellena huecos.

### 1 — Llamar al servicio

**Acción:** `docker compose --profile lab run --rm --no-deps lab m07-01`

**Por qué:** Las aplicaciones llaman al servicio, no abren el fichero del modelo.

**Resultado esperado:** `OK m07-01:` con `version=defecto-0.1` (o la que cargó al arrancar) y un dictamen. Una petición incompleta no cuela.

## Comprueba tu entendimiento

**La versión viaja**

Abre `infra/data/predicciones.jsonl` y lee `version` de la última línea.

→ Es la misma que `/salud`.

## Reto

### 1 — Pieza incompleta

El comando ya manda un JSON solo con `pieza_id`. ¿Qué código vuelve?

<details>
<summary>Ver solución</summary>

Un error 4xx. No hay dictamen.

</details>

## Errores frecuentes

| Síntoma | Causa probable | Cómo arreglarlo |
|---------|----------------|-----------------|
| el servicio no está | api no arrancó porque faltaba el joblib | `docker compose logs api` y, si falta el modelo, `m03-03` y `docker compose up -d api` |
| responde otra versión | el contenedor se arrancó con un VERSION viejo | `docker compose up -d --force-recreate api` después de cambiar el fichero |
