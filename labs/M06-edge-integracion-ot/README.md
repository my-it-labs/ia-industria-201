# M06 — Edge AI e integración industrial

[← Página anterior](../M05-ia-generativa/M05-04-agentes.md) · [Siguiente página →](M06-01-inferencia-edge.md)

> [!NOTE]
> **Cómo funciona este módulo.** Primero la **teoría**, luego la **demostración guiada**, y después **practicas tú** en los laboratorios.

## Qué aprenderás

- Ejecutar una inferencia en el puesto, junto al proceso simulado.
- Medir que la respuesta no depende de un servicio externo.
- Devolver un evento al automatismo simulado sin tocar la lógica de seguridad.

## Teoría

Edge, aquí, quiere decir: el modelo responde en una máquina cercana a la línea, no en un centro de datos. En la clase esa máquina es el portátil. La latencia que importa es la que ve el ciclo, no la de una demo en otra red.

### Híbrido

Entrenar y vigilar puede vivir en otro sitio. Inferir, si el ciclo no espera, vive al lado. Si se corta la red de oficina, el borde sigue dictaminando con el último modelo que recibió.

### IA y OT

El modelo emite un evento: pieza a revisar, anomalía, confianza baja. El automatismo decide si ese evento cambia una ruta, enciende un aviso o no hace nada. No se escribe un modelo dentro del enclavamiento de seguridad.

Eso se prueba con el simulador: hay una cola de eventos que el «PLC» lee. No hay una escritura directa al registro que pararía la línea.

## Demostración guiada

Se carga el modelo ya entrenado (el de defecto o el de visión) y se lanza una inferencia en local sobre una pieza nueva. Se mide el tiempo entre el dato de entrada y el dictamen.

Después ese dictamen se publica como evento. Un consumidor que hace de automatismo lo recibe y muestra la decisión de proceso: seguir o mandar a revisión. Cortar la red no cambia el dictamen, porque no había nube.

## Ahora practica tú

| Lab | Título | Qué harás |
|-----|--------|-----------|
| M06-01 | [Inferencia en entornos edge](M06-01-inferencia-edge.md) | Dictaminar en el puesto, sin nube. |
| M06-02 | [Integración con sistemas industriales](M06-02-integracion-ot.md) | Entregar el dictamen como evento al automatismo simulado. |

→ Empieza por **[M06-01 — Inferencia en entornos edge](M06-01-inferencia-edge.md)**.
