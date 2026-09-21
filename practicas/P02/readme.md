# Práctica 2 — Acuerdo de nivel de servicio: análisis de un SLA real y diseño de los SLOs del proyecto

## Datos del equipo

- **Equipo:** 8
- **Integrantes:**
  - Israel Márquez Cárdenas
  - Salvador
  - Esaul
- **Materia:** Sistemas Distribuidos
- **Grupo:** 7CV1
- **Proveedor seleccionado:** AWS
- **Proyecto:** Módulo de Soporte con Mesas de Ayuda para Sistema de Navegador Seguro

---

# 1. Introducción

En esta práctica se analizan SLA reales de los servicios usados por el proyecto. A partir de sus compromisos de disponibilidad se calcula la disponibilidad compuesta del sistema y se definen SLIs, SLOs y presupuestos de error.

---

# 2. B1 — Anatomía de un SLA real

## Tabla 1. Anatomía del SLA

| Integrante | Servicio y URL (fecha) | Compromiso por configuración | Definición de inactividad | Exclusiones | Créditos | Reclamación | Min/mes permitidos |
|---|---|---|---|---|---|---|---|
| Israel Márquez Cárdenas | Amazon EC2 — https://aws.amazon.com/compute/sla/ — consulta: 20/09/2026 | Instancia individual: 99.5 %. Nivel regional: 99.99 % con instancias en ≥2 AZ. | Individual: la instancia pierde conectividad externa. Regional: todas las instancias en ≥2 AZ pierden simultáneamente conectividad externa. | Factores fuera del control de AWS; acciones del cliente; equipo/software del cliente; suspensión del servicio. | < SLA y ≥99.0 %: 10 %. <99.0 % y ≥95.0 %: 30 %. <95.0 %: 100 %. | Caso en AWS Support Center con fechas, horas, región/AZ, IDs y logs. | 99.5 % → 216 min. 99.99 % → 4.32 min. |
| Salvador | [PENDIENTE] | [PENDIENTE] | [PENDIENTE] | [PENDIENTE] | [PENDIENTE] | [PENDIENTE] | [PENDIENTE] |
| Esaul | [PENDIENTE] | [PENDIENTE] | [PENDIENTE] | [PENDIENTE] | [PENDIENTE] | [PENDIENTE] | [PENDIENTE] |

## 2.1 Análisis individual — Israel Márquez Cárdenas

- **Proveedor:** AWS
- **Servicio:** Amazon EC2
- **SLA oficial:** https://aws.amazon.com/compute/sla/
- **Última actualización:** 25 de mayo de 2022
- **Fecha de consulta:** 20 de septiembre de 2026
- **Evidencia:** `evidencias/P02/P02_B1_ec2_israel.png`

### Compromiso

- Instancia individual: **99.5 %**
- Configuración regional con instancias en ≥2 AZ: **99.99 %**

Una sola instancia representa un único punto de falla. La configuración Multi-AZ aumenta la disponibilidad mediante redundancia.

### Definición de indisponibilidad

AWS considera una instancia individual no disponible cuando pierde conectividad externa. A nivel regional, la indisponibilidad ocurre cuando todas las instancias distribuidas en al menos dos AZ pierden simultáneamente conectividad.

Por ello, una aplicación puede fallar por errores de software, configuración o dependencias externas sin que EC2 sea considerado no disponible.

### Exclusiones

1. Factores fuera del control razonable de AWS.
2. Acciones u omisiones del cliente.
3. Equipo, software o tecnología del cliente.
4. Suspensión o terminación del uso del servicio.

### Créditos

| Disponibilidad | Crédito |
|---|---:|
| <99.99 % y ≥99.0 % regional / <99.5 % y ≥99.0 % individual | 10 % |
| <99.0 % y ≥95.0 % | 30 % |
| <95.0 % | 100 % |

### Reclamación

La reclamación se realiza en AWS Support Center e incluye fechas y horas del incidente, región, AZ, IDs de recursos y logs. Debe presentarse dentro del plazo establecido por AWS.

### Minutos permitidos

Ventana de 30 días:

`43 200 min`

Instancia individual:

`(1 - 0.995) × 43 200 = 216 min`

Configuración regional:

`(1 - 0.9999) × 43 200 = 4.32 min`

### Crédito a 99.0 %

Factura hipotética: **100 USD**

`100 × 0.10 = 10 USD`

### México

El SLA de Amazon Compute no publica un porcentaje distinto específicamente para México; el compromiso depende de la configuración utilizada.

## Análisis individual — Esaul

## Análisis individual - Salvador

---

# 3. B2 — Disponibilidad compuesta del proyecto

## Diagrama

![Arquitectura](../../docs/arquitectura/arquitectura_p02.png)

`DNS → Balanceador → Cómputo → Base de datos → Objetos → Servicios externos`

## Tabla 2. Disponibilidad compuesta del proyecto

| Componente | SLA individual | SLA redundante | En serie o paralelo | Costo extra de redundancia |
|---|---:|---:|---|---:|
| DNS | [PENDIENTE] | [PENDIENTE] | [PENDIENTE] | [PENDIENTE] |
| Balanceador | [PENDIENTE] | [PENDIENTE] | [PENDIENTE] | [PENDIENTE] |
| Cómputo — EC2 | 99.5 % | 99.99 % | [PENDIENTE] | [PENDIENTE] |
| Base de datos | [PENDIENTE] | [PENDIENTE] | [PENDIENTE] | [PENDIENTE] |
| Objetos | [PENDIENTE] | [PENDIENTE] | [PENDIENTE] | [PENDIENTE] |
| **Compuesto sin redundancia** | **[PENDIENTE]** | — | — | — |
| **Compuesto con redundancia** | — | **[PENDIENTE]** | — | **[PENDIENTE]** |
| **Min/mes sin redundancia** | **[PENDIENTE]** | — | — | — |
| **Min/mes con redundancia** | — | **[PENDIENTE]** | — | — |

### Fórmulas

Serie:

`A = a1 × a2 × ... × an`

Paralelo:

`A = 1 - (1 - a1)(1 - a2)`

### Resultado

- **Disponibilidad sin redundancia:** [PENDIENTE] %
- **Disponibilidad con redundancia:** [PENDIENTE] %
- **Eslabón más débil:** [PENDIENTE]
- **Costo de reforzarlo:** [PENDIENTE] USD/mes

---

# 4. B3 — SLIs, SLOs y presupuesto de error

**Responsable principal:** Israel Márquez Cárdenas

Para el Módulo de Soporte se definieron tres indicadores: disponibilidad del módulo, latencia de las solicitudes y creación exitosa de tickets. El objetivo final de disponibilidad queda sujeto al resultado de B2, ya que no puede superar la disponibilidad compuesta de la arquitectura.

## Tabla 3. SLOs del proyecto

| SLO | SLI (buenos ÷ válidos) | Punto de medición | Ventana | Objetivo | Presupuesto | Alertas 50 % / 100 % | Herramienta |
|---|---|---|---|---:|---|---|---|
| Disponibilidad | Peticiones válidas sin error 5xx / peticiones válidas | ALB / aplicación | 30 días móviles | **99.5 % provisional*** | **216 min provisional*** | 108 / 216 min | Amazon CloudWatch |
| Latencia p95 | Peticiones válidas respondidas en ≤500 ms / peticiones válidas | ALB | 30 días móviles | ≥95 % de peticiones ≤500 ms | 5 % de peticiones válidas | 2.5 % / 5 % de peticiones fuera del umbral | Amazon CloudWatch |
| Creación de tickets | Tickets creados y registrados correctamente / intentos válidos de creación | Aplicación / API | 30 días móviles | ≥99.0 % | 1 % de intentos válidos | 0.5 % / 1 % de intentos fallidos | CloudWatch Logs / métrica de aplicación |

\* El SLO de disponibilidad y su presupuesto son provisionales hasta completar B2.

## SLO de disponibilidad

- **SLI:** peticiones válidas respondidas sin error 5xx / peticiones válidas × 100.
- **Eventos válidos:** solicitudes reales al módulo; se excluyen health checks y errores 4xx atribuibles al cliente.
- **Eventos buenos:** solicitudes respondidas sin error 5xx.
- **Punto de medición:** Application Load Balancer y métricas de la aplicación.
- **Ventana:** 30 días móviles.
- **Objetivo provisional:** 99.5 %, sujeto al resultado de B2.
- **Presupuesto provisional:** `(1 - 0.995) × 43 200 = 216 min`.
- **Alertas:** 108 min (50 %) y 216 min (100 %).
- **Herramienta:** Amazon CloudWatch.

## SLO de latencia

- **SLI:** peticiones válidas respondidas en ≤500 ms / peticiones válidas × 100.
- **Objetivo:** al menos 95 % de las peticiones válidas en ≤500 ms (p95 ≤500 ms).
- **Punto de medición:** Application Load Balancer.
- **Ventana:** 30 días móviles.
- **Presupuesto:** hasta 5 % de peticiones válidas fuera del umbral.
- **Alertas:** 2.5 % y 5 % de peticiones fuera del umbral.
- **Herramienta:** Amazon CloudWatch.

## SLO de dominio — Creación de tickets

- **SLI:** tickets creados y registrados correctamente / intentos válidos de creación × 100.
- **Eventos válidos:** solicitudes autenticadas y con los campos obligatorios válidos.
- **Eventos buenos:** tickets almacenados correctamente, con identificador y estado inicial, y disponibles para seguimiento.
- **Objetivo:** ≥99.0 %.
- **Punto de medición:** API/aplicación y registro de eventos.
- **Ventana:** 30 días móviles.
- **Presupuesto:** hasta 1 % de intentos válidos pueden fallar.
- **Alertas:** 0.5 % y 1 % de intentos fallidos.
- **Herramienta:** CloudWatch Logs y métrica personalizada de la aplicación.

## Política de presupuesto de error

- **Al 50 %:** revisar logs, métricas e incidentes recientes; identificar la causa y priorizar correcciones antes de nuevos cambios de riesgo.
- **Al 100 %:** congelar nuevas funcionalidades y permitir únicamente correcciones, cambios de seguridad y mejoras de confiabilidad hasta recuperar margen en la ventana móvil.
- **Responsable:** Israel Márquez Cárdenas, en coordinación con el equipo.

Fórmula para disponibilidad:

`Presupuesto = (1 - SLO) × 43 200`

Documento completo:

[`docs/slo.md`](../../docs/slo.md)

---

# 5. B4 — Cláusula SLA del equipo

- **Compromiso mensual:** [PENDIENTE] %
- **Definición de indisponibilidad:** [PENDIENTE]

### Exclusiones

1. [PENDIENTE]
2. [PENDIENTE]
3. [PENDIENTE]
4. [PENDIENTE]

### Créditos

| Disponibilidad | Crédito |
|---|---:|
| [PENDIENTE] | [PENDIENTE] % |
| [PENDIENTE] | [PENDIENTE] % |
| [PENDIENTE] | [PENDIENTE] % |

- **Procedimiento de reclamación:** [PENDIENTE]
- **Relación SLO/SLA:** [PENDIENTE]

---

# 6. Preguntas de análisis

## Pregunta 1

[PENDIENTE]

## Pregunta 2 — Israel Márquez Cárdenas

Caída de 8 horas:

`8 × 60 = 480 min`

Disponibilidad:

`(43 200 - 480) / 43 200 × 100 = [PENDIENTE] %`

- **Crédito aplicable:** [PENDIENTE] %
- **Costo mensual elegible:** [PENDIENTE] USD
- **Crédito obtenido:** [PENDIENTE] USD
- **Pérdida estimada del negocio:** [PENDIENTE] USD

**Respuesta:**  
[PENDIENTE]

## Pregunta 3

[PENDIENTE]

## Pregunta 4

[PENDIENTE]

## Pregunta 5

- **Incidente:** [PENDIENTE]
- **Fecha:** [PENDIENTE]
- **Duración:** [PENDIENTE]
- **Causa:** [PENDIENTE]
- **¿Lo cubre el SLA?:** [PENDIENTE]
- **SLI que lo detectaría:** [PENDIENTE]
- **Presupuesto consumido:** [PENDIENTE]

**Respuesta:**  
[PENDIENTE]

## Pregunta 6 — Israel Márquez Cárdenas

[PENDIENTE]

---

# 7. Conclusiones

## Israel Márquez Cárdenas

[PENDIENTE]

## Salvador

[PENDIENTE]

## Esaul

[PENDIENTE]

## Conclusión general

[PENDIENTE]

---

# 8. Referencias

- Amazon Web Services. *Amazon Compute Service Level Agreement*. https://aws.amazon.com/compute/sla/. Consulta: 20/09/2026.
- [SLA de Salvador]
- [SLA de Esaul]
- Beyer, B. et al. *Site Reliability Engineering — Service Level Objectives*.
- [Otras referencias]

---

# 9. Uso de IA

Se utilizó ChatGPT como apoyo para comprender SLA, SLI, SLO y presupuesto de error, organizar el reporte y revisar cálculos y redacción.

Las cifras de SLA fueron verificadas con las fuentes oficiales.

---

# 10. Tabla de contribuciones

| Integrante | Contribución |
|---|---|
| Israel Márquez Cárdenas | B1: SLA de Amazon EC2. B3: SLIs, SLOs y presupuesto de error. Preguntas 2 y 6. |
| Salvador | [PENDIENTE] |
| Esaul | [PENDIENTE] |

---

# 11. Evidencias

- `evidencias/P02/P02_B1_ec2_israel.png`
- `evidencias/P02/P02_B1_[servicio]_salvador.png`
- `evidencias/P02/P02_B1_[servicio]_esaul.png`
- `docs/arquitectura/arquitectura_p02.png`
- `docs/slo.md`
- `bitacora/2026-09-15.md`