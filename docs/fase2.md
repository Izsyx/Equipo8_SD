# Fase 2 del Proyecto — SLOs y Confiabilidad del Sistema

## Información del Proyecto

- **Proyecto:** Módulo de Soporte con Mesas de Ayuda para Sistema de Navegador Seguro
- **Equipo:** 8 (Sistemas Distribuidos — 7CV1)
- **Integrantes:**
  - Israel Márquez Cárdenas (2022300395)
  - Esaul Tellez de la Cruz (2023630692)
  - Salvador Sandoval Garibay (2022630151)
- **Proveedor:** Amazon Web Services (AWS)

---

## 1. Conexión con los Objetivos de Nivel de Servicio (SLOs)

La Fase 2 del proyecto establece la base cuantitativa para evaluar la resiliencia y el comportamiento del sistema distribuido ante condiciones reales y pruebas de estrés.

El documento central de definición de indicadores y metas se encuentra disponible en:

🔗 **[Documento Oficial de SLOs del Proyecto (`docs/slo.md`)](slo.md)**

---

## 2. Resumen Ejecutivo de Métricas de Confiabilidad

1. **Disponibilidad de la API:** **99.50 %** en una ventana móvil de 30 días (Presupuesto de error: 216 minutos).
2. **Latencia del Servicio (p95):** **≥ 95.00 %** de las peticiones válidas atendidas en $\le 500\text{ ms}$.
3. **Persistencia y Creación de Tickets:** **≥ 99.00 %** de transacciones exitosas registradas en PostgreSQL y Amazon S3.

---

## 3. Próximos Pasos en el Proyecto

- **Exposición de Fase 2:** Presentación y defensa de los compromisos de confiabilidad y arquitectura (29 de septiembre de 2026).
- **Práctica 7 (Pruebas de Carga):** Medición empírica bajo estrés para verificar si el sistema cumple los SLOs aquí prometidos.
- **Práctica 11 (Observabilidad):** Despliegue de tableros de control en Grafana/CloudWatch y monitores de alerta automatizados.
