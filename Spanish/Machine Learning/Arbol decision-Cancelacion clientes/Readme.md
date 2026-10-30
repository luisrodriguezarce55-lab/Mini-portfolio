# Predicción de Cancelación de Clientes con Árboles de Decisión (StreamTico)

Nota: solo funciona en colab

## Descripción del Proyecto
Este proyecto implementa un flujo completo de ciencia de datos enfocado en la limpieza de datos ruidosos y en el modelado predictivo para la retención de clientes en la plataforma simulada StreamTico. 

El script procesa hojas de cálculo de Excel con errores deliberados e inconsistencias (duplicados, rangos fuera de lógica, símbolos de moneda, tildes y nulos), realiza un preprocesamiento robusto y entrena un modelo de Árbol de Decisión para predecir si un cliente cancelará o no el servicio.

---

## ¿Qué se encuentra en este proyecto

El cuaderno de Google Colab incluye el desarrollo paso a paso

1. Inspección y Carga de Datos Importación interactiva de archivos Excel, lectura de hojas de clientes y análisis exploratorio inicial (`head`, `info`, `describe`).
2. Depuración y Corrección de Errores de Datos
    Eliminación de registros duplicados por `id_cliente`[cite 3].
    Filtrado y tratamiento de valores fuera de rango biológico o temporal (edades e intervalos de meses activos).
    Imputación de valores faltantes mediante la mediana para conservar la estructura del dataset.
    Corrección de valores negativos en quejas mediante el valor absoluto (`.abs()`).
    Limpieza de caracteres monetarios (`₡`, comas) en el gasto mensual para transformarlo a formato numérico.
    Estandarización de variables categóricas de texto en las columnas `plan` y `cancelo`.
3. Ingeniería de Características y Selección
    Codificación de variables categóricas a formato binario (`get_dummies`) para el plan.
    Definición estratégica de la variable objetivo (`cancelo`) y exclusión de variables irrelevantes o de fuga de datos (como `id_cliente` y `encuesta_salida`).
4. Modelado Predictivo
    División de datos en conjuntos de entrenamiento (80%) y prueba (20%).
    Entrenamiento de un `DecisionTreeClassifier` con una profundidad máxima controlada (`max_depth=3`) para facilitar la interpretabilidad
5. Evaluación y Visualización
    Medición de la exactitud del modelo mediante `accuracy_score`.
    Generación y trazado gráfico del Árbol de Decisión (`plot_tree`).
6. Predicción sobre Nuevos Clientes Carga de un subconjunto de nuevos clientes para clasificar su riesgo potencial de cancelación.

---

## Tecnologías y Librerías Utilizadas
 Python
 Pandas & NumPy (Manipulación, limpieza y tratamiento de nulos)
 Scikit-Learn (`DecisionTreeClassifier`, `plot_tree`, `train_test_split`, `accuracy_score`)
 Matplotlib (Visualización del árbol de decisión y diagramas)

---

## Conclusiones y Utilidad para el Negocio
 Detección Temprana El modelo demuestra que la tasa de cancelación está fuertemente relacionada con una alta incidencia de quejas combinada con baja permanencia temporal.
 Recomendación Estratégica Se sugiere a la gerencia enfocar esfuerzos en automatizar la retención, mejorar la experiencia de usuario (UX) para mitigar errores del sistema y ofrecer atención prioritaria y beneficios de fidelización a los clientes en riesgo.