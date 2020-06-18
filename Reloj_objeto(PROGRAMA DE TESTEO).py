import PySimpleGUI as sg
from CLASS_reloj_andando import Reloj

sg.theme('Dark Blue 3')

layout = [  [sg.Text('Tiempo restante'), sg.T(' '*1), sg.Text(size=(8,1), key='-TEMP OUT-')],
            [sg.Button('Quit')]  ]

window = sg.Window('Reloj', layout, font='Default -24', return_keyboard_events=True)

R = Reloj(1,9)
cantRead = 0

while not R.getTERMINO() :            
    event, values = window.read(timeout=10)
    cantRead = cantRead + 1  

    if event in (sg.WIN_CLOSED, 'Quit'):
        break
        
    cantRead = R.temporizar(cantRead)

    window['-TEMP OUT-'].update(str(R.getMinutos()) + ":"+ str(R.getSegundos()) + ' min')

window.close()