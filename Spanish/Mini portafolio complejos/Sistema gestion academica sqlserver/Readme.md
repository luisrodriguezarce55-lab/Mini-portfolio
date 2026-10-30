 # Sistema de Gestión Académica y Control de Matrícula (SQL Server)

**Desarrollado por:** Luis Felipe Rodríguez Arce  
**Programa:** Ciencia de Datos — Módulo: Manejo y Preparación de Datos  
**Base de Datos Relacional:** `proyecto_final_mpd`  

---

## 1. Descripción del Proyecto
Este proyecto consiste en el diseño, arquitectura, desarrollo e implementación de una solución integral de Base de Datos Relacional en **Microsoft SQL Server** para administrar los procesos académicos, la matriculación de estudiantes y el flujo financiero transaccional de un centro de educación superior.

El sistema administra eficientemente el ciclo de vida estudiantil, integrando facultades, planes de estudio, oferta de asignaturas, registros docentes, matrículas semestrales, facturación e historial transaccional de pagos. Además, incluye un paquete de **Vistas Estratégicas** e **Inspecciones Analíticas en SQL** diseñadas para automatizar el control operativo, auditar el periodo lectivo y prevenir la deserción académica.

---

## 2. Modelo Relacional y Arquitectura de Datos

El esquema está compuesto por **9 tablas relacionales** estructuradas bajo reglas de normalización y optimización de tipos de datos (`INT`, `VARCHAR`, `DECIMAL`, `BIT`, `DATE`, `TIME`):

###  Módulo Académico
* **`facultad`:** Estructura organizacional por edificios y decanatos (`FAC-ING`, `FAC-CED`, `FAC-SAL`, `FAC-DER`, `FAC-EDU`).
* **`carrera`:** Catálogo de oferta académica, duración en semestres y títulos otorgados (`Ingeniero en Sistemas`, `Licenciado en Derecho`, etc.).
* **`curso`:** Planes de estudio y distribución de créditos académicos por materia.
* **`profesor`:** Registro docente, vinculación con asignaturas e identificación de modalidad de contratación (`es_tiempo_completo` mediante valores `BIT`).

###  Módulo de Gestión Estudiantil y Matrícula
* **`estudiante`:** Información demográfica, asignación de aulas, día de la semana, horario y estado de actividad (`activo`/`inactivo`).
* **`matricula`:** Registro transaccional que vincula a cada estudiante con el curso matriculado y la fecha de inscripción.
* **`detalle_matricula`:** Historial detallado del periodo lectivo (`I Semestre 2026`), rangos de fechas (inicio/fin) y estado del curso.

###  Módulo Financiero y Facturación
* **`factura`:** Registro de facturación emitida por estudiante con identificadores incrementales (`IDENTITY`).
* **`pago`:** Control transaccional de cobros procesados por diversos métodos de pago (`SINPE Móvil`, `Tarjeta de Crédito`, `Transferencia`, `Efectivo`, `Tarjeta de Débito`).

---

## 3. Componentes de Código e Implementación SQL

### A. Definición de Estructuras (DDL y Mantenimiento)
* **Creación de Esquemas:** Tablas primarias con restricciones de clave (`PRIMARY KEY`), reglas de validación (`CHECK` para estados `activo`/`inactivo`) y valores por defecto (`DEFAULT`).
* **Ajustes Estructurales (`ALTER TABLE`):** Mantenimiento de restricciones de claves primarias, homogeneización de tipos de datos (`VARCHAR`, `CHAR`, `DATE`) y flexibilización de campos opcionales (`NULL`).

### B. Vistas Estratégicas (Reportes Automatizados)
El sistema incluye 6 vistas optimizadas en SQL Server para acelerar el consumo de información por parte de las jefaturas administrativas y de cobro:

1. **`estudiantes_horarios`:** Agrupa la agenda de clases por estudiante (curso, aula, día de la semana y rango de horas).
2. **`resumen_facturacion_estudiante`:** Agrupa y consolida el total facturado por estudiante para agilizar la gestión contable.
3. **`estudiantes_actividad_carrera`:** Clasifica la cantidad de alumnos activos e inactivos por carrera para la detección temprana del riesgo de deserción.
4. **`ocupacion_cursos`:** Mide el volumen de alumnos inscritos por materia para la planificación de cupos y recursos.
5. **`profesor_estudiante`:** Mapea la relación directa y distribución entre docentes y su masa estudiantil.
6. **`auditoria_matricula_periodo`:** Genera un historial completo de matrículas cruzado con el calendario del periodo lectivo.

### C. Script de Consultas Analíticas (T-SQL)
* **Filtros Avanzados y Limpieza:** Aplicación de `WHERE`, `LIKE`, `BETWEEN`, `IN`, `NOT`, `IS NULL` e `IS NOT NULL` para detectar inconsistencias o transacciones pendientes.
* **Agregación y Métrica de Negocio:** Uso de `SUM`, `AVG`, `MIN`, `MAX` y `COUNT` agrupados con `GROUP BY` y filtrados condicionalmente con `HAVING` (ej. consolidado de recaudación por canal de pago superior a ₡1,200,000).
* **Cruzamiento Multitabla y Subconsultas:** Implementación de `INNER JOIN`, `LEFT JOIN`, `RIGHT JOIN` y subconsultas escalares para identificar transacciones superiores al promedio institucional.

---

## 4. Tecnologías y Herramientas Utilizadas
* **Motor de Base de Datos:** Microsoft SQL Server 2022 / SQL Server Express (`SQLEXPRESS`).
* **Entornos de Trabajo:** SQL Server Management Studio (SSMS) y Jupyter Notebooks con Kernel SQL (`.ipynb`).
* **Lenguaje de Consultas:** Transact-SQL (T-SQL).

---

## 5. Conclusiones e Impacto del Proyecto
* **Garantía de Integridad:** Se logró un diseño relacional que elimina la duplicidad de información y mantiene una relación coherente entre las operaciones académicas y financieras.
* **Toma de Decisiones Agilizada:** Las vistas desarrolladas permiten a los departamentos gerenciales extraer métricas clave sin necesidad de ejecutar scripts complejos de manera recurrente.