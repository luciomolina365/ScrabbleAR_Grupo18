from pattern.text.es import parse, verbs, split, lexicon, spelling
import puntuacion

#Recibe la estructura a corroborar
dic2 = {(7, 3): 'R', (7, 5): 'P', (7, 1): 'O', (7, 4): 'E', (7, 2): 'R'}

def corroboro_palabra(diccionario_que_recibe_del_tablero):
    """ Recibo un diccionario enviado por el tablero, trabajado previamente para que llegue de el estilo que esta arriba,
    lo ordeno de menor a mayor y lo transformo a string para usarlo y corroborarlo con si es un sustantivo, adjetivo o verbo """
    #Booleano para ver si la funcion privada me retorna que la palabra fue encontrada
    
    #Ordeno el diccionario por posiciones de menor a mayor
    haciaIzq=dict(sorted(diccionario_que_recibe_del_tablero.items(), key = lambda diccio: diccio[0]))

    #Ordeno el diccionario por posiciones de mayor a menor
    haciaDer=dict(sorted(diccionario_que_recibe_del_tablero.items(), key = lambda diccio: diccio[0],reverse=True))
    
    def __corroboro_palabra__(diccionario_trabajado):
        #Armo lista para la palabra
        palabra=""

        #Con el for, me quedo con las letras que ingresaron
        for k,v in diccionario_trabajado.items():
            palabra = palabra + v
            #palabra.append(v)
        
        #Busco transformar la lista de letras, en un string
        #pal=""
        #for caracter in palabra:
            #pal = pal + caracter
        
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
                    return(ok,elem[0])
    
    #llamo la funcion privada para obetener la informacion
    pal_izq = __corroboro_palabra__(haciaIzq)
    
    pal_der = __corroboro_palabra__(haciaDer)
    
    return()
    #pregunto, si alguna de estas 2 en base a la palabra ingresada del tablero es true, llamo a puntuacion y obtengo la puntuacion de esta palabra
    if(pal_izq[0]==True):
        print("-.-.-"*30)
        print(puntuacion.puntuarJugador(pal_izq[1]))
        puntuacion_parcial = puntuacion.puntuarJugador(pal_izq[1])
        return(puntuacion_parcial)
    elif (pal_der[0]==True):
        print(".-.-."*30)
        print(puntuacion.puntuarJugador(pal_der[1]))
        puntuacion_parcial = puntuacion.puntuarJugador(pal_der[1])
        return(puntuacion_parcial)
        puntuacion_final = puntuacion_final + puntuacion_parcial
    else:
        return("Ingresaste una palabra incorrecta, mejor suerte para el proximo turno")

#TESTEOS, funcionan
palabra = corroboro_palabra(dic2)
print("__"*20)
print(palabra)

#print(corroboro_palabra.__doc__)