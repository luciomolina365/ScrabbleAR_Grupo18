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


def mostrar_ten(top):
    layout=[[sg.Listbox(top, size = (45,10) , key = "listBox" , select_mode=False)],
        [sg.Cancel()]]

    window = sg.Window('ScrabbleAr', layout)
    while True:
        event, values= window.read()
        if event=="Cancel":
            window.close()
            break






while True:
    event, values= window.read()
    print(event)
    if event == "_file_":
        partida=archivos.cargarPartida(archivos.formatear_cadena_de_directorio(values[event]))
        window.close()
        Tablero.juego(partida)
        
        break
    if event == "_iniciar_":
        window.close()
        jugar()
        break
    if(event=="topTen"):
        top=archivos.TopTen_de_jugadores()
        mostrar_ten(top)
    













