import PySimpleGUI as sg
import random
from CLASS import CLASS_atril_andando
from CLASS import CLASS_bolsa_andando

def juego(FICHAS):
    sg.theme('Topanga')

    
    """En base a un diccionario predefinido, conseguir las 7 letras a usar por turnos,
    todo esto lo vamos a hacer o realizar con objetos, para que se instancien cada vez que sean necesario, y 
    la bolsa de letras se va a ir actualizando a medida de que vayamos retirando letras del abecedario tanto, 
    del jugador, como de la computadora"""



    Atril_computadora = CLASS_atril_andando.Atril({})               #Hay que darle un valor inicial pero este caso de testeo no pasa nada
    Atril_jugador = CLASS_atril_andando.Atril({})  


    B = CLASS_bolsa_andando.Bolsa(FICHAS)


    Atril_computadora.agregar_varias_fichas(B.dameFichas(7))

    Atril_jugador.agregar_varias_fichas(B.dameFichas(7))
   
    def atriles(DIC):
        LISTA = []
        for elemento in DIC:                      #Hace una lista con las letras y sus repetidas
            cant = DIC[elemento]["cantidad"]
            for i in range(cant):
                LISTA.append(elemento)
        return LISTA    

    Lista_j=atriles(Atril_jugador.getEstado())
    Lista_c=atriles(Atril_computadora.getEstado())

    
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

    titulo =  [[sg.Text(' '*15)] + [sg.Text("ScrabbleAr", size=(10,1),key="menu")]]

    tablero =[[sg.Button("", size=(2, 1),key=(j,i), pad=(2,3),button_color=('black','Dark grey'),image_filename='imagenesTablero\menos 1.png', image_size=(25, 22)) for i in range(15)] for j in range(15)]

    fichas_computadora = [
        [sg.Button(Lista_c[0], pad=(10,5), button_color=('black','white'), size=(3, 1), font=("Helvetica", 16),enable_events=False,disabled=True),
         sg.Button(Lista_c[1], pad=(10,5), button_color=('black','white'), size=(3, 1), font=("Helvetica", 16),enable_events=False,disabled=True),
         sg.Button(Lista_c[2], pad=(10,5), button_color=('black','white'), size=(3, 1), font=("Helvetica", 16),enable_events=False,disabled=True),
         sg.Button(Lista_c[3], pad=(10,5), button_color=('black','white'), size=(3, 1), font=("Helvetica", 16),enable_events=False,disabled=True),
         sg.Button(Lista_c[4], pad=(10,5), button_color=('black','white'), size=(3, 1), font=("Helvetica", 16),enable_events=False,disabled=True),
         sg.Button(Lista_c[5], pad=(10,5), button_color=('black','white'), size=(3, 1), font=("Helvetica", 16),enable_events=False,disabled=True),
         sg.Button(Lista_c[6], pad=(10,5), button_color=('black','white'), size=(3, 1), font=("Helvetica", 16),enable_events=False,disabled=True)
    ]]

    fichas_jugador = [fichasJ,[sg.Button(('Posponer partida!'),key="__save__",font=("Helvetica", 9) ,button_color=('white','grey')),sg.Button(("Terminar juego"), key="__exit__",font=("Helvetica", 9) ,button_color=('white','grey')),sg.Button(("REPARTIR NUEVAS FICHAS"),button_color=('white','grey'), key="__repartir__",font=("Helvetica", 9)),sg.Button('Pasar Turno',key="__pasar__",button_color=('black','white'), font=("Helvetica", 16))]]


    fichas_computadora = [fichasC]

    layout = titulo + fichas_computadora + tablero + fichas_jugador

    window = sg.Window('ScrabbleAr', layout, font='Courier 12')


    while True:
        event, values = window.read() 
        print(event)
        if event == "__exit__":
            break
            window.close()
        #elif event == "__save__":
            #Vamos a guardar la partida con la configuracion actual en un archivo de texto 
        elif event is Lista_j[0] or Lista_j[1] or Lista_j[2] or Lista_j[3] or Lista_j[4] or Lista_j[5] or Lista_j[6]:
            print(event[0]) #letra actual
            window[event[0]].update(disabled=True, button_color=('black','white'))
            #window.
            sg.popup("elige una posicion")
            eventPos= window.read()
            print(eventPos[0]) #posicion de la letra actual
            #jugador1[(eventPos[0])]=event[0]
            window[eventPos[0]].update(event[0],disabled=True,button_color=('','white'),image_filename='', image_size=(23, 20))

    print(juego.__doc__)