# 5. Desarrollo incremental · minutos 28–53

**Objetivo:** construir el flujo obligatorio y comprobarlo a medida que crece.

Trabaja con Agent general. Adjunta la ficha, el cuaderno y los archivos relevantes. Los tres incrementos se ajustan al plan aceptado; no constituyen tres generaciones completas de la app.

| Incremento | Tiempo | Debe producir | Comprobación antes de continuar |
|---|---|---|---|
| I1 | 7 min | Proyecto arrancado, navegación y componentes básicos con el diseño acordado | Abrir en el navegador; comprobar vista inicial, foco y ausencia de errores que impidan usarla |
| I2 | 11 min | Flujo principal completo y persistencia real local | Crear reserva/gasto, recargar y comprobar que sigue; probar operación incompatible o cálculo |
| I3 | 7 min | Resto del MVP, estados y correcciones | Cancelación/gestión o liquidaciones, entrada inválida y comparación visual con el cuaderno |

## Prompt por incremento

> Implementa solo el incremento I[n] aceptado en el cuaderno. Lee primero los archivos existentes. Resume qué vas a cambiar y por qué, usa nuestro stack y design system y conserva el alcance del reto. Ejecuta el arranque y las comprobaciones disponibles; si no puedes usar el navegador, danos pasos exactos para probarlo nosotros. Distingue código generado de comportamiento comprobado. Actualiza ARRANQUE.md y la evidencia del incremento. Espera nuestro resultado antes del siguiente incremento.

## Actividad humana

1. Leer el resumen y los comandos; aceptar solo lo necesario dentro del proyecto.
2. Abrir el prototipo, realizar los pasos y observar el resultado. No basta con la explicación del agente.
3. Comunicar errores con resultado esperado, resultado real y mensaje de consola sin secretos. Usar [la plantilla de error](../plantillas/ERROR.md) si hace falta.
4. Registrar cada incremento en la sección 5 y el arranque en [ARRANQUE.md](../entregables/ARRANQUE.md). No subir carpetas de dependencias ni datos reales.

## Entregable y criterio de finalización

Código que arranca desde los pasos escritos, mantiene los datos al recargar y cubre los requisitos de la ficha. Si quedan fallos, registrarlos como tales; el reloj no convierte pendientes en funciones completas.

Al minuto 53, congelar funciones y pasar a auditoría. Si no ha arrancado al minuto 35, pedir ayuda al profesor y simplificar componentes o dependencias con una decisión registrada; conservar las reglas de negocio del MVP.

**Pregunta para pensar:** ¿qué hemos comprobado nosotros que no habría sido suficiente con preguntar «¿está todo bien?»?

[Siguiente: auditoría](06-auditoria.md)
