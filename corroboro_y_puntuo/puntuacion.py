#Estructura que obtengo de la configuracion del juego
__configuracion = {'A':{'cantidad':11,'valor':1}, 'B':{'cantidad':3,'valor':1}, 'C':{'cantidad':4,'valor':1}, 'D':{'cantidad':4,'valor':1}, 
'E':{'cantidad':11,'valor':2}, 'F':{'cantidad':2,'valor':1}, 'G':{'cantidad':2,'valor':1}, 'H':{'cantidad':2,'valor':1}, 'I':{'cantidad':6,'valor':1}, 
'J':{'cantidad':2,'valor':1}, 'K':{'cantidad':1,'valor':1}, 'L':{'cantidad':4,'valor':1}, 'LL':{'cantidad':1,'valor':1}, 'M':{'cantidad':3,'valor':1}, 
'N':{'cantidad':5,'valor':1}, 'Ñ':{'cantidad':1,'valor':1}, 'O':{'cantidad':8,'valor':2}, 'P':{'cantidad':2,'valor':2}, 'Q':{'cantidad':1,'valor':1}, 
'R':{'cantidad':4,'valor':1}, 'RR':{'cantidad':1,'valor':8}, 'S':{'cantidad':7,'valor':1}, 'T':{'cantidad':4,'valor':1}, 'U':{'cantidad':6,'valor':1},
'V':{'cantidad':2,'valor':1}, 'W':{'cantidad':1,'valor':1}, 'X':{'cantidad':1,'valor':1}, 'Y':{'cantidad':1,'valor':1}, 'Z':{'cantidad':1,'valor':2}}


#Estructura que obtengo de la interfaz del tablero
__tablero ={(7, 4):{"letra": 'RR',#9
                "trampa": True,
                "tipo_de_trampa": 1,
                "recompensa": False,
                "tipo_de_recompensa": None},
        (7, 5):{"letra": "O", #6
                "trampa": False,
                "tipo_de_trampa": None,
                "recompensa": True,
                "tipo_de_recompensa": 3},
        (7, 2):{"letra": "Z", #2
                "trampa": False,
                "tipo_de_trampa": None,
                "recompensa": True,
                "tipo_de_recompensa": 2},
        (7, 3):{"letra": "O", #0
                "trampa": True,
                "tipo_de_trampa": 2,
                "recompensa": False,
                "tipo_de_recompensa": None}}

def __armo_mi_tablero(__tablero):
    #Obtengo el tablero como quiero, para trabajar con el
    __tablero2={}
    for k,v in __tablero.items():
        __tablero2[v['letra']]=v
    for k,v in __tablero2.items():
        del __tablero2[k]['letra']

    return(__tablero2)

def __puntuar_jugador(__palabra):
    
    __tablero2=__armo_mi_tablero(__tablero)
    
    puntuacionActual = 0
    
    for i in range(0,(len(__palabra))):
        letra = __palabra[i]
        valor = __configuracion[letra]['valor']
        trampa = __tablero2[letra]['trampa']
        valor_trampa = __tablero2[letra]['tipo_de_trampa']
        bonus = __tablero2[letra]['recompensa']
        valor_bonus = __tablero2[letra]['tipo_de_recompensa']
        if(trampa == True):
            puntuacionActual = puntuacionActual + (valor - valor_trampa)
        elif(bonus == True):
            puntuacionActual = puntuacionActual + (valor * valor_bonus)
        else:
            puntuacionActual = puntuacionActual + valor
    
    return (puntuacionActual)
