import PySimpleGUI as sg
import random
from CLASS import CLASS_atril_andando
from CLASS import CLASS_bolsa_andando
from CLASS import CLASS_reloj_andando

def juego(FICHAS):
    sg.theme('Topanga')

    
    """En base a un diccionario predefinido, conseguir las 7 letras a usar por turnos,
    todo esto lo vamos a hacer o realizar con objetos, para que se instancien cada vez que sean necesario, y 
    la bolsa de letras se va a ir actualizando a medida de que vayamos retirando letras del abecedario tanto, 
    del jugador, como de la computadora"""

    B = CLASS_bolsa_andando.Bolsa(FICHAS)

    Atril_computadora = CLASS_atril_andando.Atril(B.dameFichas(7))               #Hay que darle un valor inicial pero este caso de testeo no pasa nada
    Atril_jugador = CLASS_atril_andando.Atril(B.dameFichas(7))  



   
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


    fichas_jugador = [fichasJ+[sg.Button("Poner",key="_poner_",font=("Helvetica", 9) ,button_color=('white','grey'),size=(6, 2))],
    [sg.Button(('Posponer partida!'),key="__save__",font=("Helvetica", 9) ,button_color=('white','grey')),sg.Button(("Terminar juego"), key="__exit__",font=("Helvetica", 9) ,button_color=('white','grey')),sg.Button(("REPARTIR NUEVAS FICHAS"),button_color=('white','grey'), key="__repartir__",font=("Helvetica", 9)),sg.Button('Pasar Turno',key="__pasar__",button_color=('black','white'), font=("Helvetica", 16))]]



    fichas_computadora = [fichasC] 


    layout = titulo + fichas_computadora + tablero + fichas_jugador

    window = sg.Window('ScrabbleAr', layout, font='Courier 12')

    La_ficha=""
    tupla=""
    while True:
        event, values= window.read() 
        print("*"*50)
        print(event)
        if type(event)== tuple: 
            tupla=event
        if type(event)==str and event!= "_poner_":
            La_ficha=event
        print("/"*50)
        print(La_ficha)
        print(tupla)
        print("/"*50)
        
        if event == "__exit__":
            break
            window.close()


        #elif event == "__save__":
            #Vamos a guardar la partida con la configuracion actual en un archivo de texto 


        elif event == "_poner_":
            print("8"*50)
            print(La_ficha)
            print(tupla)
            print("8"*50)
            window[La_ficha].update(disabled=True, button_color=('black','white'))
            window[tupla].update(La_ficha,disabled=True,button_color=('','white'),image_filename='', image_size=(23, 20))
            
            

    print(juego.__doc__)