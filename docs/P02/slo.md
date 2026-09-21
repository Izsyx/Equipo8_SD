# SLOs del proyecto

## Proyecto

- **Nombre:** Módulo de Soporte con Mesas de Ayuda para Sistema de Navegador Seguro
- **Equipo:** 8
- **Responsable principal de los SLOs:** Israel Márquez Cárdenas
- **Proveedor candidato:** AWS
- **Ventana de medición:** 30 días móviles

> **Nota:** el objetivo final del SLO de disponibilidad queda pendiente de validar contra la disponibilidad compuesta calculada en B2. El valor de 99.5 % se utiliza de forma provisional.

---

## SLO 1 — Disponibilidad del Módulo de Soporte

- **Servicio:** Módulo de Soporte / Mesa de Ayuda.
- **SLI (definición):** proporción de peticiones válidas respondidas sin error 5xx.
- **Fórmula:** `peticiones válidas sin error 5xx / peticiones válidas × 100`.
- **Eventos válidos:** solicitudes reales al módulo realizadas por usuarios autorizados; se excluyen health checks y errores 4xx atribuibles al cliente.
- **Eventos buenos:** solicitudes válidas respondidas sin error 5xx.
- **Punto de medición:** Application Load Balancer y métricas de la aplicación.
- **Ventana:** 30 días móviles.
- **Objetivo (SLO):** **99.5 % provisional**, sujeto a que B2 determine una disponibilidad compuesta igual o superior.
- **Presupuesto de error provisional:** `(1 - 0.995) × 43 200 = 216 min`.
- **Alerta 50 %:** 108 min consumidos.
- **Alerta 100 %:** 216 min consumidos.
- **Herramienta:** Amazon CloudWatch.
- **Verificación externa:** monitor sintético sobre un endpoint de salud, si se implementa.
- **Responsable:** Israel Márquez Cárdenas.
- **Revisión:** cada cierre parcial.

---

## SLO 2 — Latencia de las solicitudes

- **Servicio:** interfaz/API del Módulo de Soporte.
- **SLI (definición):** proporción de peticiones válidas respondidas en 500 ms o menos.
- **Fórmula:** `peticiones válidas con tiempo ≤500 ms / peticiones válidas × 100`.
- **Eventos válidos:** peticiones reales recibidas por el módulo.
- **Eventos buenos:** peticiones válidas cuya respuesta total sea ≤500 ms.
- **Punto de medición:** Application Load Balancer.
- **Ventana:** 30 días móviles.
- **Objetivo (SLO):** **≥95 %** de las peticiones válidas en ≤500 ms, equivalente a **p95 ≤500 ms**.
- **Presupuesto de error:** hasta **5 %** de las peticiones válidas pueden superar 500 ms.
- **Alerta 50 %:** cuando 2.5 % de las peticiones válidas hayan superado el umbral.
- **Alerta 100 %:** cuando 5 % de las peticiones válidas hayan superado el umbral.
- **Herramienta:** Amazon CloudWatch.
- **Responsable:** Israel Márquez Cárdenas.
- **Revisión:** cada cierre parcial.

---

## SLO 3 — Creación exitosa de tickets

- **Servicio:** gestión de tickets del Módulo de Soporte.
- **SLI (definición):** proporción de intentos válidos de creación que terminan con un ticket correctamente registrado.
- **Fórmula:** `tickets creados correctamente / intentos válidos de creación × 100`.
- **Eventos válidos:** solicitudes de creación realizadas por usuarios autenticados, con permisos y con los campos obligatorios válidos.
- **Eventos buenos:** tickets persistidos correctamente, con identificador único, estado inicial y registro disponible para seguimiento.
- **Punto de medición:** API/aplicación y registro de eventos de creación.
- **Ventana:** 30 días móviles.
- **Objetivo (SLO):** **≥99.0 %**.
- **Presupuesto de error:** hasta **1 %** de los intentos válidos de creación pueden fallar.
- **Alerta 50 %:** cuando 0.5 % de los intentos válidos hayan fallado.
- **Alerta 100 %:** cuando 1 % de los intentos válidos hayan fallado.
- **Herramienta:** Amazon CloudWatch Logs y métrica personalizada de la aplicación.
- **Responsable:** Israel Márquez Cárdenas.
- **Revisión:** cada cierre parcial.

---

## Política del presupuesto de error

1. **Al consumir el 50 % del presupuesto:** el equipo revisará logs, métricas e incidentes recientes para identificar las principales causas de degradación. Se priorizarán correcciones antes de introducir cambios de alto riesgo.
2. **Al consumir el 100 % del presupuesto:** se congelarán temporalmente los despliegues de nuevas funcionalidades. Solo se permitirán correcciones de errores, cambios de seguridad y mejoras de confiabilidad.
3. **Responsable de la decisión:** Israel Márquez Cárdenas, en coordinación con el resto del equipo.
4. **Recuperación:** los despliegues normales podrán reanudarse cuando el sistema vuelva a tener margen suficiente dentro de la ventana móvil y el equipo confirme que la causa principal del consumo fue mitigada.

---

## Plan de medición

| SLO | Métrica principal | Punto de medición | Herramienta |
|---|---|---|---|
| Disponibilidad | Respuestas sin 5xx / peticiones válidas | ALB / aplicación | Amazon CloudWatch |
| Latencia | Porcentaje de respuestas ≤500 ms y p95 | ALB | Amazon CloudWatch |
| Creación de tickets | Tickets creados correctamente / intentos válidos | API / aplicación | CloudWatch Logs + métrica personalizada |

---

## Dependencia con B2

El SLO de disponibilidad no se considera definitivo hasta conocer la **disponibilidad compuesta del proyecto** calculada en B2.

Si B2 obtiene una disponibilidad compuesta menor a 99.5 %, el objetivo deberá reducirse a un valor realista que:

1. no supere la disponibilidad compuesta; y
2. deje margen para fallas propias de la aplicación, despliegues y configuraciones del equipo.
