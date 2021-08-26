import pandas as pd
from funcoes.pontosProximos import *
from funcoes.logradouro import *
from funcoes.menu import menu

df = pd.read_csv('pontos_taxi.csv', delimiter = ';', index_col=0)
pd.set_option('display.max_rows', None)

while True:
    op = menu()
    if(op == 1):
        MostraPontos(df)
    elif(op == 2):
        dados = Localizacao()
    elif(op == 3):
        PegaCoords(df, dados[0], dados[1])
    elif(op == 4):
        logradouro(df)
    elif(op == 5):
        break


