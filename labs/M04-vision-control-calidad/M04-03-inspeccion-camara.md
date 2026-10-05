# M04-03 — Sistema de inspección basado en cámara

[← Página anterior](M04-02-deteccion-defectos.md) · [Siguiente página →](../M05-ia-generativa/README.md)

> Práctica del módulo. La teoría y la demostración están en el [README del módulo](README.md).
>
> Lanza los comandos desde la carpeta `infra/` del repositorio. Un paso que cuadra termina con una línea que empieza por `OK`.

### Objetivo

Cierras el flujo: una carpeta de imágenes entra y sale un registro con decisión por pieza.

### Prerrequisitos

- `modelo_vision.joblib` de M04-01.
- Escribe `lote_entrada/` y `lote_resultado.csv`.

### En qué consiste

Se copian 3 buenas y 3 malas a `lote_entrada`. Cada una recibe probabilidad de defecto. Con 0,5 o más, la decisión es `revisar`; por debajo, `aceptar`. Dudar manda a revisión, no a aceptar.

### 1 — Pasar el lote

**Acción:** `docker compose --profile lab run --rm --no-deps lab m04-03`

**Por qué:** Inspeccionar es producir un dictamen por imagen, no volver a entrenar.

**Resultado esperado:** `OK m04-03:` seis filas y al menos una `revisar`. El CSV está en `infra/data/lote_resultado.csv`.

## Comprueba tu entendimiento

**El registro cuadra**

Cuenta filas del CSV y ficheros en `lote_entrada`.

→ Seis y seis.

## Reto

### 1 — Sin foto

Si falta la imagen, ¿se acepta la pieza?

<details>
<summary>Ver solución</summary>

No. Sin imagen no hay fila de aceptación. La pieza se queda fuera del registro y, en planta, iría a revisión por ausencia.

</details>

## Errores frecuentes

| Síntoma | Causa probable | Cómo arreglarlo |
|---------|----------------|-----------------|
| el registro no tiene una fila por imagen | el lote no se copió | repite `m04-03` |
| ninguna a revisión | el modelo no se cargó | lanza antes `m04-01` |
