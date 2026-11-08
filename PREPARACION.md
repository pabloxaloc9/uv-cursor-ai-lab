# Preparación antes de clase

Tiempo orientativo: 15–25 minutos, fuera de los 60 minutos del taller.

## Cada estudiante

- [ ] Instalar [Cursor desde su web oficial](https://cursor.com/downloads) y acceder con su propia cuenta. Verificar el plan Free y que Agent responde; una cuenta en prueba Pro no demuestra compatibilidad con Free.
- [ ] Crear o comprobar su cuenta de [GitHub](https://github.com/).
- [ ] Instalar [Git](https://git-scm.com/downloads) y comprobar `git --version` en una terminal.
- [ ] Tener un navegador actualizado y espacio para el proyecto. Usar un equipo sin credenciales o archivos de trabajo sensibles dentro de la carpeta del taller.
- [ ] Llevar dos capturas de interfaces de empresas reales que le gusten; sin datos personales. Anotar empresa, URL, fecha y qué le interesa de cada captura.

No publicar capturas ajenas por defecto: se adjuntan directamente al chat para el análisis. En el repositorio se registran referencias y conclusiones visuales, sin logos o imágenes de terceros. Si se desea publicar una captura, comprobar primero que se tienen derechos para hacerlo.

## Cada equipo

- [ ] Nombrar un responsable de la copia de GitHub; crear su repositorio desde la plantilla y clonarlo en Cursor. Un ordenador conduce y los otros miembros deciden y comprueban; no se comparten cuentas ni contraseñas.
- [ ] Abrir la raíz que contiene `README.md`, `AGENTS.md` y `.cursor/`, no una subcarpeta.
- [ ] Comprobar que se puede adjuntar `.cursor/agents/product-manager.md` al chat. Si el menú no lo muestra, abrir el archivo y adjuntarlo desde el editor o pegar su contenido.
- [ ] Revisar [Cursor Free](docs/CURSOR-FREE.md) y realizar su pequeña prueba de capacidad. Reservar cuota para el día de clase; la reserva no garantiza que alcance.
- [ ] Anotar qué entornos hay disponibles: `node --version`, `npm --version`, `python3 --version` (Windows: `py -3 --version`). No es obligatorio que estén todos. Si el equipo quiere poder elegir entre las rutas habituales de JavaScript y Python sin instalar durante clase, puede preparar [Node.js LTS](https://nodejs.org/en/download) y [Python](https://www.python.org/downloads/) desde sus webs oficiales. Tenerlos instalados no obliga a elegirlos.
- [ ] Si la instalación está bloqueada en un ordenador de la universidad, avisar antes al profesor. En el ejercicio 2 se compararán alternativas compatibles con el entorno disponible.

No instalar frameworks, bases de datos, extensiones de terceros, MCPs o skills externas para esta práctica. No hay suscripciones ni API keys requeridas. No es necesario activar Cloud Agents, Bugbot, automatizaciones ni permisos globales de ejecución.

## Seguridad en Cursor

Revisar los cambios y los comandos antes de aceptarlos. Si la versión ofrece sandbox, mantenerlo y aprobar solo los comandos necesarios. No activar una autorización global de terminal ni ampliar permisos para resolver deprisa un error. Nunca pegar el contenido de un `.env`, contraseña, token o credencial en el chat.

`.gitignore` evita incluir archivos en nuevos commits; `.cursorignore` reduce su acceso como contexto. Ninguno sustituye los permisos del sistema ni garantiza que un comando de terminal no pueda leerlos. En este taller no necesitamos secretos reales.

## Señal de preparación

El profesor recibe de cada equipo, por el canal habitual de la clase: nombre de equipo, copia de GitHub, ordenador que conduce y resultado de la prueba Free. Este repositorio no envía mensajes ni recopila datos automáticamente.

[Volver al README](README.md)
