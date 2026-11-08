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
| Reserva de BookFlow | Confirmación con servicio, fecha y hora. Pedir confirmación al cancelar y mostrar cuándo la hora vuelve a estar disponible. No conservar un mensaje de éxito si el guardado falla. |
| Saldo de Splitly | Mostrar «debe pagar», «debe recibir» o «cuentas saldadas», con nombre e importe. No explicar el saldo solo con un signo o un color. |
| Lista sin datos | Contar qué falta y ofrecer la siguiente acción útil: reservar, crear el grupo o añadir el primer gasto, según corresponda. |

En la revisión de BookFlow, recorre la reserva, el intento de ocupar la misma franja y la cancelación. Comprueba que los cambios de disponibilidad también se entienden visualmente. En Splitly, utiliza el ejemplo de RETOS.md y comprueba que los importes y las personas coinciden entre el formulario, la lista de gastos y los pagos propuestos.

En una ventana estrecha, comprueba que no se corten nombres, fechas, importes o botones. Recorre los controles con Tab y comprueba que se pueda reconocer y activar el elemento seleccionado. No atribuyas estas comprobaciones al script de contraste: requieren revisar la interfaz.

## Medir el contraste

La herramienta calcula la luminancia relativa sRGB y el contraste según [WCAG 2.2](https://www.w3.org/TR/WCAG22/#dfn-relative-luminance). Usa como objetivo al menos **4,5:1 para todo el texto** de este prototipo, incluidas las etiquetas de botones. La norma admite algunas excepciones, pero este objetivo evita tener que resolverlas durante el taller. Consulta [contraste del texto](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html).

Para los indicadores y límites que sean necesarios para identificar controles o estados, utiliza **3:1 frente a los colores adyacentes**. No es un requisito para cualquier borde decorativo ni demuestra por sí solo que el foco sea accesible. Consulta [contraste de elementos no textuales](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html).

Ejecuta el comando desde la raíz del repositorio con `python3` o con el nombre de Python 3 disponible en el equipo. Pasa los valores reales de la propuesta por la entrada estándar, sin crear otro entregable. Ejemplo de formato, no de paleta recomendada:

```sh
python3 .cursor/skills/extraer-design-system/scripts/contraste.py <<'JSON'
{
  "colores": {"texto": "#202020", "fondo": "#ffffff", "borde": "#767676"},
  "pares": [
    {"nombre": "Texto sobre fondo", "frente": "texto", "fondo": "fondo", "minimo": 4.5},
    {"nombre": "Límite del campo", "frente": "borde", "fondo": "fondo", "minimo": 3}
  ]
}
JSON
```

El ejemplo de comando usa una terminal compatible con este formato. En PowerShell, envía el mismo JSON a Python con una cadena multilínea y una tubería. No cambies la configuración global del equipo ni instales una terminal para ejecutar el ejemplo.

Cada par referencia dos nombres definidos en `colores`. `minimo` debe ser un número entre 1 y 21. Se aceptan colores opacos `#RGB` y `#RRGGBB`; se rechazan transparencias, degradados y fondos con imágenes porque necesitan conocer el fondo final. Si aparecen en la interfaz, comprueba el color resultante con otra herramienta apropiada o deja esa medición pendiente.

La salida JSON incluye la razón de contraste y si alcanza el umbral. El código de salida es **0** si todos los pares lo alcanzan, **1** si alguno falla y **2** si la entrada es inválida. El valor mostrado se redondea a cuatro decimales, pero la decisión utiliza el cálculo sin redondear: un resultado inferior a 4,5 no se aprueba como 4,5. Si cambias un fondo, revisa todos los textos e indicadores que se dibujen sobre él.

La herramienta solo mide las combinaciones que recibe. No inspecciona la aplicación, no comprueba el tamaño del texto y no certifica accesibilidad. En el resultado distingue «combinación propuesta medida» de «combinación comprobada en la pantalla».

## Recoger el acuerdo en PROYECTO.md

Actualiza la sección «Diseño» existente después de la aceptación. Conserva el resto del documento. Limita el contenido a lo necesario para reproducir el diseño:

- Referencias y motivo de cada elección. Indica si viste las capturas o trabajaste con descripciones; no subas las imágenes por defecto.
- Una tabla con los nombres y valores de los colores, la tipografía y la escala de espacios. Incluye anchura de contenido, bordes y esquinas. Los nombres deben permitir reutilizar esos valores en el código.
- Dos o tres reglas de los componentes que incluyan los estados relevantes del reto.
- Combinaciones medidas y resultado; pantallas revisadas y cuestiones pendientes, si las hay.

No presentes ninguna plantilla o ejemplo de esta referencia como una decisión del equipo. Evita repetir toda la conversación o crear documentos separados para cada componente.
