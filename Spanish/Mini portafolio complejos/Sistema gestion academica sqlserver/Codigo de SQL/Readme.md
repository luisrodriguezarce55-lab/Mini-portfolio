# Sistema de Gestión Académica y Control de Matrícula (SQL Server)

## Descripción del Proyecto
Este proyecto consiste en el diseño, desarrollo e implementación de una solución integral de Base de Datos Relacional para la gestión académica y financiera de un centro de educación superior (`proyecto_final_mpd`). 

El sistema administra eficientemente el ciclo de vida completo del estudiante, integrando facultades, carreras, oferta académica, docentes, matrícula por periodos lectivos, facturación y registros transaccionales de pago. Asimismo, incluye un conjunto de **Vistas Estratégicas** e **Inspecciones Analíticas en T-SQL** orientadas a auditar el desempeño operativo, controlar la deserción y facilitar decisiones financieras.

---

## Estructura de la Base de Datos y Modelo Relacional

El esquema relacional fue estructurado bajo normas de normalización de datos e incluye las siguientes entidades primarias:

1. **`facultad`:** Define la estructura organizacional por edificios y decanatos (`FAC-ING`, `FAC-CED`, `FAC-SAL`, `FAC-DER`, `FAC-EDU`).
2. **`carrera`:** Almacena los planes de estudio, duración por semestres y títulos otorgados (`Ingeniero en Sistemas`, `Licenciado en Derecho`, etc.).
3. **`curso`:** Catálogo de asignaturas con sus respectivos créditos académicos.
4. **`profesor`:** Registro docente, vinculación de asignaturas y tipo de contratación (`BIT` de tiempo completo o por horas).
5. **`estudiante`:** Información demográfica, estado de actividad (`activo`/`inactivo`), horarios, aulas y asignaciones.
6. **`matricula` & `detalle_matricula`:** Trazabilidad de inscripciones por periodos lectivos (`I Semestre 2026`), estados de curso y rangos de fechas.
7. **`factura` & `pago`:** Control de montos emitidos y transacciones recibidas por diversos métodos de pago (`SINPE Móvil`, `Tarjeta de Crédito`, `Transferencia`, `Efectivo`).

---

## Módulos y Componentes de Código

### 1. DDL y Modificaciones Estructurales (`Codigo de integracion de datos.sql` / `Codigos extras.docx`)
* Creación de tablas primarias con restricciones `PRIMARY KEY`, `CHECK` y valores predeterminados (`DEFAULT`).
* Mantenimiento estructural mediante sentencias `ALTER TABLE` para la corrección y redefinición de restricciones de Clave Primaria y homogenización de tipos de datos (`VARCHAR`, `CHAR`, `DATE`).

### 2. Vistas Analíticas e Reporting (`Vistas.PNG` / `Codigo de analisis de informacion.sql`)
Se diseñaron 6 vistas clave en SQL Server para acelerar las consultas directas de los departamentos administrativos y de cobros:
* **`estudiantes_horarios`:** Muestra la agenda semanal de clases (curso, aula, día, horas de inicio y fin) para cada estudiante.
* **`resumen_facturacion_estudiante`:** Agrupa el total facturado por estudiante para facilitar el control contable.
* **`estudiantes_actividad_carrera`:** Monitorea la cantidad de estudiantes activos e inactivos por carrera para prevenir la deserción académica.
* **`ocupacion_cursos`:** Muestra el volumen de estudiantes matriculados por materia para optimizar el cupo de aulas.
* **`profesor_estudiante`:** Mapea la relación directa entre docentes y su masa estudiantil.
* **`auditoria_matricula_periodo`:** Genera un historial de matriculación cruzado con las fechas del periodo lectivo para procesos de auditoría.

### 3. Script de Consultas de Negocio (`Codigo de analisis de informacion.sql`)
Implementación de un set extenso de consultas avanzadas en T-SQL:
* **Filtros Avanzados y Agregaciones:** Uso de `WHERE`, `LIKE`, `BETWEEN`, `IN`, `NOT`, `IS NULL` e `IS NOT NULL` para depuración de registros incompletos en pagos o facturación.
* **Análisis Estadístico:** Uso de `SUM`, `AVG`, `MIN`, `MAX` y `COUNT` agrupados por `GROUP BY` con condiciones `HAVING` (ej. filtrado de recaudación por método de pago con montos superiores a ₡1,200,000).
* **Relaciones Multitabla y Subconsultas:** Implementación de `INNER JOIN`, `LEFT JOIN`, `RIGHT JOIN` y subconsultas escalares para detectar pagos por encima del promedio general de la universidad.

---

## Tecnologías Utilizadas
* **Motor de Base de Datos:** Microsoft SQL Server 2022 / SSMS (SQL Server Management Studio).
* **Lenguaje:** T-SQL (Transact-SQL).
* **Herramientas de Documentación:** Microsoft Word & Jupyter Notebooks (`.ipynb`).

---

## Principales Insights del Análisis de Datos
1. **Recaudación Financiera:** El análisis de pagos mediante `SINPE Móvil` y `Transferencia` demuestra ser la vía principal de liquidez, permitiendo al área de cobros enfocar campañas de pronto pago.
2. **Control de Deserción:** La categorización entre estados *Activo/Inactivo* por carrera permite activar alertas tempranas en planes de estudio con mayor tasa de retiro.
3. **Eficiencia de Carga Docente:** El mapeo cruzado entre asignaturas y profesores optimiza la distribución de horas contratadas frente a la demanda real de los estudiantes.