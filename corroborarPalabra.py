from pattern.text.es import parse, verbs, split
import puntuacion
dic2 = {(7, 3): 'R', (7, 5): 'O', (7, 1): 'P', (7, 4): 'R', (7, 2): 'E'}

def corroboro_palabra(dic2):
    """ Recibo un diccionario enviado por el tablero, trabajado previamente para que llegue de el estilo que esta arriba,
    lo ordeno de menor a mayor y lo transformo a string para usarlo y corroborarlo con si es un sustantivo, adjetivo o verbo """
    dic2=dict(sorted(dic2.items(), key = lambda diccio: diccio[0])) #Ordeno el diccionario por posiciones de menor a mayor
    palabra=[]                                                      #Armo lista para la palabra
    for k,v in dic2.items():                                        #Con el for, me quedo con las letras que ingresaron
        palabra.append(v)
    pal=""                                                          #Busco transformar la lista de letras, en un string de tipo palabra
    for caracter in palabra:
        pal = pal + caracter
    pal = parse(pal).split()                                        #Hago el parse para que me identifique la palabra
    ok=False                                                        #Inicializo un booleano en false, si es verdadero, lo cambio a True y lo retorno
    for elemento in pal:
        #print(elemento)
        for elem in elemento:
            #print(elem)
            if ((elem[1] == 'VB') or ((elem [1] == "NNS") or (elem[1] ==  "NN")) or (elem[1] == 'JJ')):
               ok=True
            return(ok,elem[0])                                      #Retornamos booleano, que indica si es ss vb o adj, y la palabra




#TESTEOS, funcionan
if(corroboro_palabra(dic2)[0]==True):
    palabra = corroboro_palabra(dic2)[1]
    print(palabra)
    print(puntuacion.puntuarJugador(palabra))
else:
    print("La palabra ingresada era incorrecta, mejor suerte para el proximo turno!")

print(corroboro_palabra.__doc__)