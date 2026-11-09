# Criterios para decidir y comprobar el diseño

## Elegir lo que ayuda al usuario

Las referencias sirven para tomar decisiones concretas. Evita describirlas solo como «modernas», «limpias» o «profesionales».

| Necesidad | Decisión que conviene valorar | Cómo comprobarla después |
|---|---|---|
| Elegir un servicio o experiencia | Mostrar nombre, duración y acción de reserva en un orden constante. | La persona identifica qué puede reservar sin abrir varias pantallas. |
| Elegir una hora | Agrupar las franjas por fecha y distinguir la seleccionada de la ocupada. | Se reconoce la fecha y la hora antes de confirmar. |
| Gestionar reservas | Ordenar la agenda por día y dar más peso a la información que a la decoración. | Se encuentra una reserva y se entiende cómo cancelarla. |
| Registrar un gasto | Mantener visibles concepto, importe y persona que ha pagado. | Se puede completar el formulario y corregir un error sin perder lo escrito. |
| Entender las cuentas | Separar cuánto ha pagado cada persona de lo que debe pagar o recibir. | Se puede leer «Carla paga 15 € a Ana» sin interpretar colores o signos. |

Cuando las capturas apunten en direcciones distintas, resuelve el conflicto por su función. Por ejemplo, una página de experiencias puede inspirar la presentación de los servicios, mientras una agenda compacta puede servir para organizar las reservas. Explica esa relación; no traslades una portada promocional a todas las pantallas.

Evita acumular tarjetas, degradados, sombras o animaciones si no ayudan a distinguir información o acciones. Mantén las mismas decisiones en pantallas equivalentes. No impongas la paleta del profesor ni una biblioteca de componentes al equipo.

## Diseñar los estados que se van a utilizar

| Elemento | Estados y detalles que hay que prever |
|---|---|
| Acción principal | Texto que explique la acción, aspecto normal y foco visible. Si no está disponible, indicar el motivo cuando sea necesario. |
| Campo de formulario | Etiqueta siempre visible, ejemplo si ayuda, error junto al campo y explicación de cómo corregirlo. El ejemplo no sustituye a la etiqueta. |
| Franja de BookFlow | Disponible, seleccionada y ocupada. Añadir palabras o un indicador comprensible; no depender solo de verde y rojo. |
| Reserva de BookFlow | Confirmación con servicio, fecha y hora. Mostrar cuándo se ha cancelado y la hora vuelve a estar disponible. No conservar un mensaje de éxito si el guardado falla. |
| Saldo de Splitly | Mostrar «debe pagar», «debe recibir» o «cuentas saldadas», con nombre e importe. No explicar el saldo solo con un signo o un color. |
| Lista sin datos | Contar qué falta y ofrecer la siguiente acción útil: reservar, crear el grupo o añadir el primer gasto, según corresponda. |

En la revisión de BookFlow, recorre la reserva, el intento de ocupar la misma franja y la cancelación. Comprueba que los cambios de disponibilidad también se entienden visualmente. En Splitly, utiliza el ejemplo de RETOS.md y comprueba que los importes y las personas coinciden entre el formulario, la lista de gastos y los pagos propuestos.

En una ventana estrecha, comprueba que no se corten nombres, fechas, importes o botones. Recorre los controles con Tab y comprueba que se pueda reconocer y activar el elemento seleccionado. Revisa que se lean las etiquetas, los textos secundarios y los mensajes de error. Estas comprobaciones requieren ver la interfaz; no basta con leer los estilos del código.

## Recoger el acuerdo en PROYECTO.md

Actualiza la sección «Diseño» existente después de la aceptación. Conserva el resto del documento. Limita el contenido a lo necesario para reproducir el diseño:

- Referencias y motivo de cada elección. Indica si viste las capturas o trabajaste con descripciones; no subas las imágenes por defecto.
- Una tabla con los nombres y valores de los colores, la tipografía y la escala de espacios. Incluye anchura de contenido, bordes y esquinas. Los nombres deben permitir reutilizar esos valores en el código.
- Dos o tres reglas de los componentes que incluyan los estados relevantes del reto.
- Pantallas revisadas, problemas encontrados y cuestiones pendientes, si las hay. Indica si la revisión la ha realizado el agente o la ha comunicado el equipo.

No presentes ninguna plantilla o ejemplo de esta referencia como una decisión del equipo. Evita repetir toda la conversación o crear documentos separados para cada componente.
