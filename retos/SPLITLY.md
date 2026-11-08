# Splitly · gastos compartidos

## Punto de partida

Un grupo organiza un viaje o comparte gastos de una actividad. Unas personas pagan más que otras y nadie tiene claro quién debe a quién. Elegid un contexto: escapada de amigos, piso compartido, evento o actividad de un grupo.

Decidid nombre comercial, usuario principal, tono y ejemplos. No hace falta usar el nombre Splitly como marca final.

## MVP obligatorio

| ID | Requisito | Criterio de aceptación |
|---|---|---|
| SP-01 | Grupo y participantes | Crear un grupo con nombre y al menos dos participantes distintos; rechazar nombres vacíos y duplicados ignorando espacios exteriores y mayúsculas |
| SP-02 | Gastos | Registrar concepto, importe positivo en euros con hasta dos decimales y quién pagó; mostrar el listado y el total; pagador pertenece al grupo |
| SP-03 | Reparto igualitario | Repartir cada gasto entre todos los participantes del grupo, incluido el pagador, sin perder ni crear céntimos |
| SP-04 | Balances | Mostrar por participante lo pagado, su parte y el balance = pagado − parte; positivo: debe recibir; negativo: debe pagar; la suma exacta de balances es 0 céntimos |
| SP-05 | Liquidaciones propuestas | Mostrar quién debería pagar a quién y cuánto para dejar todos los balances a cero si se realizaran esos pagos; no exige minimizar el número de transferencias ni registrar pagos reales |
| SP-06 | Persistencia y validación | Grupo, participantes y gastos sobreviven a recargar; importes/nombres/pagadores inválidos producen mensajes útiles; texto introducido no se ejecuta como HTML o código |

**Simplificación:** un solo grupo, una moneda (EUR) y reparto entre todos. Fijar los participantes al registrar el primer gasto; si se quiere cambiarlos, ofrecer reinicio explícito con confirmación que borre solo los datos ficticios de esta app. Esto evita recalcular silenciosamente gastos anteriores. No se exige editar ni borrar gastos individuales.

## Regla exacta de céntimos

Calcular en enteros (céntimos), no con redondeos independientes de números decimales. Para un gasto de `c` céntimos y `n` participantes: parte base = división entera de `c / n`; repartir los céntimos restantes, uno a uno, a los primeros participantes según el orden de alta. Mantener ese orden estable. Mostrar el criterio en la app o en su ayuda.

Aceptar formato decimal con coma o punto; rechazar más de dos decimales, importes vacíos, no numéricos, cero y negativos. Para mantener acotados los cálculos del prototipo, máximo 10 participantes y máximo 1.000.000,00 € por gasto; validar el límite y el total de céntimos según las garantías numéricas del lenguaje elegido.

## Datos y resultados de referencia

Orden de participantes: **Ana, Bruno, Carla** (personajes ficticios).

| Caso | Gastos | Pagado A / B / C | Parte A / B / C | Balance A / B / C |
|---|---|---|---|---|
| S1 | Ana paga 30,00 € | 30,00 / 0 / 0 | 10,00 / 10,00 / 10,00 | +20,00 / −10,00 / −10,00 |
| S2 | Además, Bruno paga 15,00 € | 30,00 / 15,00 / 0 | 15,00 / 15,00 / 15,00 | +15,00 / 0 / −15,00 |
| S3, grupo reiniciado | Ana paga 10,00 € | 10,00 / 0 / 0 | 3,34 / 3,33 / 3,33 | +6,66 / −3,33 / −3,33 |

Liquidaciones válidas: S1, Bruno → Ana 10,00 y Carla → Ana 10,00; S2, Carla → Ana 15,00; S3, Bruno → Ana 3,33 y Carla → Ana 3,33. Aplicadas al balance, todas dejan cero. No ejecutan transferencias ni alteran los gastos.

## Pruebas de aceptación

| Caso | Acción | Resultado esperado |
|---|---|---|
| S1 / S2 / S3 | Introducir los datos anteriores, cada caso desde el estado indicado | Balances exactos y liquidaciones equivalentes |
| S4 | Recargar después de S2 | Mismo grupo, gastos, total y balances |
| S5 | Probar `0`, `-1`, `abc`, vacío, `1,001`, `1000000.01` y pagador inexistente | Rechazo comprensible sin crear gastos; el último importe supera el límite de 1.000.000,00 € |
| S6 | Crear «Ana» y luego « ana » | Rechazo del duplicado; no crear una segunda participante |
| S7 | Intentar cambiar participantes después del primer gasto | Bloqueo explicado o reinicio explícito con confirmación; nunca recalcular en silencio |
| S8 | Introducir `<b>Viaje</b>` como nombre o concepto | Texto literal o rechazo; no se interpreta HTML |
| S9 | Grupo sin gastos | Total y balances cero; estado vacío comprensible y ninguna liquidación |

Comprobad coma y punto en importes, navegación con Tab, foco, etiquetas y una ventana estrecha. Si no podéis hacer una prueba, registrad NO PROBADO.

## Fuera de alcance

Login, pagos reales, bancos, conexión con Bizum, varias monedas, reparto desigual, tickets con OCR, varios grupos, usuarios simultáneos y nube. Las liquidaciones son sugerencias, no movimientos de dinero.

Opcionales solo al terminar: filtros o categorías. No se puntúa añadir funciones si falta el MVP.

[Empezar producto](../ejercicios/01-producto.md)
