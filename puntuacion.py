#Estructura que obtengo de la configuracion del juego
__configuracion__ = {
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
__tablero__={(7, 4):{"letra": "RR",#9
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

def __armo_mi_tablero__(__tablero__):
    #Obtengo el tablero como quiero, para trabajar con el
    __tablero2__={}
    for k,v in __tablero__.items():
        __tablero2__[v['letra']]=v
    for k,v in __tablero2__.items():
        del __tablero2__[k]['letra']

    return(__tablero2__)

def __puntuar_jugador__(__palabra__):
    
    __tablero2__=__armo_mi_tablero__(__tablero__)
        
    puntuacionActual = 0

    indice = 0
    
    for k,v in __tablero2__.items():
        
        #Pregunto si la letra que obtuve de la palabra que ingresa en el tablero donde esta puesta tiene trampa o bonus
        if(__tablero2__[__palabra__[indice]]['trampa']==True):
            puntuacionActual = (puntuacionActual + (__configuracion__[__palabra__[indice]]['valor'] - __tablero2__[__palabra__[indice]]['tipo_de_trampa']))
        
        elif(__tablero2__[__palabra__[indice]]['recompensa']==True):
            puntuacionActual = (puntuacionActual + (__configuracion__[__palabra__[indice]]['valor'] * __tablero2__[__palabra__[indice]]['tipo_de_recompensa']))

        else:
            puntuacionActual = puntuacionActual + __configuracion__[__palabra__[indice]]['valor']

        indice += 1 
            
    return (puntuacionActual)