# M05 — Inteligencia artificial generativa en entornos industriales

[← Página anterior](../M04-vision-control-calidad/M04-03-inspeccion-camara.md) · [Siguiente página →](M05-01-modelo-local.md)

> [!NOTE]
> **Cómo funciona este módulo.** Primero la **teoría**, luego la **demostración guiada**, y después **practicas tú** en los laboratorios.

## Qué aprenderás

- Arrancar un modelo generativo en local y conocer qué pide la máquina.
- Llamarlo desde una aplicación.
- Consultar documentación técnica con recuperación.
- Dejar que un agente use una herramienta externa acotada.

## Teoría

Un modelo generativo completa texto (o imagen) a partir de un contexto. No consulta solo la planta: consulta lo que tú le pones delante. Si no le das el procedimiento, se lo inventa con fluidez.

### Piezas

| Pieza | Qué es aquí |
|-------|-------------|
| Modelo fundacional | Red grande ya entrenada, que tú no reentrenas en este curso |
| LLM | Modelo de lenguaje con el que escribes y lees instrucciones |
| Inferencia | Pasar una pregunta y obtener una respuesta, sin volver a entrenar |
| Recuperación | Buscar fragmentos de tus documentos y adjuntarlos a la pregunta |
| Agente | Un bucle que puede llamar una herramienta (por ejemplo, leer una señal) y seguir |

### Por qué en local

En una planta, el procedimiento y la telemetría no deben salir a un servicio externo por defecto. Ejecutar en el puesto enseña el coste: memoria, disco y tiempo de respuesta. Un modelo pequeño cabe en un portátil; uno grande, no.

### Límite

La respuesta puede sonar correcta y estar mal. En operación, el asistente propone y la persona contrasta con el procedimiento oficial. El agente solo llama herramientas que tú has definido, no «hace lo que quiera» en la red.

## Demostración guiada

Se arranca un modelo ya descargado en la máquina y se le hace una pregunta corta. Se observa cuánto tarda y cuánta memoria ocupa, que es el requisito de infraestructura.

Luego una aplicación mínima envía la pregunta por una API local y muestra la respuesta: el mismo modelo, llamado desde un programa.

El asistente recibe una carpeta con un procedimiento de la línea simulada y contesta citando el fragmento. Si la carpeta no tiene el dato, debe decir que no está.

El agente cierra el módulo llamando una sola herramienta: leer el último valor de la estación. No escribe en el automatismo.

## Ahora practica tú

| Lab | Título | Qué harás |
|-----|--------|-----------|
| M05-01 | [Ejecución local de modelos generativos](M05-01-modelo-local.md) | Poner en marcha un modelo en el puesto. |
| M05-02 | [Integración desde aplicaciones](M05-02-integracion-aplicacion.md) | Llamar al modelo desde un programa. |
| M05-03 | [Asistente técnico basado en documentación](M05-03-asistente-documentacion.md) | Responder citando procedimientos, no de memoria. |
| M05-04 | [Automatización mediante agentes](M05-04-agentes.md) | Dejar que un agente llame una herramienta acotada. |

→ Empieza por **[M05-01 — Ejecución local de modelos generativos](M05-01-modelo-local.md)**.
