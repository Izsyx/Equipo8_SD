# Practica No.3: Modelos de servicio y modelos de despliegue en la nube

## Actividad 1. Investigación y mapa conceptual de modelos de servicio

Los modelos de servicio en la nube se diferencian por los recursos que ofrecen y las responsabilidades que asume el proveedor. A mayor abstracción, el usuario administra menos componentes técnicos y se concentra más en desarrollar aplicaciones o utilizar sus funciones. En todos los modelos, conserva responsabilidades sobre sus datos, identidades y permisos de acceso.
 general que agrupa la entrega de capacidades tecnológicas como servicios. 

 ### 1.1. IaaS — Infraestructura como servicio

**Infrastructure as a Service**

Ofrece recursos de infraestructura bajo demanda, como máquinas virtuales, almacenamiento y redes. Permite utilizar servidores sin adquirir ni mantener el equipo físico.

| Aspecto | Descripción |
|---|---|
| **El proveedor gestiona** | Centros de datos, servidores físicos, redes físicas, almacenamiento físico y virtualización. |
| **El usuario gestiona** | Sistema operativo, actualizaciones, aplicaciones, datos y configuración de seguridad de sus recursos. |
| **Caso de uso recomendado** | Migrar una aplicación empresarial que requiere un sistema operativo específico y control sobre la configuración del servidor. |
| **Limitación** | Requiere conocimientos de administración de sistemas y mantenimiento continuo. |

**Servicios:**

- **AWS:** Amazon EC2.
- **Microsoft Azure:** Azure Virtual Machines.
- **Google Cloud:** Compute Engine.

### 1.2. PaaS — Plataforma como servicio

**Platform as a Service**

Proporciona un entorno administrado para desarrollar, desplegar y ejecutar aplicaciones. Reduce el trabajo necesario para operar la infraestructura y el entorno de ejecución.

| Aspecto | Descripción |
|---|---|
| **El proveedor gestiona** | Infraestructura, sistema operativo y componentes de la plataforma de ejecución, según el servicio contratado. |
| **El usuario gestiona** | Código, dependencias de la aplicación, datos, permisos y configuración. |
| **Caso de uso recomendado** | Publicar una aplicación web o API cuando el equipo necesita concentrarse en desarrollar funcionalidades. |
| **Limitación** | Los lenguajes, versiones y configuraciones disponibles dependen de la plataforma. |

**Servicios:**

- **AWS:** AWS Elastic Beanstalk.
- **Microsoft Azure:** Azure App Service.
- **Google Cloud:** App Engine.


### 1.3. SaaS — Software como servicio

**Software as a Service**

Entrega una aplicación terminada que se utiliza por internet, normalmente mediante una suscripción. El usuario aprovecha sus funciones sin desarrollar ni mantener el software.

| Aspecto | Descripción |
|---|---|
| **El proveedor gestiona** | Aplicación, infraestructura, plataforma, actualizaciones y operación técnica. |
| **El usuario gestiona** | Cuentas, permisos, información cargada y configuración funcional. |
| **Caso de uso recomendado** | Incorporar correo electrónico, colaboración o gestión de clientes sin desarrollar un sistema propio. |
| **Limitación** | La personalización y el control sobre el funcionamiento interno son limitados. |

**Servicios:**

- **Microsoft:** Microsoft 365.
- **Google:** Google Workspace.
- **Salesforce:** Sales Cloud.

### 1.4. FaaS — Funciones como servicio

**Function as a Service**

Permite ejecutar funciones de código en respuesta a eventos, como solicitudes HTTP, mensajes o cargas de archivos. Es una modalidad de computación *serverless*.

| Aspecto | Descripción |
|---|---|
| **El proveedor gestiona** | Servidores, infraestructura de ejecución, disponibilidad de la plataforma y mecanismos de escalamiento. |
| **El usuario gestiona** | Código de las funciones, dependencias, eventos de activación, permisos e integraciones. |
| **Caso de uso recomendado** | Generar una miniatura automáticamente cuando se carga una imagen en un almacenamiento en la nube. |
| **Limitación** | Los límites de ejecución y los posibles arranques en frío pueden afectar tareas prolongadas o sensibles a la latencia. |

**Servicios:**

- **AWS:** AWS Lambda.
- **Microsoft Azure:** Azure Functions.
- **Google Cloud:** Cloud Run functions.
- 
### 1.5. CaaS — Contenedores como servicio

**Containers as a Service**

Ofrece un entorno para desplegar y administrar aplicaciones empaquetadas en contenedores. Frecuentemente utiliza Kubernetes para coordinar su ejecución.

| Aspecto | Descripción |
|---|---|
| **El proveedor gestiona** | Componentes administrados de la plataforma de orquestación e infraestructura, según la modalidad contratada. |
| **El usuario gestiona** | Imágenes de contenedores, aplicaciones, dependencias, secretos y configuración de despliegue. En algunas modalidades también administra nodos. |
| **Caso de uso recomendado** | Ejecutar microservicios que necesitan portabilidad, escalamiento independiente y control sobre sus despliegues. |
| **Limitación** | Requiere conocimientos de contenedores, redes y orquestación. |

**Servicios:**

- **AWS:** Amazon Elastic Kubernetes Service — EKS.
- **Microsoft Azure:** Azure Kubernetes Service — AKS.
- **Google Cloud:** Google Kubernetes Engine — GKE.


### 1.6. DBaaS — Base de datos como servicio

**Database as a Service**

Proporciona una base de datos administrada. El proveedor se encarga de buena parte de la operación del motor y la infraestructura.

| Aspecto | Descripción |
|---|---|
| **El proveedor gestiona** | Infraestructura, instalación del motor, mantenimiento y mecanismos de respaldo y disponibilidad incluidos en el servicio. |
| **El usuario gestiona** | Datos, esquemas, consultas, índices, usuarios, permisos y políticas configurables. |
| **Caso de uso recomendado** | Almacenar pedidos y clientes de una tienda en línea sin operar directamente los servidores de base de datos. |
| **Limitación** | Puede restringir extensiones, configuraciones avanzadas y acceso administrativo al motor. |

**Servicios:**

- **AWS:** Amazon RDS.
- **Microsoft Azure:** Azure SQL Database.
- **Google Cloud:** Cloud SQL.


### 1.7. AIaaS — Inteligencia artificial como servicio

**Artificial Intelligence as a Service**

Ofrece capacidades de inteligencia artificial mediante APIs o plataformas administradas. Puede incluir generación de texto, reconocimiento de imágenes y herramientas para utilizar o adaptar modelos.

| Aspecto | Descripción |
|---|---|
| **El proveedor gestiona** | Infraestructura de cómputo, plataforma y operación de los modelos ofrecidos, según la modalidad. |
| **El usuario gestiona** | Integración, datos enviados, instrucciones o prompts, permisos y evaluación de resultados. |
| **Caso de uso recomendado** | Integrar un asistente que responda preguntas sobre documentos empresariales sin construir un modelo desde cero. |
| **Limitación** | Los resultados pueden contener errores y requieren evaluación antes de utilizarse en decisiones importantes. |

**Servicios:**

- **AWS:** Amazon Bedrock.
- **Microsoft Azure:** Azure OpenAI.
- **Google Cloud:** Vertex AI.


### 1.8. XaaS — Todo como servicio

**Anything as a Service**

Es un concepto general que agrupa la entrega de capacidades tecnológicas como servicios. La letra “X” representa diferentes recursos o funciones.

| Aspecto | Descripción |
|---|---|
| **El proveedor gestiona** | Los componentes establecidos por cada servicio y contrato. |
| **El usuario gestiona** | Configuración, integración, información y responsabilidades que no se delegan al proveedor. |
| **Caso de uso recomendado** | Combinar infraestructura, aplicaciones y bases de datos contratadas como servicios para reducir la operación de recursos propios. |
| **Limitación** | La combinación de servicios puede aumentar la dependencia de proveedores y la complejidad de integración y costos. |

**Servicios:**

- **AWS:** Amazon EC2, como ejemplo de IaaS.
- **Microsoft:** Microsoft 365, como ejemplo de SaaS.
- **Google Cloud:** Cloud SQL, como ejemplo de DBaaS.

```mermaid
flowchart TB
    subgraph X["XaaS · Todo como servicio"]
        direction TB

        subgraph ESCALA["Progresión general · Aumenta la abstracción"]
            direction TB
            I["IaaS · Infraestructura bajo demanda"]
            C["CaaS · Orquestación de contenedores"]
            P["PaaS · Entorno para desarrollar y ejecutar"]
            S["SaaS · Aplicación lista para utilizar"]

            I -->|"Delega la orquestación"| C
            C -->|"Delega más operación del entorno"| P
            P -->|"Delega también el desarrollo del producto"| S
        end

        subgraph ESP["Servicios especializados · Cercanos a la capa de plataforma"]
            direction TB
            F["FaaS · Ejecuta funciones por eventos"]
            D["DBaaS · Administra motores de bases de datos"]
            A["AIaaS · Ofrece modelos y plataformas de IA"]
        end

        P -.->|"Ejecución de código"| F
        P -.->|"Gestión de datos"| D
        P -.->|"Capacidades de IA"| A

        F -.->|"Automatiza tareas de"| S
        D -.->|"Almacena datos de"| S
        A -.->|"Añade inteligencia a"| S
    end
```
| Modelo | Tú gestionas | Proveedor gestiona | Ejemplo AWS | Ejemplo Azure | Ejemplo GCP |
|---|---|---|---|---|---|
| **IaaS** | Sistema operativo, parches, aplicaciones, datos y configuración de seguridad. | Hardware, redes físicas, almacenamiento físico y virtualización. | Amazon EC2 | Azure Virtual Machines | Compute Engine |
| **PaaS** | Código, dependencias, datos y configuración de la aplicación. | Infraestructura y plataforma de ejecución, según la oferta. | AWS Elastic Beanstalk | Azure App Service | App Engine |
| **SaaS** | Usuarios, permisos, datos y configuración funcional. | Aplicación, plataforma, infraestructura y actualizaciones. | Amazon WorkMail | Microsoft 365¹ | Google Workspace¹ |
| **FaaS** | Funciones, dependencias, disparadores, permisos e integraciones. | Infraestructura, entorno de ejecución y escalamiento. | AWS Lambda | Azure Functions | Cloud Run functions |
| **CaaS** | Contenedores, aplicaciones, despliegues y secretos; nodos según la modalidad. | Orquestación administrada e infraestructura según la modalidad. | Amazon EKS | Azure Kubernetes Service | Google Kubernetes Engine |


## Ejercicio 2: Análisis comparativo de modelos de despliegue 

### 1.2. Nube privada

| Aspecto | Descripción |
|---|---|
| **Definición** | Entorno de nube dedicado exclusivamente a una organización. Puede alojarse en sus instalaciones o ser operado por un tercero. |
| **Ventajas** | Mayor control sobre configuraciones y accesos; personalización; recursos dedicados a las necesidades de la organización. |
| **Desventajas** | Mayor inversión y esfuerzo operativo; necesidad de personal especializado; capacidad limitada por los recursos disponibles. |
| **Organización beneficiada** | Centros de investigación, grandes empresas y organizaciones con requisitos particulares de control o infraestructura. |
| **Ejemplo real** | **CERN opera una nube privada basada en OpenStack** para proporcionar infraestructura como servicio a sus proyectos y usuarios. [2] |

### 1.3. Nube híbrida

| Aspecto | Descripción |
|---|---|
| **Definición** | Integra infraestructura privada o local con servicios de nube pública, permitiendo que ambos entornos colaboren. |
| **Ventajas** | Conserva sistemas y datos seleccionados en el entorno local; aprovecha la capacidad de la nube pública; facilita migraciones graduales. |
| **Desventajas** | Integración compleja; administración de seguridad en varios entornos; costos de conectividad y sincronización. |
| **Organización beneficiada** | Hospitales, bancos y empresas con sistemas existentes que necesitan modernizarse sin migrar toda su operación de una sola vez. |
| **Ejemplo real** | **Liberty Latin America utiliza AWS Outposts y AWS Local Zones** para conectar infraestructura local con servicios de AWS y atender operaciones de telecomunicaciones en Puerto Rico. [3] |

### 1.4. Multi-cloud

| Aspecto | Descripción |
|---|---|
| **Definición** | Uso de servicios de dos o más proveedores de nube. Cada proveedor puede atender una necesidad diferente. |
| **Ventajas** | Permite elegir servicios especializados; reduce la concentración en un proveedor; puede mejorar la capacidad de negociación y las opciones de recuperación. |
| **Desventajas** | Mayor complejidad de administración; diferencias entre herramientas y permisos; costos de transferencia de datos y capacitación. |
| **Organización beneficiada** | Empresas grandes que requieren capacidades de distintos proveedores o buscan diversificar sus dependencias tecnológicas. |
| **Ejemplo real** | **Veritas documentó el uso de Oracle Database Service for Microsoft Azure** para simplificar un entorno multi-cloud de análisis de datos que combina servicios de Azure y Oracle Cloud Infrastructure. [4] |

### 1.5. Nube distribuida

| Aspecto | Descripción |
|---|---|
| **Definición** | Distribuye servicios de nube en distintas ubicaciones físicas y mantiene una administración coordinada. Puede incluir regiones, instalaciones locales y ubicaciones cercanas a los usuarios. |
| **Ventajas** | Acerca el procesamiento a las cargas de trabajo; reduce latencia; permite atender requisitos de ubicación y mantener políticas comunes. |
| **Desventajas** | Dificulta la coordinación entre sitios; exige controlar versiones y configuraciones; depende de la conectividad y capacidad de cada ubicación. |
| **Organización beneficiada** | Empresas con sucursales, operaciones internacionales o usuarios distribuidos geográficamente. |
| **Ejemplo real** | **Netflix implementó estaciones de trabajo para efectos visuales mediante AWS Local Zones**, acercando recursos de cómputo a sus artistas. Ilustra la distribución de servicios de nube fuera de las regiones principales. [5] |

### 1.6. Edge computing

| Aspecto | Descripción |
|---|---|
| **Definición** | Procesa información cerca del lugar donde se genera, por ejemplo en sensores, equipos industriales o servidores locales, antes de enviar todo o parte de los datos a una nube central. |
| **Ventajas** | Menor latencia; menor consumo de ancho de banda; posibilidad de mantener funciones locales ante interrupciones de internet, si se diseñan para ello. |
| **Desventajas** | Capacidad local limitada; mantenimiento de numerosos dispositivos; mayor exposición física de los equipos. |
| **Organización beneficiada** | Fábricas, empresas energéticas, operadores logísticos y organizaciones con dispositivos conectados o procesos sensibles al tiempo de respuesta. |
| **Ejemplo real** | **i GRID LAB utiliza AWS IoT Greengrass** para recopilar datos de dispositivos en el borde dentro de su plataforma energética R.E.A.L., integrada con servicios de análisis en la nube. [6] |

### 1.7. Nube soberana

| Aspecto | Descripción |
|---|---|
| **Definición** | Entorno diseñado para responder a requisitos de jurisdicción, residencia de datos y control operativo. Considera dónde se almacena la información, quién puede acceder y bajo qué condiciones. |
| **Ventajas** | Mayor control sobre ubicación y accesos; apoyo al cumplimiento regulatorio; posibilidad de establecer restricciones operativas y de gestión de claves. |
| **Desventajas** | Puede tener mayor costo; catálogo de servicios más limitado; requiere verificar que las garantías técnicas y contractuales cubran las necesidades reales. |
| **Organización beneficiada** | Dependencias gubernamentales, entidades financieras y organizaciones que manejan información especialmente sensible. |
| **Ejemplo real** | **Lengoo utilizó T-Systems Sovereign Cloud, basada en Google Cloud**, para sus soluciones de traducción con IA y requisitos de confidencialidad, según un caso publicado por T-Systems. [7] |

### 1.8. Nube comunitaria

| Aspecto | Descripción |
|---|---|
| **Definición** | Infraestructura compartida por varias organizaciones con objetivos, políticas o necesidades comunes. Su acceso se orienta a esa comunidad. |
| **Ventajas** | Distribuye costos; facilita la colaboración; permite acordar políticas adaptadas a necesidades compartidas. |
| **Desventajas** | Requiere acuerdos de gobierno y financiamiento; puede haber conflictos por prioridades; tiene una capacidad condicionada por los recursos de la comunidad. |
| **Organización beneficiada** | Universidades, centros de investigación, consorcios hospitalarios y organismos públicos que colaboran entre sí. |
| **Ejemplo real** | **EGI Federated Cloud reúne nubes de investigación** para proporcionar recursos a la comunidad científica. Ilustra un enfoque comunitario implementado mediante una federación de proveedores. [8] |

### a) ¿Por qué una empresa mexicana del sector salud podría preferir una nube híbrida en lugar de una nube pública?

Una empresa mexicana del sector salud podría preferir una nube híbrida porque le permite conservar los expedientes clínicos y sistemas críticos en un entorno privado, mientras utiliza la nube pública para aplicaciones como portales informativos o servicios de citas. Esta combinación facilita aprovechar la infraestructura existente y modernizar los sistemas de manera gradual. También permite mantener determinadas operaciones locales cuando falla la conexión a internet, siempre que la arquitectura esté preparada para ello. Sin embargo, utilizar una nube privada no garantiza automáticamente mayor seguridad: en ambos entornos deben establecerse controles de acceso, cifrado, respaldos y medidas de protección de los datos personales.

### b) ¿Qué ventaja tiene el modelo multi-cloud sobre depender de un solo proveedor? ¿Cuál es su principal desafío?

La principal ventaja del modelo multi-cloud es que permite elegir los servicios más adecuados de diferentes proveedores y reducir la concentración de dependencias tecnológicas. Por ejemplo, una empresa puede ejecutar sus aplicaciones en Azure y utilizar bases de datos de Oracle Cloud. También puede preparar alternativas de recuperación ante interrupciones, aunque estas deben diseñarse y probarse. Su principal desafío es la complejidad operativa: cada proveedor utiliza herramientas, permisos, redes y esquemas de cobro diferentes. Por ello, la organización necesita personal capacitado y mecanismos para coordinar la seguridad, el monitoreo, los costos y el intercambio de información entre plataformas.

### c) Con la apertura de regiones de AWS, Azure, GCP y Alibaba en Querétaro, ¿qué implicaciones tiene para la soberanía de datos en México? ¿Será suficiente para cumplir con la Ley Federal de Protección de Datos Personales?

La disponibilidad de regiones en México facilita almacenar y procesar datos dentro del país y reduce la latencia. Sin embargo, residencia y soberanía no son equivalentes: también importa quién controla los accesos, las claves y la operación. AWS, Azure y GCP documentan infraestructura en Querétaro; el anuncio oficial consultado de Alibaba confirma México, sin precisar ese estado. Alojar datos en territorio nacional no basta para cumplir la Ley Federal de Protección de Datos Personales en Posesión de los Particulares. También deben atenderse las obligaciones de privacidad, seguridad, consentimiento cuando corresponda y derechos ARCO, además de revisar contratos, respaldos y transferencias de información.

### d) ¿En qué escenarios el edge computing ofrece ventajas sobre el cloud centralizado? Menciona al menos dos industrias específicas.

El edge computing ofrece ventajas cuando se requieren respuestas rápidas, se generan grandes volúmenes de información o la conexión a internet es inestable. En la industria manufacturera, permite analizar imágenes de productos junto a la línea de producción y detectar defectos sin enviar todo el video a una nube central. En la industria energética, permite procesar mediciones de paneles solares, baterías o instalaciones remotas cerca de su origen y enviar únicamente los datos necesarios a la nube. En ambos casos, disminuye la latencia y el consumo de ancho de banda. La nube central complementa este procesamiento con análisis históricos, almacenamiento y coordinación entre instalaciones.


## Ejercicio 3: Exploración de servicios en AWS y Microsoft Azure

Se seleccionaron **Amazon Web Services (AWS)** y **Microsoft Azure**. Las evidencias proporcionadas muestran las consolas de ambos proveedores y un servicio representativo de cada modelo solicitado. 

### 3.1. Paneles de inicio de los proveedores

Las imágenes disponibles corresponden a servicios específicos. **Quedan pendientes las dos capturas del panel de inicio general**, una de AWS Console Home y otra de Azure Home o Dashboard. El panel de Lambda y el listado de máquinas virtuales no sustituyen estas evidencias.

### 3.2. AWS: servicios, capa gratuita y aplicaciones reales

| Evidencia | Nombre del servicio | Categoría | ¿Tiene capa gratuita? | ¿Para qué lo usaría en un proyecto real? |
|---|---|---|---|---|
| 1 | Amazon EC2 | IaaS | **Prueba mediante créditos**, para cuentas nuevas elegibles del programa AWS Free Tier; no es una VM gratuita permanente. El programa ofrece hasta USD 200 y un plan gratuito de hasta seis meses, sujeto al saldo y condiciones. [AWS Free Tier](https://aws.amazon.com/free/). | Alojar un servidor Linux para una aplicación que requiere instalar paquetes y configurar directamente el sistema operativo. |
| 2 | AWS Elastic Beanstalk | PaaS | **La plataforma no tiene cargo adicional**, pero se cobran recursos como EC2, almacenamiento y balanceadores. Su costo puede quedar cubierto por beneficios elegibles de Free Tier. [Precios de Beanstalk](https://aws.amazon.com/elasticbeanstalk/pricing/). | Publicar una aplicación web de reservaciones y delegar el aprovisionamiento y escalamiento de su entorno. |
| 3 | AWS Lambda | FaaS | **Sí:** incluye un millón de solicitudes y 400,000 GB-segundo de cómputo al mes dentro de las condiciones de su capa gratuita. Las integraciones pueden cobrarse por separado. [Precios de Lambda](https://aws.amazon.com/lambda/pricing/). | Generar miniaturas cuando los usuarios cargan fotografías a un bucket de S3. |
| 4 | Amazon Elastic Kubernetes Service (EKS) | CaaS | **No tiene una capa permanente gratuita del clúster administrado.** Se cobra por el clúster y por los recursos utilizados para ejecutar las cargas de trabajo. [Precios de EKS](https://aws.amazon.com/eks/pricing/). | Ejecutar los microservicios de catálogo, pedidos e inventario de una tienda mediante Kubernetes. |
| 5 | Amazon Relational Database Service (RDS) | DBaaS | **Prueba mediante créditos** para cuentas nuevas elegibles. La oferta anterior de instancias gratuitas durante 12 meses correspondía a cuentas creadas antes del 15 de julio de 2025; no debe asumirse para cuentas nuevas. [Oferta de RDS](https://aws.amazon.com/rds/free/). | Guardar clientes, productos y pedidos en una base relacional administrada, con mecanismos de respaldo. |
| 6 | Amazon Bedrock | AIaaS | **Sin cuota gratuita general permanente de inferencia.** El cobro depende del modelo y la modalidad de uso; los créditos promocionales, cuando apliquen, son un beneficio temporal. [Precios de Bedrock](https://aws.amazon.com/bedrock/pricing/). | Integrar un asistente que responda preguntas sobre manuales internos utilizando modelos generativos y documentos del proyecto. |

#### Evidencia 1. Amazon EC2 — IaaS

La sección **EC2 → Instancias** muestra el listado de máquinas virtuales y la opción para lanzar una instancia.

![AWS: listado de instancias de Amazon EC2](evidencia/1-aws.png)

#### Evidencia 2. AWS Elastic Beanstalk — PaaS

La sección **Elastic Beanstalk → Aplicaciones** permite consultar aplicaciones y acceder a la creación de una nueva.

![AWS: aplicaciones de Elastic Beanstalk](evidencia/2-aws.png)

#### Evidencia 3. AWS Lambda — FaaS

El panel de **Lambda** presenta funciones de eventos, métricas y la opción para crear una función.

![AWS: panel de funciones de Lambda](evidencia/3-aws.png)

#### Evidencia 4. Amazon EKS — CaaS

La sección **Amazon Elastic Kubernetes Service → Clústeres** muestra el listado de clústeres administrados.

![AWS: listado de clústeres de Amazon EKS](evidencia/4-aws.png)

#### Evidencia 5. Amazon RDS — DBaaS

La sección **Aurora and RDS → Bases de datos** permite consultar y crear bases de datos administradas. El servicio elegido para la comparación es Amazon RDS.

![AWS: bases de datos en Aurora and RDS](evidencia/5-aws.png)

#### Evidencia 6. Amazon Bedrock — AIaaS

La página **Amazon Bedrock → Información general** muestra acceso al catálogo de modelos y herramientas de prueba. En la barra superior aparece seleccionada la región **México (Central)**.

![AWS: información general de Amazon Bedrock con México Central seleccionado](evidencia/6-aws.png)

### 3.3. Microsoft Azure: servicios, capa gratuita y aplicaciones reales

Las capturas muestran la suscripción **Azure for Students**. Los beneficios generales descritos a continuación no garantizan que todas las ofertas puedan activarse en esa suscripción: su elegibilidad y los planes disponibles deben verificarse al configurar cada recurso.

| Evidencia | Nombre del servicio | Categoría | ¿Tiene capa gratuita? | ¿Para qué lo usaría en un proyecto real? |
|---|---|---|---|---|
| 1 | Azure Virtual Machines | IaaS | **Sí, temporal y limitada**, para tamaños de VM y cuentas nuevas elegibles dentro de la oferta de servicios gratuitos por 12 meses. No incluye cualquier tamaño ni todos los recursos asociados. [Servicios gratuitos de Azure](https://azure.microsoft.com/en-us/free/). | Ejecutar una aplicación institucional que necesita control sobre Windows o Linux y su configuración de red. |
| 2 | Azure App Service | PaaS | **Sí**, mediante el nivel Free/F1, con recursos compartidos y cuotas para desarrollo y pruebas. Su disponibilidad depende de la configuración y región. [Servicios gratuitos de Azure](https://azure.microsoft.com/en-us/free/). | Publicar un portal de citas con su API sin administrar directamente el sistema operativo del servidor. |
| 3 | Azure Functions | FaaS | **Sí, según el plan y la suscripción.** Consumption ofrece un millón de ejecuciones y 400,000 GB-segundo mensuales en suscripciones elegibles de pago por uso. Flex Consumption tiene cuotas distintas; el almacenamiento se cobra por separado. [Precios de Functions](https://azure.microsoft.com/en-us/pricing/details/functions/). | Procesar eventos de una cola para actualizar el estado de pedidos y generar notificaciones. |
| 4 | Azure Kubernetes Service (AKS) | CaaS | **Sí, parcialmente:** el nivel Free no cobra la administración del clúster; los nodos y otros recursos consumidos sí tienen costo. [Precios de AKS](https://azure.microsoft.com/en-us/pricing/details/kubernetes-service/). | Desplegar servicios de autenticación, catálogo y ventas en contenedores con escalamiento independiente. |
| 5 | Azure SQL Database | DBaaS | **Sí, bajo la oferta gratuita:** hasta 10 bases por suscripción, cada una con 100,000 segundos de vCore, 32 GB de datos y 32 GB de respaldo mensuales, sujeto a elegibilidad. La captura muestra el anuncio de esta oferta, no su activación. [Oferta gratuita de SQL Database](https://learn.microsoft.com/en-us/azure/azure-sql/database/free-tier?view=azuresql). | Almacenar usuarios, citas y pagos de un sistema administrativo en una base relacional administrada. |
| 6 | Azure OpenAI, mostrado dentro de Microsoft Foundry | AIaaS | **Sin capa gratuita general permanente para la API.** Se factura por consumo o capacidad aprovisionada, según el modelo y despliegue; los créditos de una suscripción no equivalen a una cuota gratuita del servicio. [Precios de Azure OpenAI](https://azure.microsoft.com/en-us/pricing/details/azure-openai/). | Crear un asistente para consultar documentos institucionales y redactar borradores de respuestas que revise una persona. |

#### Evidencia 1. Azure Virtual Machines — IaaS

La sección **Compute infrastructure → Virtual machines** muestra el listado de máquinas virtuales de la suscripción.

![Azure: listado de Virtual Machines](evidencia/1-azure.png)

#### Evidencia 2. Azure App Service — PaaS

El formulario **App Services → Create Web App** permite configurar una aplicación web. El campo **Region** muestra **Mexico Central**.

![Azure: creación de una Web App en App Service](evidencia/2-azure.png)

#### Evidencia 3. Azure Functions — FaaS

La sección **Function App** muestra el listado de aplicaciones de funciones y la opción de creación.

![Azure: listado de Function App](evidencia/3-azure.png)

#### Evidencia 4. Azure Kubernetes Service — CaaS

El formulario **Create Kubernetes cluster** corresponde a AKS. El campo **Region** muestra **(Mexico) Mexico Central**.

![Azure: creación de un clúster de AKS](evidencia/4-azure.png)

#### Evidencia 5. Azure SQL Database — DBaaS

El formulario **Create SQL Database** presenta la configuración de una base de datos y un anuncio con las cuotas de la oferta gratuita.

![Azure: creación de SQL Database y anuncio de la oferta gratuita](evidencia/5-azure.png)

#### Evidencia 6. Azure OpenAI — AIaaS

La sección **Microsoft Foundry → Azure OpenAI** muestra el listado de recursos del servicio de inteligencia artificial.

![Azure: listado de recursos de Azure OpenAI en Microsoft Foundry](evidencia/6-azure.png)

## Actividad 4: Creación de un recurso en la nube (Laboratorio)

**Duración asignada:** 1.5 horas. **Tipo:** Individual. **Opción elegida:** A — IaaS: crear una máquina virtual.

**Nota:** Las imágenes son ilustraciones generadas con IA. La creación de la VM y la verificación del servidor quedan pendientes de ejecución real.

### 4.1. Configuración de la máquina virtual

El escenario propuesto utiliza **Amazon EC2**, con una máquina Linux y Nginx como servidor web. La configuración representada es la siguiente:

| Parámetro | Valor del ejemplo |
|---|---|
| Nombre de la instancia | `practica3-web` |
| Modelo de servicio | IaaS |
| Sistema operativo | Ubuntu Server 24.04 LTS |
| Tipo de instancia | `t3.micro` |
| Almacenamiento | 8 GiB, volumen gp3 |
| Región | México (Central), `mx-central-1` |
| Par de claves | `practica3` |
| Grupo de seguridad | `practica3-sg` |
| IPv4 pública ilustrativa | `203.0.113.10` |
| IPv4 privada ilustrativa | `10.0.1.25` |

Para realizar el laboratorio con la capa gratuita, primero debe comprobarse que la cuenta, el tipo de instancia y los recursos asociados estén cubiertos por los beneficios o créditos disponibles. La imagen no demuestra la elegibilidad ni un costo de cero.

### 4.2. Reglas del grupo de seguridad

El ejemplo representa dos reglas de entrada:

| Servicio | Protocolo | Puerto | Origen | Propósito |
|---|---|---|---|---|
| SSH | TCP | 22 | IP pública del equipo administrador con máscara `/32`; en la imagen se usa `198.51.100.25/32` como ejemplo. | Administrar la VM desde la terminal. |
| HTTP | TCP | 80 | `0.0.0.0/0` | Permitir consultar el servidor web desde internet. |

**Figura 4.1. Configuración de EC2 y las reglas de entrada.**

![Configuración de una VM Ubuntu y reglas SSH y HTTP](ejercicio/iaas/1-configuracion-vm.png)

### 4.3. Conexión por SSH

El procedimiento ilustrado protege el archivo de clave y lo utiliza para iniciar una sesión como usuario `ubuntu`. En una ejecución real se sustituye `IP_PUBLICA_REAL` por la dirección asignada a la instancia y se utiliza el archivo de clave correspondiente:

```bash
chmod 400 ~/Downloads/practica3.pem
ssh -i ~/Downloads/practica3.pem ubuntu@IP_PUBLICA_REAL
```

La dirección `203.0.113.10` mostrada en las imágenes es una IP de documentación; no corresponde a una VM creada para esta práctica.

### 4.4. Instalación y comprobación de Nginx

Una vez conectado a la VM real, los comandos del procedimiento son:

```bash
sudo apt update
sudo apt install -y nginx
sudo systemctl enable --now nginx
systemctl is-active nginx
curl -I http://localhost
```

El resultado esperado es `active` al consultar el servicio y una respuesta `HTTP/1.1 200 OK` al consultar el servidor local.

**Figura 4.2. Sesión SSH con instalación y comprobación local de Nginx.**

![Sesión SSH e instalación de Nginx desde la terminal](ejercicio/iaas/2-sesion-ssh.png)

### 4.5. Comprobación desde el navegador

Para verificar el acceso público se abriría `http://IP_PUBLICA_REAL` en Firefox. La página de bienvenida de Nginx sería el resultado esperado si el servicio está activo y las reglas de red permiten el acceso HTTP.

**Figura 4.3. Página de bienvenida de Nginx en Firefox.**

![Página de bienvenida de Nginx en Firefox con una IP de ejemplo](ejercicio/iaas/3-nginx-firefox.png)
