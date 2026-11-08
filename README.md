# De una idea a un prototipo con Cursor

Práctica del Máster de Creación de Empresas Innovadoras de la Universitat de València.
**16 estudiantes · 4 equipos de 4 · 60 minutos de trabajo + exposiciones.**

> La IA propone, el equipo decide. Que algo funcione no significa que esté bien diseñado.

Este repositorio es el entorno de trabajo y los materiales del taller. La aplicación se construye durante la práctica: **no hay framework, lenguaje, base de datos ni aplicación preseleccionados**. Las herramientas de mantenimiento en Python no son el stack del prototipo.

## Antes de clase

Sigue [PREPARACION.md](PREPARACION.md). Llega con Cursor, una cuenta gratuita operativa, Git, GitHub, una copia propia de este repositorio y dos capturas de referencias visuales. No necesitas tarjeta, API key ni proveedores de nube.

1. En [el repositorio original](https://github.com/pabloxaloc9/uv-cursor-ai-lab), el responsable del equipo pulsa **Use this template → Create a new repository**. Nombre sugerido: `uv-equipo-1-bookflow` o `uv-equipo-2-splitly`.
2. En Cursor, usa **Clone Repository**, pega la URL de **tu copia** y abre su carpeta raíz. Alternativa en una terminal:

   ```bash
   git clone URL_DE_TU_COPIA
   ```

3. Lee [INICIO-RAPIDO.md](INICIO-RAPIDO.md), elige [BookFlow](retos/BOOKFLOW.md) o [Splitly](retos/SPLITLY.md) y abre [el cuaderno del equipo](entregables/EQUIPO.md).
4. Abre Agent y pega el primer prompt del recorrido. No ejecutes `npm install`, `pip install` ni un generador de aplicaciones antes de decidir el stack.

Si no aparece Use this template, usa **Fork**. Si GitHub o la autenticación fallan, descarga el ZIP desde **Code → Download ZIP**, extrae la carpeta y ábrela en Cursor; podrás subir el trabajo después. No hace falta escribir sobre el repositorio original.

## Recorrido de 60 minutos

| Minutos | Ejercicio | Resultado que debe decidir el equipo |
|---|---|---|
| 00–06 | [1. Producto](ejercicios/01-producto.md) | Usuario, problema, propuesta y MVP verificable |
| 06–15 | [2. Stack](ejercicios/02-stack.md) | Comparación de alternativas y elección razonada |
| 15–22 | [3. Design system](ejercicios/03-design-system.md) | Identidad propia, tokens y componentes |
| 22–28 | [4. Arquitectura](ejercicios/04-arquitectura.md) | Estructura, modelo de datos y tres incrementos |
| 28–53 | [5. Desarrollo](ejercicios/05-desarrollo.md) | Prototipo local con flujo completo y persistencia |
| 53–60 | [6. Auditoría](ejercicios/06-auditoria.md) | Evidencias, correcciones y límites conocidos |

Después: **2 minutos de exposición por equipo**, más las preguntas del profesor. No se descuentan de los 60 minutos.

## Cómo trabajar con los especialistas

Los cinco roles están en [`.cursor/agents/`](.cursor/agents/). La ruta base para Free es **adjuntar el archivo del rol en el chat principal** y pedir que actúe con esas instrucciones. No necesitas lanzar procesos paralelos. Cada ejercicio incluye el prompt exacto.

Si tu versión permite subagentes nativos, puedes usarlos: todos heredan el modelo disponible, sin fijar modelos de pago. En una entrevista, el subagente devuelve las preguntas al agente principal; este las presenta y espera vuestra respuesta. Un subagente no debe inventar respuestas para poder continuar.

| Elemento | Para qué sirve | Ubicación |
|---|---|---|
| Agente / rol | Perspectiva especializada: producto, stack, diseño, arquitectura o auditoría | `.cursor/agents/*.md` |
| Rule | Instrucciones persistentes y breves sobre trabajo y seguridad | `.cursor/rules/*.mdc` |
| Skill | Procedimiento reutilizable: extraer diseño o verificar un MVP | `.cursor/skills/*/SKILL.md` |
| Cuaderno | Memoria compartida de decisiones y pruebas entre conversaciones | `entregables/EQUIPO.md` |

Las skills propias son `/extraer-design-system` y `/verificar-mvp`. Si no aparecen en `/`, adjunta su `SKILL.md` como archivo. Consulta [compatibilidad con Cursor Free](docs/CURSOR-FREE.md).

## Qué se entrega

- Código del prototipo y pasos de arranque reproducibles en `entregables/ARRANQUE.md`.
- [EQUIPO.md](entregables/EQUIPO.md) completado con decisiones humanas y pruebas reales.
- Una demostración del flujo obligatorio de la ficha elegida y un caso anómalo.
- Un commit final en la copia del equipo, si GitHub está operativo; en caso contrario, la carpeta completa.

No se exige autenticación real, pagos, envío de correos ni despliegue. Los datos son ficticios. **Sí se exige conservar los datos al recargar la aplicación** y explicar dónde se guardan. La app debe funcionar localmente sin servicios de pago. Las vistas de cliente y gestión de BookFlow son una simulación sin control de acceso real.

## Ayuda y materiales

- [Preparación](PREPARACION.md) · [Inicio rápido](INICIO-RAPIDO.md) · [Bloqueos frecuentes](docs/BLOQUEOS.md)
- [Guía del profesor](profesor/GUIA.md) · [Rúbrica](profesor/RUBRICA.md) · [Validación del repositorio](profesor/VALIDACION.md)
- [Comparar tecnologías sin confundir categorías](docs/COMPARAR-STACKS.md) · [Fuentes oficiales](docs/FUENTES.md)
- [Plantilla de decisión ampliada](plantillas/DECISION.md) · [Comunicar un error](plantillas/ERROR.md) · [Preparar la exposición](plantillas/DEMO.md)

Mantenimiento opcional del material (Python 3.10 o superior, solo biblioteca estándar):

```bash
python3 herramientas/validar_repo.py
python3 -m unittest discover -s herramientas/tests -v
python3 herramientas/preflight.py
```

En Windows se puede usar `py -3` en lugar de `python3`. Estos comandos comprueban **el material del taller y el entorno**, no certifican el prototipo ni la cuota de Cursor. La rúbrica evalúa criterio, funcionamiento y evidencia, no cantidad de archivos o tokens consumidos.

Material educativo independiente; no es un producto oficial de Cursor ni una publicación oficial de la Universitat. Licencia [MIT](LICENSE).
