#Estructura que obtengo de la configuracion del juego
fichas = {
'A':{'cantidad':11,'valor':1},
'B':{'cantidad':3,'valor':1},
'C':{'cantidad':4,'valor':1},
'D':{'cantidad':4,'valor':1},
'E':{'cantidad':11,'valor':6},
'F':{'cantidad':2,'valor':1},
'G':{'cantidad':2,'valor':1},
'H':{'cantidad':2,'valor':1},
'I':{'cantidad':6,'valor':1},
'J':{'cantidad':2,'valor':1},
'K':{'cantidad':1,'valor':1},
'L':{'cantidad':4,'valor':1},
'LL':{'cantidad':1,'valor':1},
'M':{'cantidad':3,'valor':1},
'N':{'cantidad':5,'valor':1},
'Ñ':{'cantidad':1,'valor':1},
'O':{'cantidad':8,'valor':9},
'P':{'cantidad':2,'valor':3},
'Q':{'cantidad':1,'valor':1},
'R':{'cantidad':4,'valor':1},
'RR':{'cantidad':1,'valor':20},
'S':{'cantidad':7,'valor':1},
'T':{'cantidad':4,'valor':1},
'U':{'cantidad':6,'valor':1},
'V':{'cantidad':2,'valor':1},
'W':{'cantidad':1,'valor':1},
'X':{'cantidad':1,'valor':1},
'Y':{'cantidad':1,'valor':1},
'Z':{'cantidad':1,'valor':1}}

#Estructura que obtengo del la interfaz del tablero
tablero={(7, 4):{"letra": "RR",
             "trampa": True,
             "tipo_de_trampa": 1,
             "recompensa": False,
             "tipo_de_recompensa": None},
     (7, 5):{"letra": "O",
             "trampa": False,
             "tipo_de_trampa": None,
             "recompensa": True,
             "tipo_de_recompensa": 3},
     (7, 2):{"letra": "P",
             "trampa": False,
             "tipo_de_trampa": None,
             "recompensa": True,
             "tipo_de_recompensa": 2},
     (7, 3):{"letra": "E",
             "trampa": True,
             "tipo_de_trampa": 2,
             "recompensa": False,
             "tipo_de_recompensa": None}}

#Ordeno palabra que entra por si entra desordenada
#Ordeno el diccionario por posiciones de menor a mayor
dic2=dict(sorted(tablero.items(), key = lambda diccio: diccio[0]))
print('----------------------------------')
for k,v in dict.items(tablero):
    print(k)
    print(v)
print('----------------------------------')
for k,v in dict.items(dic2):
    print(k)
    print(v)
print('----------------------------------')

#Inicializo puntuacion actual, y variables de trampa y bonus
puntuacionActual = 0

bonusValor = 1
trampaValor = 0
trampa = False
bonus = False

#Obtengo la puntuacion
for k,v in dict.items(dic2):
    
    #Obtengo el valor por cada letra ingresada
    puntuacionActual = (puntuacionActual + fichas[v['letra']]['valor'])

    #Pregunto si la palabra que obtuve del tablero tiene casilleros trampa o bonus
    if(dic2[k]['trampa']==True):
        trampaValor= trampaValor + dic2[k]['tipo_de_trampa']
        trampa=True
    if(dic2[k]['recompensa']==True):
        bonusValor= bonusValor * dic2[k]['tipo_de_recompensa']
        bonus=True

print("Puntuacion Total")
print(puntuacionActual)
print('----------------------------------')
print("trampa")
print(trampaValor)
print('----------------------------------')
print("bonus")
print(bonusValor)
print('----------------------------------')

#Chequeo trampas y bonuses
if(bonus == True):
    puntuacionActual = puntuacionActual * bonusValor
    if(trampa==True):
        puntuacionActual = puntuacionActual - trampaValor

print("Puntuacion Total")
#Puntuacion final
print(puntuacionActual)

#38
#225 total