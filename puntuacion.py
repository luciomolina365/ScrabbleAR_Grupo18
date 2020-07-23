#Estructura que obtengo de la configuracion del juego
configuracion = {
'A':{'cantidad':11,'valor':1},
'B':{'cantidad':3,'valor':1},
'C':{'cantidad':4,'valor':1},
'D':{'cantidad':4,'valor':1},
'E':{'cantidad':11,'valor':2},
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
'O':{'cantidad':8,'valor':2},
'P':{'cantidad':2,'valor':2},
'Q':{'cantidad':1,'valor':1},
'R':{'cantidad':4,'valor':1},
'RR':{'cantidad':1,'valor':10},
'S':{'cantidad':7,'valor':1},
'T':{'cantidad':4,'valor':1},
'U':{'cantidad':6,'valor':1},
'V':{'cantidad':2,'valor':1},
'W':{'cantidad':1,'valor':1},
'X':{'cantidad':1,'valor':1},
'Y':{'cantidad':1,'valor':1},
'Z':{'cantidad':1,'valor':1}}


#Estructura que obtengo de la interfaz del tablero
tablero={(7, 4):{"letra": "RR",#9
                "trampa": True,
                "tipo_de_trampa": 1,
                "recompensa": False,
                "tipo_de_recompensa": None},
        (7, 5):{"letra": "O", #6
                "trampa": False,
                "tipo_de_trampa": None,
                "recompensa": True,
                "tipo_de_recompensa": 3},
        (7, 2):{"letra": "P", #4
                "trampa": False,
                "tipo_de_trampa": None,
                "recompensa": True,
                "tipo_de_recompensa": 2},
        (7, 3):{"letra": "E", #0
                "trampa": True,
                "tipo_de_trampa": 2,
                "recompensa": False,
                "tipo_de_recompensa": None}}
def armo_mi_tablero(tablero):
    #Obtengo el tablero como quiero, para trabajar con el
    tablero2={}
    for k,v in tablero.items():
        tablero2[v['letra']]=v
    for k,v in tablero2.items():
        del tablero2[k]['letra']

    return(tablero2)

def __puntuar_jugador__(palabra,configuracion,tablero2):
    
    #Inicializo puntuacion actual, y variables de trampa y bonus
    puntuacionActual = 0

    indice = 0
    for k,v in tablero2.items():
        
        #Pregunto si la letra que obtuve de la palabra que ingresa en el tablero donde esta puesta tiene trampa o bonus
        if(tablero2[palabra[0]]['trampa']==False):
            #puntuacionActual = ((puntuacionActual + configuracion[v['letra']]['valor'])-(tablero[k]['tipo_de_trampa']))
            print('Es trampa')
        #elif(dic2[k]['recompensa']==True):
            #puntuacionActual = puntuacionActual + ((configuracion[v['letra']]['valor'])*(tablero[k]['tipo_de_recompensa']))
        
        #Obtengo el valor por cada letra ingresada
        #else:
            #puntuacionActual = (puntuacionActual + configuracion[v['letra']]['valor'])
    #return ()

palabra = ["P","E","RR","O"]

#print(__puntuar_jugador__(palabra))