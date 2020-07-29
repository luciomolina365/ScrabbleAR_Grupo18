import PySimpleGUI as sg
from Archivos import metodos_de_archivos
import Tablero



archivos=metodos_de_archivos
ok= archivos.hay_partidas_a_cargar()
print(ok)
Iniciar=[sg.Button("Iniciar Partida",size=(10,5),key="_iniciar_",button_color=('white','grey'))]
if(ok==False):
    Cargar=[sg.FileBrowse(button_text="Cargar Partida",initial_folder="Archivos\\partidas",size=(10,5),key="_cargar_",disabled=True,button_color=('white','grey'))]
else:
    Cargar=[sg.Input(visible=False, enable_events=True, key="_file_"),sg.FileBrowse(button_text="Cargar Partida",initial_folder="Archivos\\partidas",size=(10,5),disabled=False,button_color=('white','grey'))]

titulo =  [[sg.Text("Scrabble", size=(20,10),auto_size_text=True)]]

layout= titulo + [Iniciar + Cargar]

window = sg.Window('ScrabbleAr', layout, font='Courier 12',background_color="black",size=(750,300),disable_close=True, disable_minimize=True)


while True:
    event, values= window.read()
    print(event)
    if event == "_file_":
        partida=archivos.cargarPartida(archivos.formatear_cadena_de_directorio(values[event]))
        Tablero.juego(partida)
        window.close()
        break
    if event == "_iniciar_":
        window.close()
        break
    













