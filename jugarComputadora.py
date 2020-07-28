#Facil 19x19 medio(9,9) . Medio 17x17 medio(8,8) . Dificil 15x15 medio(7,7)
from random import randint,randrange
import corroboro_y_puntuo
from Objetos import CLASS_tablero
from Objetos import CLASS_atril
from Objetos import CLASS_bolsa

__configuracion = {'A':{'cantidad':11,'valor':1}, 'B':{'cantidad':3,'valor':1}, 'C':{'cantidad':4,'valor':1}, 'D':{'cantidad':4,'valor':1}, 
'E':{'cantidad':11,'valor':2}, 'F':{'cantidad':2,'valor':1}, 'G':{'cantidad':2,'valor':1}, 'H':{'cantidad':2,'valor':1}, 'I':{'cantidad':6,'valor':1}, 
'J':{'cantidad':2,'valor':1}, 'K':{'cantidad':1,'valor':1}, 'L':{'cantidad':4,'valor':1}, 'LL':{'cantidad':1,'valor':1}, 'M':{'cantidad':3,'valor':1}, 
'N':{'cantidad':5,'valor':1}, 'Ñ':{'cantidad':1,'valor':1}, 'O':{'cantidad':8,'valor':2}, 'P':{'cantidad':2,'valor':2}, 'Q':{'cantidad':1,'valor':1}, 
'R':{'cantidad':4,'valor':1}, 'RR':{'cantidad':1,'valor':8}, 'S':{'cantidad':7,'valor':1}, 'T':{'cantidad':4,'valor':1}, 'U':{'cantidad':6,'valor':1},
'V':{'cantidad':2,'valor':1}, 'W':{'cantidad':1,'valor':1}, 'X':{'cantidad':1,'valor':1}, 'Y':{'cantidad':1,'valor':1}, 'Z':{'cantidad':1,'valor':2}}

__palabra ={(7, 9):{"letra": 'RR',#9
                "trampa": True,
                "tipo_de_trampa": 1,
                "recompensa": False,
                "tipo_de_recompensa": None},
        (7, 5):{"letra": "O", #6
                "trampa": False,
                "tipo_de_trampa": None,
                "recompensa": True,
                "tipo_de_recompensa": 3},
        (7, 2):{"letra": "Z", #2
                "trampa": False,
                "tipo_de_trampa": None,
                "recompensa": True,
                "tipo_de_recompensa": 2},
        (7, 3):{"letra": "O", #0
                "trampa": True,
                "tipo_de_trampa": 2,
                "recompensa": False,
                "tipo_de_recompensa": None}}


#Al llamar la jugabilidad, le pasaremos el tablero, el atril de la computadora y la bolsa de fichas

#La dificultad entra al llamar la jugabilidad de la IA
atril = ["Z","O","O","RR","RR","O","O"] #CLASS_atril.Atril.getFichas_disponibles()

#Si el turno es False = empieza el jugador, si es True, empieza la IA, esto se maneja afuera para que si, le toca el primer turno, despues se lo cambia y se pone optimo a jugar
def __jugabilidad_IA(__palabra,atril,__configuracion,dificultad,turno):

    #Reviso la dificultad que entra de la configuracion
    #Seteo valores de cantidad de jugadas y los puntos medios de la IA por si empieza a jugar
    if(dificultad==1):
        cant = 3
        medio = (9,9)
    elif(dificultad==2):
        cant = 6
        medio = (8,8)
    else:
        cant = 10
        medio = (7,7)

    #Formo la palabra en base al atril actual de la IA
    def __armo_palabra_IA(atril):
        cantLetras = randint(2,7)
        palabra_armada = []
        letras=7
        for i in range(cantLetras):
            pos = randint(0,letras)
            letras = letras - 1 
            palabra_armada.append(atril[pos])
        return palabra_armada

    #----------------------------------------------------------------------------------------------------------------------------------
    #Seteo booleano para ver si: en base a la cantidad de letras, puede insertar la palabra
    #Una lista de direcciones que representan, de un punto, avanzar hacia la derecha o izquierda o hacia arriba o abajo
    #Creamos una variable d para las direcciones, que iremos revisando 1 por 1 ya que la idea es darle mas oportunidades a la IA
    #En que pueda generar una palabra correcta
    #Si ok es false, no puede insertar la cantidad de letras que se eligieron para la IA, y se vuelve a hacer todo devuelta
    #La idea es que segun la dificultad que se eligio, la IA tenga mas posibilidades
    #En facil, tendra 3 oportunidades de crear una palabra en base a la cantidad de letras que se eligieron
    #En medio, seran 6 oportunidades
    #En dificil, seran 10 oportunidades
    
    #pos es una tupla de posiciones = (x,y)
    def __pos_valida_IA(pos,palabra):
        ok = True
        direcciones = [1,2,3,4]
        d = 3

        for i in range(len(direcciones)):
            #esto lo hago 1 vez para ver que direccion tomo, si por X ascendente o descendente o lo mismo pero por Y
            pos_dir = 0 #randint(0,d)
            if((direcciones[pos_dir]==1)and(ok==True)):
                for i in range(0,len(palabra),1):
                    if(__tablero[pos[0],pos[1]+i]['letra']!=""):
                    #if(tablero.getDatosEnCoor((pos[0],pos[1]+i))['letra'] !=""):
                        ok = False
                    else:
                        direFinal = 1
            #elif((direcciones[pos_dir])and(ok==True)):
            #    for i in range(0,len(palabra),1):
            #        if(__tablero[pos[0]+i,pos[1]]['letra']!=""):
            #        #if(tablero.getDatosEnCoor((pos[0]+i,pos[1]))['letra'] !=""):
            #            ok = False
            #        else:
            #            direFinal = 2
            #elif((direcciones[pos_dir])and(ok==True)):
            #    for i in range(0,len(palabra),1):
            #        if(__tablero[pos[0],pos[1]-i]['letra']!=""):
            #        #if(tablero.getDatosEnCoor((pos[0],pos[1]-i))['letra'] !=""):
            #            ok = False
            #        else:
            #            direFinal = 3
            #elif((direcciones[pos_dir])and(ok==True)):
            #    for i in range(0,len(palabra),1):
            #        if(__tablero[pos[0]-i,pos[1]]['letra']!=""):
            #        #if(tablero.getDatosEnCoor((pos[0]-i,pos[1]))['letra'] !=""):
            #            ok = False
            #        else:
            #            direFinal = 4
            #direcciones.pop(pos_dir)
            #d = d - 1
        return(ok,direFinal)
    #-----------------------------------------------------------------------------------------------------------------------------------
    
    def __armo_estructura_IA(palabra,pos,direccion):
        dic_IA = {}
        if(direccion==1):
            for i in range(len(palabra)):
                dic_IA[(pos[0],pos[1]+i)] = palabra[i]
        elif(direccion==2):
            for i in range(len(palabra)):
                dic_IA[(pos[0]+i,pos[1])] = palabra[i]
        elif(direccion==3):
            for i in range(len(palabra)):
                dic_IA[(pos[0],pos[1]-i)] = palabra[i]
        else:
            for i in range(len(palabra)):
                dic_IA[(pos[0]-i,pos[1])] = palabra[i]

        return(dic_IA)

    #TENGO QUE ARMAR ESTA ESTRUCTURA {(7, 5): 'O', (7, 3): 'O', (7, 2): 'Z', (7, 4): 'RR'}

    #----------------------------------------------------------------------------------------------------------------------------------
    
    def __pongo_letras_IA(pos,direccion,palabra):
        
        if(direccion==1):
            for i in range(0,len(palabra),1):
                tablero.setValorEnCoor((pos[0],pos[1]+i),palabra[i])
        elif(direccion==2):
            for i in range(0,len(palabra),1):
                tablero.setValorEnCoor((pos[0]+i,pos[1]),palabra[i])
        elif(direccion==3):
            for i in range(0,len(palabra),1):
                tablero.setValorEnCoor((pos[0],pos[1]-i),palabra[i])
        else:
            for i in range(0,len(palabra),1):
                tablero.setValorEnCoor((pos[0]-1,pos[1]),palabra[i])
    
    #-----------------------------------------------------------------------------------------------------------------------------------

    if(turno == True):
        for intento in range(cant):
            palabra = __armo_palabra_IA(atril)
            posOK = __pos_valida_IA(medio,palabra)[0]
            direccion = __pos_valida_IA(medio,palabra)[1]
            if(posOK==True):
                jugada_IA = __armo_estructura_IA(palabra,medio,direccion)
                sigue = __informacion_de_turno(jugada_IA)
                if(sigue[0]==True):
                    print("RESULTAAAAADO")
                    print(sigue[1])
                else:
                    print(sigue[1])
    else:
        for intento in range(cant):
            palabra = __armo_palabra_IA(atril)
            posOK = __pos_valida_IA(medio,palabra)[0]
            direccion = __pos_valida_IA(medio,palabra)[1]
            if(posOK==True):
                jugada_IA = __armo_estructura_IA(palabra,medio,direccion)
                sigue = __informacion_de_turno(jugada_IA)
                if(sigue[0]==True):
                    print("RESULTAAAAADO")
                    print(sigue[1])
                else:
                    print(sigue[1])

print(__jugabilidad_IA(__tablero,atril,__bolsa,2,True))