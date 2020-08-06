from pattern.text.es import parse, verbs, split, lexicon, spelling
from corroboro import puntuacion
from corroboro import posiciones_validas

def __ordenar_info(diccionario_que_recibe_del_tablero):
    """ Recibo un diccionario enviado por el tablero, trabajado previamente para que llegue de el estilo que esta arriba,
    lo ordeno de menor a mayor y lo transformo a string para usarlo y corroborarlo con si es un sustantivo, adjetivo o verbo """
    
    #Ordeno el diccionario por posiciones de menor a mayor
    haciaIzq=dict(sorted(diccionario_que_recibe_del_tablero.items(), key = lambda diccio: diccio[0]))

    #Ordeno el diccionario por posiciones de mayor a menor
    #haciaDer=dict(sorted(diccionario_que_recibe_del_tablero.items(), key = lambda diccio: diccio[0],reverse=True))

    #ME RETORNA EL DICCIONARIO QUE ENTRA POR LA PALABRA INGRESADA EN EL TABLERO, ORDENADA EN AMBOS SENTIDOS
    #RETORNA DICCIONARIO ORDENADO
    
    return(haciaIzq)
    
def __obtengo_diccionario_trabajado(__diccionario_ordenado):
    #Agarro la info que me interesa para obtener la palabra y retornarla para verificarla despues, del diccionario que recibo, armo uno con las posiciones y la letra de la posicion
    
    dic_trabajado = {}
    for k,v in __diccionario_ordenado.items():
        dic_trabajado[k] = v['letra']

    return(dic_trabajado)
        #ME RETORNA UN DICCIONARIO DONDE LA CLAVE VA A SER LA POSICION Y EL VALOR LA LETRA, ME SIRVE PARA CORROBORAR POSICIONES Y PUNTUAR
        #RETORNA DICCIONARIO TRABAJADO



def __corroboro_palabra(diccionario_trabajado,dificultad):

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
                    return(ok)
                elif((dificultad==2) or (dificultad==3)):
                    if ((elem[1]=='VB') or (elem[1]=='JJ')):
                        return(ok)
                else:
                    ok = False
                    return(ok)
    else:
        ok = False
        return(ok)


def __retorno_informacion(__palabra,__configuracion,dificultad):    
    
    #ORDENO EL DICCIONARIO QUE ENTRA DEL TABLERO pos 0 IZQUIERDA pos 1 DERECHA
    palabra_ordenada = __ordenar_info(__palabra)
    
    palabra_ordenada_izq = palabra_ordenada
    
    #palabra_ordenada_der = palabra_ordenada[1]
    
    #OBTENGO LA ESTRUCTURA QUE VOY A UTILIZAR PARA EMPEZAR A CORROBORAR TODA LA INFORMACION
    palabra_izq = __obtengo_diccionario_trabajado(palabra_ordenada_izq)
    
    #palabra_der = __obtengo_diccionario_trabajado(palabra_ordenada_der)
    
    sigue_izquierda = __corroboro_palabra(palabra_izq,dificultad)

    #sigue_derecha = __corroboro_palabra(palabra_der)

    if(sigue_izquierda == True):
    
        
        if(posiciones_validas.__posiciones_validas(palabra_izq)==True):
            
            info_final = puntuacion.__puntuar_jugador(palabra_ordenada_izq,__configuracion,palabra_izq)
            ok = True
        else:

            info_final = "TU PALABRA ES CORRECTA PERO, NO LA UBICASTE CORRECTAMENTE!!!"
            ok = False
    
    #elif(sigue_derecha == True):
    #
    #    
    #    if(posiciones_validas.__posiciones_validas(palabra_der)==True):
    #        
    #        info_final = puntuacion.__puntuar_jugador(palabra_ordenada_der,__configuracion,palabra_der)
    #        ok = True
    #    else:
    #
    #        info_final = "TU PALABRA ES CORRECTA PERO, NO LA UBICASTE CORRECTAMENTE!!!"
    #        ok = False
    #
    else:

        info_final = "INGRESASTE UNA PALABRA INCORRECTA, MEJOR SUERTE EN EL PROXIMO TURNO"
        ok=False
    
    return(ok,info_final)
#-----------------------------------------------------------------------------------

