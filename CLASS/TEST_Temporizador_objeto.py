import PySimpleGUI as sg
from CLASS_temporizador_andando import Temporizador

sg.theme('Dark Blue 3')

layout = [  [sg.Text('Tiempo restante'), sg.T(' '*1), sg.Text(size=(8,1), key='-TEMP OUT-')],
            [sg.Button('Quit')]  ]

window = sg.Window('Temporizador', layout, font='Default -24', return_keyboard_events=True)

T = Temporizador(30,45)                         #Necesario 
cantRead = 0                                    #Necesario 

while not T.getTERMINO_Reloj() :                #T.getTERMINO_Reloj() Necesario             
    event, values = window.read(timeout=10)     #timeout=10 Necesario
    cantRead = cantRead + 1                     #Necesario

    if event in (sg.WIN_CLOSED, 'Quit'):
        break
        
    cantRead = T.avanzar_tiempo(cantRead)       #Necesario

    window['-TEMP OUT-'].update(str(T.getMinutos()) + ":"+ str(T.getSegundos()) + ' min')   #Necesario LO MUESTRA

window.close()