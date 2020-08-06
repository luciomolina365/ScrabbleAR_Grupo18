from pattern.text.es import parse, verbs, split, lexicon, spelling
from jugabilidad import puntuacion
from jugabilidad import posiciones_validas

def __ordenar_info(diccionario_que_recibe_del_tablero):
    """ Recibo un diccionario enviado por el tablero, trabajado previamente para que llegue de el estilo que esta arriba,
    lo ordeno de menor a mayor y lo transformo a string para usarlo y corroborarlo con si es un sustantivo, adjetivo o verbo """
    
    #Ordeno el diccionario por posiciones de menor a mayor
    dic_ordenado=dict(sorted(diccionario_que_recibe_del_tablero.items(), key = lambda diccio: diccio[0]))


    #ME RETORNA EL DICCIONARIO QUE ENTRA POR LA PALABRA INGRESADA EN EL TABLERO, ORDENADA EN AMBOS SENTIDOS
    #RETORNA DICCIONARIO ORDENADO
    
    return(dic_ordenado)
    
def __obtengo_diccionario_trabajado(__diccionario_ordenado):
    """Obtengo el diccionario ordenado, y lo transformo a una estructura que eleji para corroborar toda la info"""
    
    dic_trabajado = {}
    for k,v in __diccionario_ordenado.items():
        dic_trabajado[k] = v['letra']

    return(dic_trabajado)
        #ME RETORNA UN DICCIONARIO DONDE LA CLAVE VA A SER LA POSICION Y EL VALOR LA LETRA, ME SIRVE PARA CORROBORAR POSICIONES Y PUNTUAR


def __corroboro_palabra(diccionario_trabajado,dificultad):

    """Transformo la estructura elegida previamente, y empiezo a corroborar con pattern"""

    palabra=""
    palabra_lista=[]

    #Con el for, me quedo con las letras que ingresaron
    for k,v in diccionario_trabajado.items():
        palabra = palabra + v
        palabra_lista.append(v)
    
    
    #Hago el parse para que me identifique la palabra
    pal = palabra.lower()
    pal = parse(pal).split()

    #Obtengo del parse la palabra para ir corroborando con el lexicon
    pal_final = pal[0][0]
       
    #Inicializo un booleano en false, esto es para saber si encontro o no la palabra
    ok=False
    for x in lexicon.keys():
        if x in spelling.keys():
            if (x==pal_final[0]):
                ok=True
    
    if(ok==True):
        #Consulto si la palabra es sustantivo, adjetivo o verbo
        for elemento in pal:
            for elem in elemento:
                if(dificultad==1):
                    return(ok,palabra)
                elif((dificultad==2) or (dificultad==3)):
                    if ((elem[1]=='VB') or (elem[1]=='JJ')):
                        return(ok,palabra)
                    else:
                        ok = False
                        return(ok,palabra)
                else:
                    ok = False
                    return(ok,palabra)
    else:
        ok = False
    
    return(ok,palabra)


def __retorno_informacion(__palabra,__configuracion,dificultad):    
    
    """En esta funcion, llamo las funciones para ordenar la informacion y obtenerla, luego, corroboro las posiciones de la palabra ingresada para ver si esta en posiciones seguidas y que no tenga una letra en otro lugar,
    por ultimo, si esta informacion que retorna posiciones_validas, es correcta, llamo a la funcion puntuacion, que me retorna la puntuacion de la palabra, si todo es incorrecto, me retornera False, puntuacion = 0 y palabra = "" """
    
    #ORDENO EL DICCIONARIO QUE ENTRA DEL TABLERO pos 0 IZQUIERDA pos 1 DERECHA
    palabra_ordenada = __ordenar_info(__palabra)
    
    palabra_ordenada_izq = palabra_ordenada
    
    #OBTENGO LA ESTRUCTURA QUE VOY A UTILIZAR PARA EMPEZAR A CORROBORAR TODA LA INFORMACION
    palabra_izq = __obtengo_diccionario_trabajado(palabra_ordenada_izq)
    
    corroboro = __corroboro_palabra(palabra_izq,dificultad)

    sigue = corroboro[0]
    
    palabra = corroboro[1]

    if(sigue == True):
    
        
        if(posiciones_validas.__posiciones_validas(palabra_izq)==True):
            
            puntaje = puntuacion.__puntuar_jugador(palabra_ordenada_izq,__configuracion,palabra_izq)
            ok = True
        else:

            puntaje = 0
            ok = False
    
    else:

        puntaje = 0
        ok=False
    
    return(ok,puntaje,palabra)
#----------------------------------------------------------------------------------------------------------------------------------

#   Mikaliunas, Leandro   -   15694/4