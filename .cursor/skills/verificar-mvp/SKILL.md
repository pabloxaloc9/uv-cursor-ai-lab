---
name: verificar-mvp
description: Verificar el flujo funcional, persistencia y casos anómalos de BookFlow o Splitly con evidencias. Usar después de cada incremento y antes de la auditoría; distinguir pruebas ejecutadas de revisión de código.
---

# Verificar un MVP

1. Leer ficha elegida, entregables/EQUIPO.md, entregables/ARRANQUE.md y código pertinente. Identificar requisitos BF-01…BF-06 o SP-01…SP-06. Los JSON de retos/casos/ aportan datos y resultados esperados independientes del stack; no ejecutan la app. Reutilizar pruebas recientes solo cuando el código relevante no haya cambiado e identificar su evidencia.
2. Separar las capacidades disponibles: comandos, navegador del agente y navegador del equipo. No decir que se abrió una página o se ejecutó una prueba si no se hizo. No instalar una biblioteca de pruebas de navegador solo por esta skill; aprovechar lo disponible y la prueba humana.
3. Preparar una tabla con ID, datos de entrada, pasos, resultado esperado, resultado observado, quién lo observó y estado. Usar PASS, FAIL o NO PROBADO. Una revisión estática puede aportar un hallazgo, pero no un PASS funcional.
4. Arrancar según ARRANQUE.md y comprobar el flujo completo con datos ficticios. BookFlow: reservar, bloquear duplicado, recargar, filtrar por fecha, cancelar, recargar y comprobar disponibilidad. Splitly: S1, S2, S3, total, suma cero y liquidaciones que dejan todos los balances a cero. Ejecutar los casos inválidos de la ficha y revisar texto de usuario seguro.
5. Comprobar persistencia en el mismo origen local tras recargar. Si la implementación declara conservar datos tras reiniciar el servidor, probarlo también. No confundir cambiar puerto/origen con el mismo almacenamiento. Probar error de almacenamiento si se puede de forma reversible; si no, marcar pendiente y revisar que no se afirme un guardado fallido.
6. Revisar interfaz en ventana estrecha y escritorio, etiquetas, Tab, foco, mensajes y estados frente al design system. Si no puedes verla, pedir al equipo pasos y observaciones concretas. No inventar capturas o resultados visuales.
7. Si hay pruebas automatizadas adecuadas al stack, ejecutarlas sin alterar su intención. Registrar comando, resultado y alcance; un check del material de este repositorio no prueba la app. Evitar pruebas de escaso valor que solo repitan la implementación.
8. Registrar evidencia breve en secciones 5–6 del cuaderno y pasarla al auditor. Si falla algo, indicar reproducción y arreglo mínimo propuesto. Corregir con el agente general dentro del incremento o auditoría acordados y repetir los casos afectados. No ampliar el alcance ni cambiar de stack.

La revisión no certifica seguridad, conformidad legal ni preparación para producción. Si falta una capacidad o cuota, dejar constancia de lo no probado y de su impacto sobre la demostración.
