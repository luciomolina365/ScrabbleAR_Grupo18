#Estructuras que tienen que entrar aca

#Estructura que obtengo de la configuracion del juego
#__configuracion = {'A':{'cantidad':11,'valor':1}, 'B':{'cantidad':3,'valor':1}, 'C':{'cantidad':4,'valor':1}, 'D':{'cantidad':4,'valor':1}, 
#'E':{'cantidad':11,'valor':2}, 'F':{'cantidad':2,'valor':1}, 'G':{'cantidad':2,'valor':1}, 'H':{'cantidad':2,'valor':1}, 'I':{'cantidad':6,'valor':1}, 
#'J':{'cantidad':2,'valor':1}, 'K':{'cantidad':1,'valor':1}, 'L':{'cantidad':4,'valor':1}, 'LL':{'cantidad':1,'valor':1}, 'M':{'cantidad':3,'valor':1}, 
#'N':{'cantidad':5,'valor':1}, 'Ñ':{'cantidad':1,'valor':1}, 'O':{'cantidad':8,'valor':3}, 'P':{'cantidad':2,'valor':2}, 'Q':{'cantidad':1,'valor':1}, 
#'R':{'cantidad':4,'valor':1}, 'RR':{'cantidad':1,'valor':10}, 'S':{'cantidad':7,'valor':1}, 'T':{'cantidad':4,'valor':1}, 'U':{'cantidad':6,'valor':1},
#'V':{'cantidad':2,'valor':1}, 'W':{'cantidad':1,'valor':1}, 'X':{'cantidad':1,'valor':1}, 'Y':{'cantidad':1,'valor':1}, 'Z':{'cantidad':1,'valor':5}}

#__palabra ={(7, 2): {'letra': 'Z', 'trampa': False, 'tipo_de_trampa': None, 'recompensa': True, 'tipo_de_recompensa': 2}, #4
#            (7, 3): {'letra': 'O', 'trampa': True, 'tipo_de_trampa': 2, 'recompensa': False, 'tipo_de_recompensa': None}, #0
#            (7, 4): {'letra': 'RR', 'trampa': True, 'tipo_de_trampa': 1, 'recompensa': False, 'tipo_de_recompensa': None},#7
#            (7, 5): {'letra': 'O', 'trampa': False, 'tipo_de_trampa': None, 'recompensa': True, 'tipo_de_recompensa': 3}} #6

#Estructura que obtengo en base a lo que entra en corroboro palabra
#Y va a ingresar a puntuacion, si y solo si, es correcta la palabra

#__palabra_lista = {(7, 2): 'Z', (7, 3): 'O', (7, 4): 'RR', (7, 5): 'O'}
# Z = 5 - O = 3 - RR = 10
# Z = 10 - O = 1 - RR = 9 - O = 9
# 10 +10 +9 = 29
def __puntuar_jugador(__palabra,__configuracion,__palabra_lista):
    bonus_palabra_x2 = 0
    bonus_palabra_x3 = 0
    puntuacionActual = 0
    puntuacion_letra = 0
    for coor in __palabra_lista:
        
        valor = __configuracion[__palabra[coor]['letra']]['valor']
        
        trampa = __palabra[coor]['trampa']
        
        bonus = __palabra[coor]['recompensa']
        
        if(trampa == True):
            valor_trampa = __palabra[coor]['tipo_de_trampa']
            if(valor_trampa == "-1"):
                puntuacion_letra = valor - 1
            
            if(valor_trampa == "-2"):
                puntuacion_letra = valor - 2
            
            if(valor_trampa == "-3"):
                puntuacion_letra = valor - 3

        elif(bonus == True):
            valor_bonus = __palabra[coor]['tipo_de_recompensa']
            if(valor_bonus == "x2"):
                puntuacion_letra = valor * 2
            
            if(valor_bonus == "x3"):
                puntuacion_letra = valor * 3
            
            if(valor_bonus == "Px2"):
                bonus_palabra_x2 = bonus_palabra_x2 + 1

            if(valor_bonus == "Px3"):
                bonus_palabra_x3 = bonus_palabra_x3 + 1

        else:

            puntuacion_letra = valor
                
        puntuacionActual = puntuacionActual + puntuacion_letra
    if(bonus_palabra_x2!=0):
        for cant in range(bonus_palabra_x2):
            puntuacionActual = puntuacionActual * 2
    elif(bonus_palabra_x3!=0):
        for cant in range(bonus_palabra_x3):
            puntuacionActual = puntuacionActual * 3

    return (puntuacionActual)

#Testeado con las estructuras que estan arriba, ya esta funcionando
#print(__puntuar_jugador(__palabra,__configuracion,__palabra_lista))