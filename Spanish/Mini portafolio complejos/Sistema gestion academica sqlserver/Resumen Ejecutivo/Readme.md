# Sistema de Gestión Universitaria y Control Académico en SQL Server

## Descripción del Proyecto
Este proyecto, desarrollado por Luis Felipe Rodríguez Arce como parte del módulo de Manejo y Preparación de Datos (Ciencia de Datos), implementa una solución relacional completa en SQL Server para gestionar de forma automatizada los procesos de matrícula, control académico y registro financiero de una institución de educación superior. 

El objetivo central consistió en diseñar una base de datos robusta, funcional y eficiente que garantice la integridad de la información y agilice la toma de decisiones gerenciales y administrativas.

---

## Estructura de la Base de Datos y Modelo E-R

El sistema está compuesto por 9 tablas relacionales interconectadas mediante llaves primarias y foráneas, utilizando tipos de datos optimizados (`INT`, `VARCHAR`, `DECIMAL`, `BIT`, `DATE`, `TIME`)

1. Módulo Académico Tablas `facultad`, `carrera`, `curso` y `profesor` (encargadas del control de planes de estudio, infraestructura de edificios y asignación docente).
2. Gestión Estudiantil Tablas `estudiante`, `matricula` y `detalle_matricula` (administran el registro de alumnos, estados de actividad, programación de horarios y auditoría de los periodos lectivos).
3. Módulo Financiero Tablas `pago` y `factura` (controlan la recaudación, los métodos de pago habilitados y la emisión de facturación).

---

## Consultas Avanzadas y Vistas Operativas

### 1. Análisis y Consultas SQL
Se ejecutó un conjunto integral de consultas en T-SQL para evaluar el rendimiento del negocio educativo
 Filtros y Rangos Uso de `WHERE`, `BETWEEN`, `IN` y `LIKE`.
 Agregaciones Estadísticas Funciones de cálculo como `SUM`, `AVG` y `COUNT` combinadas con `GROUP BY` y `HAVING` para medir recaudación, duración de carreras y promedios de facturación.
 Cruzamientos y Subconsultas Implementación de `JOINs` complejos y subconsultas escalares.

### 2. Vistas Estratégicas Implementadas
Se crearon 6 vistas en el motor de base de datos para automatizar reportes frecuentes y facilitar la consulta ejecutiva sin requerir scripts complejos
 `estudiantes_horarios` Consulta rápida de agendas y clases de los alumnos.
 `resumen_facturacion_estudiante` Control financiero consolidado por estudiante.
 `estudiantes_actividad_carrera` Monitoreo de alumnos activos e inactivos para la prevención de riesgos de deserción.
 `ocupacion_cursos` Control de cupos y cantidad de inscritos por materia.
 `profesor_estudiante` Mapeo de la relación docente-estudiante.
 `auditoria_matricula_periodo` Historial de inscripciones cruzado con los calendarios de los periodos lectivos.

---

## Tecnologías Utilizadas
 Base de Datos Microsoft SQL Server  T-SQL.
 Control de Versiones y Documentación Git, GitHub y entornos de desarrollo SQL.

---

## Conclusiones
 Integridad Garantizada Se estructuró un modelo relacional sólido que elimina la duplicidad de registros y asegura la coherencia estricta entre el área académica y la financiera.
 Eficiencia Administrativa La implementación de vistas operativas permite extraer métricas clave de forma inmediata para optimizar la gestión institucional diaria.