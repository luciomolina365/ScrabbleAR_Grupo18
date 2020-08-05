import PySimpleGUI as sg
from Archivos import metodos_de_archivos
import Tablero
from ScrabbleAR import jugar


def mostrar_partidas_guardadas(lista):

    """Muestra una nueva ventana con una listbox de todas las partidas posibles a cargar
     y al confirmar retorna la direccion a cargar."""

    layout=[[sg.Text('Seleccione la partida a cargar',text_color="white",background_color="black")],
        [sg.Listbox(lista, size = (70,15) , key = "listBox" , select_mode=False)],
        [sg.Button("Confirmar",key="confirmar"),sg.Cancel(button_color=('black','white'))]]

    window = sg.Window('Partidas guardadas', layout,background_color="black")
    datos=None
    while True:
        event, values= window.read()
        if event=="Cancel":
            window.close()
            break
        if event=="confirmar":
            if datos==None and values["listBox"]!=[]:
                datos = values["listBox"][0]
                window.close()
                return datos
            else:
                pass


def mostrar_ten(topFacil,topMedio,topDificil):
    
    """Muestra una nueva ventana con una listbox de top ten dependiendo la dificultad que elijas.  Del fomato nombre, puntaje , dificultad y fecha."""

    layout=[[sg.Text('Seleccione la dificultad para ver el Top Ten',text_color="white",background_color="black")],
        [sg.Button("Facil",key="facil",button_color=('black','white')),sg.Button("Medio",key="medio",button_color=('black','white')),sg.Button("Dificil",key="dificil",button_color=('black','white'))],
        [sg.Listbox([], size = (70,15) , key = "listBox" , select_mode=False)],
        [sg.Cancel(button_color=('black','white'))]]

    window = sg.Window('Top Ten', layout,background_color="black")
    No_hay_partidas=["No hay registros en esta dificultad"]

    while True:
        event, values= window.read()
        
        if event=="Cancel":
            window.close()
            break
        
        if event=="dificil":
            if topDificil==[]:
                window["listBox"].update(No_hay_partidas)
            else:
                window["listBox"].update(topDificil)
        
        if event=="medio":
            if topMedio==[]:
                window["listBox"].update(No_hay_partidas)
            else:
                window["listBox"].update(topMedio)    
        
        if event=="facil":
            if topFacil==[]:
                window["listBox"].update(No_hay_partidas)
            else:
                window["listBox"].update(topFacil)



"""La ventana del menu principal donde se mostrara iniciar partida,
cargar partida (estara desabilitada si no hay partidas guardadas) y el top ten de los mejores puntajes."""

archivos = metodos_de_archivos
archivos.actualizar_cant_partidas_guardadas()

ok = archivos.hay_partidas_a_cargar()
Iniciar = [sg.Button("Iniciar Partida",size=(10,5),key="_iniciar_",button_color=('white','grey'))]

if(ok == False):
    Cargar=[sg.Button("Cargar Partida",size=(10,5),disabled=True, key="cargar",button_color=('white','grey'))]
else:
    Cargar=[sg.Button("Cargar Partida",size=(10,5),enable_events=True, key="cargar",button_color=('white','grey'))]

titulo =  [[sg.Text("Scrabble", size=(22,10),auto_size_text=True)]]

Top=[[sg.Button(("Top Ten"),key="topTen",size=(22,1))]] 


layout= titulo + [Iniciar + Cargar ] + Top

window = sg.Window('ScrabbleAr', layout, font='Courier 12',background_color="black",disable_close=True, disable_minimize=True)




while True:
    event, values= window.read()

    if event == "cargar":
        lista=archivos.lista_de_partidas_a_cargar()
        direccion=mostrar_partidas_guardadas(lista)
        if direccion!= None:
            partida = archivos.cargarPartida(direccion)
            window.close()
            Tablero.juego(partida)
            break

    if event == "_iniciar_":
        window.close()
        jugar()
        break

    if(event=="topTen"):
        topFacil=archivos.TopTen_de_jugadores(1)
        topMedio=archivos.TopTen_de_jugadores(2)
        topDificil=archivos.TopTen_de_jugadores(3)
        mostrar_ten(topFacil,topMedio,topDificil)