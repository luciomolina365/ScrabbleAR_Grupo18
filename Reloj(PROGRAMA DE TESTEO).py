import PySimpleGUI as sg
from CLASS_reloj_andando import Reloj

sg.theme('Dark Blue 3')

layout = [  [sg.Text('Tiempo restante'), sg.T(' '*1), sg.Text(size=(8,1), key='-TEMP OUT-')],
            [sg.Button('Quit')]  ]

window = sg.Window('Reloj', layout, font='Default -24', return_keyboard_events=True)

R = Reloj(1,4)

while not R.getTERMINO() :            
    event, values = window.read(timeout=1000)   
    print(event, values) if event != sg.TIMEOUT_KEY else None       #debug
   
    if event in (sg.WIN_CLOSED, 'Quit'):
        break

    
    R.temporizar()

    window['-TEMP OUT-'].update(str(R.getMinutos()) + ":"+ str(R.getSegundos()) + ' min')

window.close()