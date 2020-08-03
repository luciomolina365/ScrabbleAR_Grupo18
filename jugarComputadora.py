import random
from corroboro.corroborarPalabra import __retorno_informacion
from Objetos import CLASS_tablero

# Al llamar la jugabilidad, le pasaremos el tablero, el atril de la computadora y la bolsa de fichas
#La dificultad entra al llamar la jugabilidad de la IA
#Si el turno es False = empieza el jugador, si es True, empieza la IA, esto se maneja afuera para que si, le toca el primer turno, despues se lo cambia y se pone optimo a jugar


def __dificultad_IA(dificultad):

    #Reviso la dificultad que entra de la configuracion
    #Seteo valores de cantidad de jugadas y los puntos medios de la IA por si empieza a jugar
    if(dificultad==1):
        cant = 20
        medio = (9, 9)
    elif(dificultad==2):
        cant = 10
        medio = (8, 8)
    else:
        cant = 15
        medio = (7, 7)

    return(cant,medio)

#Formo la palabra en base al atril actual de la IA
def __armo_palabra_IA(atril,cantLetras):
    
    letras=[0,1,2,3,4,5,6]
    
    copia_letras = letras[:]
    
    palabra_armada = []
    
    for i in range(cantLetras):
        
        pos = random.randint(0,(len(letras)-1))
        
        palabra_armada.append(atril[letras[pos]])
        
        del letras[pos]
        
    letras = copia_letras[:]
    
    return palabra_armada

#----------------------------------------------------------------------------------------------------------------------------------

def __posicion_inicio(dificultad):
    
    if(dificultad==1):
        x = random.randint(0,18)
        y = random.randint(0,18)
        pos = (x, y)
    elif(dificultad==2):
        x = random.randint(0,16)
        y = random.randint(0,16)
        pos = (x, y)
    else:
        x = random.randint(0,14)
        y = random.randint(0,14)
        pos = (x, y)
    
    return pos

#----------------------------------------------------------------------------------------------------------------------------------
#Seteo booleano para ver si: en base a la cantidad de letras, puede insertar la palabra
#Una lista de direcciones que representan, de un punto, avanzar hacia la derecha o izquierda o hacia arriba o abajo
#Creamos una variable d para las direcciones, que iremos revisando 1 por 1 ya que la idea es darle mas oportunidades a la IA
#En que pueda generar una palabra correcta
#Si ok es False, no puede insertar la cantidad de letras que se eligieron para la IA, y se vuelve a hacer todo devuelta
#La idea es que segun la dificultad que se eligio, la IA tenga mas posibilidades
#En facil, tendra 3 oportunidades de crear una palabra en base a la cantidad de letras que se eligieron
#En medio, seran 6 oportunidades
#En dificil, seran 10 oportunidades

#pos es una tupla de posiciones = (x , y)
def __pos_valida_IA(pos,palabra,dificultad,__tablero):
    
    direcciones = ["derecha","abajo"]
    
    posible_sentido = len(direcciones)-1
    
    direFinal = "nada"
    
    if(dificultad==1):
        fin_tablero = 18
    
    elif(dificultad==2):
        fin_tablero = 16
    
    else:
        fin_tablero = 14

    
    for dire in range(len(direcciones)):
        ok = True
        sigo=True
        #esto lo hago 1 vez para ver que direccion tomo, si por X ascendente o descendente o lo mismo pero por Y
        pos_dir = random.randint(0 , posible_sentido)

        #if(direcciones[pos_dir]=="arriba"):
        #    
        #    #me muevo en el eje Y de manera ascendente
        #    for i in range(len(palabra)):
        #        if((pos[0]-i>=0) and sigo ):
        #            if(__tablero[(pos[0]-i,pos[1])]['letra'] != ""):
        #            #if(tablero.getDatosEnCoor((pos[0]-i,pos[1]))['letra'] !=""):
        #                sigo=False
        #        else:
        #            sigo=False
        #            break
        #    if(sigo==True):
        #        direFinal = "arriba"
        #    else:
        #        direFinal = "nada"
        #        ok=False
        if(direcciones[pos_dir]=="derecha"):
            #me muevo en el X de manera ascendente
            for i in range(len(palabra)):
                if((pos[1]+i<=fin_tablero) and sigo ):
                    if(__tablero[(pos[0],pos[1]+i)]['letra'] != None):
                    #if(tablero.getDatosEnCoor((pos[0]+i,pos[1]))['letra'] !=""):
                        sigo=False
                else:
                    sigo = False
                    break
            if(sigo==True):
                direFinal = "derecha"
            else:
                direFinal = "nada"
                ok=False
        
        elif(direcciones[pos_dir]=="abajo"):
            
            #me muevo por el eje Y de manera descendente
            for i in range(len(palabra)):
                if((pos[0]+i<=fin_tablero) and sigo):
                    if(__tablero[(pos[0]+i,pos[1])]['letra'] !=""):
                    #if(tablero.getDatosEnCoor((pos[0],pos[1]-i))['letra'] !=""):
                        sigo=False
                else:
                    sigo=False
                    break
            if(sigo==True):
                direFinal = "abajo"
            else:
                direFinal = "nada"
                ok=False
        
        #elif(direcciones[pos_dir]=="izquierda"):
        #    
        #    #me muevo en el eje X de manera descentende
        #    for i in range(len(palabra)):
        #        if((pos[1]-i>=0) and sigo):
        #            if(__tablero[(pos[0],pos[1]-i)]['letra']!=""):
        #            #if(tablero.getDatosEnCoor((pos[0]-i,pos[1]))['letra'] !=""):
        #                sigo=False
        #        else:
        #            sigo=False
        #            break
        #    if(sigo==True):
        #        direFinal = "izquierda"
        #    else:
        #        direFinal = "nada"
        #        ok=False
        
        if(direFinal!="nada"):
            break
        else:
            direcciones.pop(pos_dir)
            posible_sentido = posible_sentido - 1


    return(ok,direFinal)
#-----------------------------------------------------------------------------------------------------------------------------------

def __armo_estructura_IA(palabra,pos,direccion,__tablero):
    dic_IA = {}
    #if(direccion=="arriba"):
    #    for i in range(len(palabra)):
    #        dic_IA[(pos[0]-i,pos[1])] = __tablero[(pos[0]-i,pos[1])]
    #        dic_IA[(pos[0]-i,pos[1])]['letra']=palabra[i]
    if(direccion=="derecha"):
        for i in range(len(palabra)):
            dic_IA[(pos[0],pos[1]+i)] = __tablero[(pos[0],pos[1]+i)]
            dic_IA[(pos[0],pos[1]+i)]['letra']=palabra[i]
    elif(direccion=="abajo"):
        for i in range(len(palabra)):
            dic_IA[(pos[0]+i,pos[1])] = __tablero[(pos[0]+i,pos[1])]
            dic_IA[(pos[0]+i,pos[1])]['letra']=palabra[i]
    #elif(direccion=="izquierda"):
    #    for i in range(len(palabra)):
    #        dic_IA[(pos[0],pos[1]-i)] = __tablero[(pos[0],pos[1]-i)]
    #        dic_IA[(pos[0],pos[1]-i)]['letra']=palabra[i]

    return(dic_IA)

#----------------------------------------------------------------------------------------------------------------------------------

#Funcion que llamaremos para cuando queramos hacer que la IA intercambie fichas
#Nos va a retornar una lista con las fichas que va a intercambiar

def __fichas_a_intercambiar(atril):
    
    cant_fichas_a_cambiar = random.randint(1,len(atril))

    lista_a_cambiar = []

    for i in range(cant_fichas_a_cambiar):
        
        letra = random.choice(atril)

        atril.remove(letra)

        lista_a_cambiar.append(letra)
    
    return lista_a_cambiar

#----------------------------------------------------------------------------------------------------------------------------------

#def __pongo_letras_IA(dic_IA):
#
#    for k in dic_IA.keys():
#        CLASS_tablero.Tablero.setValorEnCoor(k,dic_IA['letra'])
#    

        
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def __juega_IA(dificultad, tablero, atril, primer_turno, configuracion):

    cantLetras = random.randint(2,7)
    if(primer_turno == True):

        #Esto es por si empieza pa IA
        dif = __dificultad_IA(dificultad)

        #dif[0] me retorna la cantidad de veces que tendra que armar la palabra
        veces = dif[0]
        
        #dif[1] me retorna si el turno arranca por la IA, la pos del medio del tablero dependiendo la dificultad
        pos = dif[1]


        #armo la palabra en base a la cantidad de letras que se elige, esto le da mas posibilidades de armar palabras cortas o lagras, de la misma cantidad de letras
        palabra = __armo_palabra_IA(atril, cantLetras)


        #empiezo a preguntar por las posiciones, para armar la estructura que enviare a corroboro palabra
        posiciones = __pos_valida_IA(pos,palabra,dificultad,tablero)


        #posiciones[0] me retorna si habia lugar para insertar la palabra en 4 direcciones distintas
        pos_ok = posiciones[0]


        #posiciones[1] me retorna la direccion hacia donde encontro el lugar para insertar esta palabra
        direccion = posiciones[1]


        #empezamos a corroborar la palabra armada
        for intento in range(veces):
            
            #armo la jugada de la IA, esto me arma la estructura para enviar toda la informacion hacia corroboro palabra
            jugada_IA = __armo_estructura_IA(palabra,pos,direccion,tablero)


            #Mando la informacion a corroboro palabra
            sigue = __retorno_informacion(jugada_IA,configuracion,dificultad)


            #sigue[0] me retorna un booleano de si pudo o no corroborar toda la info
            ok = sigue[0]


            #sigue[1] me retorna el puntaje obtenido por la palabra enviada
            puntaje = sigue[1]

            #Si el booleano que me retorna sigue, es True, envio el puntaje obtenido y corto el for
            if(ok==True):
                break

            else:
                palabra = __armo_palabra_IA(atril,cantLetras)
    
    else:

        #Esto es por si empieza pa IA
        dif = __dificultad_IA(dificultad)
        
        #dif[0] me retorna la cantidad de veces que tendra que armar la palabra
        veces = dif[0]
        
        #armo la palabra en base a la cantidad de letras que se elige, esto le da mas posibilidades de armar palabras cortas o lagras, de la misma cantidad de letras
        palabra = __armo_palabra_IA(atril, cantLetras)

        pos_valida = False
        #empezamos a corroborar la palabra armada

        while(pos_valida == False):
                #Obtengo una pos de inicio de manera aleatoria
                pos = __posicion_inicio(dificultad)

                #empiezo a preguntar por las posiciones, para armar la estructura que enviare a corroboro palabra
                posiciones = __pos_valida_IA(pos,palabra,dificultad,tablero)

                #posiciones[0] me retorna si habia lugar para insertar la palabra en 4 direcciones distintas
                pos_ok = posiciones[0]

                if(pos_ok == True):
                    pos_valida = True
                    
                    #posiciones[1] me retorna la direccion hacia donde encontro el lugar para insertar esta palabra
                    direccion = posiciones[1]

        for intento in range(veces):
                   
            #armo la jugada de la IA, esto me arma la estructura para enviar toda la informacion hacia corroboro palabra
            jugada_IA = __armo_estructura_IA(palabra,pos,direccion,tablero)

            #Mando la informacion a corroboro palabra
            sigue = __retorno_informacion(jugada_IA,configuracion,dificultad)

            #sigue[0] me retorna un booleano de si pudo o no corroborar toda la info
            ok = sigue[0]

            #sigue[1] me retorna el puntaje obtenido por la palabra enviada
            puntaje = sigue[1]

            #Si el booleano que me retorna sigue, es True, envio el puntaje obtenido y corto el for
            if(ok==True):
                break

            else:
                palabra = __armo_palabra_IA(atril,cantLetras)
                #if(intento == veces):
                    #print(puntaje)
    
    return(ok,puntaje,jugada_IA,palabra)
