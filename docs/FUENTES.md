# Fuentes y decisiones de compatibilidad

Consulta documental: **08/11/2026**. Volver a verificar las condiciones antes de cada edición. No se incorporan skills de terceros ni código descargado de referencias visuales.

| Fuente oficial | Qué sustenta en este repositorio |
|---|---|
| [Cursor: modelos y planes](https://cursor.com/docs/models-and-pricing) | Free con Agent/Chat limitado; no garantizar una cantidad de uso |
| [Cursor: precios](https://cursor.com/pricing) | Comparación de capacidades actuales; no depender de Cloud Agents o modelos externos de pago |
| [Cursor: subagentes](https://cursor.com/docs/subagents) | Archivos en `.cursor/agents/`, frontmatter, `model: inherit` y auditor `readonly` |
| [Cursor: reglas](https://cursor.com/docs/rules) | Project rules en `.cursor/rules/*.mdc` y contexto AGENTS.md |
| [Cursor: skills](https://cursor.com/docs/skills) | SKILL.md, carga por relevancia e invocación desde `/` |
| [Cursor: crear y usar skills](https://cursor.com/help/customization/skills) | Ubicación `.cursor/skills/` y posibilidad de adjuntarlas como contexto |
| [Cursor: archivos ignorados](https://cursor.com/docs/reference/ignore-file) | `.cursorignore` no controla por sí solo terminal ni MCP |
| [GitHub: crear desde una plantilla](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template) | Una copia independiente por equipo |
| [GitHub: crear un repositorio plantilla](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-template-repository) | Configuración del repositorio del profesor |
| [GitHub: checkout](https://github.com/actions/checkout) y [setup-python](https://github.com/actions/setup-python) | Versiones v7 documentadas para las comprobaciones de materiales en runners alojados |
| [MDN: tecnologías web](https://developer.mozilla.org/en-US/docs/Web) | Categorías HTML/CSS/JavaScript y APIs del navegador |
| [Documentación de React](https://react.dev/) | React como biblioteca de interfaz |
| [Documentación de Next.js](https://nextjs.org/docs) | Framework sobre React; no equivalente completo de Vite |
| [Documentación de Vite](https://vite.dev/guide/) | Herramienta de desarrollo y construcción |
| [Documentación de TypeScript](https://www.typescriptlang.org/docs/) | Lenguaje y relación con JavaScript |
| [Documentación de Flask](https://flask.palletsprojects.com/) | Framework web de Python |

Los ejemplos de categorías son orientativos. No son una selección aprobada de stack para todos los equipos. Las comparaciones de costes de proveedores futuros requieren sus fuentes oficiales y fecha de consulta; se permiten importes marcados como no verificados cuando no se navegue.
