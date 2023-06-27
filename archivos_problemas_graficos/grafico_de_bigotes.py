import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("archivos_problemas_graficos\\bigotes.csv")

#creando el grafico
sns.boxplot(x="categoria",y="valor",data=df)

#mostrando el grafico
plt.show()

'''

forma basica de leer archivos :

import pandas as pa
import matplotlib.pyplot as plt
import seaborn as sns
df = pd. read_csv ('bigote.csv')
sns.boxplot (x= 'categoría', y='value', data=df)
plt. show()

para archivos grandes:
import pandas as pd
def read_csv_in_chunks(file_name):
    for i, chunk in enumerate (pd. read_csv(file_name, chunksize=1000)):
        print ("Chunk #{}" .format(i))
        print(chunk)
read_csv_in_chunks("big_file.csv")

#con archivos aun mas grandes que se puedan leer en bloques:
import csv
def read_csv_in_chunks(file_name):
    with open(file_name, 'r') as f:
        reader = csv. reader (f)
        header = next(reader)
        for i, chunk in enumerate(reader):
            print ("Chunk #{}" .format(i))
            print(chunk)
read_csv_in_chunks ("big_file.csv")
'''
