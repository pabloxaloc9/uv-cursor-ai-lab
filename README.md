# Tu primera aplicación con ayuda de la IA

Este material es para la práctica del Máster de Creación de Empresas Innovadoras de la Universitat de València. En equipo, vais a convertir una idea en una aplicación que podáis abrir, probar y mejorar. No necesitáis haber programado antes.

La IA os ayudará a comparar opciones y escribir código. **Vuestro trabajo consiste en decidir, observar el resultado, detectar problemas y pedir cambios concretos.** No basta con responder «aceptamos» a todo.

## Antes de la clase

- Cread una cuenta en GitHub y otra en [Cursor](https://cursor.com). La modalidad gratuita es suficiente para empezar: no hace falta contratar un plan de pago.
- Instalad Cursor en el portátil que traeréis a clase. No hace falta instalar Git manualmente antes de clase; comprobaremos lo necesario al preparar el proyecto.
- Podéis explorar la interfaz, pero **no utilicéis el agente para programar antes de la práctica**: las cuentas gratuitas tienen límites de uso.
- Buscad dos capturas de webs o aplicaciones cuyo diseño os guste. Guardadlas para adjuntarlas en el ejercicio de diseño. Pensad qué os gusta de ellas. Si no tenéis capturas, podréis describir el estilo que buscáis.

El profesor indicará el repositorio definitivo de alumnos y os ayudará a abrir una copia en Cursor. No es necesario traer una aplicación empezada.

## Preparar Cursor y empezar

En el selector de modelos, **si vuestra cuenta ofrece Composer 2.5, seleccionadlo sin activar Fast**. Esta configuración puede ayudar a moderar el consumo; no garantiza una cantidad fija de peticiones. Si el modelo no aparece, preguntad al profesor. Evitad pruebas repetidas o conversaciones paralelas innecesarias durante el taller.

En modo **Agent**, iniciad una conversación con este mensaje:

> Lee README.md y RETOS.md. Somos un equipo de estudiantes sin experiencia programando. Queremos construir una de las dos aplicaciones. Haznos en un único mensaje las preguntas necesarias para elegir el reto y concretar nuestra idea; después ayúdanos a comparar tecnologías y a diseñar, construir y revisar una primera versión. Queremos tomar decisiones reales y probar el resultado, no limitarnos a decir «aceptamos». Explica con ejemplos las palabras técnicas. No escribas código hasta que hayamos elegido la tecnología.

Podéis pedir aclaraciones y cambiar de opinión cuando tengáis un motivo. Una persona manejará el ordenador y el resto decidirá y revisará con ella; procurad turnaros.

## El recorrido de la práctica

**1. Definir la idea.** Elegid [BookFlow o Splitly](RETOS.md) y responded en una sola tanda quién lo utilizaría, en qué situación, qué problema tiene hoy y qué necesita conseguir. Podéis personalizar nombres y contexto.

**2. Elegir la tecnología.** Contestad juntos una ronda de preguntas sobre vuestra experiencia, prioridades y necesidades futuras. Comparad alternativas, elegid la que entendéis mejor y explicad qué limitación aceptáis.

**3. Diseñar.** Adjuntad referencias y contad qué aspectos os gustan. Usad la skill `extraer-design-system` incluida en el proyecto para trasladar esas preferencias a decisiones concretas. Si no tenéis capturas, describidlo con suficiente detalle. Pedid una interfaz visualmente cuidada desde la primera versión y valoradla al verla, no solo leyendo códigos de color.

**4. Revisar el plan.** Pedid un resumen corto de pantallas, datos y funcionamiento. Corregid solo lo que afecte realmente al producto. No hace falta aprobar cada detalle ni revisar un documento largo.

**5. Construir y probar.** Pedid una **primera versión funcional completa** (no una pantalla decorativa sin lógica) y abridla. Probad vuestro caso con los nombres y datos que habéis elegido. Si falla, contad qué habéis hecho, qué esperabais y qué ocurrió. Podéis pedir mejoras de diseño si no se parece a vuestra referencia.

**6. Revisar y mejorar.** Comprobad las funciones de [vuestro reto](RETOS.md), que los datos siguen al recargar y que la aplicación rechaza alguna entrada incorrecta. Pedid al revisor que detecte los problemas más importantes y corregid al menos uno. Repetid la prueba afectada.

No hace falta que confirméis cada respuesta de Cursor. Intervenid cuando haya una decisión o un problema real. Si el agente se detiene con algo a medio construir, pedidle que termine el recorrido funcional acordado antes de añadir funciones nuevas.

## Resultado y exposición

Cursor dejará en `PROYECTO.md` una ficha breve con la idea, la tecnología elegida, el diseño, cómo abrir la aplicación y qué queda por resolver. No hay que rellenar documentación adicional.

Al terminar, entregaréis la copia del proyecto e indicaréis cómo probarlo. Cada equipo enseñará lo construido y explicará **una decisión propia, un cambio que pidió a la IA y un fallo o limitación que encontró**. No hace falta preparar diapositivas ni disimular lo que no funciona.

Trabajad con nombres y datos inventados. No compartáis contraseñas, claves ni archivos `.env`. El prototipo solo necesita funcionar localmente y recordar los datos al recargar; no hay que publicarlo ni usar pagos reales.
