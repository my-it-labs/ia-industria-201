# M02-03 — Preparación de información para analítica

[← Página anterior](M02-02-protocolos.md) · [Siguiente página →](../M03-ml-prediccion-anomalias/README.md)

> Práctica del módulo. La teoría y la demostración están en el [README del módulo](README.md).
>
> Lanza los comandos desde la carpeta `infra/` del repositorio. Un paso que cuadra termina con una línea que empieza por `OK`.

### Objetivo

Pasas el histórico crudo a una fila por pieza, en grados, con los huecos contados y los 9999 apartados.

### Prerrequisitos

- Solo el contenedor `lab`. No hace falta la línea en vivo.
- Genera `infra/data/crudo.csv`, `limpio.csv` e `imposibles.csv` (pocos MB).

### En qué consiste

El crudo son 800 piezas sintéticas de EST-01. Una parte de las temperaturas falta, otra viene en décimas (×10) y algunas valen 9999 (sensor clavado). El entrenamiento posterior usa solo el limpio.

### 1 — Generar y limpiar

**Acción:** `docker compose --profile lab run --rm --no-deps lab m02-03`

**Por qué:** Hay que ver el recuento antes de fiarse de un modelo.

**Resultado esperado:** `OK m02-03:` con filas de crudo, filas limpias (menos) y huecos > 0.

### 2 — Abrir los tres ficheros

**Acción:** En `infra/data/`, abre `crudo.csv`, `limpio.csv` e `imposibles.csv`.

**Por qué:** El crudo conserva el desastre. El limpio es el que se entrena. Los 9999 no se convierten en una temperatura.

**Resultado esperado:** En el limpio no hay 9999 ni valores de cientos de grados. `imposibles.csv` no está vacío.

## Comprueba tu entendimiento

**Una pieza, una fila**

Cuenta filas y valores distintos de `pieza_id` en `limpio.csv`.

→ Son el mismo número.

## Reto

### 1 — No rellenes el hueco

Localiza en el crudo una temperatura vacía y comprueba que esa pieza no está en el limpio.

<details>
<summary>Ver solución</summary>

Se excluye, no se sustituye por la media. Rellenarla escondería un sensor mudo.

</details>

## Errores frecuentes

| Síntoma | Causa probable | Cómo arreglarlo |
|---------|----------------|-----------------|
| la temperatura limpia no está en grados | una décima no se escaló | vuelve a lanzar `m02-03`; el comando es quien limpia |
| imposibles vacío | el crudo no trae 9999 | borra `infra/data/crudo.csv` y repite el comando |
