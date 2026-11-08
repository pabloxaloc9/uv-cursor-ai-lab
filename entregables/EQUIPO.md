# Cuaderno del equipo

Completar con frases y tablas breves. El agente puede redactar borradores; el equipo toma las decisiones. No rellenar pruebas que nadie haya observado. Las plantillas empiezan pendientes de forma intencionada.

## 0. Equipo y entorno

- Equipo / reto / nombre comercial: _Por completar_.
- Cuatro miembros o alias y funciones iniciales: _Por completar_.
- Copia GitHub y persona que conduce Cursor: _Por completar_.
- Sistema operativo, versión de Cursor, plan real y modelo disponible: _Por completar_.
- Entornos disponibles (lenguajes/runtimes, versiones, restricciones): _Por completar_.
- Referencias visuales preparadas: _Por completar_.

## 1. Producto

- Usuario y situación: _Por completar_.
- Problema y solución actual: _Por completar_.
- Propuesta de valor en una frase: _Por completar_.
- Flujo de la demo, de inicio a fin: _Por completar_.
- Personalización elegida y por qué: _Por completar_.
- Supuesto que validaríamos con un cliente: _Por completar_.
- Requisitos: BF-01…BF-06 o SP-01…SP-06, según la ficha elegida.
- Fuera de alcance: datos reales, autenticación, pagos, servicios de pago y despliegue; añadir otras exclusiones decididas.
- **Producto acordado por el equipo:** PENDIENTE. Registrar aceptación o correcciones expresas.

## 2. Elección del stack

Resumir las dos tandas de entrevista: experiencia; entorno; interacción; datos compartidos futuros; datos y riesgo de pérdida; presupuesto/tiempo; integraciones futuras; dos prioridades.

| Alternativa | Lenguaje + interfaz + ejecución + persistencia | Entorno y complejidad | Ventajas | Inconvenientes y mantenimiento | Coste local / futuro y fuentes |
|---|---|---|---|---|---|
| A | _Por completar_ | | | | |
| B | _Por completar_ | | | | |
| C | _Por completar_ | | | | |

- Recomendación del agente y cuándo elegiría otra alternativa: _Por completar_.
- **Elección expresa del equipo:** PENDIENTE.
- Criterios que sustentan nuestra elección: _Por completar_.
- Alternativa descartada y renuncia que aceptamos: _Por completar_.
- Dónde persistirán los datos del prototipo y límite frente a producción: _Por completar_.
- Qué habría que cambiar para usuarios reales en varios dispositivos: _Por completar_.
- Importes futuros no verificados y fecha de fuentes consultadas: _Por completar_.

## 3. Design system

- Tres cualidades de nuestra identidad: _Por completar_.

| Empresa / URL / fecha | Qué observamos en su captura | Qué tomamos y cómo lo adaptamos | Qué es estimado o no determinable |
|---|---|---|---|
| Referencia 1 | | | |
| Referencia 2 | | | |

| Token semántico | Valor elegido | Uso |
|---|---|---|
| Fondo / superficie | | |
| Texto / texto secundario | | |
| Primario / texto sobre primario | | |
| Borde / foco | | |
| Error / éxito | | |
| Tipografía y tamaños | | |
| Espaciados y radios | | |

| Componente | Apariencia y jerarquía | Foco, error, deshabilitado u otros estados |
|---|---|---|
| Botones | | |
| Campos y etiquetas | | |
| Tarjetas / navegación | | |
| Listado, agenda o balances | | |
| Estados vacío, error y éxito | | |

- Contraste: herramienta y resultado si se ha medido; si no, PENDIENTE.
- **Diseño acordado por el equipo:** PENDIENTE.

## 4. Arquitectura

- Pantallas y componentes reutilizables: _Por completar_.
- Estructura mínima de archivos y función de cada parte: _Por completar_.

| Entidad | Campos esenciales y tipos | Relaciones y reglas |
|---|---|---|
| _Por completar_ | | |

- Persistencia (mecanismo, ubicación/clave/tabla y carga inicial): _Por completar_.
- Qué ocurre al recargar, reiniciar y cambiar de origen/puerto: _Por completar_.
- Regla contra duplicados / regla de reparto y redondeo: _Por completar_.
- Validaciones y respuesta si el almacenamiento falla: _Por completar_.
- Límite con pestañas simultáneas o dispositivos distintos: _Por completar_.
- **Plan aceptado por el equipo antes del código:** PENDIENTE.

## 5. Plan y desarrollo

| Incremento | Archivos / cambio y requisitos | Prueba de finalización | Observación real y quién la hizo | Estado |
|---|---|---|---|---|
| I1 · 7 min | Arranque y estilo | Abrir y navegar | _Sin probar_ | PENDIENTE |
| I2 · 11 min | Flujo y persistencia | Crear, recargar y comprobar | _Sin probar_ | PENDIENTE |
| I3 · 7 min | MVP restante y validaciones | Caso anómalo y coherencia visual | _Sin probar_ | PENDIENTE |

- Decisión que cambiamos durante el desarrollo, motivo y quién la tomó: _Por completar o ninguna_.
- Comandos realmente ejecutados y resultado relevante: _Por completar_.
- Instrucciones de arranque: completar [ARRANQUE.md](ARRANQUE.md).

## 6. Auditoría y evidencia

Sustituir ID-01…ID-06 por BF-01…BF-06 o SP-01…SP-06. Marcar PASS solo con una prueba observada; FAIL cuando se observa un fallo y NO PROBADO cuando falta comprobarlo. Una lectura de código no es prueba funcional.

| Requisito | Caso / pasos / datos | Resultado esperado | Observado, por quién y evidencia | Estado |
|---|---|---|---|---|
| ID-01 | | | | NO PROBADO |
| ID-02 | | | | NO PROBADO |
| ID-03 | | | | NO PROBADO |
| ID-04 | | | | NO PROBADO |
| ID-05 | | | | NO PROBADO |
| ID-06 | | | | NO PROBADO |
| Diseño y ventana estrecha | | | | NO PROBADO |
| Etiquetas, Tab y foco | | | | NO PROBADO |
| Seguridad y texto de usuario | | | | NO PROBADO |
| Arranque reproducible | | | | NO PROBADO |

| Hallazgo y severidad | Evidencia / ubicación | Arreglo mínimo | Resultado de la nueva prueba o pendiente |
|---|---|---|---|
| _Por completar o ninguno observado_ | | | |

- Qué funciona y podemos demostrar: _Por completar_.
- Qué falta, falla o no hemos probado: _Por completar_.
- Principal limitación antes de producción: _Por completar_.
- Qué decisión tomó el equipo frente a una propuesta de la IA: _Por completar_.

## 7. Exposición posterior

- Demostración de 60 segundos y datos ficticios que usaremos: _Por completar_.
- Una elección tecnológica y su renuncia: _Por completar_.
- Una decisión visual y un fallo detectado: _Por completar_.
- Siguiente paso para validar el negocio: _Por completar_.

Comprobar que cada miembro puede explicar una decisión. Usar [DEMO.md](../plantillas/DEMO.md) si queréis un guion más detallado.
