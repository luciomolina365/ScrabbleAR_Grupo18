from pattern.text.es import parse, verbs, split, lexicon, spelling
from corroboro import puntuacion
from corroboro import posiciones_validas

#Va a recibir un diccionario con este formato: {(x,y):'letra',...}
#Corroboro al derecha y al reves, esta palabra que me manda el tablero
#__palabra ={(4, 2):{"letra": 'RR',#9
#                "trampa": True,
#                "tipo_de_trampa": 1,
#                "recompensa": False,
#                "tipo_de_recompensa": None},
#        (4, 3):{"letra": "O", #6
#                "trampa": False,
#                "tipo_de_trampa": None,
#                "recompensa": True,
#                "tipo_de_recompensa": 3},
#        (4, 4):{"letra": "Z", #2
#                "trampa": False,
#                "tipo_de_trampa": None,
#                "recompensa": True,
#                "tipo_de_recompensa": 2},
#        (4, 1):{"letra": "O", #0
#                "trampa": True,
#                "tipo_de_trampa": 2,
#                "recompensa": False,
#                "tipo_de_recompensa": None}}

#__configuracion = bolsa.getEstado()

#__configuracion = {'A':{'cantidad':11,'valor':1}, 'B':{'cantidad':3,'valor':1}, 'C':{'cantidad':4,'valor':1}, 'D':{'cantidad':4,'valor':1}, 
#'E':{'cantidad':11,'valor':2}, 'F':{'cantidad':2,'valor':1}, 'G':{'cantidad':2,'valor':1}, 'H':{'cantidad':2,'valor':1}, 'I':{'cantidad':6,'valor':1}, 
#'J':{'cantidad':2,'valor':1}, 'K':{'cantidad':1,'valor':1}, 'L':{'cantidad':4,'valor':1}, 'LL':{'cantidad':1,'valor':1}, 'M':{'cantidad':3,'valor':1}, 
#'N':{'cantidad':5,'valor':1}, 'Ñ':{'cantidad':1,'valor':1}, 'O':{'cantidad':8,'valor':3}, 'P':{'cantidad':2,'valor':2}, 'Q':{'cantidad':1,'valor':1}, 
#'R':{'cantidad':4,'valor':1}, 'RR':{'cantidad':1,'valor':10}, 'S':{'cantidad':7,'valor':1}, 'T':{'cantidad':4,'valor':1}, 'U':{'cantidad':6,'valor':1},
#'V':{'cantidad':2,'valor':1}, 'W':{'cantidad':1,'valor':1}, 'X':{'cantidad':1,'valor':1}, 'Y':{'cantidad':1,'valor':1}, 'Z':{'cantidad':1,'valor':5}}

def __ordenar_info(diccionario_que_recibe_del_tablero):
    """ Recibo un diccionario enviado por el tablero, trabajado previamente para que llegue de el estilo que esta arriba,
    lo ordeno de menor a mayor y lo transformo a string para usarlo y corroborarlo con si es un sustantivo, adjetivo o verbo """
        
    #Ordeno el diccionario por posiciones de menor a mayor
    haciaIzq=dict(sorted(diccionario_que_recibe_del_tablero.items(), key = lambda diccio: diccio[0]))

    #Ordeno el diccionario por posiciones de mayor a menor
    haciaDer=dict(sorted(diccionario_que_recibe_del_tablero.items(), key = lambda diccio: diccio[0],reverse=True))

    #ME RETORNA EL DICCIONARIO QUE ENTRA POR LA PALABRA INGRESADA EN EL TABLERO, ORDENADA EN AMBOS SENTIDOS
    #RETORNA DICCIONARIO ORDENADO
    return(haciaIzq,haciaDer)
    
def __obtengo_diccionario_trabajado(__diccionario_ordenado):
    #Agarro la info que me interesa para obtener la palabra y retornarla para verificarla despues, del diccionario que recibo, armo uno con las posiciones y la letra de la posicion
    dic_trabajado = {}
    for k,v in __diccionario_ordenado.items():
        dic_trabajado[k] = v['letra']
    
    #ME RETORNA UN DICCIONARIO DONDE LA CLAVE VA A SER LA POSICION Y EL VALOR LA LETRA, ME SIRVE PARA CORROBORAR POSICIONES Y PUNTUAR
    #RETORNA DICCIONARIO TRABAJADO
    return(dic_trabajado)


def __corroboro_palabra(diccionario_trabajado):
    
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
            if (pal_final[0]==x):
                ok=True
    
    #Consulto si la palabra es sustantivo, adjetivo o verbo
    for elemento in pal:
        for elem in elemento:
            if ((elem[1] == 'VB') or ((elem [1] == "NNS") or (elem[1] ==  "NN")) or (elem[1] == 'JJ')):

                #ME RETORNA UNA LISTA DONDE LA POS 0 RETORNA SI LA PALABRA QUE SE INGRESO SE ENCONTRO O NO EN PATTERN
                #LA POS 1 ME RETORNA LA PALABRA EN SI
                return(ok,elem[0])


def __retorno_informacion(__palabra,__configuracion):    

    #ORDENO EL DICCIONARIO QUE ENTRA DEL TABLERO pos 0 IZQUIERDA pos 1 DERECHA
    palabra_ordenada = __ordenar_info(__palabra)
    
    palabra_ordenada_izq = palabra_ordenada[0] 
    
    palabra_ordenada_der = palabra_ordenada[1]
    
    #OBTENGO LA ESTRUCTURA QUE VOY A UTILIZAR PARA EMPEZAR A CORROBORAR TODA LA INFORMACION
    palabra_izq = __obtengo_diccionario_trabajado(palabra_ordenada_izq)
    
    palabra_der = __obtengo_diccionario_trabajado(palabra_ordenada_der)
       
    if(__corroboro_palabra(palabra_izq)[0] == True):
        
        if(posiciones_validas.__posiciones_validas(palabra_izq)==True):
            
            info_final = puntuacion.__puntuar_jugador(palabra_ordenada_izq,__configuracion,palabra_izq)
            ok = True
        else:

            info_final = "TU PALABRA ES CORRECTA PERO, NO LA UBICASTE CORRECTAMENTE!!!"
            ok = False
    
    elif(__corroboro_palabra(palabra_der)[0] == True):
        
        if(posiciones_validas.__posiciones_validas(palabra_der)==True):
            
            info_final = puntuacion.__puntuar_jugador(palabra_ordenada_der,__configuracion,palabra_der)
            ok = True
        else:

            info_final = "TU PALABRA ES CORRECTA PERO, NO LA UBICASTE CORRECTAMENTE!!!"
            ok = False
    
    else:

        info_final = "INGRESASTE UNA PALABRA INCORRECTA, MEJOR SUERTE EN EL PROXIMO TURNO"
        ok=False
    
    return(ok,info_final)
#-----------------------------------------------------------------------------------
#TESTEOS, funcionan
#print("puntuacion de la palabra ingresada")
#print(__retorno_informacion(__palabra,__configuracion))




#print(corroboro_palabra.__doc__)