# M03-03 — Comparación de modelos predictivos

[← Página anterior](M03-02-anomalias.md) · [Siguiente página →](../M04-vision-control-calidad/README.md)

> Práctica del módulo. La teoría y la demostración están en el [README del módulo](README.md).
>
> Lanza los comandos desde la carpeta `infra/` del repositorio. Un paso que cuadra termina con una línea que empieza por `OK`.

### Objetivo

Comparas regresión logística y un árbol poco profundo sobre el mismo corte, y te quedas con uno por una regla explícita.

### Prerrequisitos

- El `limpio.csv` de M02-03.
- Deja `modelo_defecto.joblib` y `VERSION`. Ese fichero es el que sirven M06 y M07.

### En qué consiste

Los dos ven el mismo 70/30. Gana el de mayor recall de defecto; si empatan, el de menos falsas alarmas. La versión queda escrita como `defecto-0.1`.

### 1 — Misma vara

**Acción:** `docker compose --profile lab run --rm --no-deps lab m03-03`

**Por qué:** Sin el mismo corte, la comparación no vale.

**Resultado esperado:** `OK m03-03:` con el nombre elegido, su recall y su tasa de falsas alarmas. Existen `modelo_defecto.joblib`, `modelo_elegido.txt` y `VERSION`.

## Comprueba tu entendimiento

**La regla**

Lee `infra/data/modelo_elegido.txt`.

→ Pone `logreg` o `arbol`, el que imprimió el OK.

## Reto

### 1 — Empate

Si los dos recall fueran iguales, ¿con cuál te quedas?

<details>
<summary>Ver solución</summary>

Con el de menor tasa de falsas alarmas. Es la segunda clave de la comparación.

</details>

## Errores frecuentes

| Síntoma | Causa probable | Cómo arreglarlo |
|---------|----------------|-----------------|
| los dos modelos no salen | no está el CSV | lanza `m02-03` |
| VERSION vacío | el comando no terminó en OK | repite `m03-03` |
