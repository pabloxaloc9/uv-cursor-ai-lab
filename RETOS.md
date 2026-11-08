# ¿Qué aplicación vais a construir?

Podéis elegir entre estas dos ideas. En ambos casos, el primer paso será concretar quién usaría vuestra aplicación y para qué. También podéis darle otro nombre y elegir su aspecto.

## BookFlow: organizar las reservas de un negocio

Imaginad un pequeño negocio que recibe sus reservas por mensajes. Su responsable tiene que consultar la agenda cada vez que alguien pregunta por una hora. A veces se equivoca y acepta dos reservas para la misma franja.

Vuestra aplicación le ayudará a organizarse. Podéis pensar en una escuela de surf, un taller de cerámica, una empresa de visitas guiadas u otro negocio que os interese.

La primera versión debe permitir que una persona consulte los servicios y las horas disponibles, elija una franja y haga una reserva. Después debe poder consultar su reserva y cancelarla. El negocio tendrá una agenda sencilla con las reservas de cada fecha; basta con una lista ordenada por días.

Para esta práctica, cada franja admite una sola reserva por servicio. Si alguien la cancela, esa hora vuelve a estar disponible. No hace falta crear cuentas de usuario ni cobrar las reservas.

**Cómo comprobar que funciona:** haced una reserva e intentad reservar de nuevo la misma franja. La aplicación debe impedirlo. Recargad la página y comprobad que la primera reserva sigue guardada. Después, canceladla y comprobad que esa hora vuelve a estar libre. Intentad también enviar el formulario sin rellenarlo.

## Splitly: repartir los gastos de un grupo

Imaginad que varias personas hacen un viaje juntas. Una paga la cena, otra compra los billetes y otra se encarga del alojamiento. Al terminar, necesitan saber cuánto debe pagar o recibir cada una.

Vuestra aplicación les ayudará a repartir los gastos por igual. Podéis situar la idea en un viaje, un piso compartido o una actividad que organicen varias personas.

La primera versión debe permitir crear un grupo y añadir sus participantes. Después se podrán registrar los gastos, indicando qué se ha comprado, cuánto ha costado y quién ha pagado. La aplicación mostrará cuánto debe pagar o recibir cada persona y propondrá los pagos necesarios para saldar las cuentas. Solo mostrará las cantidades; no moverá dinero real.

Para esta práctica, trabajaréis con un solo grupo, en euros y con los participantes elegidos antes de añadir el primer gasto. Las cuentas deben conservar todos los céntimos. Por ejemplo, 10 € entre tres personas se pueden repartir como 3,34 €, 3,33 € y 3,33 €. Pedid a Cursor que os explique cómo lo resuelve.

**Cómo comprobar que funciona:** cread un grupo con Ana, Bruno y Carla. Añadid un gasto de 30 € pagado por Ana y otro de 15 € pagado por Bruno. La aplicación debe indicar que Carla tiene que pagar 15 € a Ana y que Bruno ya ha pagado su parte. Recargad la página y comprobad que los datos siguen ahí. Intentad también añadir un gasto negativo: la aplicación debe rechazarlo.

En cualquiera de los dos retos, terminad estas funciones antes de añadir otras. Utilizad datos inventados en todas las pruebas.
