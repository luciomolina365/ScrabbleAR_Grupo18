def __puntuar_jugador(__palabra,__configuracion,__palabra_lista):
    
    """ Funcion para obtener la puntuacion del jugador, en base a la palabra ingresada, vamos a obtener la puntuacion de cada letra y ademas, la posicion de esta letra,
     con esto, verificamos si la letra en esa posicion, tiene, recompensa o trampa, y que tipo de recompensa o trampa tiene"""
    
    ok_x2 = False
    ok_x3 = False
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
                puntuacion_letra = valor
                ok_x2 = True

            if(valor_bonus == "Px3"):
                puntuacion_letra = valor
                ok_x3 = True

        else:

            puntuacion_letra = valor
                
        puntuacionActual = puntuacionActual + puntuacion_letra
    
    if(ok_x2):
        puntuacionActual = puntuacionActual * 2
    
    elif(ok_x3):
        puntuacionActual = puntuacionActual * 3

    return (puntuacionActual)
