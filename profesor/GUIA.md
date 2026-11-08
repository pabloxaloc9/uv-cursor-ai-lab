# Guía del profesor

## Resultado educativo

El alumnado dirige a la IA para transformar una idea en un prototipo comprobable. Debe distinguir propuesta de decisión, generación de código de funcionamiento y prototipo de producto preparado para usuarios reales. No se busca aprender un framework en una hora.

Formato acordado: 16 estudiantes, 4 equipos de 4, 60 minutos efectivos y exposiciones después. Dos equipos por reto ayuda a comparar soluciones, pero cada equipo puede escoger. No necesita conocer el código para justificar usuario, stack, diseño, datos y pruebas.

## Antes de clase

Enviar [PREPARACION.md](../PREPARACION.md) y pedir confirmación de equipo, copia del repo, capturas y prueba de Cursor Free. Recordar que la prueba no garantiza cuota para toda la sesión. No usar una cuenta Pro del profesor como evidencia de compatibilidad Free.

Comprobar proyector, red y permisos de instalación de los ordenadores. Es conveniente que tengan runtimes disponibles si desean compararlos; no instalar un framework por adelantado. No exigir crear cuentas en proveedores de nube.

Revisar [CURSOR-FREE.md](../docs/CURSOR-FREE.md), ensayar el recorrido completo y registrar qué se ha comprobado realmente en [VALIDACION.md](VALIDACION.md). La edición inicial incorpora comprobaciones locales; el ensayo real dentro de Cursor Free requiere una cuenta y ordenador representativos.

El repo del profesor debe ser público y plantilla. Cada equipo crea una copia independiente; no se necesitan permisos de escritura en el original ni gestionar 16 contribuyentes durante la sesión. El responsable puede invitar a sus compañeros a su copia si lo desea; durante la práctica basta un ordenador conductor y cuatro personas decidiendo. No compartir cuentas.

## Reparto de los 60 minutos

| Minutos | Fase | Intervención útil del profesor |
|---|---|---|
| 00–06 | Producto | «¿Qué problema concreto y de quién?»; evitar añadir funciones |
| 06–15 | Stack | «¿Qué renuncia aceptáis y por qué?»; exigir comparación y elección humana |
| 15–22 | Diseño | «¿Qué decisión tomáis de cada referencia?»; pedir estados además de colores |
| 22–28 | Arquitectura | «¿Dónde vive una reserva o un gasto y cómo vuelve después de recargar?» |
| 28–35 | I1 | Asegurar app arrancada; ayudar a quitar complejidad innecesaria |
| 35–46 | I2 | Pedir flujo principal, recarga y regla de negocio |
| 46–53 | I3 | Comprobar resto del MVP, errores y diseño |
| 53–60 | Auditoría | 3 min de pruebas, 1 de revisión y 3 de corrección/registro; congelar funciones nuevas |

El temporizador empieza con el entorno preparado. Las exposiciones son después: 2 minutos por equipo (8 minutos), más preguntas. Reservar aproximadamente 12 minutos adicionales si se quiere una pregunta breve por equipo.

## Por qué separar stack y arquitectura

| Rol | Pregunta | Resultado | Límite |
|---|---|---|---|
| Asesor de stack | ¿Con qué tecnologías y por qué? | Alternativas, costes, límites y elección | No crea estructura ni instala |
| Arquitecto | ¿Cómo organizamos lo elegido para cumplir el MVP? | Componentes, datos, persistencia y plan | No vuelve a elegir herramientas salvo incompatibilidad |

La separación hace visible que elegir un framework no resuelve el diseño de la aplicación. No implica dos procesos paralelos ni dos entrevistas repetidas: el cuaderno hace el traspaso. Para Free ambos pueden ser roles secuenciales del mismo chat.

## Participación de los cuatro miembros

Empezar con conducción de Cursor, criterio de producto/tecnología, pruebas y registro. Rotar tras producto, diseño y el primer incremento. No dejar que la persona con más experiencia opere y decida todo. Pedir a distintos miembros que expliquen una elección y una limitación. El cuaderno puede usar alias en un repo público.

## Intervenir sin decidir por ellos

- Si piden «¿cuál es el mejor stack?», devolver «¿mejor según qué dos criterios de vuestro caso?».
- Si quieren backend solo porque parece profesional, preguntar qué requisito local lo necesita y qué aporta para el futuro.
- Si eligen una solución solo de navegador, preguntar qué ocurriría con dos dispositivos; puede ser adecuada para el prototipo si reconocen el límite.
- Si el agente instala antes de elegir, detenerlo y volver a la decisión; no dar por aceptada una propuesta por haberla ejecutado.
- Si el diseño es genérico, pedir trazabilidad a las referencias y tres tokens concretos.
- Si dicen «funciona», pedir una acción completa y una entrada inválida; ver recarga y estado persistente.

## Plan de ayuda ante bloqueos

Al minuto 35 debe haber una app abierta. Si falla, priorizar diagnóstico, entorno y eliminación justificada de dependencias. No rebajar silenciosamente el requisito de persistencia o las reglas de negocio. Si falta tiempo, declarar alcance incompleto en lugar de marcarlo como completo.

Si se agota la cuota, no forzar un pago. Guardar el trabajo y comprobar disponibilidad en las cuentas propias de los otros miembros, sin compartir credenciales ni crear cuentas para evadir límites. Si no hay disponibilidad, terminar revisión manual y presentar el estado y diagnóstico. Valorar las decisiones y pruebas que sí existen conforme a la rúbrica.

No distribuir una aplicación ya resuelta en la rama inicial. Si el profesor quiere una demostración de reserva, prepararla en una copia independiente después de elegir su propio stack; distinguirla del trabajo del equipo.

## Exposición y evaluación

Usar [DEMO.md](../plantillas/DEMO.md) y [RUBRICA.md](RUBRICA.md). Preguntas posibles: ¿qué propuso la IA y rechazasteis?, ¿qué cambiaría para tres usuarios simultáneos?, ¿cómo comprobasteis que no se pierden céntimos o se duplican reservas?, ¿qué fallo detectasteis probando?

Cerrar el debate identificando una decisión de negocio pendiente de validación real y una tarea técnica necesaria antes de producción. No presentar el taller como una certificación de seguridad o cumplimiento normativo.

## Mantenimiento de futuras ediciones

Revisar fuentes y planes; actualizar fecha y matriz de compatibilidad. Ejecutar el verificador y sus tests antes de publicar. El workflow solo valida el material: los tests de cada aplicación se acuerdan según el stack del equipo. Las modificaciones pedagógicas relevantes se reflejan en README.md, taller.json, ejercicios y guía para mantener tiempos y requisitos coherentes.
