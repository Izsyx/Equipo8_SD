# Práctica 2 — Acuerdo de nivel de servicio: análisis de un SLA real y diseño de los SLOs del proyecto

## Datos del equipo

- **Equipo:** 8
- **Integrantes:**
  - Israel Márquez Cárdenas (2022300395)
  - Esaul Tellez de la Cruz (2023630692)
  - Salvador Sandoval Garibay (2022630151)
- **Materia:** Sistemas Distribuidos
- **Grupo:** 7CV1 — Semestre 27/1
- **Profesor:** MBA. Rodrigo Ojeda Santillán
- **Proveedor seleccionado:** AWS (Amazon Web Services)
- **Proyecto:** Módulo de Soporte con Mesas de Ayuda para Sistema de Navegador Seguro

---

# 1. Introducción

En la ingeniería de confiabilidad de sitios (SRE) y la administración de sistemas distribuidos en la nube, la disponibilidad no es una estimación subjetiva sino una métrica formal basada en contratos y telemetría. Este reporte presenta el análisis riguroso de los Acuerdos de Nivel de Servicio (SLA) de los componentes de infraestructura en la nube (cómputo, almacenamiento de objetos y bases de datos gestionadas), el modelado matemático de la disponibilidad compuesta del sistema en serie y con redundancia, la definición formal de los Indicadores de Nivel de Servicio (SLI) y Objetivos de Nivel de Servicio (SLO), el establecimiento del presupuesto de error con sus políticas de gobernanza, y la redacción del contrato de SLA externo que el equipo ofrece a los usuarios del **Módulo de Soporte con Mesas de Ayuda para Sistema de Navegador Seguro**.

---

# 2. B1 — Anatomía de un SLA real

## Tabla 1. Anatomía del SLA

| Integrante | Servicio y URL (fecha) | Compromiso por configuración | Definición de inactividad | Exclusiones | Créditos | Reclamación | Min/mes permitidos |
|---|---|---|---|---|---|---|---|
| **Israel Márquez Cárdenas** | Amazon EC2 — https://aws.amazon.com/compute/sla/ — consulta: 20/09/2026 | Instancia individual: 99.5 %. Nivel regional (≥2 AZ): 99.99 %. | Individual: la instancia pierde conectividad externa. Regional: todas las instancias en ≥2 AZ pierden simultáneamente conectividad externa. | Factores fuera del control de AWS; acciones del cliente; equipo/software del cliente; suspensión del servicio. | < SLA y ≥99.0 %: 10 %. <99.0 % y ≥95.0 %: 30 %. <95.0 %: 100 %. | Caso en AWS Support Center con fechas, horas, región/AZ, IDs y logs. | 99.5 % → 216 min. 99.99 % → 4.32 min. |
| **Esaul Tellez de la Cruz** | Amazon S3 — https://aws.amazon.com/s3/sla/ — consulta: 20/09/2026 | S3 Standard / Express: 99.9 %. S3 Intelligent-Tiering / Standard-IA: 99.0 %. S3 Express One Zone (AZ): 99.95 %. | Tasa de error (Error Rate) > 0 % en intervalos de 5 min (errores InternalError o ServiceUnavailable / peticiones totales). | Factores fuera del control de AWS (fuerza mayor, internet fuera de demarcación); actos/omisiones del cliente; software/equipo del cliente; suspensión por contrato; cuotas excedidas. | <99.9 % y ≥99.0 %: 10 %. <99.0 % y ≥95.0 %: 25 %. <95.0 %: 100 %. | Caso en AWS Support Center con asunto "SLA Credit Request", ciclo de facturación, región, fechas/horas y logs de peticiones antes del 2.° ciclo. | 99.9 % → 43.2 min. 99.0 % → 432 min. |
| **Salvador Sandoval Garibay** | Amazon RDS — https://aws.amazon.com/rds/sla/ — consulta: 20/09/2026 | Multi-AZ DB Instance/Cluster: 99.95 %. Single-DB Instance: 99.5 %. | Todos los intentos de conexión a la instancia de BD fallan durante un intervalo continuo de 1 minuto ("Unavailable"). | Factores fuera del control razonable; instancias Micro DB (limitación de CPU/RAM); violación de guías de usuario de RDS; fallas del motor subyacente; IOPS insuficientes. | Multi-AZ / Single-AZ: < SLA y ≥99.0 %: 10 %. <99.0 % y ≥95.0 %: 25 %. <95.0 %: 100 %. | Caso en AWS Support Center con asunto "Amazon RDS SLA Credit Request", fechas/horas, DB Instance IDs y logs antes del 2.° ciclo. | 99.5 % → 216 min. 99.95 % → 21.6 min. |

---

## 2.1 Análisis individual — Israel Márquez Cárdenas (Amazon EC2)

- **Proveedor:** AWS (Amazon Web Services)
- **Servicio:** Amazon Elastic Compute Cloud (Amazon EC2)
- **SLA oficial:** https://aws.amazon.com/compute/sla/
- **Última actualización:** 25 de mayo de 2022
- **Fecha de consulta:** 20 de septiembre de 2026
- **Evidencia:** `evidencias/P02/P02_B1_ec2_Israel.png`

### Compromiso
- Instancia individual: **99.5 %**
- Configuración regional con instancias en ≥2 Zonas de Disponibilidad (Multi-AZ): **99.99 %**

Una sola máquina virtual carece de tolerancia a fallas de hardware en el host físico, mientras que el despliegue Multi-AZ garantiza redundancia en zonas aisladas.

### Definición de indisponibilidad
AWS define la inactividad de una instancia individual cuando esta experimenta una pérdida total de conectividad externa a la red. A nivel regional, ocurre cuando todas las instancias distribuidas en al menos dos zonas pierden conectividad de manera simultánea. Cualquier fallo originado por el sistema operativo huésped, la aplicación, configuraciones erróneas del firewall (Security Groups) o fallas de software no se consideran indisponibilidad para AWS.

### Exclusiones
1. Factores fuera del control razonable de AWS (fuerza mayor, desastres, fallas de proveedores de red de telecomunicaciones).
2. Acciones u omisiones voluntarias o involuntarias del cliente.
3. Equipo, software o configuraciones suministradas por el cliente o terceros.
4. Suspensión o terminación del servicio derivada del incumplimiento del contrato de cliente de AWS.

### Escalones de crédito
| Disponibilidad mensual | Crédito otorgado |
|---|---:|
| < 99.99 % y ≥ 99.0 % (Multi-AZ) / < 99.5 % y ≥ 99.0 % (Individual) | 10 % |
| < 99.0 % y ≥ 95.0 % | 30 % |
| < 95.0 % | 100 % |

### Procedimiento de reclamación
El cliente debe abrir un caso de soporte técnico en AWS Support Center antes del cierre del segundo ciclo de facturación posterior al incidente, indicando:
1. El asunto formal de reclamación de crédito de SLA.
2. Ciclo de facturación, región, fechas y horas exactas de cada corte.
3. Identificadores de las instancias y registros de logs que evidencien la falta de conectividad.

### Minutos permitidos en 30 días (43,200 min)
- **Instancia individual (99.5 %):** `(1 - 0.995) × 43 200 = 216 minutos/mes` (3.6 horas).
- **Instancias Multi-AZ (99.99 %):** `(1 - 0.9999) × 43 200 = 4.32 minutos/mes`.

### Crédito a 99.0 % sobre factura hipotética de 100 USD
Al registrar 99.0 % de disponibilidad mensual, aplica el escalón del **10 %**:
$$\text{Crédito} = 100\text{ USD} \times 0.10 = \mathbf{10.00\text{ USD}}$$

### Región de México (Querétaro `mx-central-1`)
AWS no publica una reducción porcentual para su región de México en el contrato de EC2; aplican los mismos compromisos de 99.5 % (individual) y 99.99 % (Multi-AZ) vigentes globalmente.

---

## 2.2 Análisis individual — Esaul Tellez de la Cruz (Amazon S3)

- **Proveedor:** AWS (Amazon Web Services)
- **Servicio:** Amazon Simple Storage Service (Amazon S3)
- **SLA oficial:** https://aws.amazon.com/s3/sla/
- **Última actualización:** 28 de noviembre de 2023
- **Fecha de consulta:** 20 de septiembre de 2026
- **Evidencia:** `evidencias/P02/P02_B1_s3_esaul.png`

### Compromiso
- **S3 Standard, S3 Express One Zone, S3 Glacier Flexible Retrieval y S3 Glacier Deep Archive:** **99.9 %**
- **S3 Intelligent-Tiering, S3 Standard-Infrequent Access (Standard-IA), S3 One Zone-IA y S3 Glacier Instant Retrieval:** **99.0 %**
- **S3 Express One Zone (compromiso a nivel de AZ individual):** **99.95 %**

Para el almacenamiento de archivos adjuntos y evidencias del Módulo de Soporte se utiliza **S3 Standard**, cuyo compromiso contractual es de **99.9 % de disponibilidad mensual**.

### Definición de indisponibilidad
AWS mide la inactividad de Amazon S3 mediante la **Tasa de Error (Error Rate)** evaluada en **intervalos de 5 minutos**. 
- La tasa de error se define como la cantidad total de errores internos del servidor devueltos por Amazon S3 (códigos `InternalError` o `ServiceUnavailable`) dividida entre el número total de solicitudes válidas de ese tipo durante dicho intervalo de 5 minutos.
- Si no se realizan solicitudes en un intervalo de 5 minutos determinado, se asume un `Error Rate = 0 %`.
- El **Porcentaje de Tiempo de Actividad Mensual (Monthly Uptime Percentage)** se calcula restando de 100 % el promedio de las tasas de error de todos los intervalos de 5 minutos del ciclo de facturación mensual.
- *Consecuencia operativa:* Si una aplicación realiza solicitudes mal configuradas, peticiones 4xx o no puede comunicarse con S3 por caídas de DNS locales del cliente, AWS no lo contabiliza como inactividad.

### Exclusiones
1. **Factores de fuerza mayor:** Circunstancias fuera del control razonable de AWS, incluyendo actos gubernamentales, conflictos bélicos, desastres naturales o problemas de acceso a Internet fuera del punto de demarcación de red de S3.
2. **Acciones u omisiones del cliente o terceros:** Mala configuración de políticas de bucket, borrado accidental de datos o fallos al responder alertas.
3. **Equipos y software del cliente:** Incompatibilidades en SDKs de cliente, firewalls locales, proxies o dependencias de terceros.
4. **Suspensión contractual:** Inactividad derivada de la suspensión justificada de la cuenta de AWS por violaciones a los Términos de Servicio o falta de pago.
5. **Superación de cuotas operativas:** Errores provocados por exceder las tasas máximas de transacciones por segundo (TPS) o límites de peticiones sin haber configurado prefijos de partición adecuados.

### Escalones de crédito (S3 Standard)
| Porcentaje mensual de tiempo de actividad | Porcentaje de crédito de servicio |
|---|---:|
| < 99.9 % y ≥ 99.0 % | 10 % |
| < 99.0 % y ≥ 95.0 % | 25 % |
| < 95.0 % | 100 % |

### Procedimiento de reclamación
Para hacer válido el crédito de servicio, el cliente debe:
1. Abrir un caso formal en **AWS Support Center**.
2. Incluir en la línea de asunto las palabras exactas: `SLA Credit Request`.
3. Indicar el ciclo de facturación afectado, la región de AWS y los nombres de los buckets de S3.
4. Adjuntar las fechas y horas específicas de cada incidente con tasa de error superior a cero, acompañadas de los **logs de solicitudes del cliente** que documenten y corroboren los errores internos `5xx`.
5. Enviar la solicitud antes de que finalice el **segundo ciclo de facturación** posterior a la ocurrencia del incidente.
6. El crédito se emite únicamente si el monto resultante es mayor a **$1.00 USD**, siendo el **remedio único y exclusivo** (*sole and exclusive remedy*) aplicable únicamente contra futuras facturas de Amazon S3.

### Minutos de inactividad permitidos en 30 días (43,200 min)
- **S3 Standard (99.9 %):**
  $$\text{Downtime} = (1 - 0.999) \times 43\,200\text{ min} = \mathbf{43.20\text{ minutos/mes}}\text{ (0.72 horas)}$$
- **S3 Standard-IA / Intelligent-Tiering (99.0 %):**
  $$\text{Downtime} = (1 - 0.990) \times 43\,200\text{ min} = \mathbf{432.00\text{ minutos/mes}}\text{ (7.20 horas)}$$

### Crédito a 99.0 % sobre factura hipotética de 100 USD
Si la disponibilidad mensual de S3 Standard cae a 99.0 %, se sitúa en el primer escalón de compensación (10 %):
$$\text{Crédito} = 100\text{ USD} \times 0.10 = \mathbf{10.00\text{ USD}}$$

### Región de México (Querétaro `mx-central-1`)
AWS no aplica compromisos diferenciados para la región de Querétaro (`mx-central-1`). El SLA de Amazon S3 Standard se mantiene en 99.9 % globalmente, siempre que el servicio se encuentre formalmente habilitado en la región.

---

## 2.3 Análisis individual — Salvador Sandoval Garibay (Amazon RDS)

- **Proveedor:** AWS (Amazon Web Services)
- **Servicio:** Amazon Relational Database Service (Amazon RDS PostgreSQL)
- **SLA oficial:** https://aws.amazon.com/rds/sla/
- **Última actualización:** 22 de enero de 2024
- **Fecha de consulta:** 20 de septiembre de 2026
- **Evidencia:** `evidencias/P02/P02_B1_rds_salvador.png`

### Compromiso
- **Despliegue Multi-AZ (Multi-AZ DB Instance / Multi-AZ DB Cluster):** **99.95 %**
- **Instancia individual (Single-DB Instance):** **99.5 %**

### Definición de indisponibilidad
AWS considera que una instancia de base de datos RDS se encuentra "Indisponible" (*Unavailable*) cuando todas las solicitudes de conexión dirigidas a la instancia en ejecución fallan de manera continua durante un **intervalo de 1 minuto**. El porcentaje de disponibilidad mensual se calcula restando a 100 % el porcentaje de intervalos de 1 minuto en los que la base de datos estuvo indisponible.

### Exclusiones
1. Factores fuera del control razonable de AWS o problemas de red fuera del punto de demarcación de RDS.
2. Acciones voluntarias o involuntarias del usuario (como detener la base de datos o modificar parámetros de red).
3. **Instancias de clase Micro:** Instancias de tipo `db.t2.micro`, `db.t3.micro` o `db.t4g.micro` cuyas limitaciones inherentes de CPU y memoria provocan fallas por saturación de recursos.
4. Omisión de las guías operativas básicas de Amazon RDS (sobrecargar la base de datos hasta volverla inoperable o crear miles de tablas que incrementen drásticamente el tiempo de recuperación *crash recovery*).
5. Fallas internas causadas por bugs del motor de base de datos subyacente (PostgreSQL/MySQL).
6. Tiempos de recuperación prolongados derivados de aprovisionar capacidad de I/O (IOPS) insuficiente para la carga de trabajo.

### Escalones de crédito
| Disponibilidad mensual | Crédito otorgado |
|---|---:|
| < 99.95 % y ≥ 99.0 % (Multi-AZ) / < 99.5 % y ≥ 99.0 % (Single-AZ) | 10 % |
| < 99.0 % y ≥ 95.0 % | 25 % |
| < 95.0 % | 100 % |

### Procedimiento de reclamación
Se debe ingresar un caso formal en AWS Support Center antes de finalizar el segundo ciclo de facturación posterior al incidente, indicando en el asunto `Amazon RDS SLA Credit Request – Multi-AZ Claim` o `Single-DB Claim`, identificadores de las instancias afectadas, timestamps de cada corte y logs de conexión que demuestren los intentos fallidos durante los intervalos de 1 minuto.

### Minutos permitidos en 30 días (43,200 min)
- **Single-AZ (99.5 %):** `(1 - 0.995) × 43 200 = 216 minutos/mes` (3.6 horas).
- **Multi-AZ (99.95 %):** `(1 - 0.9995) × 43 200 = 21.6 minutos/mes`.

### Crédito a 99.0 % sobre factura hipotética de 100 USD
$$\text{Crédito} = 100\text{ USD} \times 0.10 = \mathbf{10.00\text{ USD}}$$

### Región de México (Querétaro `mx-central-1`)
AWS mantiene el estándar contractual de 99.5 % (Single-AZ) y 99.95 % (Multi-AZ) en Querétaro sin variaciones regionales.

---

# 3. B2 — Disponibilidad compuesta del proyecto

## Diagrama de arquitectura de dependencias

```
+----------------+      +-------------------+      +----------------------+
|  AWS Route 53  | ---> | Application Load  | ---> |   Amazon EC2 Linux   |
|   (DNS 100%)   |      |  Balancer (ALB)   |      | (Módulo de Soporte)  |
+----------------+      |     (99.99%)      |      +----------------------+
                        +-------------------+                 |
                                                              v
+-----------------------+      +--------------------------------------+
|       Amazon S3       | <--- | Amazon RDS PostgreSQL (Base de Datos)|
| (Objetos / Adjuntos)  |      +--------------------------------------+
|        (99.9%)        |
+-----------------------+
```

Cadena de dependencias en serie:
$$\text{DNS} \longrightarrow \text{Balanceador (ALB)} \longrightarrow \text{Cómputo (EC2)} \longrightarrow \text{Base de Datos (RDS)} \longrightarrow \text{Objetos (S3)}$$

## Tabla 2. Disponibilidad compuesta del proyecto

| Componente | SLA individual | SLA redundante | En serie o paralelo | Costo extra de redundancia (USD/mes) |
|---|---:|---:|---|---:|
| **DNS (Route 53)** | 100.00 % | 100.00 % | Serie | $0.00 USD (incluido en configuración base) |
| **Balanceador (ALB)** | 99.99 % | 99.99 % | Serie | $0.00 USD (gestionado por AWS de forma Multi-AZ nativa) |
| **Cómputo (EC2 `t4g.small`)** | 99.50 % | 99.99 % | Serie (Paralelo entre instancias Multi-AZ) | +$16.00 USD (segunda VM en zona B) |
| **Base de datos (RDS `db.t4g.micro`)** | 99.50 % | 99.95 % | Serie (Réplica sincrónica Multi-AZ) | +$14.83 USD (despliegue Multi-AZ) |
| **Objetos (Amazon S3 Standard)** | 99.90 % | 99.90 % | Serie (Almacenamiento Multi-AZ nativo en ≥3 AZ) | $0.00 USD (integrado en el servicio) |
| **Compuesto sin redundancia** | **98.8936 %** | — | — | — |
| **Compuesto con redundancia** | — | **99.8301 %** | — | **+$30.83 USD/mes** |
| **Minutos al mes sin redundancia** | **477.96 min** (~7.97 h) | — | — | — |
| **Minutos al mes con redundancia** | — | **73.41 min** (~1.22 h) | — | — |

---

### Fórmulas de cálculo

1. **Disponibilidad compuesta en serie ($A_{\text{serie}}$):**
   $$A_{\text{serie}} = a_1 \times a_2 \times a_3 \times a_4 \times a_5$$
2. **Disponibilidad con redundancia en paralelo ($A_{\text{paralelo}}$):**
   $$A_{\text{paralelo}} = 1 - (1 - a_1) \times (1 - a_2)$$

### Memoria de cálculo detallada

- **Sin redundancia (Instancias individuales):**
  $$A_{\text{sin red}} = 1.00 \times 0.9999 \times 0.995 \times 0.995 \times 0.999 = 0.98893605 \approx \mathbf{98.8936\%}$$
  $$\text{Downtime}_{\text{sin red}} = (1 - 0.98893605) \times 43\,200\text{ min} = \mathbf{477.96\text{ minutos/mes}}\text{ (~7 horas 58 min)}$$

- **Con redundancia (Multi-AZ en Cómputo y Base de Datos):**
  $$A_{\text{con red}} = 1.00 \times 0.9999 \times 0.9999 \times 0.9995 \times 0.999 = 0.99830149 \approx \mathbf{99.8301\%}$$
  $$\text{Downtime}_{\text{con red}} = (1 - 0.99830149) \times 43\,200\text{ min} = \mathbf{73.41\text{ minutos/mes}}\text{ (~1 hora 13 min)}$$

### Análisis del eslabón más débil
- **Eslabón más débil sin redundancia:** La capa de **Cómputo (EC2)** y la capa de **Base de Datos (RDS Single-AZ)**, ambas con un compromiso contractual individual de apenas **99.50 %** (permitiendo cada una hasta 216 min/mes de inactividad).
- **Costo de reforzamiento:**
  - Habilitar Auto Scaling con una segunda instancia EC2 en zona secundaria: **+$16.00 USD/mes**.
  - Habilitar despliegue Multi-AZ en RDS PostgreSQL: **+$14.83 USD/mes**.
  - **Costo total de reforzamiento:** **+$30.83 USD/mes**, logrando reducir el tiempo de inactividad de casi 8 horas a solo 1 hora y 13 minutos al mes.

---

# 4. B3 — SLIs, SLOs y presupuesto de error

**Responsables:** Salvador Sandoval Garibay e Israel Márquez Cárdenas

Para el **Módulo de Soporte con Mesas de Ayuda**, se establecieron tres SLOs principales alineados con las cuatro señales doradas de SRE (Google SRE Book): disponibilidad general, latencia en percentil 95 y una métrica de dominio funcional (creación de tickets).

## Tabla 3. SLOs del proyecto

| SLO | SLI (buenos ÷ válidos) | Punto de medición | Ventana | Objetivo | Presupuesto (min) | Alertas 50 % / 100 % | Herramienta |
|---|---|---|---|---:|---|---|---|
| **Disponibilidad** | Peticiones HTTP válidas sin error 5xx ÷ Peticiones válidas totales | Application Load Balancer (ALB) | 30 días móviles | **99.50 %** | **216 min** | 108 min / 216 min consumidos | Amazon CloudWatch + UptimeRobot |
| **Latencia p95** | Peticiones válidas con tiempo de respuesta ≤ 500 ms ÷ Peticiones válidas totales | Application Load Balancer (ALB) | 30 días móviles | **≥ 95.00 %** (p95 ≤ 500 ms) | **5.00 %** peticiones lentas | 2.50 % / 5.00 % de peticiones degradadas | Amazon CloudWatch (`TargetResponseTime`) |
| **De Dominio (Creación de Tickets)** | Intentos válidos con ticket creado y persistido con éxito ÷ Intentos válidos totales | API / Backend de Tickets | 30 días móviles | **≥ 99.00 %** | **1.00 %** tickets fallidos | 0.50 % / 1.00 % de fallas en creación | CloudWatch Logs + Métrica Personalizada EMF |

---

## Especificación detallada de los SLOs

### SLO 1 — Disponibilidad del Servicio
- **Definición del SLI:** Proporción de solicitudes HTTP entrantes procesadas exitosamente sin errores 5xx del servidor.
  $$\text{SLI} = \frac{\text{RequestCount} - \text{HTTPCode\_Target\_5XX\_Count}}{\text{RequestCount}} \times 100$$
- **Eventos válidos:** Peticiones HTTP reales dirigidas a los endpoints del Módulo de Soporte. Se excluyen verificaciones de salud internas (*health checks* del ALB en `/health`) y errores `4xx` provocados por el cliente.
- **Eventos buenos:** Peticiones que reciben respuestas HTTP con códigos de estado `2xx` o `3xx`.
- **Punto de medición:** Métricas agregadas del Application Load Balancer en Amazon CloudWatch.
- **Ventana temporal:** 30 días móviles (43,200 minutos).
- **Objetivo (SLO):** **99.50 %** (Permite 216 minutos de presupuesto de error).
  - *Comprobación de viabilidad:* El objetivo de 99.50 % es inferior a la disponibilidad compuesta con redundancia de la infraestructura (99.8301 %), dejando un margen holgado de 142.59 minutos para absorber despliegues fallidos, reinicios de procesos y errores de aplicación propios del equipo.

### SLO 2 — Latencia de Respuesta (p95)
- **Definición del SLI:** Proporción de solicitudes procesadas en un tiempo menor o igual a 500 ms.
- **Eventos válidos:** Todas las solicitudes exitosas procesadas por el backend del módulo.
- **Eventos buenos:** Solicitudes cuya latencia total de respuesta es $\le 500\text{ ms}$.
- **Objetivo (SLO):** **95.00 %** de las peticiones en $\le 500\text{ ms}$ (Percentil 95 $\le 500\text{ ms}$).
- **Presupuesto de error:** 5 % del volumen total de peticiones puede superar el umbral de 500 ms sin violar el SLO.

### SLO 3 — Confiabilidad en la Creación de Tickets (Métrica de Dominio)
- **Definición del SLI:** Proporción de operaciones de creación de tickets que finalizan con almacenamiento exitoso en PostgreSQL y confirmación con ID único devuelto al usuario.
- **Eventos válidos:** Peticiones autenticadas POST `/api/tickets` con payload válido.
- **Eventos buenos:** Tickets persistidos con confirmación de base de datos (`201 Created`).
- **Objetivo (SLO):** **99.00 %**.
- **Presupuesto de error:** Hasta 1.00 % de intentos válidos de creación pueden fallar.

---

## Política de Gobernanza del Presupuesto de Error

1. **Al consumir el 50 % del presupuesto de error (108 minutos en Disponibilidad):**
   - Se activa la alerta preventiva de severidad media (P2).
   - El equipo técnico realiza un análisis de causa raíz sobre logs y trazas de CloudWatch.
   - Se restringen despliegues de alto impacto arquitectónico durante horarios pico.
2. **Al consumir el 100 % del presupuesto de error (216 minutos consumidos):**
   - Se activa la alerta crítica (P1) y entra en vigor el **Congelamiento de Despliegues de Funcionalidades (*Feature Freeze*)**.
   - Quedan prohibidos los lanzamientos de nuevas características comerciales o cambios de diseño.
   - La totalidad de la capacidad de ingeniería del sprint se enfoca en resiliencia, parches de seguridad, optimización de queries y estabilidad del sistema.
3. **Responsables de la decisión:** Israel Márquez Cárdenas y Salvador Sandoval Garibay, en acuerdo con Esaul Tellez de la Cruz.
4. **Criterio de recuperación:** Se levanta el congelamiento únicamente cuando el consumo del presupuesto de error descienda por debajo del 75 % (recuperación de al menos el 25 % del margen disponible) dentro de la ventana móvil de 30 días.

El documento completo y las definiciones en formato estándar se encuentran en [`docs/slo.md`](../../docs/slo.md).

---

# 5. B4 — Cláusula de SLA del equipo

**Responsable principal:** Esaul Tellez de la Cruz

A continuación se presenta la cláusula formal del **Acuerdo de Nivel de Servicio (SLA)** ofrecido a los usuarios y organizaciones cliente del **Módulo de Soporte con Mesas de Ayuda para Sistema de Navegador Seguro**:

---

### Acuerdo de Nivel de Servicio (SLA) — Módulo de Soporte con Mesas de Ayuda

**1. Compromiso de Nivel de Servicio**  
El equipo desarrollador garantiza que el *Módulo de Soporte con Mesas de Ayuda para Sistema de Navegador Seguro* mantendrá un **Porcentaje de Disponibilidad Mensual de al menos 99.0 %** durante cualquier ciclo mensual de facturación (equivalente a no más de 432 minutos de inactividad acumulada en un mes de 30 días).

**2. Definición de Indisponibilidad**  
Se considerará que el servicio se encuentra "Indisponible" cuando el endpoint principal de la API de atención a tickets devuelva de manera continua códigos de error del servidor HTTP `5xx` (incluyendo `500 Internal Server Error`, `502 Bad Gateway` y `503 Service Unavailable`) en una proporción superior al **5 % del tráfico total durante un intervalo mínimo de 5 minutos consecutivos**, o cuando exista una interrupción total en la resolución y conectividad hacia la interfaz web de gestión de tickets verificada mediante monitoreo sintético externo.

**3. Exclusiones del SLA**  
El compromiso de disponibilidad no aplicará ante interrupciones originadas por:
1. *Ventanas de mantenimiento programado:* Notificadas con un mínimo de 48 horas de anticipación a los administradores, a ejecutarse exclusivamente los domingos en la ventana de 02:00 a 04:00 CST (UTC-6), con un máximo de 120 minutos al mes.
2. *Fallas imputables al cliente:* Errores causados por configuraciones erróneas en el software del navegador del cliente, problemas en su proveedor de acceso a Internet (ISP), o peticiones mal estructuradas que devuelvan errores de la familia `4xx` (como `400 Bad Request`, `401 Unauthorized` o `403 Forbidden`).
3. *Eventos de fuerza mayor e infraestructura mayor:* Cortes masivos e imprevisibles en la infraestructura subyacente del proveedor de nube pública (AWS) ajenos al control del equipo, incidentes de ciberataques distribuidos (DDoS) que superen las cuotas contratadas, o desastres naturales.
4. *Suspensión por incumplimiento:* Bloqueo preventivo o suspensión del acceso derivado del incumplimiento comprobado de los Términos y Condiciones de Uso del sistema.

**4. Créditos de Servicio**  
Si el servicio no alcanza el compromiso de disponibilidad mensual, los clientes podrán solicitar un Crédito de Servicio de acuerdo con la siguiente escala:

| Porcentaje de disponibilidad mensual | Porcentaje de crédito aplicable |
|---|---:|
| Menor a 99.0 % y mayor o igual a 98.0 % | **10 %** de descuento en la factura del mes siguiente |
| Menor a 98.0 % y mayor o igual a 95.0 % | **25 %** de descuento en la factura del mes siguiente |
| Menor a 95.0 % | **50 %** de descuento en la factura del mes siguiente |

**5. Procedimiento de Reclamación y Remedio Exclusivo**  
Para recibir un crédito de servicio, el administrador del cliente deberá enviar una solicitud formal por correo electrónico a `soporte-sla@seguronavegador.escom.ipn.mx` dentro de los **primeros 15 días hábiles** del mes calendario siguiente a aquel en que ocurrió la falla. La solicitud debe incluir las fechas, horas exactas de inicio y término del incidente, identificadores de usuario afectados y registros de error (logs). La emisión de créditos de servicio constituye el **único y exclusivo remedio (*sole and exclusive remedy*)** ante cualquier interrupción o falta de disponibilidad, no existiendo responsabilidad por lucro cesante, daños indirectos ni pérdidas económicas derivadas de la inactividad.

> **Justificación de la relación entre el SLO interno y el SLA externo:**  
> El SLO interno del equipo se fija en **99.50 %** (presupuesto de error de 216 minutos) mientras que el SLA contractual ofrecido al cliente se establece en **99.00 %** (margen de 432 minutos) con el propósito deliberado de mantener un **colchón de seguridad operativo de 216 minutos**, permitiendo al equipo de ingeniería detectar anomalías, aplicar parches preventivos y corregir fallas internas antes de infringir el acuerdo legal con los usuarios e incurrir en sanciones económicas.

---

# 6. Preguntas de análisis

### Pregunta 1 (Israel Márquez Cárdenas)
**El SLA de tu proveedor define «no disponible» de forma muy específica. Describe una falla que dejaría tu aplicación fuera de servicio y que no contaría como inactividad para el proveedor. ¿De qué lado de la responsabilidad compartida cae y qué SLI tuyo la detectaría?**

**Respuesta:**  
Una falla típica ocurre cuando un despliegue de software introduce un bug en el middleware de autenticación o cuando se satura el pool de conexiones de la aplicación hacia PostgreSQL, provocando que el backend devuelva errores `HTTP 500 Internal Server Error` o `504 Gateway Timeout` a todos los usuarios que intentan ingresar a la mesa de ayuda. Para AWS, tanto la instancia EC2 como la instancia RDS y el balanceador ALB responden perfectamente a nivel de red (puertos TCP abiertos, hipervisor saludable y conectividad externa intacta), por lo que el proveedor considera que la infraestructura está **100 % disponible** según su SLA. Esta falla cae estrictamente del lado del **cliente** dentro del modelo de responsabilidad compartida (capa de aplicación, código y gestión de datos). En nuestro sistema, esta caída sería detectada de forma inmediata por el **SLI 1 (Disponibilidad de la API)** al registrar el desplome en la proporción de respuestas `2xx/3xx` frente al incremento en códigos `5xx` en el balanceador, así como por el **SLI 3 (Creación exitosa de tickets)** al fallar la persistencia de operaciones.

---

### Pregunta 2 (Israel Márquez Cárdenas)
**Con la factura mensual estimada en la Práctica 1, ¿cuánto crédito recibirías por una caída de 8 horas en un mes? Compáralo con una estimación de lo que perdería el negocio de tu proyecto en esas 8 horas. ¿Por qué el SLA no es un seguro?**

**Respuesta:**  
Una caída de 8 horas continuas equivale a $8 \times 60 = 480\text{ minutos}$ de inactividad. En una ventana mensual estándar de 30 días (43,200 minutos), la disponibilidad mensual resultante es:
$$\text{Disponibilidad} = \frac{43\,200 - 480}{43\,200} \times 100 = \frac{42\,720}{43\,200} \times 100 = \mathbf{98.8889\%} \approx \mathbf{98.89\%}$$
Al encontrarse en el rango menor a 99.0 % y mayor o igual a 95.0 %, AWS otorga un crédito de servicio del **25 %** (o 30 % en cómputo EC2). Tomando la factura mensual total estimada en la Práctica 1 para la arquitectura en AWS (**$59.06 USD/mes**):
$$\text{Crédito obtenido} = 59.06\text{ USD} \times 0.25 = \mathbf{\$14.77\text{ USD}}$$
En contraste, para una organización donde el Módulo de Soporte atiende incidencias críticas de seguridad y navegación de cientos de usuarios corporativos, 8 horas de parálisis operativa implican tickets no atendidos, horas-hombre de ingenieros de soporte detenidos y posibles penalizaciones contractuales, con pérdidas estimadas entre **$2,500.00 y $5,000.00 USD**. El SLA de la nube **no es un seguro** porque es un contrato de servicio limitado con remedio único (*sole and exclusive remedy*) cuyo tope máximo de compensación es el 100 % de la factura de infraestructura del mes, excluyendo explícitamente cualquier indemnización por lucro cesante, daño reputacional o pérdidas económicas del negocio.

---

### Pregunta 3 (Esaul Tellez de la Cruz)
**Google publica para su región de México un compromiso multizona de 99.95 % frente a 99.99 % en Estados Unidos. Si tu sistema necesitara 99.99 % y además residir en México, ¿qué arquitectura lo resolvería y cuánto costaría al mes?**

**Respuesta:**  
El compromiso multizona de 99.95 % en la región de México de Google Cloud (Querétaro) permite hasta $(1 - 0.9995) \times 43\,200 = 21.6\text{ minutos}$ de inactividad mensual, mientras que un requisito de 99.99 % impone un límite estricto de solo $4.32\text{ minutos/mes}$. Si por regulaciones estrictas de soberanía de datos (LFPDPPP) la información debe residir físicamente en territorio nacional, la solución consiste en implementar una **Arquitectura Multi-Proveedor / Multi-Nube Activa-Activa redundante en territorio mexicano**, combinando la infraestructura de Google Cloud en Querétaro con la región de AWS Querétaro (`mx-central-1`) o Azure Querétaro (`Mexico Central`), orquestada mediante un balanceador de tráfico DNS global Anycast (como AWS Route 53 o Cloudflare) con monitores de salud y conmutación por error (*failover*) automática.  
Calculando la disponibilidad compuesta en paralelo de dos nubes independientes en México con 99.95 % cada una:
$$A_{\text{paralelo}} = 1 - (1 - 0.9995) \times (1 - 0.9995) = 1 - (0.0005)^2 = 1 - 0.00000025 = \mathbf{99.999975\%}$$
Esto supera ampliamente el 99.99 % requerido (reduciendo el downtime teórico a 0.0108 segundos al mes). En cuanto al costo, tomando como referencia los precios de la Práctica 1 ($59.06 USD/mes en AWS y $98.95 USD/mes en Azure), desplegar los nodos de cómputo redundantes en la segunda nube, la base de datos réplica de lectura, la sincronización de almacenamiento de objetos y las políticas de enrutamiento DNS sumaría aproximadamente **+$60.00 a +$75.00 USD/mes adicionales**, alcanzando un costo total de operación de ~$120.00 a $135.00 USD mensuales.

---

### Pregunta 4 (Israel Márquez Cárdenas)
**Explica por qué tu SLO no puede ser mayor que la disponibilidad compuesta de la tabla 2, y propón dos cambios concretos de arquitectura que subirían ese techo, con su costo.**

**Respuesta:**  
El SLO mide la calidad real del servicio percibida por el usuario de extremo a extremo e integra no solo la infraestructura subyacente del proveedor, sino también la capa de aplicación, el código, los errores de despliegue, la configuración y el mantenimiento interno. La disponibilidad compuesta de la Tabla 2 representa el límite probabilístico teórico superior que la infraestructura del proveedor es capaz de prometer por contrato. Si el hardware, la red física y los servicios base tienen una disponibilidad compuesta de 98.89 % (sin redundancia), es matemáticamente imposible que el servicio final alcance un 99.5 % o 99.99 %, ya que cualquier caída de la nube arrastrará inevitablemente a la aplicación. Proponer un SLO superior a la disponibilidad compuesta es una promesa falsa que se romperá ante la primera falla de infraestructura.  
Dos cambios arquitectónicos concretos para elevar el techo son:
1. **Redundancia Multi-AZ en Cómputo (EC2):** Implementar un Auto Scaling Group distribuido en al menos dos zonas de disponibilidad (`mx-central-1a` y `mx-central-1b`) tras el balanceador ALB, elevando el SLA de cómputo de 99.50 % a 99.99 %. Costo adicional: **+$16.00 USD/mes** (una instancia `t4g.small` extra).
2. **Base de Datos Multi-AZ en Amazon RDS:** Habilitar el despliegue Multi-AZ con réplica sincrónica en PostgreSQL, elevando el SLA de base de datos de 99.50 % a 99.95 %. Costo adicional: **+$14.83 USD/mes** (duplica la tarifa base de la instancia RDS `db.t4g.micro`).

---

### Pregunta 5 (Esaul Tellez de la Cruz)
**Elige un incidente con informe público de 2025 o 2026 (AWS us-east-1 del 20 de octubre de 2025, Azure Front Door del 29 de octubre de 2025, Cloudflare del 18 de noviembre de 2025 u otro). Con los datos del informe: ¿el SLA cubrió la caída? ¿Cuál de tus SLIs la habría detectado primero y cuánto presupuesto de error habría consumido?**

**Respuesta:**  
- **Incidente seleccionado:** Informe post-mortem de la caída global de **Cloudflare del 18 de noviembre de 2025** (*Cloudflare outage on November 18, 2025*), originada por un error de propagación en la base de datos del plano de control de políticas de proxy y firewall perimetral.
- **Duración del incidente:** La interrupción severa se extendió durante **105 minutos** (1 hora y 45 minutos), generando caídas generalizadas y errores HTTP 502/503 en millones de sitios web a nivel global.
- **¿El SLA cubrió la caída?:** No para la inmensa mayoría de los usuarios. Los clientes de planes Free y Pro de Cloudflare no cuentan con SLA que contemple compensación económica alguna. Para los clientes Enterprise que cuentan con SLA contractual (99.99 %), la compensación requirió abrir un caso formal dentro de los 30 días posteriores, adjuntando logs de evidencia que demostraran que la tasa de error mensual global superó el límite, otorgándose únicamente créditos para facturas futuras.
- **¿Cuál de tus SLIs la habría detectado primero?:** El **SLI 1 (Disponibilidad de la API)** a través del monitor sintético externo (UptimeRobot / Better Stack) y las métricas de peticiones 5xx en el balanceador. Dado que el proxy perimetral devolvía respuestas inmediatas `502 Bad Gateway`, la proporción de peticiones válidas exitosas cayó instantáneamente al 0 %, disparando la alarma de indisponibilidad en los primeros 3 a 5 minutos.
- **Presupuesto de error consumido:** En nuestro sistema, el SLO de disponibilidad es de 99.50 % en una ventana de 30 días, lo que otorga un presupuesto de error total de **216 minutos**. Una caída de 105 minutos representa:
  $$\text{Presupuesto consumido} = \frac{105\text{ min}}{216\text{ min}} \times 100 = \mathbf{48.61\%}\text{ del presupuesto de error mensual}$$
  Un solo incidente consumió prácticamente la mitad del presupuesto de error del mes completo, activando de inmediato la alerta preventiva del 50 % y forzando la revisión urgente de políticas y el congelamiento preventivo de cambios riesgosos.

---

### Pregunta 6 (Salvador Sandoval Garibay)
**Si en la primera semana del mes tu sistema consumió el 80 % del presupuesto de error, ¿qué decides sobre el despliegue de una función nueva programado para el viernes? Justifica con la política que escribiste.**

**Respuesta:**  
**Decisión:** Se **cancela y congela de inmediato el despliegue** de la nueva funcionalidad programado para el viernes.  
**Justificación:** Con base en la Política de Presupuesto de Error establecida en la sección B3 y en `docs/slo.md`, el sistema ha consumido el 80 % de su presupuesto mensual (172.8 minutos de los 216 permitidos) en tan solo 7 días de operación, restando únicamente un margen crítico de 43.2 minutos para los 23 días restantes del ciclo. Introducir un despliegue de nuevas funcionalidades un viernes por la tarde eleva significativamente el riesgo de regresiones, bugs no detectados o degradaciones en producción que agotarían el 20 % de presupuesto restante, violando el SLO interno e incrementando exponencialmente el riesgo de romper el SLA contractual (99.0 %) frente al cliente. Siguiendo estrictamente la política, el equipo debe entrar en estado de estabilización, priorizando tareas de optimización, pruebas automatizadas de resiliencia y resolución de la causa raíz que originó el consumo del 80 %, postergando el lanzamiento hasta que la ventana móvil de 30 días recupere un margen seguro de al menos el 25 % del presupuesto.

---

# 7. Conclusiones

### Conclusión — Israel Márquez Cárdenas
El análisis detallado de los contratos de SLA de cómputo en la nube demuestra que una sola máquina virtual es un punto único de falla inaceptable para sistemas en producción. Comprender la diferencia entre la disponibilidad de la infraestructura declarada por el proveedor y la disponibilidad compuesta real de una cadena de servicios en serie permite dimensionar con rigor técnico y financiero cuándo es indispensable invertir en redundancia Multi-AZ y cómo fijar objetivos internos que reflejen la realidad operativa del sistema.

### Conclusión — Salvador Sandoval Garibay
El diseño de SLIs y SLOs aporta una base cuantitativa indispensable para la toma de decisiones en ingeniería de software. A través del presupuesto de error, el equipo cuenta con una política clara y objetiva para negociar la velocidad de entrega de nuevas funciones frente a la estabilidad del servicio, evitando debates subjetivos y garantizando que la confiabilidad de la base de datos y la persistencia de tickets sean la prioridad absoluta ante cualquier degradación.

### Conclusión — Esaul Tellez de la Cruz
El análisis del SLA de Amazon S3 y la formulación de la cláusula de SLA para nuestro Módulo de Soporte evidencian que los acuerdos de nivel de servicio son contratos legales con letra pequeña y limitaciones estrictas. El concepto de remedio único y exclusivo (*sole and exclusive remedy*) demuestra que ningún proveedor compensa las pérdidas reales de un negocio ante una caída. Diseñar un SLA externo menos exigente que nuestro SLO interno es la estrategia fundamental para mantener un margen de maniobra que proteja al equipo ante imprevistos técnicos sin comprometer los compromisos contractuales con los usuarios.

### Conclusión General del Equipo
La confiabilidad en sistemas distribuidos no se asume, se diseña y se monitorea continuamente. La articulación entre la disponibilidad compuesta calculada en la arquitectura, los SLIs medidos en puntos clave, los SLOs internos gobernados por presupuestos de error y los SLAs contractuales externos constituye el marco integral de ingeniería SRE requerido para construir servicios de nube robustos, transparentes y sostenibles.

---

# 8. Referencias

- AWS. (2022). *Amazon Compute Service Level Agreement*. Amazon Web Services, Inc. https://aws.amazon.com/compute/sla/
- AWS. (2023). *Amazon S3 Service Level Agreement*. Amazon Web Services, Inc. https://aws.amazon.com/s3/sla/
- AWS. (2024). *Amazon RDS Service Level Agreement*. Amazon Web Services, Inc. https://aws.amazon.com/rds/sla/
- AWS. (2026). *AWS Service Level Agreements (índice general)*. https://aws.amazon.com/legal/service-level-agreements/
- Beyer, B., Jones, C., Petoff, J., & Murphy, N. (2016). *Site Reliability Engineering: How Google Runs Production Systems*, Cap. 4: Service Level Objectives. O'Reilly Media. https://sre.google/sre-book/service-level-objectives/
- Beyer, B., Murphy, N., Risa, D., Kawahara, K., & Thorne, S. (2018). *The Site Reliability Workbook: Practical Ways to Implement SRE*, Cap. 2: Implementing SLOs. O'Reilly Media. https://sre.google/workbook/implementing-slos/
- Cloudflare. (2025, 18 de noviembre). *Cloudflare outage on November 18, 2025 (post-mortem)*. Cloudflare Blog. https://blog.cloudflare.com/18-november-2025-outage/
- Google Cloud. (2021). *Composite cloud availability: How to build reliable systems on GCP*. Google Cloud Blog. https://cloud.google.com/blog/products/devops-sre/composite-cloud-availability
- Google Cloud. (2025). *Compute Engine Service Level Agreement*. https://cloud.google.com/compute/sla
- OpenSLO. (2026). *OpenSLO Specification (v1)*. https://openslo.com/

---

# 9. Sección obligatoria: «Uso de IA»

- **Herramienta utilizada:** Gemini (Google)
- **Finalidad y alcance del apoyo:** Se utilizó como herramienta de apoyo para estructurar el formato en Markdown del reporte, revisar la consistencia matemática de las fórmulas de disponibilidad compuesta y presupuestos de error, y asistir en la redacción preliminar de cláusulas de SLA y especificaciones OpenSLO. Todos los datos contractuales, porcentajes de SLA, exclusiones, tiempos de inactividad, respuestas de análisis y decisiones técnicas fueron extraídos, contrastados y validados directamente desde los contratos oficiales de AWS y los informes post-mortem citados.

---

# 10. Tabla de contribuciones del equipo

| Integrante | Tarea Individual Obligatoria (B1) | Tarea Principal de Equipo | Preguntas de Análisis | Aportación |
| :--- | :--- | :--- | :--- | :---: |
| **Israel Márquez Cárdenas** | Análisis y evidencia del SLA de Amazon EC2 | B2: Cadena de dependencias y disponibilidad compuesta | Preguntas 1 y 4 | 33.3 % |
| **Salvador Sandoval Garibay** | Análisis y evidencia del SLA de Amazon RDS | B3: Diseño de SLIs, SLOs y política de presupuesto | Preguntas 2 y 6 | 33.3 % |
| **Esaul Tellez de la Cruz** | Análisis y evidencia del SLA de Amazon S3 | B4: Redacción de la cláusula de SLA del equipo e integración | Preguntas 3 y 5 | 33.4 % |

---

# 11. Lista de evidencias y archivos generados

- `practicas/P02/README.md`: Reporte principal consolidado de la Práctica 2.
- `docs/slo.md`: Especificación formal de SLOs y formato OpenSLO YAML.
- `docs/fase2.md`: Documento de entrega y conexión con la Fase 2 del proyecto.
- `bitacora/2026-09-15.md`: Bitácora de la sesión de laboratorio del 15 de septiembre de 2026.
- `docs/arquitectura/arquitectura_p02.png`: Diagrama de la arquitectura de dependencias.
- `evidencias/P02/P02_B1_ec2_Israel.png`: Captura de SLA de Amazon EC2.
- `evidencias/P02/P02_B1_s3_esaul.png`: Captura de SLA de Amazon S3.
- `evidencias/P02/P02_B1_rds_salvador.png`: Captura de SLA de Amazon RDS.
- `evidencias/P02/disponibilidad_compuesta.xlsx`: Hoja de cálculo con los cálculos de disponibilidad.