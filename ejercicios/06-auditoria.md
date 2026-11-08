# 6. Auditoría y entrega · minutos 53–60

**Objetivo:** comprobar el prototipo contra el encargo, localizar fallos y presentar evidencia honesta.

## Actividad

1. Primeros 3 minutos: ejecutar `/verificar-mvp` o adjuntar [la skill](../.cursor/skills/verificar-mvp/SKILL.md) al agente general. El equipo prueba en el navegador los casos de la ficha. Si ya hay evidencia reciente válida, reutilizarla e identificarla; no repetir por rutina ni inventar resultados.
2. Siguiente minuto: adjuntar [auditor.md](../.cursor/agents/auditor.md) con ficha, cuaderno, código y evidencia. Revisar funcionalidad, diseño, seguridad, código y requisitos. El auditor nativo es de solo lectura; no se le pide ejecutar pruebas que escriban archivos.
3. Últimos 3 minutos: corregir con el agente general el fallo prioritario y repetir la prueba afectada, registrar lo pendiente y preparar la demo. Si no cabe corregir, declarar el fallo.

## Prompts

Verificación:

> Sigue la skill verificar-mvp. Revisa nuestra ficha y evidencia, propón o ejecuta las pruebas útiles que falten y guía nuestras comprobaciones en navegador. No marques PASS si no hay una prueba observada. Registra BF-01…BF-06 o SP-01…SP-06 como PASS, FAIL o NO PROBADO. Comprueba persistencia al recargar, un caso inválido y las reglas de negocio.

Auditoría:

> Actúa como el auditor adjunto. Contrasta código, funcionalidad demostrada, design system, seguridad y requisitos. Primero informa; no reescribas la aplicación. Devuelve hasta cinco hallazgos por prioridad con evidencia, ubicación, impacto y arreglo mínimo. Separa riesgo de fallo reproducido y señala las pruebas que no pudiste realizar.

Corrección:

> Corrige solo el hallazgo prioritario que acabamos de elegir: [identificador]. Conserva stack, diseño y requisitos. Explica el cambio mínimo y repite su prueba y las relacionadas. Actualiza el estado real en el cuaderno.

## Entrega

Completar sección 6 del cuaderno, revisar ARRANQUE.md y guardar el código. El equipo puede pedir al agente un commit después de revisar qué archivos se incluirán. Si es público, usar alias y no subir capturas ajenas ni datos personales.

### Exposición posterior, 2 minutos por equipo

- 20 s: usuario, problema y propuesta.
- 60 s: flujo funcionando y caso anómalo, con datos ficticios.
- 20 s: stack elegido, alternativa y renuncia.
- 20 s: una decisión visual, un fallo encontrado y siguiente paso.

Plantilla opcional: [DEMO.md](../plantillas/DEMO.md). El profesor puede hacer preguntas después; las exposiciones quedan fuera de los 60 minutos. Evaluación: [rúbrica](../profesor/RUBRICA.md).

**Pregunta para pensar:** ¿qué tarea del negocio todavía no deberíamos confiar a este prototipo?
