# Objetivos de Nivel de Servicio (SLOs) del Proyecto

## Información General

- **Proyecto:** Módulo de Soporte con Mesas de Ayuda para Sistema de Navegador Seguro
- **Equipo:** 8 (Sistemas Distribuidos — 7CV1)
- **Integrantes:**
  - Israel Márquez Cárdenas (2022300395)
  - Esaul Tellez de la Cruz (2023630692)
  - Salvador Sandoval Garibay (2022630151)
- **Proveedor de Infraestructura:** Amazon Web Services (AWS)
- **Ventana de Evaluación:** 30 días móviles (43,200 minutos)
- **Disponibilidad Compuesta de la Infraestructura (B2):** 99.8301 % (con redundancia Multi-AZ)
- **Fecha de Establecimiento:** 15 de septiembre de 2026

---

## SLO 1 — Disponibilidad de la API del Módulo de Soporte

- **Servicio:** `modulo-soporte-api` (Endpoint público `/api/v1/soporte` detrás del Application Load Balancer)
- **SLI (definición):** Proporción de peticiones HTTP válidas respondidas sin códigos de error del servidor 5xx.
- **SLI (implementación):** 
  $$\text{SLI} = \frac{\text{RequestCount} - \text{HTTPCode\_Target\_5XX\_Count}}{\text{RequestCount}} \times 100$$
  Medido en el balanceador de carga de aplicaciones (Amazon CloudWatch, métricas `AWS/ApplicationELB`). Se excluyen verificaciones de salud internas (*health checks* en `/health`) y errores `4xx` imputables al cliente.
- **Ventana:** 30 días móviles (ventana rodante de 43,200 minutos).
- **Objetivo (SLO):** **99.50 %**
  - *Validación arquitectónica:* El objetivo es inferior a la disponibilidad compuesta con redundancia de la infraestructura (99.8301 %), dejando un margen de 142.59 minutos para absorber despliegues, reinicios y fallas internas de software.
- **Presupuesto de error:** 
  $$\text{Presupuesto} = (1 - 0.9950) \times 43\,200\text{ min} = \mathbf{216.00\text{ minutos por ventana}}$$
- **Alertas:**
  - *Aviso preventivo (P2):* Al consumir el 50 % del presupuesto de error (108 minutos consumidos).
  - *Alerta crítica (P1):* Al consumir el 100 % del presupuesto de error (216 minutos consumidos).
- **Política de presupuesto de error:** Al agotarse el presupuesto (100 % consumido), se declaran congeladas de forma inmediata las publicaciones de nuevas funcionalidades (*Feature Freeze*). Todo el equipo de desarrollo se aboca exclusivamente a tareas de resiliencia, parches de estabilidad, análisis de logs y mitigación de la causa raíz hasta recuperar al menos el 25 % del margen de error (consumo $\le 75\%$) en la ventana móvil.
- **Verificación externa:** Monitor sintético externo (UptimeRobot / Better Stack) ejecutando solicitudes HTTP `GET /health` cada 5 minutos desde múltiples ubicaciones geográficas.
- **Responsable:** Israel Márquez Cárdenas / Salvador Sandoval Garibay
- **Revisión:** Cada cierre de parcial y tras incidentes de severidad P1.

```yaml
apiVersion: openslo/v1
kind: SLO
metadata:
  name: api-disponibilidad
  displayName: Disponibilidad de la API del Módulo de Soporte
spec:
  description: Proporción de peticiones válidas respondidas sin error 5xx en el balanceador
  service: modulo-soporte-api
  indicator:
    metadata:
      name: peticiones-exitosas-ratio
    spec:
      ratioMetric:
        counter: true
        good:
          metricSource:
            type: CloudWatch
            spec:
              query: SUM(RequestCount) - SUM(HTTPCode_Target_5XX_Count)
        total:
          metricSource:
            type: CloudWatch
            spec:
              query: SUM(RequestCount)
  timeWindow:
    - duration: 30d
      isRolling: true
  budgetingMethod: Occurrences
  objectives:
    - displayName: Objetivo mensual de disponibilidad
      target: 0.995
```

---

## SLO 2 — Latencia de Respuesta de la API

- **Servicio:** `modulo-soporte-api` (Interacciones y consultas de tickets vía REST API)
- **SLI (definición):** Proporción de peticiones HTTP válidas procesadas y devueltas en un tiempo total de respuesta menor o igual a 500 ms.
- **SLI (implementación):** 
  $$\text{SLI} = \frac{\text{Count}(\text{TargetResponseTime} \le 0.500\,\text{s})}{\text{RequestCount}} \times 100$$
  Medido en Amazon CloudWatch utilizando métricas del Application Load Balancer (`TargetResponseTime` percentil 95).
- **Ventana:** 30 días móviles.
- **Objetivo (SLO):** **≥ 95.00 %** de las peticiones válidas en $\le 500\text{ ms}$ (Percentil 95 $\le 500\text{ ms}$).
- **Presupuesto de error:** Hasta un **5.00 %** de peticiones con latencia degradada (> 500 ms) permitido durante la ventana de 30 días.
- **Alertas:**
  - *Alerta preventiva (P2):* Cuando el 2.50 % del volumen total de peticiones haya superado el umbral de 500 ms.
  - *Alerta crítica (P1):* Cuando el 5.00 % de las peticiones excedan 500 ms.
- **Política de presupuesto de error:** Al sobrepasar el umbral crítico, se activan réplicas de lectura en Amazon RDS, se ajustan índices en PostgreSQL y se habilitan cachés en memoria para consultas frecuentes de tickets.
- **Responsable:** Esaul Tellez de la Cruz
- **Revisión:** Quincenal.

```yaml
apiVersion: openslo/v1
kind: SLO
metadata:
  name: api-latencia-p95
  displayName: Latencia Percentil 95 de la API
spec:
  description: Proporción de peticiones válidas procesadas en 500 ms o menos
  service: modulo-soporte-api
  indicator:
    metadata:
      name: peticiones-rapidas-ratio
    spec:
      thresholdMetric:
        metricSource:
          type: CloudWatch
          spec:
            query: TargetResponseTime
        operator: lte
        value: 0.500
  timeWindow:
    - duration: 30d
      isRolling: true
  budgetingMethod: Occurrences
  objectives:
    - displayName: Objetivo mensual de latencia p95
      target: 0.95
```

---

## SLO 3 — Creación Exitosa de Tickets (Métrica de Dominio)

- **Servicio:** `modulo-soporte-tickets` (Gestión transaccional del ciclo de vida de tickets)
- **SLI (definición):** Proporción de intentos válidos de creación de ticket que finalizan con persistencia exitosa en PostgreSQL, registro de evidencia en Amazon S3 y emisión del identificador único de ticket.
- **SLI (implementación):** 
  $$\text{SLI} = \frac{\text{TicketsPersistidosExitosamente}}{\text{IntentosValidosCreacionTicket}} \times 100$$
  Medido mediante métricas de aplicación estructuradas (*Embedded Metric Format* - EMF) emitidas a Amazon CloudWatch Logs en el controlador de tickets.
- **Ventana:** 30 días móviles.
- **Objetivo (SLO):** **≥ 99.00 %**
- **Presupuesto de error:** Hasta **1.00 %** de intentos válidos de creación pueden presentar fallo en el proceso transaccional.
- **Alertas:**
  - *Alerta preventiva:* Tasa de error transaccional $\ge 0.50\%$.
  - *Alerta crítica:* Tasa de error transaccional $\ge 1.00\%$.
- **Política de presupuesto de error:** Al alcanzar la alerta crítica, se activa de forma automática una cola de reintentos asíncrona (Amazon SQS) para desacoplar la ingesta de tickets de la persistencia directa en base de datos.
- **Responsable:** Salvador Sandoval Garibay / Israel Márquez Cárdenas
- **Revisión:** Cada cierre de sprint o parcial.

```yaml
apiVersion: openslo/v1
kind: SLO
metadata:
  name: tickets-creacion-exitosa
  displayName: Creación Exitosa de Tickets de Soporte
spec:
  description: Proporción de transacciones de creación de ticket registradas exitosamente
  service: modulo-soporte-tickets
  indicator:
    metadata:
      name: tickets-creados-ratio
    spec:
      ratioMetric:
        counter: true
        good:
          metricSource:
            type: CloudWatch
            spec:
              query: SUM(TicketCreationSuccessCount)
        total:
          metricSource:
            type: CloudWatch
            spec:
              query: SUM(TicketCreationAttemptCount)
  timeWindow:
    - duration: 30d
      isRolling: true
  budgetingMethod: Occurrences
  objectives:
    - displayName: Objetivo de persistencia de tickets
      target: 0.990
```

---

## Matriz Resumen de Telemetría y Monitoreo

| SLO | Métrica Principal | Fuente de Datos | Granularidad | Herramienta |
|---|---|---|---|---|
| **1. Disponibilidad** | `HTTPCode_Target_5XX_Count` vs `RequestCount` | ALB CloudWatch Metrics | 1 minuto | Amazon CloudWatch / UptimeRobot |
| **2. Latencia (p95)** | `TargetResponseTime` (Percentil 95) | ALB CloudWatch Metrics | 1 minuto | Amazon CloudWatch |
| **3. Creación de Tickets** | `TicketCreationSuccess` vs `TicketCreationAttempt` | CloudWatch Logs EMF | En tiempo real | Amazon CloudWatch Logs Insights |
