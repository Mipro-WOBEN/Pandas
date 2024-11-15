import pandas as pd
import matplotlib.pyplot as plt


documento = 'Consolidado_de_ventas.xlsx'
df = pd.read_excel(documento, sheet_name='ENERO')
RangoExtraer=df.loc[0:5,'Vendedora']
print(type(RangoExtraer))
print(RangoExtraer)
ListaVendedores = []
for item in RangoExtraer:
    ListaVendedores.append(item)
RangoExtraerFilas = df.loc[0:5,'Maquillaje']
ListaMaquillaje = []
for item in RangoExtraerFilas:
    ListaMaquillaje.append(item)



datos = {
    "Vendedores":ListaVendedores,"Maquillaje":ListaMaquillaje
    }
dw=pd.DataFrame(datos)
# la función read_excel() lee el archivo .xlsx que le escribimos y tambien puede seleccionar la hoja para trabajar.
resultados = dw.plot(x="Vendedores",y="Maquillaje",kind="line")
# Con df.plot.line() se puede graficar un conjunto de datos 
plt.show()
# Con plt.show se puede puede mostrar el gráfico

#datos = {'Productos':['Zapatos', 'Ropa', 'Polos', 'Micas'], 'Costos':[250, 440, 220, 1200]}
#df = pd.DataFrame(datos)
#
#df.plot(x='Productos', y='Costos', kind='bar')
#plt.show()
