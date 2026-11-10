# Tu primera aplicación con ayuda de la IA

Este material es para la práctica del Máster de Creación de Empresas Innovadoras de la Universitat de València. En equipo, vais a convertir una idea en una aplicación que podáis abrir, probar y mejorar. No necesitáis haber programado antes.

La IA os ayudará a comparar opciones y escribir código. **Vuestro trabajo consiste en decidir, observar el resultado, detectar problemas y pedir cambios concretos.** No basta con responder «aceptamos» a todo.

## Antes de la clase

- Cread una cuenta en GitHub y otra en [Cursor](https://cursor.com). La modalidad gratuita es suficiente para empezar: no hace falta contratar un plan de pago.
- Instalad Cursor en el portátil que traeréis a clase. No hace falta instalar Git manualmente antes de clase; comprobaremos lo necesario al preparar el proyecto.
- Podéis explorar la interfaz, pero **no utilicéis el agente para programar antes de la práctica**: las cuentas gratuitas tienen límites de uso.
- Buscad dos capturas de webs o aplicaciones cuyo diseño os guste. Guardadlas para adjuntarlas en el ejercicio de diseño. Pensad qué os gusta de ellas. Si no tenéis capturas, podréis describir el estilo que buscáis.

El profesor os indicará el repositorio de alumnos. Para empezar sin bloqueos podéis abrir **Code → Download ZIP**, descomprimir el proyecto y abrir esa carpeta en **Cursor → File → Open Folder**. Es importante abrir la carpeta completa, que contiene `.cursor/` con las reglas, agentes y skills. Si ya tenéis Git preparado, también podéis clonar el repositorio. **Para trabajar con la carpeta ZIP no hace falta instalar Git.** No es necesario traer una aplicación empezada.

## Preparar Cursor y empezar

En el selector de modelos, **si vuestra cuenta ofrece Composer 2.5, seleccionadlo sin activar Fast**. Esta configuración puede ayudar a moderar el consumo; no garantiza una cantidad fija de peticiones. Si el modelo no aparece, preguntad al profesor. Evitad pruebas repetidas o conversaciones paralelas innecesarias durante el taller.

En modo **Agent**, iniciad una conversación con este mensaje:

> Lee README.md y RETOS.md. Somos un equipo de estudiantes sin experiencia programando. Queremos construir una de las dos aplicaciones. Haznos en un único mensaje las preguntas necesarias para elegir el reto y concretar nuestra idea; después ayúdanos a comparar por separado el stack del prototipo y el de una posible solución real, diseñar y construir la primera versión. Queremos tomar decisiones reales y probar el resultado, no limitarnos a decir «aceptamos». Explica con ejemplos las palabras técnicas. No escribas código hasta que hayamos elegido la tecnología.

Podéis pedir aclaraciones y cambiar de opinión cuando tengáis un motivo. Una persona manejará el ordenador y el resto decidirá y revisará con ella; procurad turnaros.

## El recorrido de la práctica

**1. Definir la idea.** Elegid [BookFlow o Splitly](RETOS.md) y responded en una sola tanda quién lo utilizaría, en qué situación, qué problema tiene hoy y qué necesita conseguir. Podéis personalizar nombres y contexto.

**2. Elegir la tecnología: dos escenarios.** Contestad juntos una ronda de preguntas sobre vuestra experiencia, prioridades y necesidades futuras. Comparad opciones para el **prototipo local** y elegid una, explicando sus ventajas e inconvenientes. Después imaginad la **solución real para clientes**: ¿qué stack recomendaríais, dónde estarían los datos, qué haría falta para usarla desde distintos dispositivos y cómo afectarían costes y mantenimiento? No tenéis que construir esa versión real ni crear cuentas en proveedores.

**3. Diseñar.** Adjuntad referencias y contad qué aspectos os gustan. Invocad la skill **`/extraer-design-system`** desde el chat de Cursor (o pedid expresamente al agente que use esa skill si no aparece en el menú) para trasladar esas preferencias a decisiones concretas. Si no tenéis capturas, describidlo con suficiente detalle. Pedid una interfaz visualmente cuidada desde la primera versión y valoradla al verla, no solo leyendo códigos de color.

**4. Revisar el plan.** Pedid un resumen corto de pantallas, datos y funcionamiento. Corregid solo lo que afecte realmente al producto. No hace falta aprobar cada detalle ni revisar un documento largo.

**5. Construir y probar.** Pedid una **primera versión funcional completa** (no una pantalla decorativa sin lógica) y abridla. Probad vuestro caso con los nombres y datos que habéis elegido. Si falla, contad qué habéis hecho, qué esperabais y qué ocurrió. Podéis pedir mejoras de diseño si no se parece a vuestra referencia.

**6. Ampliar o mejorar el prototipo (opcional).** Si la versión básica funciona y queda tiempo y uso de IA, elegid una funcionalidad adicional o una mejora importante de experiencia visual. Explicad por qué aporta valor al usuario, implementadla y comprobad que no rompe lo anterior.

**7. Revisión independiente (último paso opcional).** Si todavía quedan tiempo y créditos, escribid `/revisor` para solicitar una revisión con el **subagente Revisor**. Pedidle que compruebe el proyecto frente a los requisitos y devuelva los fallos más importantes. No hace falta hacerlo si el uso gratuito está agotándose: las pruebas manuales del paso 5 siguen siendo obligatorias.

No hace falta que confirméis cada respuesta de Cursor. Intervenid cuando haya una decisión o un problema real. Si el agente se detiene con algo a medio construir, pedidle que termine el recorrido funcional acordado antes de añadir funciones nuevas.

## Resultado y exposición

Cursor dejará en `PROYECTO.md` una ficha breve con la idea, la tecnología elegida, el diseño, cómo abrir la aplicación y qué queda por resolver. No hay que rellenar documentación adicional.

Al terminar, entregaréis la carpeta o copia del proyecto e indicaréis cómo probarlo. Cada equipo dispondrá de **5 minutos para presentar**:

1. **Proyecto:** qué reto elegisteis, por qué, quién es vuestro usuario y cuál es su caso de uso.
2. **Tecnología:** stack del prototipo y propuesta de stack para una solución real; ventajas, inconvenientes y diferencias.
3. **Diseño:** referencias utilizadas y decisiones sobre el estilo visual.
4. **Demostración:** enseñad la aplicación funcionando y, si la añadisteis, una mejora propia.
5. **Aprendizajes:** qué os sorprendió, qué falló o fue difícil y qué haríais de otro modo.

No hace falta preparar diapositivas. Organizad el orden de intervención para no gastar los cinco minutos buscando archivos o navegando sin rumbo. Un fallo explicado con criterio es mejor que fingir que todo funciona.

Trabajad con nombres y datos inventados. No compartáis contraseñas, claves ni archivos `.env`. El prototipo solo necesita funcionar localmente y recordar los datos al recargar; no hay que publicarlo ni usar pagos reales.
