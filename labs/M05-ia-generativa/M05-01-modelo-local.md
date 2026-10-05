# M05-01 — Ejecución local de modelos generativos

[← Página anterior](README.md) · [Siguiente página →](M05-02-integracion-aplicacion.md)

> Práctica del módulo. La teoría y la demostración están en el [README del módulo](README.md).
>
> Lanza los comandos desde la carpeta `infra/` del repositorio. Un paso que cuadra termina con una línea que empieza por `OK`.

### Objetivo

Arrancas un modelo generativo en el puesto y compruebas que responde en local.

### Prerrequisitos

- Para el panel si sigue en marcha (`docker compose stop panel`): el modelo pide RAM.
- Fichero `infra/modelos/qwen2.5-0.5b-instruct-q4_k_m.gguf` (~470 MB). Descarga, una sola vez:
- `curl -L -o modelos/qwen2.5-0.5b-instruct-q4_k_m.gguf https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct-GGUF/resolve/main/qwen2.5-0.5b-instruct-q4_k_m.gguf`
- Luego `docker compose up -d llm`. Techo del contenedor: 2 GB. CPU, sin GPU. La primera carga tarda.

### En qué consiste

El contenedor `llm` carga Qwen2.5 de 0,5B cuantizado a 4 bits y escucha en el puerto 8088. No llama a ningún proveedor. En un Codespace justo, no lo dejes conviviendo con el panel.

### 1 — Esperar a que cargue

**Acción:** Abre http://localhost:8088/salud hasta que responda `estado: ok`.

**Por qué:** Hasta que el proceso no tiene el modelo en memoria, no hay inferencia.

**Resultado esperado:** JSON con el nombre del fichero `.gguf`.

### 2 — Una pregunta corta

**Acción:** `docker compose --profile lab run --rm --no-deps lab m05-01`

**Por qué:** Mide el puesto: tiempo de una respuesta corta.

**Resultado esperado:** `OK m05-01:` con los segundos y la URL `http://llm:8088` (dentro de la red Docker eso es el propio puesto, no internet).

## Comprueba tu entendimiento

**Sigue en local**

La URL que imprime el OK, ¿sale del puesto o de un dominio externo?

→ Es `http://llm:8088`, el contenedor. No aparece un proveedor.

## Reto

### 1 — Modelo más grande

¿Por qué este curso no baja un modelo de varios GB?

<details>
<summary>Ver solución</summary>

En 8 GB de RAM y sin GPU no responde a tiempo de un laboratorio. 0,5B cabe y basta para ver inferencia, recuperación y el límite de un modelo pequeño.

</details>

## Errores frecuentes

| Síntoma | Causa probable | Cómo arreglarlo |
|---------|----------------|-----------------|
| el servicio local no responde | sigue cargando o falta el gguf | `docker compose logs llm` y comprueba `infra/modelos/` |
| tarda minutos | es la primera carga en CPU | espera a `/salud` antes de repetir el comando |
