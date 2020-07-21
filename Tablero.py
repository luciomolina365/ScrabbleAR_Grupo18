import PySimpleGUI as sg
import random

def juego():
    abecedario="A,A,A,A,A,A,A,A,A,A,A,B,B,B,C,C,C,C,D,D,D,D,E,E,E,E,E,E,E,E,E,E,E,F,F,G,G,H,H,I,I,I,I,I,I,J,J,K,L,L,L,L,LL,M,M,M,N,N,N,N,N,Ñ,O,O,O,O,O,O,O,O,P,P,Q,R,R,R,R,RR,S,S,S,S,S,S,S,T,T,T,T,U,U,U,U,U,U,V,V,W,X,Y,Z"
    abecedario=abecedario.split(",")
    
    sg.theme('Topanga')

    def letras_jugador():
        """Lo que buscamos hacer, es en base a un diccionario predefinido, conseguir las 7 letras a usar por turnos,
         todo esto lo vamos a hacer o realizar con objetos, para que se instancien cada vez que sean necesario, y 
         la bolsa de letras se va a ir actualizando a medida de que vayamos retirando letras del abecedario tanto, 
         del jugador, como de la computadora"""


        letras=[]
        for i in range(1,8):
            a=random.randrange(1,len(abecedario))
            letras.append(abecedario[a])
        return letras

    titulo =  [[sg.Text(' '*15)] + [sg.Text("ScrabbleAr", size=(10,1),key="menu")]]

    tablero =[[sg.Button("", size=(2, 1),key=(j,i), pad=(2,3)) for i in range(15)] for j in range(15)]
    letras_j = letras_jugador()
    letras_c = letras_jugador()
    
    def cant_fichas_tablero_jugador(un_numero=7): #Seteo cant fichas
        fichas=[]
        for i in range(un_numero):
            fichas.append(sg.Button(letras_j[i], pad=(10,5), button_color=('white', 'black'), size=(3, 1), font=("Helvetica", 16)))
        return fichas
    
    def cant_fichas_tablero_computadora(un_numero=7): #Seteo cant fichas
        fichas=[]
        for i in range(un_numero):
            fichas.append(sg.Button("?", pad=(10,5), button_color=('white', 'black'), size=(3, 1), font=("Helvetica", 16)))
        return fichas
    
    fichasJ = cant_fichas_tablero_jugador()
    fichasC = cant_fichas_tablero_computadora()



    fichas_jugador = [fichasJ,[sg.Button(('PAUSA'),key="__save__",font=("Helvetica", 9)),sg.Button(("FINALIZAR PARTIDA"), key="__exit__",font=("Helvetica", 9)),sg.Button(("REPARTIR NUEVAS FICHAS"), key="__repartir__",font=("Helvetica", 9))]]


    fichas_computadora = [fichasC]

    layout = titulo + fichas_computadora + tablero + fichas_jugador

    window = sg.Window('ScrabbleAr', layout, font='Courier 12')

    pos = []
    jugador1={}
    while True:
        #sg.popup("elige una ficha")
        event, values = window.read() 
        if event == "__exit__" or sg.WIN_CLOSED:
            break
        #elif event == "__save__":
            #Vamos a guardar la partida con la configuracion actual en un archivo de texto 
        elif event is letras_j[0] or letras_j[1] or letras_j[2] or letras_j[3] or letras_j[4] or letras_j[5] or letras_j[6]:
            print(event[0]) #letra actual
            window[event[0]].update(disabled=True)
            #window.
            #sg.popup("elige una posicion")
            eventPos= window.read()
            print(eventPos[0]) #posicion de la letra actual
            jugador1[(eventPos[0])]=event[0]
            window[eventPos[0]].update(event[0],disabled=True)
    print(jugador1)
    print(juego.__doc__)