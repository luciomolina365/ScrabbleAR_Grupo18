dic2 = {(7, 3): 'O', (7, 1): 'O', (7, 4): 'Z', (7, 2): 'RR'}
#Ordeno el diccionario por posiciones de menor a mayor
haciaIzq=dict(sorted(dic2.items(), key = lambda diccio: diccio[0]))

#Ordeno el diccionario por posiciones de mayor a menor
haciaDer=dict(sorted(dic2.items(), key = lambda diccio: diccio[0],reverse=True))


def __posiciones_validas(diccionario):
    
    #Obtengo una lista de tuplas de las posiciones para manejarla a mi gusto
    posiciones = []
    for k in diccionario:
        posiciones.append(k)
    
    #Agarro los primeros datos de la palabra, previamente ordenada
    
    #Empiezo a corroborar posiciones
    for i in range (1, len(posiciones)): 
        
        if( posiciones[i][0] == posiciones[i+1][0]):
            ok_x_ascendente = True
            x=posiciones[i][0]
        else:
            ok_x_ascendente = False
            if(x-1 == posiciones[i][0]):
                ok_x_descendente = True
                x=posiciones[i][0]
            else:
                ok_x_descendente = True
        

        if(y+1 == posiciones[i][1]):
            ok_y_ascendente = True
            y=posiciones[i][1]
        else:
            ok_y_ascendente = False
            if(y-1 == posiciones[i][1]):
                ok_y_descendente = True
                y=posiciones[i][1]
            else:
                ok_x_descendente = True


    return()

__posiciones_validas(haciaIzq)
print("___"*20)
__posiciones_validas(haciaDer)
