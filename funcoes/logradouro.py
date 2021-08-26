import os

def MostraPonto(arq, array, log):
    os.system('cls') or None
    print(f'\nOs pontos de taxi ao longo de {log} são:\n')
    print(arq.iloc[array])


def buscaLogradouro(log, arq):
    dado = arq['logradouro']
    tam = len(dado)
    pontos = []
    flag = 0
    
    for index in range(tam):
        if(dado[index].startswith(log)):
            pontos.append(index)
            flag += 1
    if(flag):
        MostraPonto(arq, pontos, log)
    else: 
        print('\nNenhum logradouro foi encontrado.')

def logradouro(arq):
    os.system('cls') or None
    log = input('Digite todo ou parte do logradouro:\n')
    log = log.upper()
    buscaLogradouro(log, arq)