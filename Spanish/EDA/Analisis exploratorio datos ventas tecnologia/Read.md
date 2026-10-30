Readme
Manejo de datos (EDA)

1. Cargar archivo csv
2. Ver Readme (informacion del proyecto)
3. Salir

Elige una opcion: 2

    PROYECTO FINAL - MANEJO DE DATOS (EDA)


De que se trata

Este programa carga un archivo CSV y permite explorarlo, limpiarlo,
analizarlo y graficarlo de forma interactiva, aplicando las tecnicas
de Analisis Exploratorio de Datos (EDA) vistas en el modulo: revision
de tipos de datos, valores nulos, duplicados, valores atipicos,
estadisticas descriptivas, filtros, agrupaciones, graficos y
correlacion entre variables.


Como esta seccionado el codigo

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