import PySimpleGUI as sg
import webbrowser as wb
import saves

sg.ChangeLookAndFeel('Topanga')
fichas_predefinidas = {'A':{'cantidad':11,'valor':1},'B':{'cantidad':3,'valor':1},'C':{'cantidad':4,'valor':1},'D':{'cantidad':4,'valor':1},
'E':{'cantidad':11,'valor':1},'F':{'cantidad':2,'valor':1},'G':{'cantidad':2,'valor':1},'H':{'cantidad':2,'valor':1},'I':{'cantidad':6,'valor':1},
'J':{'cantidad':2,'valor':1},'K':{'cantidad':1,'valor':1},'L':{'cantidad':4,'valor':1},'LL':{'cantidad':1,'valor':1},'M':{'cantidad':3,'valor':1},
'N':{'cantidad':5,'valor':1},'Ñ':{'cantidad':1,'valor':1},'O':{'cantidad':8,'valor':1},'P':{'cantidad':2,'valor':1},'Q':{'cantidad':1,'valor':1},
'R':{'cantidad':4,'valor':1},'RR':{'cantidad':1,'valor':1},'S':{'cantidad':7,'valor':1},'T':{'cantidad':4,'valor':1},
'U':{'cantidad':6,'valor':1},'V':{'cantidad':2,'valor':1},'W':{'cantidad':1,'valor':1},'X':{'cantidad':1,'valor':1},
'Y':{'cantidad':1,'valor':1},'Z':{'cantidad':1,'valor':1}}

fichas_propias=fichas_predefinidas

# ------ Menu Definition ------ #
menu_def = [['&File', ['&Open', '&Save', 'E&xit']],
            ['&Help', ('Link del Repositorio')],
            ]



layout = [
    [sg.Menu(menu_def, tearoff=True)],
    [sg.Text('Configuracion del juego scrabble!', size=(40,1), justification='center', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE)],
    [sg.Text('Ingrese el nombre de la configuracion del nuevo juego ')],
    [sg.InputText('')],
    [sg.Button(("Cargar partida previa"),key="cargar")],
    [sg.Frame(layout=[
    [sg.Checkbox('Datos predefinidos', size=(20,1),default=True,key="_predefinido_",enable_events=True),sg.Text("(Valores predefinidos para las letras)")],
    [sg.Radio('Dificultad facil  ', "RADIO1", default=True, size=(10,1)), sg.Radio('Dificultad Media!', "RADIO1"),sg.Radio('Dificultad Dificil', "RADIO1")]], title='Configuracion del juego',title_color='red', relief=sg.RELIEF_SUNKEN, tooltip='Use these to set flags')],
    [sg.Frame('Puntuacion de letras',[[
        sg.InputOptionMenu(('A', 'B', 'C','D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'LL', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'RR', 'S', 'T', 'U', 'V', 'V', 'W', 'X', 'Y', 'Z'))],
        [sg.Text("Modificar cantidad"),sg.Slider(range=(1, 15), orientation='v', size=(13, 25), default_value=6,enable_events=False),sg.Text("Modificar valor"),sg.Slider(range=(1, 20), orientation='v', size=(13, 25), default_value=13,enable_events=False)],
        [sg.Button("Modificar",key="_modificar_")]
        ],visible=False,key="slider")],
    [sg.Text('_' * 80)],
<<<<<<< HEAD
    [sg.Text('Choose A Folder', size=(35, 1))],
    [sg.Text('Your Folder', size=(10, 1), auto_size_text=False, justification='right'),
     sg.InputText('Default Folder'), sg.FolderBrowse()],
    [sg.Submit(tooltip='Click to submit this form'), sg.Cancel(), sg.Exit(("Exit"), key="__exit__"]]
=======
    [sg.Button("Confirmar configuracion"), sg.Cancel()]]
>>>>>>> 8afd0864daf02195b5884ced1785b533cdc4d283

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
        fichas_propias[values[5]]["cantidad"]=int(values[6])
        fichas_propias[values[5]]["valor"]=int(values[7])
    print("-"*60)
    print(fichas_propias)
    print("-"*60)
    print(event)
    print(values)
    
    # if(event=="cargar"):
            #Manejo de archivo
        
        
    if(event=="Link del Repositorio"):
        wb.open("https://github.com/luciomolina365/ScrabbleAR_Grupo18", new=0, autoraise=True)
    if(event=="Cancel"):
        break
    # if(event=="Confirmar configuracion"):
    #     if(values["_predefinido_"==True]):
    #         paso los valores de dic predefinidos.
        #   else 
        #         valores_propios
        # if values[2]==True:
        #     Dificultad="Facil"
        # elif values[3]==True:
        #     Dificultad="Medio"
        # else:
        #     Dificultad="Dificil"
window.close()

