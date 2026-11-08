# BookFlow · reservas de servicios o experiencias

## Punto de partida

Un pequeño negocio gestiona reservas por mensajes y hojas sueltas. Los clientes no saben qué horas están libres y el responsable necesita ver las reservas de un vistazo. Elegid un caso concreto: talleres de cerámica, clases de surf, visitas guiadas u otro servicio o experiencia.

Decidid nombre comercial, usuario principal, tono y catálogo. No hace falta usar el nombre BookFlow como marca final.

## MVP obligatorio

| ID | Requisito | Criterio de aceptación |
|---|---|---|
| BF-01 | Catálogo | Mostrar al menos tres servicios/experiencias con nombre, descripción breve y duración; cada uno puede tener franjas propias |
| BF-02 | Disponibilidad | Mostrar franjas concretas por servicio y fecha y distinguir libres de ocupadas; las ocupadas no se pueden reservar |
| BF-03 | Crear una reserva | Elegir servicio, franja y alias ficticio del cliente; confirmar con resumen; una segunda reserva activa del mismo servicio y franja se rechaza sin duplicar datos |
| BF-04 | Cancelar una reserva | Cancelar desde el listado; la reserva deja de estar activa y la franja vuelve a estar disponible; repetir la cancelación no daña el estado |
| BF-05 | Gestión y calendario básico | Vista o sección de gestión con reservas agrupadas por fecha, servicio, cliente y estado; seleccionar una fecha y ver sus reservas. Una agenda/lista por fechas vale como calendario básico |
| BF-06 | Persistencia y validación | Reservas y cancelaciones sobreviven a la recarga; campos vacíos o franja inválida muestran un mensaje comprensible; texto introducido no se ejecuta como HTML o código |

Modelo simplificado obligatorio: **una plaza por franja y servicio**. Servicios distintos pueden tener franjas a la misma hora porque no se modela un recurso compartido. No se exige resolver solapamientos de personal o instalaciones. La duración se muestra; las franjas publicadas ya son válidas. La ficha no promete concurrencia entre pestañas o dispositivos.

## Datos ficticios para probar

Podéis crear tres servicios propios. Para la demo usad una fecha futura y al menos dos franjas de un servicio. El cliente es un alias como «Cliente A», no un email o un nombre real. La gestión de fechas será local al navegador; no se exigen husos horarios múltiples.

## Pruebas de aceptación

| Caso | Pasos | Resultado esperado |
|---|---|---|
| B1 | Abrir catálogo y seleccionar un servicio | Se ven sus franjas y los datos del servicio |
| B2 | Reservar una franja con «Cliente A» | Confirmación y una reserva activa; franja ocupada |
| B3 | Intentar reservar la misma franja otra vez en el mismo contexto de uso | Rechazo claro, sigue existiendo una sola reserva activa |
| B4 | Recargar la página | La reserva sigue en la gestión y la franja sigue ocupada |
| B5 | Cancelar, intentar cancelar de nuevo y recargar | Estado coherente sin duplicados; franja libre; cancelación conservada |
| B6 | Filtrar la gestión por fecha | Solo aparecen reservas de esa fecha y sus estados |
| B7 | Enviar alias vacío o franja inexistente | Mensaje útil; no se crea una reserva inválida |
| B8 | Introducir texto como `<b>Cliente</b>` en el alias | Se muestra como texto literal o se rechaza; no se interpreta como HTML |

Comprobad también navegación con Tab, foco visible, formulario etiquetado y uso en una ventana estrecha. Si no podéis realizar una prueba, registrad NO PROBADO.

## Fuera de alcance

Autenticación real, protección de la vista de gestión, pagos, emails, WhatsApp, integraciones de calendario, nube y usuarios simultáneos. El responsable y el cliente se simulan en el mismo ordenador. No usar este prototipo para reservas reales.

Opcionales solo al terminar: búsqueda en catálogo, filtro por servicio o un pequeño resumen de ocupación. No se puntúa añadir funciones si falta el MVP.

[Empezar producto](../ejercicios/01-producto.md)
