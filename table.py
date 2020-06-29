import PySimpleGUI as sg
import random

abecedario="A,A,A,A,A,A,A,A,A,A,A,B,B,B,C,C,C,C,D,D,D,D,E,E,E,E,E,E,E,E,E,E,E,F,F,G,G,H,H,I,I,I,I,I,I,J,J,K,L,L,L,L,LL,M,M,M,N,N,N,N,N,Ñ,O,O,O,O,O,O,O,O,P,P,Q,R,R,R,R,RR,S,S,S,S,S,S,S,T,T,T,T,U,U,U,U,U,U,V,V,W,X,Y,Z"
abecedario2={'A':1,'B':2,'M':2,'I':1}

print(abecedario)

abecedario=abecedario.split(",")

print(abecedario)

sg.theme('Topanga')

def letras_jugador():
    letras=[]
    for i in range(1,8):
        a=random.randrange(1,len(abecedario))
        letras.append(abecedario[a])
    return letras

titulo =  [[sg.Text(' '*15)] + [sg.Text("ScrabbleAr", size=(10,1),key="menu")]]

tablero =[[sg.Button("", size=(2, 1),key=(j,i), pad=(2,3)) for i in range(15)] for j in range(15)]
letras_j = letras_jugador()
letras_c = letras_jugador()

fichas_jugador = [
    [sg.Button(letras_j[0], pad=(10,5), button_color=('white', 'black'), size=(3, 1), font=("Helvetica", 16)),
    sg.Button(letras_j[1], pad=(10,5), button_color=('white', 'black'), size=(3, 1), font=("Helvetica", 16)),
    sg.Button(letras_j[2], pad=(10,5), button_color=('white', 'black'), size=(3, 1), font=("Helvetica", 16)),
    sg.Button(letras_j[3], pad=(10,5), button_color=('white', 'black'), size=(3, 1), font=("Helvetica", 16)),
    sg.Button(letras_j[4], pad=(10,5), button_color=('white', 'black'), size=(3, 1), font=("Helvetica", 16)),
    sg.Button(letras_j[5], pad=(10,5), button_color=('white', 'black'), size=(3, 1), font=("Helvetica", 16)),
    sg.Button(letras_j[6], pad=(10,5), button_color=('white', 'black'), size=(3, 1), font=("Helvetica", 16))],
    [sg.Button('Save'),sg.Button(("Exit"), key="__exit__")]
      ]

    
fichas_computadora = [
    [sg.Button(letras_c[0], pad=(10,5), button_color=('white', 'black'), size=(3, 1), font=("Helvetica", 16), visible=True),
    sg.Button(letras_c[1], pad=(10,5), button_color=('white', 'black'), size=(3, 1), font=("Helvetica", 16), visible=True),
    sg.Button(letras_c[2], pad=(10,5), button_color=('white', 'black'), size=(3, 1), font=("Helvetica", 16), visible=True),
    sg.Button(letras_c[3], pad=(10,5), button_color=('white', 'black'), size=(3, 1), font=("Helvetica", 16), visible=True),
    sg.Button(letras_c[4], pad=(10,5), button_color=('white', 'black'), size=(3, 1), font=("Helvetica", 16), visible=True),
    sg.Button(letras_c[5], pad=(10,5), button_color=('white', 'black'), size=(3, 1), font=("Helvetica", 16), visible=True),
    sg.Button(letras_c[6], pad=(10,5), button_color=('white', 'black'), size=(3, 1), font=("Helvetica", 16), visible=True)],
      ]

layout = titulo + fichas_computadora + tablero + fichas_jugador

window = sg.Window('ScrabbleAr', layout, font='Courier 12')

pos = []
jugador1={}
while True:
    sg.popup("elige una ficha")
    event, values = window.read() 
    if event == "__exit__" or sg.WIN_CLOSED:
        break 
    elif event is letras_j[0] or letras_j[1] or letras_j[2] or letras_j[3] or letras_j[4] or letras_j[5] or letras_j[6]:
        print(event[0]) #letra actual
        window[event[0]].update(disabled=True)
        #window.
        sg.popup("elige una posicion")
        eventPos= window.read()
        print(eventPos[0]) #posicion de la letra actual
        jugador1[(eventPos[0])]=event[0]
        window[eventPos[0]].update(event[0],disabled=True)
print(jugador1)