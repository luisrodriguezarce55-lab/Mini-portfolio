
#Paso 1

import pandas as pd #Para importar pandas
import numpy as np #Para importar numpy
import matplotlib.pyplot as plt #Para importar matplotlib

from sklearn.tree import DecisionTreeClassifier, plot_tree  #Para incorporar sklearn.tree, train_test_split
from sklearn.metrics import accuracy_score #Para incorporar sklearn.metrics, accuracy_score
from google.colab import files #Para incorporar google.colab files

#Paso 2

# cargar el archivo de excel interactivo mediante un botón en colab
archivo_subido = files.upload()
nombre_archivo_excel = list(archivo_subido.keys())[0]

#Paso 3

# lee la hoja de clientes del archivo y explorar su estructura general
df_clientes = pd.read_excel(nombre_archivo_excel, sheet_name='clientes')
df_clientes = df_clientes.dropna(axis=1, how="all")
df_clientes.columns = [str(columna).strip() for columna in df_clientes.columns]
# escribe ("las primeras 5 filas de la base de datos:")
print("las primeras 5 filas de la base de datos:")
display(df_clientes.head())
#escribe información de la base de datos y los tipos de datos de ella:
print("\ninformación de la base de datos y los tipos de datos de ella:")
df_clientes.info()
# Escribe informacion de lasw variables numericas:
print("\ninformacion de lasw variables numericas:")
display(df_clientes.describe())

"""#Paso 4
Errores del excel
1. id_cliente,df_clientes.duplicated(subset=['id_cliente']): Eliminación de registros duplicados conservando la primera instancia.

2. edad,Filtrado de valores fuera del rango biológico lógico <18 o >100.: Reemplazo por valores nulos np.nan para posterior imputación.

3. meses_activo,Validación de umbrales temporales suscripciones >60 meses o
'<'1: ,Asignación de valores nulos ante inconsistencias temporales.

4. meses_activo,Conteo de valores nulos con .isnull().sum(). :Imputación de datos faltantes empleando la mediana de la columna.

5. quejas,Filtrado condicional de registros con valores numéricos negativos.: Conversión de valores negativos a positivos absolutos .abs()\.

6. gasto_mensual,Evaluación del tipo de dato objeto con caracteres monetarios.: Limpieza de símbolos (₡) y comas para transformar a formato numérico.

7. plan,Inspección de valores únicos .unique() con variaciones tipográficas.: "Estandarización de mayúsculas, espacios y acentos ortográficos."

8. cancelo,Verificación de cadenas de texto heterogéneas en la variable dependiente.: "Unificación de variantes nominales al formato estándar ("Sí" / "No").

9. cancelo,Identificación de registros nulos previos a la codificación de texto.: Eliminación de filas sin datos en la variable objetivo.

10. edad,Cuantificación de nulos generados tras la depuración inicial de edad.: Imputación de los espacios vacíos resultantes utilizando la mediana.
"""

#Paso 5

print(f"filas originales antes de corregir errores: {len(df_clientes)}")

# error 1: elimina las filas duplicadas que tienen el mismo id_cliente
df_clientes = df_clientes.drop_duplicates(subset=['id_cliente'], keep='first')

# error 2: pasar a nulos las edades fuera del rango válido de 18 a 100 años, porque son los rangos mas determinados para no eliminar personas que pueden ser clientes
df_clientes.loc[(df_clientes['edad'] < 18) | (df_clientes['edad'] > 100), 'edad'] = np.nan

# error 3: pasa a nulos los meses de suscripción ilógicos dando entender que no puedes subscribir menos de un mes si uno es el minimo o mayores a 60 meses no se puede porque se toma como datos corrupto
df_clientes.loc[(df_clientes['meses_activo'] < 1) | (df_clientes['meses_activo'] > 60), 'meses_activo'] = np.nan

# error 4: rellenar los valores vacíos de meses_activo usando la mediana, y se uso la mediana para no perder datos valiosos y dañar la estructura si quiciera usar promedios
df_clientes['meses_activo'] = df_clientes['meses_activo'].fillna(df_clientes['meses_activo'].median())

# error 5: convertir las quejas negativas en valores positivos absolutos porque se ve como un dedazo del usuario
df_clientes.loc[df_clientes['quejas'] < 0, 'quejas'] = df_clientes['quejas'].abs()

# error 6: limpiar el símbolo de colón y comas del gasto mensual para pasarlo a numérico para que no se dañe el Árbol de Decisión porque no pueden hacer operaciones matemáticas con text
if df_clientes['gasto_mensual'].dtype == object:
    df_clientes['gasto_mensual'] = df_clientes['gasto_mensual'].astype(str).str.replace('₡', '').str.replace(',', '').str.strip()
    df_clientes['gasto_mensual'] = pd.to_numeric(df_clientes['gasto_mensual'], errors='coerce')

# error 7: estandarizar los nombres de la colunma planes quitando espacios, tildes y mayúsculas
df_clientes['plan'] = df_clientes['plan'].astype(str).str.strip().str.capitalize()
df_clientes['plan'] = df_clientes['plan'].replace({'Basico': 'Básico', 'Estandar': 'Estándar'})

# error 8: borrar filas vacias en la columna cancelo
df_clientes = df_clientes.dropna(subset=['cancelo'])

# error 9: unificar las variantes de texto en cancelacion asi no ahi variantes iguales pero escritas diferente
df_clientes['cancelo'] = df_clientes['cancelo'].astype(str).str.strip().str.capitalize()
df_clientes['cancelo'] = df_clientes['cancelo'].replace({'Si': 'Sí', 'No ': 'No'})

# error 10: rellenar los espacios vacíos de edad resultantes de la limpieza usando la mediana y se uso la mediana para no perder datos valiosos y dañar la estructura si quiciera usar promedios
df_clientes['edad'] = df_clientes['edad'].fillna(df_clientes['edad'].median())

print(f"filas despues de ser corregidas: {len(df_clientes)}")
print("revisando nulos:\n", df_clientes[['edad', 'meses_activo', 'quejas', 'plan', 'gasto_mensual', 'cancelo']].isnull().sum())

"""Paso 6 -
Significado de las variables x y y

Variable Y:
 Elegí la columna cancelo porque es justamente lo que queremos que el modelo aprenda a predecir (si el cliente se va a ir del servicio o se va a quedar).

 Variables X

 Para que el modelo tenga buenas pistas, se incluyo la edad, los meses_activo, las quejas, el gasto_mensual y el tipo de plan convertido a columnas binarias.

 Estas características reflejan de forma directa el comportamiento y la satisfacción de cada usuario.

 Las variables que se dejaron fuera: Por un lado, descarto el id_cliente porque es solo un código numérico único que no aporta ningún patrón estadístico útil es mas por referencia de la empresa.

  Por otro lado, se decidio omitir la encuesta_salida a propósito para evitar una perdidad de datos, ya que esa información solo se genera después de que el cliente ya tomó la decisión de cancelar, lo cual falsearía el aprendizaje del modelo.
"""

#Paso 7
# convertir la column plan a binario
df_modelo_streamtico = pd.get_dummies(df_clientes, columns=['plan'], drop_first=True)

# definir variables predictoras la x y variable objetivo la y
variables_predictoras = df_modelo_streamtico[['edad', 'meses_activo', 'quejas', 'gasto_mensual'] + [columna for columna in df_modelo_streamtico.columns if columna.startswith('plan_')]]
variable_objetivo = df_modelo_streamtico['cancelo']

# separar datos dejando 80% para entrenamiento y 20% para prueba
X_entrenamiento, X_prueba, y_entrenamiento, y_prueba = train_test_split(variables_predictoras, variable_objetivo, test_size=0.2, random_state=42)

#Paso 8
# configurar el árbol de decisión con una profundidad que sea maximo a 3 y random state de 42
arbol_decision_cliente = DecisionTreeClassifier(max_depth=3, random_state=42)
arbol_decision_cliente.fit(X_entrenamiento, y_entrenamiento)

# colocar el arbol de decision
plt.figure(figsize=(30, 12))
plot_tree(arbol_decision_cliente, feature_names=list(variables_predictoras.columns), class_names=['No', 'Sí'], filled=True, rounded=True)
plt.title("arbol de Decisión de Cancelación de los clientes de StreamTico")
plt.show()

#Paso 9
# medir la exactitud del modelo evaluando con el arbol de desicion
predicciones_prueba = arbol_decision_cliente.predict(X_prueba)
exactitud_modelo = accuracy_score(y_prueba, predicciones_prueba)
print(f"exactitud del modelo {exactitud_modelo * 100:.2f}%")

#Paso 10
# cargar la hoja de clientes nuevos y aplicar la misma estructura columnas
df_clientes_nuevos = pd.read_excel(nombre_archivo_excel, sheet_name='clientes_nuevos')
df_nuevos_codificados = pd.get_dummies(df_clientes_nuevos, columns=['plan'], drop_first=True)

for columna in variables_predictoras.columns:
    if columna not in df_nuevos_codificados.columns:
        df_nuevos_codificados[columna] = 0
X_clientes_nuevos = df_nuevos_codificados[variables_predictoras.columns]

# realiza la predicción para determinar qué clientes nuevos puede que cancelen o no el servicio
df_clientes_nuevos['prediccion_cancelo'] = arbol_decision_cliente.predict(X_clientes_nuevos)
print(" La prediccion para nuevos clientes")
display(df_clientes_nuevos[['id_cliente', 'edad', 'meses_activo', 'quejas', 'plan', 'prediccion_cancelo']])

"""#Paso 11
Conclusiones y Recomendaciones para mejorar StreamTico:

Los resultados del árbol de decisión demuestra que existe una deserción de usuarios constante y el motivo es la alta incidencia de quejas combinada con una baja cantidad de constancia temporales en la plataforma.

Se recomieda a la gerencia de StreamTico enfocar esfuerzos de retención automatizados y aplicacion de mejoramiento UX en para y en los clientes debido que aumentado la quejas de las bugs del sistema, asi tambien aprovechar en dar atención prioritaria y beneficios de fidelización para mitigar la tasa de cancelación.
"""

