import pandas as pd
import matplotlib.pyplot as plt


#documento = 'Consolidado_de_ventas.xlsx'
#df = pd.read_excel(documento, sheet_name='ENERO')
# la función read_excel() lee el archivo .xlsx que le escribimos y tambien puede seleccionar la hoja para trabajar.
#resultados = df.plot.line()
# Con df.plot.line() se puede graficar un conjunto de datos 
#plt.show()
# Con plt.show se puede puede mostrar el gráfico

datos = {'Productos':['Zapatos', 'Ropa', 'Polos', 'Micas'], 'Costos':[250, 440, 220, 1200]}
df = pd.DataFrame(datos)

df.plot(x='Productos', y='Costos', kind='bar')
plt.show()
