import PySimpleGUI as sg
import random
import CLASS



def juego(fichas):
    sg.theme('Topanga')
    B=CLASS.CLASS_bolsa_andando.Bolsa(fichas)
    def letras_jugador(fichas):
        """En base a un diccionario predefinido, conseguir las 7 letras a usar por turnos,
         todo esto lo vamos a hacer o realizar con objetos, para que se instancien cada vez que sean necesario, y 
         la bolsa de letras se va a ir actualizando a medida de que vayamos retirando letras del abecedario tanto, 
         del jugador, como de la computadora"""

        
        letras={}
        letras=B.dameFichas(7)
        return letras

    titulo =  [[sg.Text(' '*15)] + [sg.Text("ScrabbleAr", size=(10,1),key="menu")]]

    tablero =[[sg.Button("", size=(2, 1),key=(j,i), pad=(2,3),button_color=('black','Dark grey'),image_filename='imagenesTablero\menos 1.png', image_size=(25, 22)) for i in range(15)] for j in range(15)]
    letras_j = letras_jugador(fichas)
    letras_c = letras_jugador(fichas)
    
    le={}
    A=CLASS.CLASS_atril_andando.Atril(le)

    def cant_fichas_tablero_jugador(un_numero=7): #Seteo cant fichas
        fichas=[]
        for i in range(un_numero):
            fichas.append(sg.Button(letras_j.keys()[i], pad=(10,5), button_color=('white', 'black'), size=(3, 1), font=("Helvetica", 16)))
        return fichas
    
    def cant_fichas_tablero_computadora(un_numero=7): #Seteo cant fichas
        fichas=[]
        for i in range(un_numero):
            fichas.append(sg.Button("?", pad=(10,5), button_color=('white', 'black'), size=(3, 1), font=("Helvetica", 16)))
        return fichas
    
    fichasJ = cant_fichas_tablero_jugador()
    fichasC = cant_fichas_tablero_computadora()



    fichas_jugador = [
        [sg.Button(letras_j[0], pad=(10,5), button_color=('black','white'), size=(3, 1), font=("Helvetica", 16)),
         sg.Button(letras_j[1], pad=(10,5), button_color=('black','white'), size=(3, 1), font=("Helvetica", 16)),
         sg.Button(letras_j[2], pad=(10,5), button_color=('black','white'), size=(3, 1), font=("Helvetica", 16)),
         sg.Button(letras_j[3], pad=(10,5), button_color=('black','white'), size=(3, 1), font=("Helvetica", 16)),
         sg.Button(letras_j[4], pad=(10,5), button_color=('black','white'), size=(3, 1), font=("Helvetica", 16)),
         sg.Button(letras_j[5], pad=(10,5), button_color=('black','white'), size=(3, 1), font=("Helvetica", 16)),
         sg.Button(letras_j[6], pad=(10,5), button_color=('black','white'), size=(3, 1), font=("Helvetica", 16))
          ]]


    fichas_computadora = [
        [sg.Button(letras_c[0], pad=(10,5), button_color=('black','white'), size=(3, 1), font=("Helvetica", 16)),
         sg.Button(letras_c[1], pad=(10,5), button_color=('black','white'), size=(3, 1), font=("Helvetica", 16)),
         sg.Button(letras_c[2], pad=(10,5), button_color=('black','white'), size=(3, 1), font=("Helvetica", 16)),
         sg.Button(letras_c[3], pad=(10,5), button_color=('black','white'), size=(3, 1), font=("Helvetica", 16)),
         sg.Button(letras_c[4], pad=(10,5), button_color=('black','white'), size=(3, 1), font=("Helvetica", 16)),
         sg.Button(letras_c[5], pad=(10,5), button_color=('black','white'), size=(3, 1), font=("Helvetica", 16)),
         sg.Button(letras_c[6], pad=(10,5), button_color=('black','white'), size=(3, 1), font=("Helvetica", 16))
    ]]

    fichas_jugador = [fichasJ,[sg.Button(('Posponer partida!'),key="__save__",font=("Helvetica", 9) ,button_color=('white','grey')),sg.Button(("Terminar juego"), key="__exit__",font=("Helvetica", 9) ,button_color=('white','grey')),sg.Button(("REPARTIR NUEVAS FICHAS"),button_color=('white','grey'), key="__repartir__",font=("Helvetica", 9)),sg.Button('Pasar Turno',key="__pasar__",button_color=('black','white'), font=("Helvetica", 16))]]


    fichas_computadora = [fichasC]

    layout = titulo + fichas_computadora + tablero + fichas_jugador

    window = sg.Window('ScrabbleAr', layout, font='Courier 12')

    pos = []
    jugador1={}
    while True:
        sg.popup("elige una ficha")
        event, values = window.read() 
        if event == "__exit__":
            break
        #elif event == "__save__":
            #Vamos a guardar la partida con la configuracion actual en un archivo de texto 
        elif event is letras_j[0] or letras_j[1] or letras_j[2] or letras_j[3] or letras_j[4] or letras_j[5] or letras_j[6]:
            print(event[0]) #letra actual
            window[event[0]].update(disabled=True, button_color=('black','white'))
            #window.
            sg.popup("elige una posicion")
            eventPos= window.read()
            print(eventPos[0]) #posicion de la letra actual
            jugador1[(eventPos[0])]=event[0]
            window[eventPos[0]].update(event[0],disabled=True,button_color=('','white'),image_filename='', image_size=(23, 20))
    print(jugador1)
    print(juego.__doc__)