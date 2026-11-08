# Comparar tecnologías con criterio

Un stack es una combinación de piezas. El equipo decide cuáles necesita y puede omitir las que no aportan al prototipo.

| Pregunta | Categoría | Ejemplos ilustrativos, no obligatorios |
|---|---|---|
| ¿Con qué escribimos lógica? | Lenguaje | JavaScript, TypeScript, Python u otro conocido por el equipo |
| ¿Cómo expresamos estructura y estilo? | Marcado / estilo | HTML y CSS; una biblioteca visual puede ayudar, pero no es obligatoria |
| ¿Cómo construimos la interfaz? | Enfoque o biblioteca de interfaz | HTML y DOM del navegador, plantillas de servidor, React, Vue u otro |
| ¿Cómo organizamos una app completa? | Framework, si hace falta | Flask, Django, Next.js u otro; tienen responsabilidades distintas |
| ¿Cómo ejecutamos o preparamos el proyecto? | Runtime / herramientas | Navegador, Node.js, Python, Vite u otras herramientas según el stack |
| ¿Dónde sobreviven los datos? | Persistencia | Almacenamiento del navegador, un archivo gestionado por servidor, SQLite u otra opción justificada |
| ¿Dónde se aloja un producto futuro? | Infraestructura | Comparar después según backend, datos y operación; para clase basta ejecutar localmente |

React y Flask no sustituyen exactamente las mismas piezas. Next.js incorpora React y otras capacidades; Vite es una herramienta de desarrollo y construcción, no un lenguaje ni un equivalente completo de Next.js. TypeScript es un lenguaje que normalmente se transforma en JavaScript; no es un framework. HTML estructura contenido y CSS lo presenta.

## Criterios para las tres alternativas

1. ¿Cubren el flujo obligatorio y la persistencia al recargar?
2. ¿Podemos arrancarlas en el entorno disponible y entender los archivos?
3. ¿Qué complejidad añaden y qué problema real resuelven con ella?
4. ¿Qué coste tiene construir, operar y mantener? Separar tiempo, licencias y servicios.
5. ¿Qué límites tienen frente a dispositivos y usuarios simultáneos, datos personales o integraciones futuras?
6. ¿Qué aceptaríamos perder al elegirlas y qué costaría cambiar después?

No existe una respuesta única. Una solución local sencilla puede ser suficiente para validar una interacción y exigir cambios importantes para un negocio real. Un stack más amplio puede facilitar evolución y consumir el tiempo del taller. El equipo debe explicar esa renuncia.

## Costes sin cifras inventadas

El prototipo del taller tiene presupuesto de servicios 0 € y usa datos ficticios. Un alojamiento futuro puede tener coste aunque el software tenga licencia gratuita. Las capas gratuitas pueden tener límites de uso, caducidad, suspensión o condiciones distintas; verificar las condiciones en la fuente oficial y anotar fecha. Si no se ha verificado un importe, escribir «no verificado».

El asesor no debe ir creando cuentas ni contratando servicios durante la comparación.

[Ejercicio 2](../ejercicios/02-stack.md) · [Fuentes](FUENTES.md)
