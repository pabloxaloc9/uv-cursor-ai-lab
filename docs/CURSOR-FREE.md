# Cursor Free: compatibilidad y prueba previa

Revisión documental: **8 de noviembre de 2026**. Las interfaces, modelos y condiciones del plan pueden cambiar. Revalidar antes de impartir la clase.

## Qué puede prometer este material

Las páginas oficiales de [planes](https://cursor.com/docs/models-and-pricing) y [precios](https://cursor.com/pricing) indican Agent y Chat con uso limitado en Free. No publican una cuota universal que garantice completar este taller. No se usa un número supuesto de peticiones ni se depende de modelos externos de pago.

Se distinguen tres cosas: que el material use formatos documentados; que una cuenta/versión tenga una función disponible; y que su cuota alcance para la sesión. Un script local no puede certificar las dos últimas.

| Capacidad | Ruta de clase | Si no aparece o no está disponible |
|---|---|---|
| Agent / Chat | Cuenta Free propia con modelo disponible | Comprobar sesión, plan y cuota; si no responde, avisar al profesor antes de clase |
| Reglas del proyecto | `.cursor/rules/*.mdc` con `alwaysApply: true` | Adjuntar AGENTS.md y las reglas al iniciar el chat; no son una barrera técnica de permisos |
| Roles especializados | Adjuntar `.cursor/agents/<rol>.md` en el chat principal | Abrir y pegar las instrucciones del rol; no hace falta delegación nativa |
| Subagentes nativos | Mejora opcional con `model: inherit` | Usar el rol en el chat principal; en entrevistas el principal pregunta al equipo |
| Skills propias | `/extraer-design-system`, `/verificar-mvp` | Adjuntar su SKILL.md y pedir que siga el procedimiento |
| Capturas de referencia | Adjuntar dos imágenes reales | Abrirlas en el equipo y describirlas; registrar que el agente no hizo análisis visual directo |
| Navegador controlado por agente | Opcional | El equipo prueba en su navegador y aporta observaciones concretas |
| Cloud Agents, MCP, Bugbot o APIs externas | No requeridos | No instalarlos para resolver este taller |

La ruta manual evita depender de la carga nativa de un rol o skill, **no elimina el consumo de IA ni evita un límite de cuota**. Las páginas de planes anteriores pueden mostrar nombres o prestaciones distintos; comprobar lo que realmente indica la cuenta de cada estudiante.

## Prueba previa por equipo, 3–5 minutos

Con una cuenta que realmente figure como Free, sin trial Pro:

1. Abrir la copia raíz y anotar versión, plan, modelo disponible y fecha en el cuaderno.
2. Pedir a Agent que lea README.md y resuma qué cosas debe decidir el equipo antes del código. Comprobar que menciona el stack y el plan y que no instala nada.
3. Adjuntar product-manager.md; pedir la primera tanda y comprobar que pregunta y espera, sin inventar respuestas.
4. Comprobar que se puede adjuntar una captura. Probar la skill de diseño nativa o adjuntada, sin generar todavía un design system completo.
5. Pedir un cambio mínimo en una nota temporal con datos ficticios y revisarlo. Borrar esa nota después de la comprobación. No es necesario generar la app ni consumir la cuota preparando una solución.
6. Anotar cualquier función ausente y confirmar la ruta alternativa del cuadro anterior.

## Ensayo del profesor

Realizar un ensayo completo con una cuenta Free representativa del alumnado, registrar consumo observado si la interfaz lo muestra y repetir cerca de la fecha de clase. No extrapolar un éxito a una garantía de cuota para 16 cuentas distintas. Si no se dispone de esa cuenta, el ensayo real queda pendiente y debe decirse expresamente.

| Evidencia | Estado de esta edición |
|---|---|
| Documentación oficial de Agent/Chat Free consultada | Revisada el 08/11/2026 |
| Formatos de reglas, agentes y skills | Contrastados con documentación y verificador local |
| Necesidad de API keys, nube o modelo de pago | Ninguna en el recorrido base |
| Ensayo completo dentro de Cursor con cuenta Free real | PENDIENTE: requiere el ordenador y cuenta del profesor o un equipo |
| Cuota suficiente en cada cuenta el día de clase | No se puede garantizar; comprobar con antelación |

## Si se agota la cuota

Detener las solicitudes repetidas. Guardar cuaderno y código. El equipo puede continuar en el ordenador y la cuenta **propia** de otro miembro si esa cuenta tiene disponibilidad, sin compartir credenciales y sin crear cuentas para eludir límites. Transferir solo código y datos ficticios mediante su copia del repositorio o la carpeta de trabajo. Si las cuentas disponibles se agotan, pedir apoyo al profesor; se puede terminar la revisión manual y presentar lo construido, declarando la limitación. No exigir contratar un plan para aprobar la práctica.

[Preparación](../PREPARACION.md) · [Fuentes oficiales](FUENTES.md)
