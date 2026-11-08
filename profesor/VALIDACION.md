# Validación y alcance de las comprobaciones

Este documento distingue el repositorio educativo, el entorno Cursor Free y las aplicaciones que crearán los estudiantes.

## Resultado de la revisión inicial · 08/11/2026

| Comprobación ejecutada | Resultado observado |
|---|---|
| Verificador con `--plantilla` | PASS: estructura, enlaces locales, tiempos, metadatos, casos y neutralidad inicial |
| Suite del verificador | 11 tests ejecutados, 11 correctos |
| Compilación de las herramientas Python | Correcta en Python 3.12 |
| Inventario de entorno local | Material completo; Git, Node/npm y Python detectados; CLI de Cursor no detectada |
| Revisión de ambos contratos de MVP | Flujos y casos definidos; ejemplos numéricos de Splitly consistentes con sus liquidaciones |
| Ejecución dentro de Cursor Free | No realizada en este entorno; pendiente del ensayo previo del profesor |
| Ejecución del workflow en GitHub | Pendiente de publicación; comandos equivalentes ejecutados localmente |

El resultado no demuestra que un equipo termine su app en 60 minutos. Ese ajuste se contrasta en el ensayo de clase indicado abajo.

## Comprobación local del material

Desde la raíz, con Python 3.10 o superior:

```bash
python3 herramientas/validar_repo.py --plantilla
python3 -m unittest discover -s herramientas/tests -v
python3 herramientas/preflight.py
```

El primer comando comprueba estructura, rutas internas, tiempos, frontmatter, consistencia básica de los casos y neutralidad de la plantilla. `--plantilla` se usa para la rama original sin app. En una copia ya desarrollada, omitirlo: no queremos rechazar un stack que el equipo haya decidido.

Los tests verifican que el comprobador detecta enlaces rotos, rutas fuera de raíz, fases incoherentes, formatos incompletos y ejemplos de aceptación inconsistentes. No son tests de una aplicación estudiantil ni una simulación de consumo de IA.

`preflight.py` es opcional y de solo lectura. Muestra Git y entornos disponibles, y recuerda las comprobaciones manuales que no puede realizar: plan, cuota, carga efectiva de reglas/roles/skills y adjuntos visuales. No requiere que el prototipo use Python.

## Revisión de cada recorrido

| Recorrido | Criterio de revisión |
|---|---|
| Producto → stack | La entrevista de producto no elige tecnologías; la siguiente fase usa sus respuestas |
| Stack → arquitectura | Debe existir elección expresa y persistencia; el arquitecto no reabre por preferencia el stack |
| Diseño → desarrollo | Los tokens, componentes y estados quedan en el cuaderno y se contrastan con la interfaz |
| Desarrollo → auditoría | Se entregan arranque, pruebas y límites; no se toma código generado como evidencia funcional |
| Ruta Free | Roles y skills adjuntados al chat; sin obligación de delegación, nube, API keys o modelo de pago |
| BookFlow | Probar reserva, duplicado, recarga, cancelación y agenda por fecha según la ficha |
| Splitly | Probar balances S1/S2/S3, céntimos, suma cero, liquidaciones y recarga según la ficha |

La revisión de los contratos y materiales puede realizarse aquí. Las apps se construyen en las copias y se verifican allí con su stack. No se incluyen soluciones terminadas que impongan un stack de partida.

## Prueba real pendiente antes de impartir clase

- [ ] Ensayo de 60 minutos con cuenta que figure como Cursor Free y versión del alumnado.
- [ ] Comprobar lectura real de reglas y adjuntos y, si se desean, carga de agentes/skills nativos.
- [ ] Comprobar dos capturas y ruta alternativa si no se admiten.
- [ ] Completar cada reto en una copia independiente y registrar arranque y evidencia del navegador.
- [ ] Comprobar disponibilidad y cuota de los equipos cerca de la fecha de clase.

Estos puntos no los certifica la revisión documental ni GitHub Actions. Registrar aquí fecha, versión, cuenta Free confirmada (sin email), duración, resultado y limitaciones cuando el profesor haga el ensayo. No marcar casillas por expectativa.

## Qué ejecuta GitHub Actions

El workflow `.github/workflows/materiales.yml` ejecuta el verificador de materiales y sus tests, con permisos de solo lectura y sin secretos. No despliega, publica apps, instala servicios ni prueba automáticamente una app cuyo stack todavía no se ha decidido.

Si los equipos quieren CI de su aplicación, podrán añadirlo como ampliación después del taller, adecuado a su stack y sin sustituir estas comprobaciones por un «todo verde» sin significado.
