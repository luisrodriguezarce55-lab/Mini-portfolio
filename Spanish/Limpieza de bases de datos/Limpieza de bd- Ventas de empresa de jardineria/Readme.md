# Limpieza, Transformación de Datos (ETL) y Modelado en Power Query — Vivero El Jardín Oriental

## Descripción del Proyecto
Este proyecto documenta el proceso completo de **ETL (Extracción, Transformación y Carga)** realizado en **Power Query** para una base de datos comercial del **Vivero El Jardín Oriental**. 

El archivo original presentaba múltiples inconsistencias operativas derivadas del registro descentralizado en distintas cajas y hojas de cálculo. El objetivo principal de este proyecto fue estandarizar, depurar y estructurar la información para garantizar la máxima confiabilidad antes de su integración en un tablero analítico en Power BI.

---

## Principales Errores Encontrados y Correcciones Aplicadas

El proceso de depuración abarcó la resolución de más de 25 tipos de anomalías críticas, entre las cuales destacan:

1. **Tipos de Datos Erróneos:** Conversión de campos numéricos clave (`ID_Venta`, `ID_Cliente`) almacenados incorrectamente como texto a formatos enteros y decimales.
2. **Integridad de Datos y Duplicados:** Eliminación de filas 100% duplicadas (incrementando la unicidad del registro de ventas) y supresión de valores nulos críticos en campos obligatorios como `Nombre_Cliente`, `Ciudad`, `Vendedor` y `Metodo_Pago`.
3. **Normalización de Fechas (`Fecha_Venta`):** 
   * Homologación de formatos de texto mezclados.
   * Corrección de fechas inválidas e lógicas (ej. el inexistente `31/02/2025`).
   * Filtrado del rango temporal operativo (del 01/01/2024 al 31/12/2025) para eliminar registros atípicos fuera de período (1998 y 2030).
4. **Estandarización de Textos Geográficos y Categóricos:** 
   * Limpieza de espacios excedentes mediante la función de recorte (`Trim`).
   * Corrección ortográfica y de mayúsculas en nombres de ciudades (ej. estandarización de variaciones como `ESCAZÚ` y `PÉREZ ZELEDON`).
   * Consolidación de categorías de productos y nombres de artículos que presentaban variantes tipográficas y abreviaturas inconsistentes.
5. **Corrección de Valores Numéricos y Métricas:**
   * Eliminación de cadenas de texto concatenadas (ej. la palabra "unidades" en la columna de cantidad).
   * Manejo de valores negativos y ceros mediante la función de valor absoluto (`Number.Abs`) y filtros de exclusión en precios unitarios y cantidades atípicas o ilógicas (ej. 5,000 a 12,000 unidades).
6. **Depuración de Contactos (`Email_Cliente` y `Telefono`):**
   * Corrección de errores en dominios de correo electrónico (reemplazo de comas por puntos en dominios erróneos como `correo,com`).
   * Normalización de números telefónicos a un formato estándar de 8 dígitos.

---

## Estructura del Repositorio
* **`documentacion/`**: Incluye los reportes y detalles descriptivos del proceso de transformación.
* **`capturas_power_query/`**: Evidencias gráficas del historial de pasos aplicados en Power Query (`Applied Steps`).

---

## Conclusión sobre la Calidad de los Datos
Antes de la intervención en Power Query, la confiabilidad de la base de datos era sumamente baja debido a la ausencia de controles de calidad en el origen. Tras la ejecución de este pipeline de limpieza, la información quedó completamente estructurada, sin duplicados ni valores atípicos, asegurando métricas financieras y comerciales precisas para la toma de decisiones gerenciales.