### Proyecto final del modulo de manejo de datos (EDA)
### Final project for the data handling module (EDA)
import os
import re
import pandas as pd
import matplotlib.pyplot as plt
from google.colab import files

### Variable global donde se guarda el dataframe cargado
### Global variable that stores the loaded dataframe
df = None

### Lista donde se guardan los registros ingresados manualmente
### List that stores the manually entered records
nuevos_registros = []


### 1. Carga de datos / Data loading
def cargar_csv():
    ### Muestra el boton de colab para elegir el archivo csv
    ### Shows the colab button to choose the csv file
    global df

    ### Boton "elegir archivos" que abre el selector de colab
    ### "Choose files" button that opens the colab file picker
    archivo_subido = files.upload()

    if not archivo_subido:
        ### El usuario no eligio ningun archivo
        ### The user didn't choose any file
        print("\nNo se selecciono ningun archivo.\n")
        return

    ### Extrae el nombre del archivo subido para poder leerlo con pandas
    ### Extracts the uploaded file's name so it can be read with pandas
    nombre_archivo_subido = next(iter(archivo_subido))

    try:
        df = pd.read_csv(nombre_archivo_subido)
        print(f"\nArchivo cargado correctamente: {nombre_archivo_subido}\n")
        display(df)
    except Exception as error:
        ### Por si el archivo tiene algun problema al leerlo
        ### In case the file has some problem while reading it
        print(f"\nOcurrio un error al cargar el archivo: {error}\n")


def hay_datos_cargados():
    ### Verifica que ya se haya cargado un csv antes de permitir cualquier analisis
    ### Checks that a csv has already been loaded before allowing any analysis
    if df is None:
        print("\nPrimero debes cargar un archivo csv (opcion 1).\n")
        return False
    return True


### 2. Exploracion basica / Basic exploration
def mostrar_info():
    ### Muestra info general: columnas, tipos, cantidad de filas
    ### Shows general info: columns, types, row count
    if not hay_datos_cargados():
        return
    print("\nInformacion general del dataset:")
    print(df.info())
    print(f"\nFilas: {df.shape[0]}  |  Columnas: {df.shape[1]}\n")


def mostrar_filas():
    ### Muestra las primeras y ultimas 5 filas del dataset
    ### Shows the first and last 5 rows of the dataset
    if not hay_datos_cargados():
        return
    print("\nPrimeras 5 filas:")
    print(df.head())
    print("\nUltimas 5 filas:")
    print(df.tail())
    print()


def analizar_tipos_datos():
    ### Muestra el tipo de dato de cada columna
    ### Shows the data type of each column
    if not hay_datos_cargados():
        return
    print("\nTipos de datos por columna:")
    print(df.dtypes)
    print()


def analizar_nulos():
    ### Cuenta los valores nulos o faltantes por columna
    ### Counts null / missing values per column
    if not hay_datos_cargados():
        return
    print("\nValores nulos por columna:")
    print(df.isnull().sum())
    print()


def analizar_duplicados():
    ### Detecta filas duplicadas y permite eliminarlas segun la respuesta del usuario
    ### Detects duplicate rows and removes them based on the user's answer
    global df
    if not hay_datos_cargados():
        return
    cantidad_duplicados = df.duplicated().sum()
    print(f"\nCantidad de filas duplicadas: {cantidad_duplicados}\n")
    if cantidad_duplicados > 0:
        confirmacion_borrado = input("Deseas eliminar los duplicados? (s/n): ").lower()
        if confirmacion_borrado == "s":
            df = df.drop_duplicates()
            print("Duplicados eliminados.\n")


def limites_atipicos(serie):
    ### Calcula el rango normal de una columna numerica usando cuartiles
    ### Q1 = cuartil 25%, Q3 = cuartil 75%, IQR = distancia entre ellos
    ### Todo lo que quede muy lejos de ese rango se considera un dato atipico
    ### Calculates the normal range of a numeric column using quartiles
    ### Q1 = 25th percentile, Q3 = 75th percentile, IQR = distance between them
    ### Anything far outside that range is considered an outlier
    q1 = serie.quantile(0.25)
    q3 = serie.quantile(0.75)
    iqr = q3 - q1
    limite_inferior = q1 - 1.5 * iqr
    limite_superior = q3 + 1.5 * iqr
    return limite_inferior, limite_superior


def analizar_atipicos():
    ### Busca valores atipicos en cada columna numerica usando cuartiles
    ### y muestra TODOS los valores encontrados, no solo la cantidad
    ### Looks for outliers in each numeric column using quartiles
    ### and shows ALL the values found, not just the count
    if not hay_datos_cargados():
        return

    columnas_numericas = list(df.select_dtypes(include="number").columns)

    if not columnas_numericas:
        print("\nNo hay columnas numericas para buscar valores atipicos.\n")
        return

    print("\nValores atipicos por columna numerica (segun cuartiles):")
    for columna_numerica in columnas_numericas:
        datos_columna = df[columna_numerica].dropna()
        limite_inferior, limite_superior = limites_atipicos(datos_columna)
        valores_atipicos = datos_columna[(datos_columna < limite_inferior) | (datos_columna > limite_superior)]

        print(f"\nColumna: {columna_numerica}")
        print(f"Rango normal: {round(limite_inferior, 2)} a {round(limite_superior, 2)}")
        print(f"Cantidad de valores atipicos: {len(valores_atipicos)}")
        if len(valores_atipicos) > 0:
            print("Valores atipicos encontrados:")
            print(valores_atipicos.to_list())
    print()


def estadisticas_descriptivas():
    ### Muestra promedio, minimo, maximo, desviacion estandar, etc
    ### Shows mean, minimum, maximum, standard deviation, etc
    if not hay_datos_cargados():
        return
    print("\nEstadisticas descriptivas:")
    ### Se usa describe() porque en una sola llamada devuelve el promedio, el minimo,
    ### el maximo, la desviacion estandar y los tres cuartiles (25%, 50% que es la
    ### mediana, y 75%)
    ### describe() is used because in a single call it returns the mean, min, max,
    ### standard deviation and the three quartiles (25%, 50% which is the median, and 75%)
    print(df.describe())

    ### Columnas numericas para calcular rango y varianza por separado,
    ### ya que describe() no las incluye
    ### Numeric columns to calculate range and variance separately,
    ### since describe() doesn't include them
    columnas_numericas = list(df.select_dtypes(include="number").columns)

    print("\nRango y varianza por columna numerica:")
    for columna_numerica in columnas_numericas:
        rango = df[columna_numerica].max() - df[columna_numerica].min()
        varianza = df[columna_numerica].var()
        print(f"- {columna_numerica}: rango = {rango}  |  varianza = {round(varianza, 2)}")
    print()


### 3. Filtros y agrupaciones / Filters and groupings
def filtrar_datos():
    ### Filtra el dataset segun la columna y el valor que indique el usuario
    ### Filters the dataset based on the column and value entered by the user
    if not hay_datos_cargados():
        return
    print("\nColumnas disponibles:", list(df.columns))
    print(f"Ejemplo: si quieres filtrar por '{df.columns[0]}', escribe exactamente {df.columns[0]}")
    columna_filtro = input("Columna a filtrar: ")

    if columna_filtro not in df.columns:
        print("Esa columna no existe.\n")
        return

    valor_buscado = input(f"Valor a buscar en '{columna_filtro}': ")
    try:
        ### Convierte la columna a texto antes de comparar, para que el filtro
        ### funcione igual sin importar si la columna es numerica o de texto
        ### Converts the column to text before comparing, so the filter works
        ### the same way whether the column is numeric or text
        filas_filtradas = df[df[columna_filtro].astype(str) == valor_buscado]
        print(f"\nSe encontraron {len(filas_filtradas)} coincidencias:")
        print(filas_filtradas)
        print()
    except Exception as error:
        print(f"Error al filtrar: {error}\n")


def agrupar_datos():
    ### Agrupa por una columna y calcula el promedio de otra
    ### Groups by one column and calculates the average of another
    if not hay_datos_cargados():
        return

    ### Separa las columnas de texto (sirven para agrupar) de las numericas (sirven para calcular)
    ### Separates the text columns (used to group) from the numeric ones (used to calculate)
    columnas_texto = list(df.select_dtypes(exclude="number").columns)
    columnas_numericas = list(df.select_dtypes(include="number").columns)

    print("\nColumnas de texto o categoria (sirven para agrupar):", columnas_texto)
    print("Columnas numericas (sirven para calcular el promedio):", columnas_numericas)

    if columnas_texto:
        ejemplo_grupo = columnas_texto[0]
    else:
        ejemplo_grupo = list(df.columns)[0]

    if columnas_numericas:
        ejemplo_num = columnas_numericas[0]
    else:
        ejemplo_num = list(df.columns)[-1]

    print(f"Ejemplo: agrupar por '{ejemplo_grupo}' y calcular el promedio de '{ejemplo_num}'")
    print("(Escribe el nombre de la columna tal cual aparece en la lista, sin comillas)")

    columna_grupo = input(f"Agrupar por columna (ejemplo: {ejemplo_grupo}): ")
    columna_num = input(f"Columna numerica para calcular el promedio (ejemplo: {ejemplo_num}): ")

    if columna_grupo not in df.columns or columna_num not in df.columns:
        print("Una de las columnas no existe.\n")
        return

    try:
        promedios_por_grupo = df.groupby(columna_grupo)[columna_num].mean()
        print("\nPromedio por grupo:")
        print(promedios_por_grupo)
        print()
    except Exception as error:
        print(f"Error al agrupar: {error}\n")


### 4. Graficos / Charts
### Esta seccion limpia los datos automaticamente antes de graficar
### (elimina duplicados y valores atipicos) y avisa si hay valores nulos
### This section cleans the data automatically before charting
### (removes duplicates and outliers) and warns if there are null values
def normalizar_columna_texto(serie):
    ### Pasa el texto a minusculas y quita espacios extra
    ### para que valores iguales escritos distinto (mayusculas/espacios)
    ### se agrupen como uno solo al graficar
    ### Converts text to lowercase and strips extra spaces
    ### so that equal values written differently (uppercase/spacing)
    ### are grouped together when charting
    return serie.astype(str).str.strip().str.lower()


def generar_graficos():
    ### Menu de graficos: histograma, barras, lineas o dispersion
    ### Chart menu: histogram, bar chart, line chart or scatter plot
    global df
    if not hay_datos_cargados():
        return

    ### Limpieza automatica antes de graficar
    ### Automatic cleaning before charting
    cantidad_duplicados = df.duplicated().sum()
    if cantidad_duplicados > 0:
        df = df.drop_duplicates()

    cantidad_nulos = df.isnull().sum().sum()

    print("\nAviso: el programa limpio los datos automaticamente antes de graficar.")
    print(f"- Duplicados eliminados: {cantidad_duplicados}")
    print(f"- Valores nulos encontrados: {cantidad_nulos}")
    if cantidad_nulos > 0:
        print("  (Los nulos no se eliminan solos, se excluyen solo de la columna que se vaya a graficar)")
    print("  (Las columnas de texto se pasan a minusculas al graficar, para que valores iguales")
    print("   escritos con mayusculas o espacios distintos se agrupen como uno solo)")
    print("  (En las columnas numericas se calculan los cuartiles y se excluyen los valores")
    print("   atipicos que queden muy lejos del rango normal de los datos)")
    print()

    ### Columnas numericas: se usan para validar las columnas antes de graficar
    ### Numeric columns: used to validate the columns before charting
    columnas_numericas = list(df.select_dtypes(include="number").columns)

    print("Tipos de grafico disponibles:")
    print("1. Histograma (para ver como se distribuyen los valores de UNA columna numerica)")
    print("2. Grafico de barras (submenu: solo X, o X y Y)")
    print("3. Grafico de lineas (frecuencia de los valores de UNA columna)")
    print("4. Grafico de dispersion (para ver relacion entre DOS columnas numericas)")
    tipo_grafico = input("Elige una opcion: ")

    print("\nColumnas disponibles:", list(df.columns))
    print(f"(Escribe el nombre tal cual aparece, por ejemplo {df.columns[0]})")

    if tipo_grafico == "1":
        print("\nEste grafico solo necesita el eje X.")
        columna_grafico = input("Columna para el eje X: ")
        if columna_grafico not in df.columns:
            print("Esa columna no existe.\n")
        elif columna_grafico not in columnas_numericas:
            print(f"La columna '{columna_grafico}' no es numerica, no se puede hacer un histograma con ella.\n")
        else:
            ### Excluye los nulos solo de esta columna para no dañar el grafico
            ### Excludes nulls only from this column so they don't damage the chart
            nulos_columna = df[columna_grafico].isnull().sum()
            datos_columna = df[columna_grafico].dropna()
            if nulos_columna > 0:
                print(f"Se excluyeron {nulos_columna} valores nulos de '{columna_grafico}' para este grafico.")

            ### Excluye los valores atipicos de la columna usando el rango calculado por cuartiles
            ### Excludes the column's outliers using the range calculated from quartiles
            limite_inferior, limite_superior = limites_atipicos(datos_columna)
            total_antes_filtro = len(datos_columna)
            datos_columna = datos_columna[(datos_columna >= limite_inferior) & (datos_columna <= limite_superior)]
            valores_atipicos = total_antes_filtro - len(datos_columna)
            if valores_atipicos > 0:
                print(f"Se excluyeron {valores_atipicos} valores atipicos de '{columna_grafico}' "
                      f"(fuera del rango {round(limite_inferior, 2)} a {round(limite_superior, 2)}).")

            datos_columna.hist(color="#2E86AB", edgecolor="white")
            plt.title(f"Histograma de {columna_grafico}")
            plt.xlabel(columna_grafico)
            plt.ylabel("Frecuencia")
            guardar_grafico(f"histograma_{columna_grafico}")

    elif tipo_grafico == "2":
        print("\n--- Submenu: grafico de barras ---")
        print("1. Solo eje X (cuenta cuantas veces se repite cada valor)")
        print("2. Eje X y eje Y (promedio de una columna numerica por categoria)")
        modo_barras = input("Elige una opcion: ")

        if modo_barras == "1":
            columna_grafico = input("Columna para el eje X: ")
            if columna_grafico in df.columns:
                nulos_columna = df[columna_grafico].isnull().sum()
                if nulos_columna > 0:
                    print(f"Se excluyeron {nulos_columna} valores nulos de '{columna_grafico}' para este grafico.")
                datos_columna = df[columna_grafico].dropna()

                if columna_grafico in columnas_numericas:
                    ### Si la columna es numerica, tambien se le quitan los atipicos
                    ### If the column is numeric, outliers are also removed
                    limite_inferior, limite_superior = limites_atipicos(datos_columna)
                    total_antes_filtro = len(datos_columna)
                    datos_columna = datos_columna[(datos_columna >= limite_inferior) & (datos_columna <= limite_superior)]
                    valores_atipicos = total_antes_filtro - len(datos_columna)
                    if valores_atipicos > 0:
                        print(f"Se excluyeron {valores_atipicos} valores atipicos de '{columna_grafico}'.")
                else:
                    ### Normaliza el texto para que valores iguales escritos con mayusculas
                    ### o espacios distintos se cuenten como uno solo
                    ### Normalizes the text so equal values written with different
                    ### uppercase/spacing are counted as one
                    datos_columna = normalizar_columna_texto(datos_columna)

                datos_columna.value_counts().plot(kind="bar", color="#E67E22")
                plt.title(f"Conteo de valores - {columna_grafico}")
                plt.xlabel(columna_grafico)
                plt.ylabel("Cantidad")
                guardar_grafico(f"barras_{columna_grafico}")
            else:
                print("Esa columna no existe.\n")

        elif modo_barras == "2":
            col_x = input("Columna para el eje X (categoria): ")
            col_y = input("Columna para el eje Y (numerica): ")
            if col_x not in df.columns or col_y not in df.columns:
                print("Una de las columnas no existe.\n")
            elif col_y not in columnas_numericas:
                print(f"La columna '{col_y}' no es numerica, no se puede calcular el promedio.\n")
            else:
                ### Excluye las filas con nulos en cualquiera de las dos columnas usadas en este grafico
                ### Excludes rows with nulls in either of the two columns used in this chart
                datos_grafico = df[[col_x, col_y]].dropna()
                nulos_excluidos = len(df) - len(datos_grafico)
                if nulos_excluidos > 0:
                    print(f"Se excluyeron {nulos_excluidos} filas con valores nulos para este grafico.")

                ### Excluye los valores atipicos de la columna numerica del eje Y
                ### Excludes the outliers from the numeric column on the Y axis
                limite_inferior, limite_superior = limites_atipicos(datos_grafico[col_y])
                total_antes_filtro = len(datos_grafico)
                datos_grafico = datos_grafico[(datos_grafico[col_y] >= limite_inferior) & (datos_grafico[col_y] <= limite_superior)]
                valores_atipicos = total_antes_filtro - len(datos_grafico)
                if valores_atipicos > 0:
                    print(f"Se excluyeron {valores_atipicos} filas con valores atipicos de '{col_y}'.")

                if col_x not in columnas_numericas:
                    ### Normaliza la columna de categoria antes de agrupar, para evitar
                    ### que la misma categoria quede repetida por diferencias de formato
                    ### Normalizes the category column before grouping, to avoid the
                    ### same category being duplicated due to formatting differences
                    datos_grafico[col_x] = normalizar_columna_texto(datos_grafico[col_x])
                datos_grafico.groupby(col_x)[col_y].mean().plot(kind="bar", color="#27AE60")
                plt.title(f"Promedio de {col_y} por {col_x}")
                plt.xlabel(col_x)
                plt.ylabel(f"Promedio de {col_y}")
                guardar_grafico(f"barras_{col_x}_{col_y}")
        else:
            print("Opcion no valida.\n")

    elif tipo_grafico == "3":
        print("\nEste grafico solo necesita el eje X.")
        columna_grafico = input("Columna para el eje X: ")
        if columna_grafico not in df.columns:
            print("Esa columna no existe.\n")
        else:
            nulos_columna = df[columna_grafico].isnull().sum()
            if nulos_columna > 0:
                print(f"Se excluyeron {nulos_columna} valores nulos de '{columna_grafico}' para este grafico.")
            datos_columna = df[columna_grafico].dropna()

            if columna_grafico in columnas_numericas:
                ### Si la columna es numerica, tambien se le quitan los atipicos
                ### If the column is numeric, outliers are also removed
                limite_inferior, limite_superior = limites_atipicos(datos_columna)
                total_antes_filtro = len(datos_columna)
                datos_columna = datos_columna[(datos_columna >= limite_inferior) & (datos_columna <= limite_superior)]
                valores_atipicos = total_antes_filtro - len(datos_columna)
                if valores_atipicos > 0:
                    print(f"Se excluyeron {valores_atipicos} valores atipicos de '{columna_grafico}'.")
            else:
                datos_columna = normalizar_columna_texto(datos_columna)

            ### Ordena por el valor de la columna (no por frecuencia) antes de graficar,
            ### para que la linea siga una secuencia logica y no salte de un lado a otro
            ### Sorts by the column's value (not by frequency) before plotting,
            ### so the line follows a logical sequence instead of jumping around
            datos_columna.value_counts().sort_index().plot(kind="line", color="#C0392B", marker="o")
            plt.title(f"Frecuencia de valores - {columna_grafico}")
            plt.xlabel(columna_grafico)
            plt.ylabel("Frecuencia")
            guardar_grafico(f"lineas_{columna_grafico}")

    elif tipo_grafico == "4":
        print("\nEste grafico necesita dos columnas numericas: eje X y eje Y.")
        col_x = input("Columna para el eje X: ")
        col_y = input("Columna para el eje Y: ")
        if col_x not in df.columns or col_y not in df.columns:
            print("Una de las columnas no existe.\n")
        elif col_x not in columnas_numericas or col_y not in columnas_numericas:
            print("Ambas columnas deben ser numericas para hacer un grafico de dispersion.\n")
        else:
            ### Excluye las filas con nulos en cualquiera de las dos columnas usadas en este grafico
            ### Excludes rows with nulls in either of the two columns used in this chart
            datos_grafico = df[[col_x, col_y]].dropna()
            nulos_excluidos = len(df) - len(datos_grafico)
            if nulos_excluidos > 0:
                print(f"Se excluyeron {nulos_excluidos} filas con valores nulos para este grafico.")

            ### Excluye los valores atipicos de ambas columnas (eje X y eje Y)
            ### Excludes the outliers from both columns (X axis and Y axis)
            lim_x_inf, lim_x_sup = limites_atipicos(datos_grafico[col_x])
            lim_y_inf, lim_y_sup = limites_atipicos(datos_grafico[col_y])
            total_antes_filtro = len(datos_grafico)
            datos_grafico = datos_grafico[
                (datos_grafico[col_x] >= lim_x_inf) & (datos_grafico[col_x] <= lim_x_sup) &
                (datos_grafico[col_y] >= lim_y_inf) & (datos_grafico[col_y] <= lim_y_sup)
            ]
            valores_atipicos = total_antes_filtro - len(datos_grafico)
            if valores_atipicos > 0:
                print(f"Se excluyeron {valores_atipicos} filas con valores atipicos de '{col_x}' o '{col_y}'.")

            datos_grafico.plot.scatter(x=col_x, y=col_y, color="#8E44AD")
            plt.title(f"{col_x} vs {col_y}")
            guardar_grafico(f"dispersion_{col_x}_{col_y}")
    else:
        print("Opcion no valida.\n")

    ### Pregunta al usuario si quiere generar otro grafico sin volver al menu principal
    ### Asks the user whether they want to generate another chart without going back to the main menu
    confirmacion_otro_grafico = input("Quieres generar otro grafico? (s/n): ").lower()
    if confirmacion_otro_grafico == "s":
        generar_graficos()


def guardar_grafico(nombre_base):
    ### Guarda el grafico como imagen png para poder pegarlo despues en el documento de Word
    ### Saves the chart as a png image so it can be pasted later into the Word document
    plt.savefig(f"{nombre_base}.png")
    print(f"Grafico guardado como {nombre_base}.png")
    print(f"Ruta completa: {os.path.abspath(nombre_base)}.png")
    plt.show()
    plt.close()


### 4.1 Analisis adicional / Additional analysis
def detectar_formato_fechas():
    ### Busca columnas de texto que parezcan de fecha y compara cuantos
    ### registros usan cada formato (AAAA-MM-DD vs DD/MM/AAAA). Si encuentra
    ### una mezcla, ofrece estandarizar la columna a un solo formato, para
    ### que un ordenamiento o grafico por fecha no salga mal sin darse cuenta.
    ### Looks for text columns that look like dates and compares how many
    ### records use each format (YYYY-MM-DD vs DD/MM/YYYY). If it finds a
    ### mix, it offers to standardize the column to a single format, so that
    ### sorting or charting by date doesn't silently break.
    global df

    patron_anio_mes_dia = r"^\d{4}-\d{2}-\d{2}$"
    patron_dia_mes_anio = r"^\d{2}/\d{2}/\d{4}$"

    columnas_texto = list(df.select_dtypes(exclude="number").columns)
    columna_fecha_encontrada = False

    print("\nRevision de formato de fecha en columnas de texto:")
    for columna_texto in columnas_texto:
        valores_columna = df[columna_texto].dropna().astype(str)
        if valores_columna.empty:
            continue

        coincide_anio_mes_dia = valores_columna.str.match(patron_anio_mes_dia)
        coincide_dia_mes_anio = valores_columna.str.match(patron_dia_mes_anio)
        total_coincidencias = (coincide_anio_mes_dia | coincide_dia_mes_anio).sum()

        ### Solo se trata como columna de fecha si la mayoria de sus valores
        ### coinciden con alguno de los dos formatos esperados
        ### Only treated as a date column if most of its values match
        ### one of the two expected formats
        if total_coincidencias / len(valores_columna) < 0.5:
            continue

        columna_fecha_encontrada = True
        cantidad_formato_1 = int(coincide_anio_mes_dia.sum())
        cantidad_formato_2 = int(coincide_dia_mes_anio.sum())
        cantidad_sin_formato_reconocido = len(valores_columna) - total_coincidencias

        print(f"\nColumna: {columna_texto}")
        print(f"- Formato AAAA-MM-DD: {cantidad_formato_1} registros")
        print(f"- Formato DD/MM/AAAA: {cantidad_formato_2} registros")
        if cantidad_sin_formato_reconocido > 0:
            print(f"- Valores con un formato distinto o no reconocido: {cantidad_sin_formato_reconocido}")

        if cantidad_formato_1 > 0 and cantidad_formato_2 > 0:
            print("  Esta columna mezcla dos formatos de fecha distintos.")
            confirmacion_estandarizar = input(
                f"  Deseas estandarizar '{columna_texto}' a formato AAAA-MM-DD? (s/n): "
            ).lower()
            if confirmacion_estandarizar == "s":
                df[columna_texto] = df[columna_texto].apply(
                    lambda valor: convertir_fecha_a_formato_estandar(valor, patron_anio_mes_dia, patron_dia_mes_anio)
                )
                print(f"  Columna '{columna_texto}' estandarizada a formato AAAA-MM-DD.")

    if not columna_fecha_encontrada:
        print("No se detectaron columnas con formato de fecha reconocible.\n")
    else:
        print()


def convertir_fecha_a_formato_estandar(valor, patron_anio_mes_dia, patron_dia_mes_anio):
    ### Convierte un valor de fecha en AAAA-MM-DD o DD/MM/AAAA al formato
    ### unico AAAA-MM-DD. Si el valor no coincide con ninguno de los dos
    ### formatos conocidos, se deja igual para no perder informacion.
    ### Converts a date value in YYYY-MM-DD or DD/MM/YYYY into the single
    ### YYYY-MM-DD format. If the value doesn't match either known format,
    ### it's left unchanged so no information is lost.
    texto = str(valor)
    if re.match(patron_anio_mes_dia, texto):
        return texto
    elif re.match(patron_dia_mes_anio, texto):
        dia, mes, anio = texto.split("/")
        return f"{anio}-{mes}-{dia}"
    else:
        return texto


def analisis_adicional():
    ### Calcula la correlacion entre las columnas numericas
    ### para ver que tan relacionadas estan unas con otras
    ### Calculates the correlation between numeric columns
    ### to see how related they are to each other
    if not hay_datos_cargados():
        return

    columnas_numericas = list(df.select_dtypes(include="number").columns)
    columnas_texto = list(df.select_dtypes(exclude="number").columns)

    if len(columnas_numericas) >= 2:
        print("\nMatriz de correlacion entre columnas numericas:")
        print("(Valores cercanos a 1 o -1 indican una relacion fuerte entre las variables)")
        print(df[columnas_numericas].corr())
    else:
        print("\nSe necesitan al menos dos columnas numericas para calcular correlaciones.")

    ### Revisa si hay valores negativos en las columnas numericas
    ### Checks for negative values in the numeric columns
    print("\nValores negativos por columna numerica:")
    for columna_numerica in columnas_numericas:
        valores_negativos = (df[columna_numerica] < 0).sum()
        print(f"- {columna_numerica}: {valores_negativos} valores negativos")

    ### Revisa las columnas de texto en busca de posibles inconsistencias de mayusculas o espacios
    ### Checks the text columns for possible uppercase/spacing inconsistencies
    print("\nPosibles inconsistencias de formato en columnas de texto:")
    for columna_texto in columnas_texto:
        valores_originales = df[columna_texto].nunique()
        valores_normalizados = df[columna_texto].astype(str).str.lower().str.strip().nunique()
        if valores_originales > valores_normalizados:
            print(f"- {columna_texto}: {valores_originales} valores distintos, pero solo {valores_normalizados} despues de normalizar mayusculas y espacios")
    print()

    ### Revisa tambien si hay columnas con formatos de fecha mezclados
    ### Also checks for columns with mixed date formats
    detectar_formato_fechas()


### 5. Ingreso manual de datos (submenu) / Manual data entry (submenu)
def submenu_ingreso():
    ### Submenu para agregar nuevos registros a mano
    ### Submenu to add new records manually
    while True:
        print("\n--- Submenu: ingreso de datos ---")
        print("1. Ingresar un nuevo registro")
        print("2. Mostrar registros ingresados")
        print("3. Guardar los nuevos datos")
        print("4. Regresar al menu principal")
        opcion_submenu = input("Elige una opcion: ")

        if opcion_submenu == "1":
            ingresar_registro()
        elif opcion_submenu == "2":
            mostrar_registros()
        elif opcion_submenu == "3":
            guardar_registros()
        elif opcion_submenu == "4":
            break
        else:
            print("Opcion no valida, intenta de nuevo.\n")


def convertir_valor_a_tipo_columna(valor_texto, nombre_columna):
    ### Intenta convertir el texto ingresado al mismo tipo de dato que tiene
    ### esa columna en el dataset original (numero entero, decimal o texto),
    ### para que al juntar los registros nuevos con el csv no se dañen los
    ### calculos de esa columna.
    ### Tries to convert the entered text into the same data type that
    ### column has in the original dataset (integer, float or text), so
    ### that merging the new records with the csv doesn't break that
    ### column's calculations.
    if valor_texto == "":
        ### Campo vacio: se guarda como valor faltante, no como texto vacio
        ### Empty field: stored as a missing value, not as empty text
        return None

    tipo_columna = df[nombre_columna].dtype

    try:
        if pd.api.types.is_integer_dtype(tipo_columna):
            return int(valor_texto)
        elif pd.api.types.is_float_dtype(tipo_columna):
            return float(valor_texto)
        else:
            return valor_texto
    except ValueError:
        print(f"Aviso: '{valor_texto}' no es un numero valido para '{nombre_columna}', se guarda como texto.")
        return valor_texto


def ingresar_registro():
    ### Solicita un valor por cada columna del dataset para armar un nuevo registro,
    ### convirtiendo cada valor al tipo de dato que corresponde segun el csv original
    ### Asks for a value for each dataset column to build a new record,
    ### converting each value to the data type it has in the original csv
    if not hay_datos_cargados():
        print("Debes cargar un csv primero para conocer la estructura.\n")
        return

    registro = {}
    print("\nIngresa la informacion para cada columna:")
    for nombre_columna in df.columns:
        valor_ingresado = input(f"{nombre_columna}: ")
        registro[nombre_columna] = convertir_valor_a_tipo_columna(valor_ingresado, nombre_columna)

    nuevos_registros.append(registro)
    print("Registro guardado en memoria.\n")


def mostrar_registros():
    ### Muestra todos los registros ingresados durante esta sesion
    ### Shows all the records entered during this session
    if not nuevos_registros:
        print("\nAun no se han ingresado registros nuevos.\n")
        return
    print("\nRegistros ingresados:")
    for indice, registro in enumerate(nuevos_registros, start=1):
        print(f"{indice}. {registro}")
    print()


def guardar_registros():
    ### Guarda los registros nuevos en un archivo csv aparte, y tambien los agrega
    ### al dataset actual si ya hay uno cargado
    ### Saves the new records to a separate csv file, and also adds them
    ### to the current dataset if one is already loaded
    global df
    if not nuevos_registros:
        print("\nNo hay registros nuevos para guardar.\n")
        return

    nuevos_df = pd.DataFrame(nuevos_registros)

    if df is not None:
        df = pd.concat([df, nuevos_df], ignore_index=True)
        print("\nLos nuevos registros se agregaron al dataset actual.\n")

    nombre_archivo = input("Nombre del archivo para guardar los registros nuevos (sin extension): ")
    nuevos_df.to_csv(f"{nombre_archivo}.csv", index=False)
    print(f"Registros guardados como {nombre_archivo}.csv\n")


### Readme / Informacion del proyecto
def mostrar_readme():
    ### Presenta un resumen del proyecto: de que se trata, como esta seccionado
    ### el codigo, como funciona por dentro y como se usa. Pensado para que
    ### alguien que abre el programa por primera vez entienda todo sin tener
    ### que leer el codigo fuente.
    ### Presents a summary of the project: what it's about, how the code is
    ### sectioned, how it works internally, and how to use it. Meant so that
    ### someone opening the program for the first time understands it
    ### without having to read the source code.
    print("""
    PROYECTO FINAL - MANEJO DE DATOS (EDA)


De que se trata:

Este programa carga un archivo CSV y permite explorarlo, limpiarlo,
analizarlo y graficarlo de forma interactiva, aplicando las tecnicas
de Analisis Exploratorio de Datos (EDA) vistas en el modulo: revision
de tipos de datos, valores nulos, duplicados, valores atipicos,
estadisticas descriptivas, filtros, agrupaciones, graficos y
correlacion entre variables.


Como esta destribuido el codigo

  1. Carga de datos
     Sube el archivo CSV y lo guarda en memoria para el resto
     del programa.

  2. Exploracion basica
     Informacion general, primeras/ultimas filas, tipos de dato
     y valores nulos por columna.

  3. Filtros y agrupaciones
     Deteccion de duplicados y de valores atipicos (por cuartiles),
     estadisticas descriptivas, filtros por columna/valor y
     agrupaciones con promedios.

  4. Graficos
     Histograma, barras, lineas y dispersion. Antes de graficar,
     el programa limpia duplicados, avisa de nulos y excluye
     valores atipicos automaticamente para no distorsionar la
     imagen.

  4.1 Analisis adicional
      Matriz de correlacion entre columnas numericas, conteo de
      valores negativos y deteccion de inconsistencias de texto
      (mayusculas/espacios).

  5. Ingreso manual de datos (submenu)
     Permite escribir registros nuevos a mano, verlos y guardarlos
     en un CSV aparte.


Como funciona el codigo

  El dataframe cargado se guarda en la variable global df, y todas
  las funciones de analisis la leen (o la modifican, cuando hace
  falta, como al borrar duplicados) desde ahi, en vez de pasarla
  de funcion en funcion.

  Cada opcion del menu esta conectada a una funcion propia (por
  ejemplo, la opcion 5 llama a analizar_nulos()), asi que cada
  herramienta se puede leer y probar por separado.

  Antes de dejar analizar o graficar cualquier cosa, se llama a
  hay_datos_cargados(), que revisa que ya exista un csv en memoria.
  Si no hay datos, avisa y regresa al menu en vez de fallar.

  El menu principal y los submenus corren dentro de un ciclo
  while True que se repite hasta que el usuario elige salir o
  regresar, y las opciones invalidas se manejan con un else que
  avisa y vuelve a mostrar el menu, sin cerrar el programa.


Como se usa

  - Empieza siempre por la opcion "Cargar archivo csv": mientras no
    haya un archivo cargado, el menu solo deja cargar uno, ver este
    Readme o salir.
  - Una vez cargado el archivo, se abre el menu completo con todas
    las herramientas de analisis numeradas.
  - Cada herramienta se elige escribiendo el numero de la opcion.
  - El submenu de ingreso de datos (opcion 13) tiene su propio menu
    para no mezclarse con el analisis del archivo original.
  - En cualquier momento se puede volver a cargar otro CSV desde la
    opcion 1 del menu completo, o salir con la ultima opcion.
""")


### Menu principal / Main menu
def menu_principal():
    ### Medida de seguridad: el menu completo solo se muestra despues de cargar un csv
    ### Security measure: the full menu is only shown after a csv has been loaded
    while True:
        print("\nProyecto final - manejo de datos (EDA)\n")

        if df is None:
            ### Menu reducido: se muestra mientras no haya ningun csv cargado
            ### Reduced menu: shown while no csv has been loaded yet
            print("1. Cargar archivo csv")
            print("2. Ver Readme (informacion del proyecto)")
            print("3. Salir")

            opcion_menu = input("\nElige una opcion: ")

            if opcion_menu == "1":
                cargar_csv()
            elif opcion_menu == "2":
                mostrar_readme()
            elif opcion_menu == "3":
                print("\nSaliendo del programa. Hasta luego!")
                break
            else:
                print("\nOpcion no valida, intenta de nuevo.\n")

        else:
            ### Menu completo: se muestra una vez que ya hay un csv cargado en memoria
            ### Full menu: shown once a csv has already been loaded into memory
            print("1. Cargar otro archivo csv")
            print("2. Mostrar informacion del conjunto de datos")
            print("3. Mostrar primeras y ultimas filas")
            print("4. Analizar tipos de datos")
            print("5. Analizar valores nulos")
            print("6. Analizar datos duplicados")
            print("7. Analizar valores atipicos")
            print("8. Obtener estadisticas descriptivas")
            print("9. Filtrar o consultar datos")
            print("10. Realizar agrupaciones")
            print("11. Generar representaciones graficas")
            print("12. Realizar analisis adicional")
            print("13. Ingresar nuevos datos (submenu)")
            print("14. Salir")

            opcion_menu = input("\nElige una opcion: ")

            if opcion_menu == "1":
                cargar_csv()
            elif opcion_menu == "2":
                mostrar_info()
            elif opcion_menu == "3":
                mostrar_filas()
            elif opcion_menu == "4":
                analizar_tipos_datos()
            elif opcion_menu == "5":
                analizar_nulos()
            elif opcion_menu == "6":
                analizar_duplicados()
            elif opcion_menu == "7":
                analizar_atipicos()
            elif opcion_menu == "8":
                estadisticas_descriptivas()
            elif opcion_menu == "9":
                filtrar_datos()
            elif opcion_menu == "10":
                agrupar_datos()
            elif opcion_menu == "11":
                generar_graficos()
            elif opcion_menu == "12":
                analisis_adicional()
            elif opcion_menu == "13":
                submenu_ingreso()
            elif opcion_menu == "14":
                print("\nSaliendo del programa. Hasta luego!")
                break
            else:
                print("\nOpcion no valida, intenta de nuevo.\n")


### Punto de entrada del programa / Program entry point
if __name__ == "__main__":
    menu_principal()