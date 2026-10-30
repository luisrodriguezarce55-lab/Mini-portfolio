# Pipeline de Limpieza, Auditoría y Transformación de Datos (Online Retail)

**Desarrollado por:** Luis Felipe Rodríguez Arce  
**Lenguaje:** Python  
**Librerías principales:** Pandas, NumPy, `python-docx`, Tkinter  

---

## 1. Descripción del Proyecto
Este proyecto implementa un **Pipeline automatizado de Ingeniería y Limpieza de Datos** diseñado para auditar, depurar y enriquecer grandes volúmenes de datos transaccionales (basado en el conjunto de datos de comercio electrónico *Online Retail*). 

El script no solo limpia anomalías estructurales y de contenido, sino que **automatiza la generación de un reporte ejecutivo oficial en formato Word (`.docx`)** detallando cada métrica, error detectado y acción correctiva aplicada.

---

## 2. Resumen de Métricas del Pipeline
* **Registros iniciales (filas):** 541,909
* **Registros limpios finales (filas):** 467,335
* **Total de registros filtrados o modificados:** 74,574
* **Estado:** Totalmente auditado, corrección de errores de tipeo en cantidades a valores positivos, importes monetarios limpios y enriquecido para análisis avanzado.

---

## 3. Fases del Proceso de Limpieza y Auditoría

El script ejecuta un flujo secuencial robusto de 11 pasos:

1. **Eliminación de Duplicados:** Detección y supresión de 5,268 filas idénticas duplicadas para evitar la inflación artificial de las métricas comerciales.
2. **Estandarización de Texto:** Limpieza de espacios en blanco, conversión de códigos a mayúsculas y formateo de descripciones.
3. **Manejo de Datos Corruptos:** Identificación de celdas vacías o símbolos extraños (`?`, `??`) transformándolos de manera estandarizada a la etiqueta `'UNKNOWN'` (1,509 registros).
4. **Diferenciación de Productos y Cargos:** Separación de artículos físicos frente a cargos administrativos o de entrega (como costos de franqueo, comisiones o tarifas de Amazon) mediante validación de códigos (`StockCode`).
5. **Gestión de IDs de Clientes Faltantes:** Reemplazo de los 135,037 valores nulos en el identificador de cliente por la etiqueta `'N/D'` (No Disponible).
6. **Procesamiento Temporal:** Conversión de fechas a formato estándar y extracción de variables de tiempo (*YearMonth*, *Month*, *DayOfWeek*, *Hour*).
7. **Validación Numérica:** Conversión estricta de tipos de datos para cantidades y precios unitarios.
8. **Corrección de Errores de Tipeo en Cantidades:** Transformación de 10,587 cantidades negativas (introducidas por error operativo) en valores absolutos positivos para preservar el volumen de ventas legítimo.
9. **Filtrado de Precios No Comerciales:** Exclusión de 2,512 registros con precios menores o iguales a cero.
10. **Eliminación de Valores Atípicos (*Outliers*):** Aplicación rigurosa del método del Rango Intercuartílico (IQR) para remover 66,794 valores extremos e inconsistencias severas.
11. **Cálculo de Ingresos:** Generación de la métrica financiera `TotalAmount` multiplicando cantidad por precio unitario, redondeada a 2 decimales.

---

## 4. Enriquecimiento de Datos (*Feature Engineering*)
* **`IsProduct`:** Etiqueta booleana que separa elementos de inventario reales de cobros administrativos.
* **`YearMonth`:** Campo en formato `YYYY-MM` ideal para análisis de series temporales y tableros de control (*dashboards*).
* **Componentes de Tiempo:** Extracción detallada de mes, día de la semana y hora para estudiar patrones de comportamiento del consumidor.
* **`TotalAmount`:** Métrica de ingresos por línea de transacción.

---

## 5. Automatización de Reportes (`Data_Cleaning_Report.docx`)
Mediante la integración de la librería `python-docx`, el programa compila de manera autónoma un documento Word estructurado con:
* Resumen general del estado del dataset.
* Tabla de registro detallado de errores y correcciones (Bitácora de auditoría).
* Tabla explicativa con las nuevas columnas creadas y su propósito comercial.

---

## 6. Tecnologías y Librerías
* **Python:** Lenguaje principal de programación.
* **Pandas & NumPy:** Manipulación, análisis y limpieza de estructuras tabulares masivas.
* **Python-Docx:** Creación programática y estilización tipográfica de reportes en Word.
* **Tkinter:** Interfaz gráfica nativa para la selección interactiva de archivos mediante diálogos del sistema operativo.