import pandas as pd

df = pd.read_excel('ul_elements.xlsx')
df.columns =['Lista']
df.to_excel('ul_elements.xlsx')