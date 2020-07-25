import PySimpleGUI as sg

ok=False
Iniciar=[sg.Button("Iniciar Partida",size=(10,5),key="_iniciar_",button_color=('white','grey'))]
if(ok==True):
    Cargar=[sg.FileBrowse(button_text="Cargar Partida",initial_folder="Archivos\\partidas",size=(10,5),key="_cargar_",disabled=True,button_color=('white','grey'))]
else:
    Cargar=[sg.FileBrowse(button_text="Cargar Partida",initial_folder="Archivos\\partidas",size=(10,5),key="_cargar_",disabled=False,button_color=('white','grey'))]

titulo =  [[sg.Text("Scrabble", size=(20,10),auto_size_text=True)]]

layout= titulo + [Iniciar + Cargar]

window = sg.Window('ScrabbleAr', layout, font='Courier 12',background_color="black",size=(750,300),disable_close=True, disable_minimize=True,)


while True:
    event, values= window.read()
    print(event)
    
    if event== "_iniciar_":
        window.close()
        break
    













