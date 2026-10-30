# Predicción y Análisis Estadístico de Sorteos con Machine Learning

Nota solo funciona en colab

## Descripción del Proyecto
Este proyecto implementa un pipeline completo de procesamiento de datos históricos de sorteos para realizar análisis de frecuencias, mapas de calor y **predicciones de múltiples salidas (Multi-Output Classification)** utilizando algoritmos de aprendizaje automático en Python. 

El script procesa archivos Excel con registros de sorteos, transforma los datos a un formato de matriz binaria histórica y entrena un modelo de ensamblaje (*Random Forest*) para estimar la probabilidad de aparición de los números.

---

## ¿Qué se puede encontrar en este proyecto?

El script de Python incluye las siguientes etapas clave:

1. **Carga y Limpieza Automatizada:** Importación dinámica de archivos de Excel, eliminación de filas/columnas vacías y normalización de nombres de columnas.
2. **Procesamiento de Fechas y Series Temporales:** Detección automática de columnas de fechas, conversión a formato `datetime` y ordenamiento cronológico de los sorteos.
3. **Matriz Binaria Histórica:** Transformación de los números ganadores de cada sorteo en una tabla binaria de presencia/ausencia para un rango de 0 a 99.
4. **Ingeniería de Características (Features):** Creación de variables predictoras basadas en medias móviles (`rolling window` de 28 sorteos) para capturar tendencias recientes.
5. **Modelado Predictivo de Múltiples Salidas:** 
   * Uso de `MultiOutputClassifier` combinado con `RandomForestClassifier` (100 estimadores).
   * División de datos en conjuntos de entrenamiento y prueba sin mezclar la cronología (`shuffle=False`).
6. **Evaluación de Rendimiento:** Cálculo de la exactitud (*accuracy*) del modelo frente a la probabilidad teórica estimada por azar.
7. **Visualizaciones Avanzadas (Seaborn y Matplotlib):**
   * **Mapa de Calor:** Distribución de apariciones en los últimos sorteos agrupados por decenas.
   * **Importancia de Variables:** Gráfico de barras con el Top 10 de números con mayor peso de importancia según el modelo.
   * **Comparativa de Rendimiento:** Gráfica de barras contrastando la precisión del modelo predictivo frente al azar.

---

## Tecnologías y Librerías Utilizadas
* **Python**
* **Pandas & NumPy** (Manipulación y estructuración de matrices de datos)
* **Scikit-Learn** (Modelos de clasificación, `RandomForestClassifier`, `MultiOutputClassifier` y métricas de evaluación)
* **Matplotlib & Seaborn** (Generación de mapas de calor y gráficos estadísticos personalizados)

---

## Utilidades y Aplicaciones
* Permite automatizar la lectura de reportes históricos de sorteos o eventos numéricos recurrentes.
* Sirve como base práctica para la aplicación de modelos de clasificación multietiqueta (*multi-label / multi-output*) en series temporales.
* Facilita la interpretación visual rápida mediante dashboards estáticos generados directamente con scripts de análisis exploratorio.