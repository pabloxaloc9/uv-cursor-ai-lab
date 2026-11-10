# ¿Qué aplicación vais a construir?

Elegid una de las dos ideas y adaptadla a un caso concreto que os interese. Los nombres y situaciones son ejemplos, **no datos obligatorios que debáis introducir ni pruebas que os obliguen a borrar vuestro trabajo**. Vuestro equipo decide el nombre, las personas y el aspecto.

## BookFlow: reservas para un negocio

Un pequeño negocio recibe reservas por mensajes y a veces acepta dos para la misma hora. Podéis plantearlo para una escuela de surf, un taller de cerámica, visitas guiadas u otro servicio.

**La primera versión debe permitir:** consultar servicios y horarios disponibles, elegir una franja y reservarla; localizar y cancelar una reserva; y mostrar al negocio una agenda sencilla ordenada por días. Para un mismo servicio y una misma franja, solo cabe una reserva. Al cancelar, esa hora vuelve a quedar disponible. No hacen falta cuentas ni cobros.

**Cómo probar vuestro propio caso:** inventad una reserva con vuestro servicio, día y hora. Intentad reservar otra vez exactamente esa franja para el mismo servicio: debe impedirlo. Recargad y comprobad que se conserva la primera reserva. Canceladla y verificad que la franja vuelve a estar disponible. Probad también a enviar un formulario incompleto. **No es necesario cambiar los nombres ni reiniciar los datos para hacer estas pruebas.**

## Splitly: gastos compartidos

Varias personas hacen un viaje, comparten piso u organizan una actividad. Una paga la cena, otra el transporte y otra el alojamiento; quieren saber cuánto debe pagar o recibir cada una.

**La primera versión debe permitir:** crear un grupo con participantes, añadir gastos con concepto, importe y persona que ha pagado; calcular los saldos y mostrar pagos propuestos para saldar las cuentas. No se transfiere dinero real. Trabajad con un grupo, en euros, y definid las personas antes del primer gasto.

**Un detalle que importa:** las cuentas deben cuadrar hasta el último céntimo. Por ejemplo, 10 € entre tres personas se reparten como 3,34 €, 3,33 € y 3,33 €, no como tres importes de 3,33 €. Pedid a Cursor que os explique cómo trata ese céntimo.

**Cómo probar vuestro propio caso:** registrad varios gastos con los integrantes que habéis elegido. Calculad entre todos cuánto ha pagado cada uno y cuánto le correspondía; las cantidades a pagar y a recibir deben compensarse. Recargad y comprobad que los gastos siguen ahí. Intentad añadir un gasto negativo o vacío: debe rechazarlo.

**Ejemplo opcional para comprobar cálculos, sin sustituir vuestro grupo:** Ana paga 30 € y Bruno 15 € en un grupo de tres personas con Carla. Cada uno debe asumir 15 €; por tanto, Carla paga 15 € a Ana y Bruno queda saldado. Este ejemplo se puede razonar en papel o utilizar en una prueba aislada; **no borréis los datos de vuestra aplicación para reproducirlo**.

## Para los dos retos

Prioridad: terminar el recorrido principal y probarlo antes de añadir extras. Si queréis sincronizar varios móviles, publicar la aplicación, crear cuentas o integrar pagos, anotadlo como una mejora futura y preguntad qué implicaría: no es obligatorio para el prototipo local.

Usad datos inventados. Ningún resultado está «probado» solo porque Cursor lo afirme: comprobadlo vosotros en la aplicación.
