import PySimpleGUI as sg
import webbrowser as wb

sg.ChangeLookAndFeel('Topanga')

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
    [sg.Checkbox('Datos predefinidos', size=(20,1),default=True),sg.Text("(Valores predefinidos para las letras)")],
    [sg.Radio('Dificultad facil  ', "RADIO1", default=True, size=(10,1)), sg.Radio('Dificultad Media!', "RADIO1"),sg.Radio('Dificultad Dificil', "RADIO1")]], title='Configuracion del juego',title_color='red', relief=sg.RELIEF_SUNKEN, tooltip='Use these to set flags')],
    [sg.InputOptionMenu(('A', 'B', 'C','D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'LL', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'RR', 'S', 'T', 'U', 'V', 'V', 'W', 'X', 'Y', 'Z'))],
    [sg.Frame('Puntuacion de letras',[[
        sg.Slider(range=(1, 10), orientation='v', size=(13, 25), default_value=13),
     ]])],
    [sg.Text('_' * 80)],
    [sg.Text('Choose A Folder', size=(35, 1))],
    [sg.Text('Your Folder', size=(10, 1), auto_size_text=False, justification='right'),
     sg.InputText('Default Folder'), sg.FolderBrowse()],
    [sg.Submit(tooltip='Click to submit this form'), sg.Cancel()]]

window = sg.Window('Menu', layout, default_element_size=(40, 1), grab_anywhere=False)
event, values = window.read()
print(event)
print(values)
if(event=="Link del Repositorio"):
    wb.open("https://github.com/luciomolina365/ScrabbleAR_Grupo18", new=0, autoraise=True)

window.close()

# sg.Popup('Title',
#          'The results of the window.',
#          'The button clicked was "{}"'.format(event),
#          'The values are', values)