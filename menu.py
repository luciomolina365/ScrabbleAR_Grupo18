import PySimpleGUI as sg
import webbrowser as wb

sg.ChangeLookAndFeel('Topanga')
Fichas_predefinido = {'A': 11, 'B':3, 'C':4, 'D':4, 'E':11, 'F':2, 'G':2, 'H':2, 'I':6, 'J':2,'K':1, 'L':4, 'LL':1, 'M':3, 'N':5, 'Ñ':1, 'O':8, 'P':2, 'Q':1, 'R':4, 'RR':1, 'S':7, 'T':4, 'U':6, 'V':2, 'W':1, 'X':1, 'Y':1, 'Z':1}
fichas_propias={'A': 11, 'B':3, 'C':4, 'D':4, 'E':11, 'F':2, 'G':2, 'H':2, 'I':6, 'J':2,'K':1, 'L':4, 'LL':1, 'M':3, 'N':5, 'Ñ':1, 'O':8, 'P':2, 'Q':1, 'R':4, 'RR':1, 'S':7, 'T':4, 'U':6, 'V':2, 'W':1, 'X':1, 'Y':1, 'Z':1}
# ------ Menu Definition ------ #
menu_def = [['&File', ['&Open', '&Save', 'E&xit']],
            ['&Help', ('Link del Repositorio')],
            ]



layout = [
    [sg.Menu(menu_def, tearoff=True)],
    [sg.Text('Configuracion del juego scrabble!', size=(40,1), justification='center', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE)],
    [sg.Text('Ingrese el nombre de la configuracion del juego ')],
    [sg.InputText('')],
    [sg.Frame(layout=[
    [sg.Checkbox('Datos predefinidos', size=(20,1),default=True,key="_predefinido_",enable_events=True),sg.Text("(Valores predefinidos para las letras)")],
    [sg.Radio('Dificultad facil  ', "RADIO1", default=True, size=(10,1)), sg.Radio('Dificultad Media!', "RADIO1"),sg.Radio('Dificultad Dificil', "RADIO1")]], title='Configuracion del juego',title_color='red', relief=sg.RELIEF_SUNKEN, tooltip='Use these to set flags')],
    [sg.Frame('Puntuacion de letras',[[
        sg.InputOptionMenu(('A', 'B', 'C','D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'LL', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'RR', 'S', 'T', 'U', 'V', 'V', 'W', 'X', 'Y', 'Z'))],
        [sg.Slider(range=(1, 10), orientation='v', size=(13, 25), default_value=13,enable_events=False)],
        [sg.Button("Modificar",key="_modificar_")]
        ],visible=False,key="slider")],
    [sg.Text('_' * 80)],
    [sg.Text('Choose A Folder', size=(35, 1))],
    [sg.Text('Your Folder', size=(10, 1), auto_size_text=False, justification='right'),
     sg.InputText('Default Folder'), sg.FolderBrowse()],
    [sg.Submit(tooltip='Click to submit this form'), sg.Cancel()]]

window = sg.Window('Menu', layout, default_element_size=(40, 1), grab_anywhere=False)
while True:
    event, values = window.read()
    print(event)
    print(values)
    if values["_predefinido_"]==False:
        window["slider"].update(visible=True)
    if values["_predefinido_"]==True:
        window["slider"].update(visible=False)
    if(event=="_modificar_"):
        fichas_propias[values[5]]=int(values[6])

    print("-"*60)
    print(fichas_propias)
    print("-"*60)
    print(event)
    print(values)
    if(event=="Link del Repositorio"):
        wb.open("https://github.com/luciomolina365/ScrabbleAR_Grupo18", new=0, autoraise=True)
    # if(event=="confirmar configuracion"):
    #     if(values["_predefinido_"==True]):
    #         paso los valores de dic predefinidos
window.close()

# sg.Popup('Title',
#          'The results of the window.',
#          'The button clicked was "{}"'.format(event),
#          'The values are', values)