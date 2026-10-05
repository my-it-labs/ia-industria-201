# M07 — Operación, MLOps y observabilidad

[← Página anterior](../M06-edge-integracion-ot/M06-02-integracion-ot.md) · [Siguiente página →](M07-01-servicio-inferencia.md)

> [!NOTE]
> **Cómo funciona este módulo.** Primero la **teoría**, luego la **demostración guiada**, y después **practicas tú** en los laboratorios.

## Qué aprenderás

- Exponer el modelo como un servicio que otra aplicación puede llamar.
- Guardar una versión identificable del modelo.
- Detectar que el servicio empeora cuando los datos ya no se parecen a los del entrenamiento.

## Teoría

Entrenar en un cuaderno no es operar. Operar es que otra pieza del sistema pueda pedir un dictamen, que se sepa qué versión contestó y que alguien note si esa versión deja de servir.

### Qué vigilar

| Señal | Pregunta |
|-------|----------|
| El servicio responde | ¿Hay errores y tiempos raros? |
| La entrada cambia | ¿Las señales de hoy se parecen a las del entrenamiento? |
| La salida cambia | ¿De repente casi todo es defecto, o casi nada lo es? |
| La versión | ¿Qué fichero de modelo contestó esta pieza? |

Reentrenar es la respuesta cuando el proceso ha cambiado (utillaje, material, receta), no un reflejo semanal. Primero se ve la degradación; después se decide.

Contenerizar —empaquetar servicio y dependencias para llevarlo a otra máquina— es parte de este relato. En el laboratorio el servicio es un proceso del puesto, con versión y contrato claros, que es lo que la operación necesita aunque el paquete final sea otro.

## Demostración guiada

Se publica el modelo de defecto como un servicio local. Una llamada con las señales de una pieza devuelve dictamen y nombre de versión.

Luego se alimenta el servicio con un tramo de datos desplazado (la estación «se ha ido» respecto al entrenamiento) y se ve el cambio en la tasa de avisos y en el perfil de entrada. Eso es la degradación, antes de hablar de reentrenar.

## Ahora practica tú

| Lab | Título | Qué harás |
|-----|--------|-----------|
| M07-01 | [Publicación de servicios de inferencia](M07-01-servicio-inferencia.md) | Dejar el modelo llamable por otras aplicaciones. |
| M07-02 | [Monitorización y seguimiento operacional](M07-02-monitorizacion.md) | Ver rendimiento y degradación del modelo desplegado. |

→ Empieza por **[M07-01 — Publicación de servicios de inferencia](M07-01-servicio-inferencia.md)**.
