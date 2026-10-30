
from pandas.core.dtypes.missing import notna
from google.colab import files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Colores para los graficos
color_fondo_crema = "#FDFBF7"
plt.rcParams['figure.facecolor'] = color_fondo_crema
plt.rcParams['axes.facecolor'] = color_fondo_crema
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
# 1. Carga del archivo
uploaded = files.upload()
nombre_archivo = list(uploaded.keys())[0]
# 2. Lectura y limpieza inicial
df = pd.read_excel(nombre_archivo, sheet_name=0)
df = df.dropna(axis=1, how="all")
df.columns = [str(c).strip() for c in df.columns]
# 3. Procesamiento de fechas y ordenamiento
col_fecha = [c for c in df.columns if "Fecha" in c][0]
df[col_fecha] = pd.to_datetime(df[col_fecha])
df = df.sort_values(col_fecha).reset_index(drop=True)
# 4. Selección de columnas numericas
cols_numeros = [c for c in df.columns if "Número" in c and "Sorteo" not in c]
print(f"{len(df)} sorteos cargados, del {df[col_fecha].min().date()} al {df[col_fecha].max().date()}")
# 5. Convertir a formato de tabla binaria historica
rango_100 = list(range(100))
binaria = pd.DataFrame(0, index=df.index, columns=rango_100)
for c in cols_numeros:
    for idx, val in df[c].items():
        if pd.notna(val):
            binaria.loc[idx, int(val)] = 1
# 6. Crear variables predictoras
ventana = 28
n_sorteos = 569
muestra = binaria.tail(n_sorteos).reset_index(drop=True)
x = pd.DataFrame({
    f"f_{num}": muestra[num].rolling(ventana, min_periods=1).mean().shift(1).fillna(0)
    for num in rango_100
})
y = muestra
print("x (variables):", x.shape)
print("y (objetivo):", y.shape)
# 7. Entrenar al modelo
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.multioutput import MultiOutputClassifier
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.5, shuffle=False)
modelo = MultiOutputClassifier(
    RandomForestClassifier(n_estimators=100, max_depth=5, random_state=45)
)
modelo.fit(x_train, y_train)
pred = modelo.predict(x_test)
# 8. Evaluar el modelo
from sklearn.metrics import accuracy_score
acc_modelo = accuracy_score(y_test.values.ravel(), pred.ravel())
acc_azar = 3 / 100
print(f"\nexactitud del modelo: {acc_modelo:.2%}")
print(f"exactitud esperada por azar: {acc_azar:.2%}")
# 9. Prediccion
x_ultimo = x.tail(1)
probabilidades = np.array([
    modelo.estimators_[i].predict_proba(x_ultimo)[0][1]
    for i in range(len(rango_100))
])
ranking = pd.DataFrame({
    "numero": rango_100,
    "probabilidad": probabilidades
}).sort_values("probabilidad", ascending=False).reset_index(drop=True)
print("--Numeritos recomendados:", ranking.loc[0, "numero"])
print(f"---Probabilidad estimada: {ranking.loc[0, 'probabilidad']:.2%}")
print("-_"*55)
print("\n el top 25 numeros con mas probabiliad de salir:")
print(ranking.head(25).to_string(index=False))
# 10. Graficos
print(">"*160)
# Grafico 1: Mapa de calor
fig, ax = plt.subplots(figsize=(10, 7))
fig.patch.set_facecolor(color_fondo_crema)
ax.set_facecolor(color_fondo_crema)
ultimos_datos = muestra.tail(ventana).sum().values.reshape(10, 10)
sns.heatmap(ultimos_datos, annot=True, fmt="d", cmap="YlOrBr", cbar=True,
            xticklabels=range(10), yticklabels=[f"{i*0}-{i*9+9}" for i in range(10)], ax=ax)
plt.title(f'Apariciones en los ultimos {ventana} Sorteos', fontsize=14, fontweight='bold', pad=15, color="#2c3e50")
plt.xlabel('Numeros de 0 a 9', fontsize=11, labelpad=10, color="#2c3e50")
plt.ylabel('Decenas', fontsize=11, labelpad=10, color="#2c3e50")
plt.tight_layout()
plt.show()
print("-_"*90)
# Grafico 2: Importancia de variable
fig, ax = plt.subplots(figsize=(10, 5))
fig.patch.set_facecolor(color_fondo_crema)
ax.set_facecolor(color_fondo_crema)
importancias = np.mean([est.feature_importances_ for est in modelo.estimators_], axis=0)
df_imp = pd.DataFrame({'numero': rango_100, 'importancia': importancias}).sort_values('importancia', ascending=False).head(10)
df_imp['etiqueta'] = df_imp['numero'].apply(lambda n: f"Nº {n:02d}")
sns.barplot(x='etiqueta', y='importancia', hue='etiqueta', data=df_imp, palette='copper', legend=False, ax=ax)
plt.title('Top 10 Numeros con mayor probabilidad', fontsize=14, fontweight='bold', pad=15, color="#2c3e50")
plt.xlabel('Numero', fontsize=11, labelpad=10, color="#2c3e50")
plt.ylabel('Peso de Importancia', fontsize=11, labelpad=10, color="#2c3e50")
plt.tight_layout()
plt.show()
print("."*145)
# Grafico 3: Comparacion de Rendimiento
fig, ax = plt.subplots(figsize=(6, 5))
fig.patch.set_facecolor(color_fondo_crema)
ax.set_facecolor(color_fondo_crema)
categorias = ['Modelo predictico', 'El azar']
valores = [acc_modelo * 100, acc_azar * 100]
sns.barplot(x=categorias, y=valores, hue=categorias, palette=['#d97706', '#9ca3af'], legend=False, ax=ax)
plt.title('Comparacion de exactitud', fontsize=14, fontweight='bold', pad=15, color="#2c3e50")
plt.ylabel('Porcentaje', fontsize=11, labelpad=10, color="#2c3e60")
plt.ylim(0, 105)
for p in ax.patches:
    h = p.get_height()
    ax.annotate(f'{h:.2f}%',
                (p.get_x() + p.get_width() / 2., h),
                ha='center', va='bottom', fontsize=11, fontweight='bold', xytext=(0, 4),
                textcoords='offset points', color="#2c3e40")
plt.tight_layout()
plt.show()