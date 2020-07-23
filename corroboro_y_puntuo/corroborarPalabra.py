from pattern.text.es import parse, verbs, split, lexicon, spelling
import puntuacion

#Recibe la estructura a corroborar
dic2 = {(7, 3): 'E', (7, 1): 'O', (7, 4): 'P', (7, 2): 'RR'}

def __informacion_de_turno__(diccionario_que_recibe_del_tablero):
    """ Recibo un diccionario enviado por el tablero, trabajado previamente para que llegue de el estilo que esta arriba,
    lo ordeno de menor a mayor y lo transformo a string para usarlo y corroborarlo con si es un sustantivo, adjetivo o verbo """
    #Booleano para ver si la funcion privada me retorna que la palabra fue encontrada
    
    #Ordeno el diccionario por posiciones de menor a mayor
    haciaIzq=dict(sorted(diccionario_que_recibe_del_tablero.items(), key = lambda diccio: diccio[0]))

    #Ordeno el diccionario por posiciones de mayor a menor
    haciaDer=dict(sorted(diccionario_que_recibe_del_tablero.items(), key = lambda diccio: diccio[0],reverse=True))
    
    def __corroboro_palabra__(diccionario_trabajado):
        
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
                    return(ok,elem[0],palabra_lista)
    
    #llamo la funcion privada para obetener la informacion
    def __retorno_puntuacion__():    
        if(__corroboro_palabra__(haciaIzq)[0] == True):
            pal_izq = __corroboro_palabra__(haciaIzq)[2]
            return(puntuacion.__puntuar_jugador__(pal_izq))
        
        elif(__corroboro_palabra__(haciaDer)[0] == True):
            pal_der = __corroboro_palabra__(haciaDer)[2]
            return(puntuacion.__puntuar_jugador__(pal_der))
        else:
            return("INGRESASTE UNA PALABRA INCORRECTA, MEJOR SUERTE EN EL PROXIMO TURNO")
    
    
    info_final = __retorno_puntuacion__()
    return info_final
#-----------------------------------------------------------------------------------
#TESTEOS, funcionan
palabra = __informacion_de_turno__(dic2)
print("__"*20)
print(palabra)

#print(corroboro_palabra.__doc__)