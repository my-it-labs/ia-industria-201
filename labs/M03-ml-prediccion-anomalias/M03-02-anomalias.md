# M03-02 — Detección temprana de anomalías

[← Página anterior](M03-01-prediccion-defectos.md) · [Siguiente página →](M03-03-comparacion-modelos.md)

> Práctica del módulo. La teoría y la demostración están en el [README del módulo](README.md).
>
> Lanza los comandos desde la carpeta `infra/` del repositorio. Un paso que cuadra termina con una línea que empieza por `OK`.

### Objetivo

Ajustas un detector con ciclos normales y cuentas cuántos ciclos raros inyectados avisa.

### Prerrequisitos

- CPU. No usa la etiqueta de defecto para avisar.
- Unos 0,5 GB en el `run`.

### En qué consiste

El ajuste usa solo piezas sin defecto del histórico limpio. Cada señal se pone en su propia escala y el aviso sale de la distancia de Mahalanobis: cuánto se aleja el ciclo, en conjunto, de lo normal. Un bosque de aislamiento no vale aquí: un valor muy alto se queda en la misma rama que el máximo del histórico y no se aísla. Luego se puntúa otro fichero: 180 ciclos normales y 20 con la vibración subida a propósito. Esa marca `inyectada` no entra al modelo; solo sirve para saber si el aviso acertó.

### 1 — Ajustar y avisar

**Acción:** `docker compose --profile lab run --rm --no-deps lab m03-02`

**Por qué:** La anomalía es «no se parece a lo normal», no «se parece a un defecto ya etiquetado».

**Resultado esperado:** `OK m03-02:` con detectados/inyectados de al menos 70 %.

## Comprueba tu entendimiento

**Para qué es la marca**

¿El modelo recibe la columna `inyectada`?

→ No. Si la recibiera, no estaría detectando: estaría leyendo la respuesta.

## Reto

### 1 — Umbral más duro

Si el detector marcara la mitad del día, dejaría de ser una alerta.

<details>
<summary>Ver solución</summary>

El corte es una distancia de Mahalanobis de 13,3 (el percentil 99 de una chi-cuadrado con 4 señales). Subirlo esconde los inyectados; bajarlo llena el turno de avisos sobre ciclos normales.

</details>

## Errores frecuentes

| Síntoma | Causa probable | Cómo arreglarlo |
|---------|----------------|-----------------|
| no ve los ciclos inyectados | entrenó con los raros dentro | el comando separa normales e inyectados; relánzalo |
| FALLO sin número | falta scikit-learn en la imagen | `docker compose build` otra vez |
