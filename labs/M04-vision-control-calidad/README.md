# M04 — Visión artificial para control de calidad

[← Página anterior](../M03-ml-prediccion-anomalias/M03-03-comparacion-modelos.md) · [Siguiente página →](M04-01-clasificacion-componentes.md)

> [!NOTE]
> **Cómo funciona este módulo.** Primero la **teoría**, luego la **demostración guiada**, y después **practicas tú** en los laboratorios.

## Qué aprenderás

- Entrenar un clasificador visual de pieza correcta y defectuosa.
- Ver qué pasa cuando el defecto es pequeño o el dataset está sesgado.
- Cerrar un ciclo de inspección: imagen, dictamen, registro.

## Teoría

La cámara no «ve calidad». Ve una imagen. El modelo propone una clase o señala una zona. Alguien, o un automatismo, convierte eso en aceptar, revisar o rechazar.

### Dos tareas

| Tarea | Salida | Cuándo |
|-------|--------|--------|
| Clasificación de la imagen | Pieza correcta o defectuosa | El defecto cambia el aspecto general y basta un sí o un no |
| Detección del defecto | Zona de la imagen donde está el problema | Hace falta decir dónde está, no solo que la pieza está mal |

Las dos fallan si el dataset miente: pocas piezas malas, luz distinta a la de línea, o fotos de laboratorio que no se parecen al puesto.

### Qué limita la precisión

- Pocas imágenes del defecto que de verdad importa.
- Fondo, reflejo o posición que el modelo usa como atajo.
- Un umbral de aceptación demasiado alegre: deja pasar defectos.
- Un umbral demasiado duro: manda a revisión casi todo.

El laboratorio mide ese compromiso. No busca un porcentaje redondo.

## Demostración guiada

Se muestra un conjunto pequeño de imágenes de componente, etiquetadas como correctas o defectuosas, y un modelo que clasifica imágenes nuevas del mismo puesto.

Después se enseña un caso en el que el defecto ocupa poco en la imagen: la clasificación global duda y una detección por zona acota mejor el problema.

El cierre es una carpeta de entrada que el sistema vacía produciendo un dictamen por imagen, guardado al lado, como haría un puesto de inspección.

## Ahora practica tú

| Lab | Título | Qué harás |
|-----|--------|-----------|
| M04-01 | [Clasificación automática de componentes](M04-01-clasificacion-componentes.md) | Separar imágenes de pieza correcta y defectuosa. |
| M04-02 | [Detección automática de defectos](M04-02-deteccion-defectos.md) | Localizar el defecto, no solo clasificar la pieza. |
| M04-03 | [Sistema de inspección basado en cámara](M04-03-inspeccion-camara.md) | Analizar imágenes y dejar un dictamen automático. |

→ Empieza por **[M04-01 — Clasificación automática de componentes](M04-01-clasificacion-componentes.md)**.
