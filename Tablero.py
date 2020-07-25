import PySimpleGUI as sg
import random
from CLASS import CLASS_atril_andando
from CLASS import CLASS_bolsa_andando
from CLASS import CLASS_temporizador_andando
from CLASS import CLASS_tablero_andando
#from corroboro_y_puntuo import corroborarPalabra


def juego(FICHAS):
    sg.theme('Topanga')

    
    """En base a un diccionario predefinido, conseguir las 7 letras a usar por turnos,
    todo esto lo vamos a hacer o realizar con objetos, para que se instancien cada vez que sean necesario, y 
    la bolsa de letras se va a ir actualizando a medida de que vayamos retirando letras del abecedario tanto, 
    del jugador, como de la computadora"""

    B = CLASS_bolsa_andando.Bolsa(FICHAS)

    Atril_computadora = CLASS_atril_andando.Atril(B.dameFichas(7))     #LA IDEA ES QUE RECIBA UN DICCIONARIO DE FORMATO ESPECIFICO, QUE VIENE DE LA CONFIGURACION O PARTIDA
    Atril_jugador = CLASS_atril_andando.Atril(B.dameFichas(7))  


    def formatear(ficha):

        aux = []
        for LETRA in ficha:
            if not LETRA.isdecimal():
                aux.append(LETRA)

        nueva_cadena = ""
        for letra in aux: 
            nueva_cadena = nueva_cadena + letra

        return nueva_cadena
   

    Lista_j=Atril_jugador.getFichas_disponibles()
    Lista_c=Atril_computadora.getFichas_disponibles()

    
    def cant_fichas_tablero_jugador(Lista_j): #Seteo cant fichas
        fichas=[]
        for i in Lista_j:
            fichas.append(sg.Button(i, pad=(10,5), button_color=('white', 'black'), size=(3, 1), font=("Helvetica", 16)))
        return fichas
    
    def cant_fichas_tablero_computadora(Lista_c): #Seteo cant fichas
        fichas=[]
        for i in Lista_c:
            fichas.append(sg.Button("?", pad=(10,5), button_color=('white', 'black'), size=(3, 1), font=("Helvetica", 16),disabled=True))
        return fichas
    
    fichasJ = cant_fichas_tablero_jugador(Lista_j)
    fichasC = cant_fichas_tablero_computadora(Lista_c)

    def CreandoTablero(tableroD,cant):#areglar i,j o j,i        se crea el tablero recibiendo el tablero y la cantidad de filas y columnas 
        tablero=[]
        lista1=[]
        for i in range(cant):
            lista1.clear()
            for j in range(cant):
                if TableroD[(i,j)]["trampa"]==True:
                    if TableroD[(i,j)]["tipo_de_trampa"]=="-1":
                        lista1.append(sg.Button("",size=(2, 1),key=(i,j), pad=(2,3),button_color=('black','Dark grey'),image_filename='imagenes\menos 1.png',image_size=(25, 22)))
                    elif TableroD[(i,j)]["tipo_de_trampa"]=="-2":
                        lista1.append(sg.Button("",size=(2, 1),key=(i,j), pad=(2,3),button_color=('black','Dark grey'),image_filename='imagenes\menos 2.png',image_size=(25, 22)))
                    else:
                        lista1.append(sg.Button("",size=(2, 1),key=(i,j), pad=(2,3),button_color=('black','Dark grey'),image_filename='imagenes\menos 3.png',image_size=(25, 22)))
                elif TableroD[(i,j)]["recompensa"]==True:
                    if TableroD[(i,j)]["tipo_de_recompensa"]=="x2":
                        lista1.append(sg.Button("",size=(2, 1),key=(i,j), pad=(2,3),button_color=('black','Dark grey'),image_filename='imagenes\multiplicador x2.png',image_size=(25, 22)))
                    else:
                        lista1.append(sg.Button("",size=(2, 1),key=(i,j), pad=(2,3),button_color=('black','Dark grey'),image_filename='imagenes\multiplicador x3.png',image_size=(25, 22)))
                else:
                    lista1.append(sg.Button("",size=(2, 1),key=(i,j), pad=(2,3),button_color=('black','Dark grey'),image_filename='imagenes\GRIS.png',image_size=(25, 22)))
            lista1=[lista1]
            tablero=tablero+lista1
        return tablero

    def actualizando_tablero(dic,Tablero,window):#Aca vuelven la tabla a su estado original si el jugador pone una palabra erronea
        for i in dic.keys():
                window[dic[i]["letra"]].update(disabled=False, button_color=('white', 'black'))
                Tablero.setValorEnCoor(i,"")
                lugar=Tablero.getDatosEnCoor(i)
                print(i)
                print(lugar)
                if lugar["trampa"]==True: 
                    if lugar["tipo_de_trampa"]=="-1":
                        window[i].update("",disabled=False,image_filename='imagenes\menos 1.png',image_size=(25, 22))
                    elif lugar["tipo_de_trampa"]=="-2":
                        window[i].update("",disabled=False,image_filename='imagenes\menos 2.png',image_size=(25, 22))
                    else:
                        window[i].update("",disabled=False,image_filename='imagenes\menos 3.png',image_size=(25, 22))
                elif lugar["recompensa"]==True:
                    if lugar["tipo_de_recompensa"]=="x2":
                        window[i].update("",disabled=False,image_filename='imagenes\multiplicador x2.png',image_size=(25, 22))
                    else:
                        window[i].update("",disabled=False,image_filename='imagenes\multiplicador x3.png',image_size=(25, 22))
                else:
                    window[i].update("",disabled=False,image_filename='imagenes\GRIS.png',image_size=(25, 22))

    def actualizar_fichas(dic,B,window,Atril_jugador):
        cant=len(dic.keys())
        Nuevas=B.damefichas(cant)
        lista=[]
        dic={}
        for i in dic.keys():
            lista.append(dic[i]["letra"])
            dic[i]["letra"]=Atril_jugador.getEstado()
        Atril_jugador.sacar_varias_fichas(lista) 
             



    TableroD= {(0, 0): {'letra': None, 'trampa': True, 'tipo_de_trampa': "-1", 'recompensa': False, 'tipo_de_recompensa': None}, (0, 1): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (0, 2): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (0, 3): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (0, 4): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (0, 5): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (0, 6): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (0, 7): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (0, 8): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (0, 9): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (0, 10): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (0, 11): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (0, 12): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (0, 13): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (0, 14): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (0, 15): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (1, 0): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (1, 1): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (1, 2): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (1, 3): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (1, 4): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (1, 5): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (1, 6): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (1, 7): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (1, 8): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (1, 9): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (1, 10): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (1, 11): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (1, 12): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (1, 13): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (1, 14): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (1, 15): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (2, 0): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (2, 1): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (2, 2): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (2, 3): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (2, 4): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (2, 5): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (2, 6): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (2, 7): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (2, 8): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (2, 9): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (2, 10): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (2, 11): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (2, 12): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (2, 13): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (2, 14): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (2, 15): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (3, 0): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 
        'tipo_de_recompensa': None}, (3, 1): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (3, 2): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (3, 3): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (3, 4): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (3, 5): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (3, 6): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (3, 7): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (3, 8): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (3, 9): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (3, 10): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (3, 11): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (3, 12): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (3, 13): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (3, 14): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (3, 15): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (4, 0): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (4, 1): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (4, 2): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (4, 3): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (4, 4): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (4, 5): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (4, 6): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (4, 7): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (4, 8): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (4, 9): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (4, 10): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (4, 11): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (4, 12): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (4, 13): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (4, 14): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (4, 15): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (5, 0): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (5, 1): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (5, 2): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (5, 3): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (5, 4): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (5, 5): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (5, 6): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (5, 7): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (5, 8): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (5, 9): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (5, 10): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (5, 11): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (5, 12): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (5, 13): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (5, 14): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (5, 15): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (6, 0): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (6, 1): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (6, 2): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (6, 3): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (6, 4): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (6, 5): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (6, 6): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (6, 7): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (6, 8): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (6, 9): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (6, 10): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (6, 11): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (6, 12): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, 
        (6, 13): {'letra': None, 'trampa': True, 'tipo_de_trampa': "-2", 'recompensa': False, 'tipo_de_recompensa': None}, (6, 14): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (6, 15): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (7, 0): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (7, 1): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (7, 2): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (7, 3): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (7, 4): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (7, 5): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (7, 6): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (7, 7): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (7, 8): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (7, 9): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (7, 10): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (7, 11): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (7, 12): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (7, 13): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (7, 14): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (7, 15): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (8, 0): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (8, 1): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (8, 2): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (8, 3): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (8, 4): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (8, 5): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (8, 6): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (8, 7): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (8, 8): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (8, 9): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (8, 10): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (8, 11): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (8, 12): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (8, 13): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (8, 14): {'letra': None, 'trampa': False, 
        'tipo_de_trampa': None, 'recompensa': True, 'tipo_de_recompensa': "x3"}, (8, 15): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (9, 0): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (9, 1): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (9, 2): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (9, 3): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (9, 4): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (9, 5): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (9, 6): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (9, 7): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (9, 8): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (9, 9): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (9, 10): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (9, 11): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (9, 12): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (9, 13): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (9, 14): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (9, 15): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (10, 0): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (10, 1): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (10, 2): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (10, 3): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (10, 4): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (10, 5): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (10, 6): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (10, 7): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (10, 8): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (10, 9): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (10, 10): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (10, 11): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (10, 12): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (10, 13): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (10, 14): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (10, 15): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (11, 0): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (11, 1): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (11, 2): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (11, 3): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (11, 4): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (11, 5): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (11, 6): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (11, 7): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (11, 8): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (11, 9): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (11, 10): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, 
        (11, 11): {'letra': None, 'trampa': True, 'tipo_de_trampa': "-3", 'recompensa': False, 'tipo_de_recompensa': None}, (11, 12): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (11, 13): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (11, 14): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (11, 15): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (12, 0): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (12, 1): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (12, 2): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (12, 3): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (12, 4): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (12, 5): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (12, 6): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (12, 7): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (12, 8): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (12, 9): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (12, 10): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (12, 11): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (12, 12): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (12, 13): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (12, 14): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (12, 15): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (13, 0): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (13, 1): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (13, 2): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (13, 3): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (13, 4): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (13, 5): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (13, 6): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (13, 7): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, 
        (13, 8): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': True, 'tipo_de_recompensa': "x2"}, (13, 9): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (13, 10): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (13, 11): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (13, 12): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (13, 13): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (13, 14): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (13, 15): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (14, 0): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (14, 1): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (14, 2): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (14, 3): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (14, 4): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (14, 5): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (14, 6): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (14, 7): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (14, 8): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (14, 9): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (14, 10): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (14, 11): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (14, 12): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (14, 13): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (14, 14): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (14, 15): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (15, 0): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (15, 1): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (15, 2): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (15, 3): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (15, 4): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (15, 5): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (15, 6): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (15, 7): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (15, 8): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (15, 9): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (15, 10): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (15, 11): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (15, 12): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (15, 13): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (15, 14): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (15, 15): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}}   

    titulo =  [[sg.Text(' '*15)] + [sg.Text("ScrabbleAr", size=(10,1),key="menu")],
    [sg.Text('Tiempo restante'), sg.T(' '*1), sg.Text(size=(10,1), key='-TEMP OUT-')]]


            
    tabla=CreandoTablero(TableroD,15)



    fichas_jugador = [fichasJ+[sg.Button("Poner",key="_poner_",font=("Helvetica", 9) ,button_color=('white','grey'),size=(6, 2))],
    [sg.Button(('Posponer partida!'),key="__save__",font=("Helvetica", 9) ,button_color=('white','grey')),sg.Button(("Terminar juego"), key="__exit__",font=("Helvetica", 9) ,button_color=('white','grey')),sg.Button(("REPARTIR NUEVAS FICHAS"),button_color=('white','grey'), key="__repartir__",font=("Helvetica", 9)),sg.Button('Pasar Turno',key="__pasar__",button_color=('black','white'), font=("Helvetica", 16))]]



    fichas_computadora = [fichasC] 


    layout = titulo + fichas_computadora + tabla + fichas_jugador

    window = sg.Window('ScrabbleAr', layout, font='Courier 12')

    T = CLASS_temporizador_andando.Temporizador(40,30)                         
    cantRead = 0                                    

    La_ficha=""
    tupla=""
    tablero=CLASS_tablero_andando.Tablero(TableroD)
    dic={}
    while not T.getTERMINO_Temporizador():
        event, values= window.read(timeout=10)
        cantRead = cantRead + 1  
        cantRead = T.avanzar_tiempo(cantRead)  
        window['-TEMP OUT-'].update(str(T.getMinutos()) + ":"+ str(T.getSegundos()) + ' min')       
        if type(event)== tuple and event!= '__TIMEOUT__' : 
            tupla=event
            print(tupla)
        if type(event)==str and event!= "_poner_" and event!= '__TIMEOUT__' :
            aux=event
            La_ficha=formatear(event)
            print(La_ficha)

        if event == "__exit__" and event!= '__TIMEOUT__' :
            window.close()
            break
        #elif event == "__save__":
            #Vamos a guardar la partida con la configuracion actual en un archivo de texto 
        if event == "_poner_" and La_ficha!="" and tupla!="" and event!= '__TIMEOUT__' :
            window[aux].update(disabled=True, button_color=('black','white'))
            window[tupla].update(La_ficha,disabled=True,button_color=('','white'),image_filename='', image_size=(23, 20))
            dic[tupla]=tablero.getDatosEnCoor(tupla)
            dic[tupla]["letra"]=La_ficha
            La_ficha=""
            tupla=""
        #if event=="__repartir__":
        if event=="__pasar__" and event!= '__TIMEOUT__' :
            correcta=True
            if(correcta==True):
                #puntaje=corroborarPalabra.puntuacion()
                print("hola")
                print(dic)
            else:
                actualizando_tablero(dic,tablero,window)




            
        
    print(juego.__doc__)