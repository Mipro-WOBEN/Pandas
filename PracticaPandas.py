import pandas as pd
import matplotlib.pyplot as plt

# Crear un DataFrame de ejemplo
data = {'A': [1, 2, 3, 4, 5], 'B': [10, 20, 30, 40, 50]}
df = pd.DataFrame(data)

# Crear un gráfico simple
df.plot(x='A', y='B', kind='line')

# Mostrar el gráfico
plt.show()

#start winword Nombredelarchivo -> Abre un archivo word
#start excel Nombredelarchivo -> Abre un archivo excel

#plt.show() #-> Muestra una grafica


#Contadas = df3['Column3'].value_counts() # -> Da el numero de veces que existe una categoria en una columna, por ejemplo, de M001 hay 500 y M002 hay 200
#ListaValores = [i for i in range(1,44)] #Crea un lista de valores
#df3.columns = ListaValores #La lista se almacena en la lista de columnas del datagrama 'df3'
#print(df3.head(5))


#df3.drop_duplicates() #-> Quitar dupicados
#df3.dropna(inplace=True, axis=1) #-> Eliminar datos null
#resultado = df2.loc[df['Column2']=='2024REY10600003283', ['Column1', 'Column2', 'Column3']] #Me trae 3 columnas y una fila que tenga un valor en especifico
#Partes = df2.loc[2:10]
#Aislar = df2[df2.index.isin(range(2,10))]
#df2.loc[2:5, 'Column1'] = None
#resultado = df2['Column1'].isnull().head(7) #Aqui defino que columna puedo traer, si tiene valores nulos dentro de un rango de filas.
#print(df2['Column1'].isnull().head(7).sum())
#print(f'De {df2.shape[0]} son valores null')
# df2.loc[2:5, 'Column1'] -> Establece valores en un rango dentro de una columna
# df2.isnull().sum() -> Para contar el numero de nulos de cada columna
# df2.isnull().head() -> Para comprobar si falta algun elemento
# df2 = df.copy -> Realizamos una copia de la lista principal
#print(list(df.columns)) -> nombres de las columnas en una lista para manipular
#print(df.columns) -> nombres de las columnas
#print(df.shape[0]) -> numero de filas
#print(df.shape[1]) -> numero de columnas
#df.shape -> Da el numero de columnas y filas

#df.read_excel(nombre_del_archivo, sheet_name=  nombre_de_la_hoja) #-> Acceder a una hoja especifica dentro del archivo
#hojas = pd.ExcelFile(nombre_archivo).sheet_names #->Imprimir todas las hojas de archivo


#df = pd.read_csv('ListaDetra.TXT', sep="\t", encoding='latin1')