# Predicción de Abandono y Segmentación de Clientes en E-commerce (TicoShop)

## Descripción del Proyecto
Este proyecto de Machine Learning e Inteligencia de Negocios está enfocado en el sector **Retail / E-commerce** (específicamente simulado para la plataforma *TicoShop*). Su objetivo principal es analizar el comportamiento histórico de compra de los clientes para identificar patrones de deserción, segmentar la base de usuarios mediante análisis RFM (Recencia, Frecuencia y Monto) y desplegar un modelo predictivo capaz de anticipar qué clientes tienen mayor probabilidad de abandonar el negocio.

Lo anterior permite a los equipos comerciales y de retención enfocar sus esfuerzos presupuestarios y operativos en la retención de clientes de alto valor antes de que se produzca la pérdida.

---

## ¿Qué se puede encontrar en este proyecto?

El cuaderno de Jupyter / Google Colab incluye el desarrollo paso a paso del flujo de ciencia de datos:

1. **Exploración y Análisis de Datos (EDA):** Carga y limpieza de datos, estandarización de columnas y análisis comparativo de variables clave entre los clientes que retienen y los que abandonan (recencia, frecuencia, monto, quejas y uso de la aplicación).
2. **Segmentación RFM y K-Means:** 
   * Asignación de puntuaciones de Recencia, Frecuencia y Monto (RFM) mediante cuantiles.
   * Agrupación de clientes en 4 clústeres mediante el algoritmo **K-Means**, etiquetándolos comercialmente como *Campeones*, *Regulares*, *Enfriándose* y *Dormidos*.
3. **Modelado Predictivo de Abandono (Churn):**
   * Entrenamiento y validación de modelos de clasificación: **Regresión Logística** y **Árbol de Decisión**.
   * Evaluación de métricas clave como **Recall** y **Precisión**.
4. **Análisis de Factores de Riesgo:** Extracción e interpretación de los coeficientes del modelo logístico para identificar qué variables incrementan o reducen la probabilidad de que un cliente se vaya.
5. **Plan de Acción Comercial:** Generación automática de una lista prioritaria de clientes con alto riesgo de abandono y mayor valor monetario para focalizar campañas de retención directa (ej. C1343, C1848, etc.).

---

## Tecnologías y Librerías Utilizadas
* **Python**
* **Pandas & NumPy** (Manipulación y análisis de datos)
* **Scikit-Learn** (Estandarización, K-Means, Regresión Logística, Árboles de Decisión y métricas de evaluación)
* **Matplotlib** (Visualización de datos y gráficos analíticos).

---

## Utilidades del Negocio
* **Optimización de Presupuesto:** Permite centrar los incentivos y descuentos en los clientes correctos en lugar de hacer campañas masivas ineficaces.
* **Mitigación de Fuga de Ingresos:** Protege la cartera de clientes de mayor valor (LTV).
* **Estrategia de Retención Proactiva:** Automatiza la detección de alertas tempranas basadas en el comportamiento del usuario (como días sin comprar o incremento en quejas).