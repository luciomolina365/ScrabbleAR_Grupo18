import PySimpleGUI as sg
from Archivos import metodos_de_archivos
import Tablero
from ScrabbleAR import jugar



archivos=metodos_de_archivos
archivos.actualizar_cant_partidas_guardadas()

ok= archivos.hay_partidas_a_cargar()
Iniciar=[sg.Button("Iniciar Partida",size=(10,5),key="_iniciar_",button_color=('white','grey'))]
if(ok==False):
    Cargar=[sg.FileBrowse(button_text="Cargar Partida",initial_folder="Archivos\\partidas",size=(10,5),key="_cargar_",disabled=True,button_color=('white','grey'))]
else:
    Cargar=[sg.Input(visible=False, enable_events=True, key="_file_"),sg.FileBrowse(button_text="Cargar Partida",initial_folder="Archivos\\partidas",size=(10,5),disabled=False,button_color=('white','grey'))]

titulo =  [[sg.Text("Scrabble", size=(22,10),auto_size_text=True)]]

Top=[[sg.Button(("Top Ten"),key="topTen",size=(22,1))]] 


layout= titulo + [Iniciar + Cargar ] + Top

window = sg.Window('ScrabbleAr', layout, font='Courier 12',background_color="black",disable_close=True, disable_minimize=True)


def mostrar_ten(topFacil,topMedio,topDificil):
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



while True:
    event, values= window.read()
    print(event)
    if event == "_file_":
        partida = archivos.cargarPartida(archivos.formatear_cadena_de_directorio(values[event]))
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