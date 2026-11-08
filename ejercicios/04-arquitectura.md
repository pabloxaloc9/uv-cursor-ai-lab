# 4. Arquitectura · minutos 22–28

**Objetivo:** convertir el stack y el diseño decididos en una organización construible y comprobable.

Entrada: secciones 1–3 del cuaderno acordadas. Adjuntar [arquitecto.md](../.cursor/agents/arquitecto.md), la ficha y el cuaderno.

## Actividad

1. Revisar pantallas, componentes y estructura mínima de archivos propuesta por el arquitecto.
2. Revisar entidades, campos y relaciones. Preguntar qué impide datos incoherentes.
3. Decidir dónde se guardarán los datos y cómo se cargan al iniciar. Comprobar que recargar no los elimina. Explicar si se comparten entre pestañas, dispositivos o usuarios.
4. Acordar tres incrementos, cada uno con una prueba observable. Registrar secciones 4 y 5; aceptar el plan antes de generar código.

## Prompt inicial

> Actúa como el arquitecto adjunto. Usa el producto, stack y diseño ya elegidos; no reabras la elección de tecnologías salvo incompatibilidad concreta. Tenemos 6 minutos. Propón estructura mínima, pantallas/componentes, modelo de datos, persistencia y validaciones. Organiza 25 minutos de desarrollo en tres incrementos con requisitos y pruebas. Explica todo con ejemplos de nuestra app. Espera que aceptemos el plan antes de escribir código.

## Entregable y criterio de finalización

Sección 4: estructura, entidades y relaciones, persistencia, validaciones y límites. Sección 5: plan de tres incrementos aceptado. El equipo puede explicar dónde vive una reserva o un gasto y qué cambia al crearlo, recargar y cancelarlo o liquidarlo.

**Pregunta para pensar:** ¿qué regla debe seguir siendo cierta aunque el usuario envíe un formulario incorrecto?

No se pide microservicios, una arquitectura empresarial ni diagramas extensos. Un dibujo breve o una tabla son suficientes si ayudan a comprender la solución.

[Siguiente: desarrollo](05-desarrollo.md)
