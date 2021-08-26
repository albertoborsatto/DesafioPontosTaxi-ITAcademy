import os
from math import radians, sin, cos, sqrt, asin
from operator import itemgetter


def MostraPontos(arq):
    os.system('cls') or None
    print(arq)


def Troca(lat, lon, char1, char2):
    lat = lat.replace(char1, char2)
    lon = lon.replace(char1, char2)
    return [lat, lon]


def Localizacao():
    os.system('cls') or None
    lat = input('Digite sua latitude: ')
    lon = input('Digite sua longitude: ')
    coords1 = Troca(lat, lon, ',', '.')
    return [coords1[0], coords1[1]]


def Ordena(array):
    array = sorted(array, key=itemgetter(0))
    return array

def TestaIguais(lat, lon, arq, indice, flag):
    search1 = arq['latitude']
    search2 = arq['longitude']
    
    for index in range(len(search1)):
        if(flag):
            if(index != indice):
                if(search1[index] == lat and search2[index] == lon):
                    return index
        else:
            if(search1[index] == lat and search2[index] == lon):
                return index
   
def Mostra(array, arq):
    os.system('cls') or None
    print('Os pontos de taxi mais próximos são:\n')
    print(arq.iloc[[array[0], array[1], array[2]]])


def MaisProximos2(stringArray, arq):
    flag = 0
    indice = 0
    pontos = []
    
    for coord in stringArray:
        final = Troca(coord[0], coord[1], '.', ',')
        lat = final[0]
        lon = final[1]
        if(lat == '1,0'): lat = '1'
        if(lon == '1,0'): lon = '1'
        print(lat, lon)
        indice = TestaIguais(lat, lon, arq, indice, flag)
        flag += 1
        pontos.append(indice)
    Mostra(pontos, arq)
    

def FloatToString(array):
    for coord in array:
        coord[0] = str(coord[0])
        coord[1] = str(coord[1])
    return array


def MaisProximos(array, arq):
    ostres = []
    final = Ordena(array)
    
    for i in range(3):
        ostres.append(final[i][1:])
    string = FloatToString(ostres)
    MaisProximos2(string, arq)


def PegaCoords(arq, lat1, lon1):
    dists = []
    lat = arq['latitude']
    lon = arq['longitude']

    for linha in range(len(lat)):
        coords2 = Troca(lat[linha], lon[linha], ',', '.')
        final = Haversine(float(lat1), float(lon1), float(coords2[0]), float(coords2[1]))
        dists.append(final)
    MaisProximos(dists, arq)
        

def Haversine(lat1, lon1, lat2, lon2):
    aux1 = lat2
    aux2 = lon2
    
    R = 6372.8

    dLat = radians(lat2 - lat1)
    dLon = radians(lon2 - lon1)
    lat1 = radians(lat1)
    lat2 = radians(lat2)

    a = sin(dLat / 2)**2 + cos(lat1) * cos(lat2) * sin(dLon / 2)**2
    c = 2 * asin(sqrt(a))
    return [R * c, aux1, aux2]
    


