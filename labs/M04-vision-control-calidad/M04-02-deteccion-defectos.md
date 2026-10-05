# M04-02 — Detección automática de defectos

[← Página anterior](M04-01-clasificacion-componentes.md) · [Siguiente página →](M04-03-inspeccion-camara.md)

> Práctica del módulo. La teoría y la demostración están en el [README del módulo](README.md).
>
> Lanza los comandos desde la carpeta `infra/` del repositorio. Un paso que cuadra termina con una línea que empieza por `OK`.

### Objetivo

Localizas el rayón en la imagen y compruebas que una pieza buena no dispara la misma marca.

### Prerrequisitos

- Las imágenes de M04-01.
- CPU. No hay red neuronal de detección.

### En qué consiste

La clasificación dice «mala». Este paso dice «dónde»: la fila más brillante de la imagen. El manifiesto guarda la fila real del rayón para poder medir el error. En una pieza buena esa fila brillante no aparece.

### 1 — Medir la zona

**Acción:** `docker compose --profile lab run --rm --no-deps lab m04-02`

**Por qué:** Calidad necesita saber dónde mirar. Una clase sola no lo dice.

**Resultado esperado:** `OK m04-02:` zona correcta en 5 defectos y ninguna buena marcada como rayón.

## Comprueba tu entendimiento

**Tres casos**

Abre una defectuosa, señala la línea clara y compara con la fila que encontrarías barriendo la imagen de arriba a abajo.

→ La línea es la fila más clara. Si caes en el borde de la pieza, estás mirando el contorno, no el defecto.

## Reto

### 1 — Límite

Este detector busca una línea blanca. ¿Qué defecto no vería?

<details>
<summary>Ver solución</summary>

Uno oscuro, o uno que no cambia el brillo de una fila. Por eso un puesto real no se fía de un solo truco.

</details>

## Errores frecuentes

| Síntoma | Causa probable | Cómo arreglarlo |
|---------|----------------|-----------------|
| la zona no cae sobre el rayón | el manifiesto no es el de estas imágenes | regenera con `m04-01` |
| falsos en buenas | el umbral de brillo es demasiado bajo | el comando usa 230; no lo bajes para «pillar más» |
