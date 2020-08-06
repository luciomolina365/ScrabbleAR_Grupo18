def __posiciones_validas(diccionario):
    
    """Esta funcion lo que hace es verificar las posiciones ingresadas desde el tablero en base a la palabra armada por el jugador o la IA, lo que verifica es si: esta palabra esta ingresada correctamente en espacios
     continuos"""

    #Obtengo una lista de tuplas de las posiciones para manejarla a mi gusto
    posiciones = []
    for k in diccionario:
        posiciones.append(k)
    
    #Empiezo a corroborar posiciones
    ok=True
    
    for i in range(0,len(posiciones)+1):
        
        #Corte de control para que no siga el for
        if(ok==True):            
            
            #Pregunto si de la palabra que ingresa, la coordenada X de la primer letra es igual a la de la segunda letra... 
            if(posiciones[i][0] == posiciones[i+1][0]):
                
                #Variable para utilizar como corte de control
                es_x=True

                #Si es correcto avanza por X y pregunto si es ascendente, si la coordenada Y de la primera letra +1, es igual a la de la 2da letra
                if((posiciones[i][1]+1 == posiciones[i+1][1])and(es_x==True)):
                    ok=True
                
                #Si no, si la coordenada Y - 1 de la primer letra, es igual a la coordenada Y de la 2da letra, avanza de forma descendente
                elif((posiciones[i][1]-1 == posiciones[i+1][1]) and (es_x==True)):
                    ok = True
                
                else:
                    ok=False

            #Pregunto si de la palabra que ingresa, la coordenada Y de la primer letra es igual a la de la segunda letra 
            elif(posiciones[i][1] == posiciones[i+1][1]):
                #Variable para utilizar como corte de control
                es_y=True
            
                #Si es correcto, pregunto si es ascendente, preguntando si la coordenada X de la primera letra +1, es igual a la del 2da letra
                if((posiciones[i][0]+1 == posiciones[i+1][0])and (es_y==True)):
                    ok=True
            
                #Si no, si la coordenada X - 1 de la primer letra, es igual a la coordenada Y de la segunda letra, avanza por coordenada X de forma descendente
                elif((posiciones[i][0]-1 == posiciones[i+1][0])and (es_y==True)):
                    ok = True
                else:
                    ok = False
            else:
                ok=False

        if(i==(len(posiciones)-2) or ok==False):
            break
    
    return(ok)

#----------------------------------------------------------------------------------------------------------------------------------

#   Mikaliunas, Leandro   -   15694/4