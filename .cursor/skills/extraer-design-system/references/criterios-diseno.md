# Criterios para decidir y comprobar el diseño

Estas referencias son un instrumento de trabajo para la skill, no preguntas adicionales para alumnos. Valora juntos contenido, composición y acabado visual.

## Relacionar el producto con la referencia

| Necesidad | Decisión visual | Cómo comprobarla |
|---|---|---|
| Elegir un servicio | Destacar servicios, duración y acción, con jerarquía y aire suficientes. | Identifican qué reservar sin recorrer toda la pantalla. |
| Elegir una franja | Agrupar por día, separar estados disponible/ocupada/seleccionada. | Se distingue fecha y hora antes de confirmar. |
| Gestionar reservas | Agenda ordenada, acciones de cancelar visibles sin confundirlas con reservar. | Encuentran una reserva y entienden qué ocurre al cancelarla. |
| Registrar un gasto | Concepto, importe y pagador fáciles de localizar y completar. | Añaden el gasto y corrigen errores sin perder datos. |
| Entender las cuentas | Separar lo aportado del saldo final y las transferencias propuestas. | Pueden contar quién paga a quién sin depender de signos o colores. |

Si dos referencias se contradicen, toma de cada una lo que mejor resuelva una necesidad concreta. No conviertas la aplicación en una mezcla de componentes sin unidad.

## Qué significa un diseño cuidado

Una interfaz no se vuelve «premium» por añadir muchos gradientes, iconos y sombras. Tampoco basta con un formulario alineado y un fondo gris. Comprueba si existe:
- **Jerarquía intencional:** título, información principal, acción y contenido secundario claramente diferenciados.
- **Composición equilibrada:** agrupaciones legibles, alineaciones consistentes, espacio negativo y adaptación a distintas anchuras.
- **Detalle coherente:** radios, bordes, tipografía, elevación y colores que repiten una lógica.
- **Interacción comprensible:** estados al pasar, seleccionar, enfocar, guardar, vaciar o mostrar error; animaciones ligeras con opción de movimiento reducido.
- **Fidelidad a la referencia expresada:** una estética minimalista sofisticada exige más cuidado que simplemente evitar adornos. Explica las elecciones sin afirmar que has analizado una captura que no existe.

No impongas colores del profesor, una biblioteca determinada ni estilos ajenos a lo que el equipo pidió. Usa variables y componentes compartidos para que las decisiones se mantengan entre pantallas.

## Estados que conviene prever

| Elemento | Estados importantes |
|---|---|
| Acción principal | Normal, foco visible, pulsado y deshabilitado con motivo si corresponde. |
| Campo | Etiqueta siempre visible, entrada, validación, error y ayuda sin perder datos. |
| Franja BookFlow | Disponible, seleccionada, ocupada y liberada tras cancelación; no solo colores. |
| Reserva BookFlow | Confirmación con fecha y hora, localización posterior y cancelación. |
| Saldo Splitly | «Debe pagar», «debe recibir», «cuentas saldadas», nombre e importe. |
| Lista vacía | Qué falta y siguiente acción clara. |

Para revisar, utiliza **los datos y nombres del propio equipo**. Los importes de ejemplo en RETOS.md sirven para explicar el reparto, no son requisitos de reiniciar el grupo ni de introducir otras personas. En BookFlow tampoco sustituyas el negocio propio por el ejemplo del enunciado.

En una ventana estrecha comprueba que no se corten fechas, nombres, importes ni botones. Con Tab revisa foco y etiquetas. Si no puedes ver la página, no asegures haberla revisado visualmente.

## Registrar lo decidido

En «Diseño» de PROYECTO.md guarda de forma breve las referencias reales o descritas, dirección visual, paleta funcional, jerarquía de texto, espaciados, componentes claves y observaciones o ajustes. No inventes mediciones exactas de una captura. No presentes las propuestas del archivo como decisiones acordadas.
