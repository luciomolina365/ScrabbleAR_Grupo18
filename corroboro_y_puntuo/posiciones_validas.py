dic2 = {(1, 8): 'O', (3, 9): 'O', (4, 8): 'Z', (2, 8): 'RR'}
#Ordeno el diccionario por posiciones de menor a mayor
haciaIzq=dict(sorted(dic2.items(), key = lambda diccio: diccio[0]))

#Ordeno el diccionario por posiciones de mayor a menor
haciaDer=dict(sorted(dic2.items(), key = lambda diccio: diccio[0],reverse=True))


def __posiciones_validas(diccionario):
    
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