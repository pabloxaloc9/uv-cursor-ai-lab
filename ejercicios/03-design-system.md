# 3. Design system · minutos 15–22

**Objetivo:** pasar de «me gusta esta web» a un conjunto de decisiones visuales reutilizables.

Entrada: dos capturas reales seleccionadas por el equipo, con empresa y URL. Adjuntarlas al chat; guardarlas en un enlace privado no permite que el agente las vea automáticamente. Adjuntar [disenador-producto.md](../.cursor/agents/disenador-producto.md) y el cuaderno. Usar `/extraer-design-system` si aparece, o adjuntar [su SKILL.md](../.cursor/skills/extraer-design-system/SKILL.md).

## Actividad

1. Cada equipo explica qué le interesa de sus dos referencias: jerarquía, espacio, color, navegación o componentes. Evitar «copia esta pantalla».
2. El agente separa observaciones de propuestas y produce una identidad propia. Los colores medidos o estimados deben identificarse; no afirmar que se conoce una fuente por una captura.
3. Elegir y ajustar colores semánticos, tipografía, escala de espacio y componentes. Definir estados vacío, error y éxito.
4. Registrar el sistema en la sección 3 del cuaderno; se aplicará en todos los incrementos. No hace falta un manual de marca extenso ni instalar una biblioteca.

## Prompt inicial

> Actúa como el diseñador adjunto y sigue la skill extraer-design-system. Estas son nuestras dos capturas y estas son sus empresas y URLs: [añadir referencias]. Nos interesa [explicar por qué]. Ayúdanos a crear una identidad propia para nuestro producto. Separa lo que observas de lo que propones y lo que no puedes determinar. Tenemos 7 minutos. Propón los tokens, componentes y estados mínimos, espera nuestros ajustes y registra solo lo acordado en la sección 3 del cuaderno. No copies logos ni activos ni añadas dependencias.

## Entregable y criterio de finalización

Sección 3 completa: referencias, intención visual, colores con funciones, tipografía, espaciado, componentes y estados. El equipo puede explicar una decisión tomada de cada referencia y una decisión propia. Un componente debe describir cómo se ve y cómo responde al error o al foco.

**Pregunta para pensar:** ¿cómo reconoceríamos nuestra aplicación si ocultamos el nombre y el logotipo?

Si las imágenes no se pueden adjuntar, el equipo describe las capturas y el agente marca el análisis visual como limitado. No fingir que se han visto.

[Siguiente: arquitectura](04-arquitectura.md)
