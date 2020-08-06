import random
from jugabilidad.corroborarPalabra import __retorno_informacion
from Objetos import CLASS_tablero

"""En esta hoja, lo que hacemos, setear la IA en todos sus aspectos, desde la dificultad elegida por el usuario, hasta la cantidad de veces que va a intentar hacer una palabra asi tambien como elegir una posicion random
 y verificar su estado hacia los dos sentidos que a lo largo de la letra"""

def __dificultad_IA(dificultad):

    """Seteamos en base a la dificultad, la cantidad de iteraciones para formar una palabra y el medio del tablero, ficha donde se inicia la jugada en el primer turno"""
    
    if(dificultad==1):
        cant = 10
        medio = (9, 9)
    elif(dificultad==2):
        cant = 15
        medio = (8, 8)
    else:
        cant = 20
        medio = (8, 8)

    return(cant,medio)


def __armo_palabra_IA(atril,cantLetras):

    """Armamos la palabra de la IA en base a su atril actual"""
    
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
    """Funcion que le da a la IA una posicion random no de ser el primer turno"""
    
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

def __pos_valida_IA(pos,palabra,dificultad,__tablero):
    """Funcion donde verificamos, si la posicion elegida por la IA es correcta, ya sea, se puede insertar la palabra porque no existe letras en el camino, o porque no llego al final del tablero """
    
    direcciones = ["derecha","abajo"]
    
    posible_sentido = len(direcciones)-1
    
    direFinal = "nada"
    
    if(dificultad==1):
        fin_tablero = 18

    else:
        fin_tablero = 16

    
    for dire in range(len(direcciones)):
        ok = True
        sigo=True
        #esto lo hago 1 vez para ver que direccion tomo, si por X ascendente o descendente o lo mismo pero por Y
        pos_dir = random.randint(0 , posible_sentido)

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
        
        
        if(direFinal!="nada"):
            break
        else:
            direcciones.pop(pos_dir)
            posible_sentido = posible_sentido - 1


    return(ok,direFinal)
#-----------------------------------------------------------------------------------------------------------------------------------

def __armo_estructura_IA(palabra,pos,direccion,__tablero):
    
    """Armamos la estructura de la IA para corroborar la informacion, se arma para enviar a la funcion corroboro_palabra y que esta me retorne si la informacion enviada es correcta"""
    
    dic_IA = {}

    if(direccion=="derecha"):
        for i in range(len(palabra)):
            dic_IA[(pos[0],pos[1]+i)] = __tablero[(pos[0],pos[1]+i)]
            dic_IA[(pos[0],pos[1]+i)]['letra']=palabra[i]
    elif(direccion=="abajo"):
        for i in range(len(palabra)):
            dic_IA[(pos[0]+i,pos[1])] = __tablero[(pos[0]+i,pos[1])]
            dic_IA[(pos[0]+i,pos[1])]['letra']=palabra[i]


    return(dic_IA)

#----------------------------------------------------------------------------------------------------------------------------------

#Funcion que llamaremos para cuando queramos hacer que la IA intercambie fichas
#Nos va a retornar una lista con las fichas que va a intercambiar

def __fichas_a_intercambiar(atril):

    """Funcion donde hacemos que la IA intercambie sus fichas"""
    
    cant_fichas_a_cambiar = random.randint(1,len(atril))

    copia_atril = atril[:]

    lista_a_cambiar = []

    for i in range(cant_fichas_a_cambiar):
        
        letra = random.choice(copia_atril)

        lista_a_cambiar.append(letra)

        copia_atril.remove(letra)
    

    return lista_a_cambiar


#----------------------------------------------------------------------------------------------------------------------------------
def __juega_IA(dificultad, tablero, atril, primer_turno, configuracion):

    """Aca es donde hacemos que la IA llame a todas las funciones y juegue, recibiendo toda la informacion necesaria para poder formar una palabra, lo hacemos en base a la cantidad de veces que predefinimos, que son los 
     intentos de la IA para formar una palabra, lo unico que no cambia es la posicion, porque queremos que, si encuentra una posicion valida, en base a la cantidad de letras seleccionada, guarde la posicion, e intentar formar
     una palabra en base a la cantidad de letras seleccionadas, es para darle mas chances a la IA de que forme una palabra correcta"""

    pal_armada=""
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
    if(ok==True):
        for letra in range(len(palabra)):
            pal_armada = pal_armada + palabra[letra]
    
    return(ok,puntaje,jugada_IA,pal_armada)
#----------------------------------------------------------------------------------------------------------------------------------

#   Mikaliunas, Leandro   -   15694/4