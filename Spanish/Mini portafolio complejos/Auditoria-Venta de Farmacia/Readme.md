# Análisis de Ventas de Farmacia, Limpieza ETL y Modelado SQL

## Descripción del Proyecto
Este proyecto integra la arquitectura completa de inteligencia de negocios para una cadena de farmacias en Costa Rica, abarcando desde la estructuración de la base de datos relacional en **SQL Server**, la depuración y transformación de datos en **Power Query**, hasta la creación de un cuadro de mando ejecutivo interactivo en **Power BI**.

El análisis evalúa el comportamiento comercial durante el primer semestre del año (**01/01/2026 al 30/06/2026**), analizando **₡2.74 Millones CRC** en ventas totales distribuidas en sucursales regionales, categorías de medicamentos y tipos de seguro.

---

## Estructura del Proyecto

### 1. Modelo Relacional e Infraestructura SQL (`farmacia.sql`)
Creación de la base de datos `farmacia` en SQL Server y definición de tablas relacionales clave:
* **`Sucursales`:** Identificador, nombre de sucursal, provincia y encargado.
* **`Clientes`:** Datos demográficos, provincia y tipo de seguro (`Privado`, `CCSS`, `Ninguno`).
* **`Medicamentos`:** Catálogo de 25 productos, categorías, precio unitario y requerimiento de receta médica.
* **`Ventas`:** Registro transaccional que vincula fecha, sucursal, cliente, medicamento, cantidades y totales en moneda local (CRC).

---

### 2. Pipeline de Limpieza de Datos y ETL en Power Query (`Limpieza_de_datos.docx`)
Aplicación de reglas de calidad de datos para garantizar la integridad analítica:
* **Estandarización Categórica:** Corrección de inconsistencias tipográficas en nombres de sucursales (ej. *sucursal heredios* a *Sucursal Heredia*).
* **Tratamiento de Inconsistencias Temporales:** Corrección de fechas inválidas (como el inexistente *31/02/2026*) sustituyéndolas por el límite válido más cercano (*01/03/2026*) para evitar pérdida de registros.
* **Eliminación de Duplicados y Corrección de Rangos:** Supresión de filas repetidas en `Venta_ID` y conversión de cantidades negativas (*-3* a *3*) interpretadas como errores de digitación.
* **Manejo de Valores Nulos:** Imputación de un ID genérico (`0`) para clientes desconocidos o ventas de mostrador (*walk-in*), y para sucursales no identificadas sin alterar los montos agregados de venta.
* **Formateo de Monedas y Tipos de Datos:** Conversión de texto a número entero/moneda (CRC) en precios y totales, y limpieza de espacios excedentes (*trim*) en nombres de clientes.

---

### 3. Dashboard de Ventas en Power BI (`Dashboard-Venta_de_Farmacia.pbix`)
Visualización de indicadores clave de rendimiento (KPIs) e insights comerciales:
* **Ventas Totales:** **₡2.74 Millones CRC**.
* **Ventas por Categoría de Medicamento:** Jerarquización de ingresos liderada por *Cardiovasculares*, *Antibióticos* y *Dermatológicos*, seguidos por *Vitaminas*, *Antigripales*, *Gastrointestinales*, *Analgésicos* y *Antialérgicos*.
* **Distribución por Tipo de Seguro:** Desglose del volumen comercial según perfil de cliente (*39.68% Seguro Privado*, *31.27% CCSS*).
* **Ventas que Precisan Receta:** Identificación del porcentaje de ventas sujetas a regulación médica.
* **Participación por Sucursal:** Distribución porcentual balanceada entre las sucursales (aproximadamente ~20% por sucursal).
* **Tendencia Mensual:** Comportamiento temporal acumulado entre enero y junio de 2026.

---

## Tecnologías Utilizadas
* **Microsoft SQL Server / SQL:** Definición de esquemas de datos relacionales.
* **Power BI Desktop & Power Query:** Proceso ETL, modelado dimensional DAX y diseño visual de dashboards.
* **Microsoft Excel & Word:** Documentación del registro de errores y base de datos origen.

---

## Conclusiones del Análisis
1. **Calidad de Datos Restablecida:** La estandarización de sucursales e imputación de clientes desconocidos permitió conservar la totalidad de las ventas registradas sin sesgar el balance contable.
2. **Productos Clave:** La alta concentración de ventas en medicamentos *Cardiovasculares* y *Antibióticos* sugiere enfocar los esfuerzos de gestión de inventario y negociación con proveedores en estas categorías de alta rotación.
3. **Equilibrio Operativo:** Las ventas se mantienen distribuidas de forma equitativa entre las distintas sucursales regionales, reflejando una demanda sólida a nivel provincial.