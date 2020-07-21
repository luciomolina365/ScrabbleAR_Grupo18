import PySimpleGUI as sg
from CLASS_reloj_andando import Reloj

sg.theme('Dark Blue 3')

layout = [  [sg.Text('Tiempo restante'), sg.T(' '*1), sg.Text(size=(8,1), key='-TEMP OUT-')],
            [sg.Button('Quit')]  ]

window = sg.Window('Reloj', layout, font='Default -24', return_keyboard_events=True)

R = Reloj(0,5)                                  #Necesario 
cantRead = 0                                    #Necesario 

while not R.getTERMINO_Reloj() :                #R.getTERMINO_Reloj() Necesario             
    event, values = window.read(timeout=10)     #timeout=10 Necesario
    cantRead = cantRead + 1                     #Necesario

    if event in (sg.WIN_CLOSED, 'Quit'):
        break
        
    cantRead = R.temporizar(cantRead)           #Necesario

    window['-TEMP OUT-'].update(str(R.getMinutos()) + ":"+ str(R.getSegundos()) + ' min')   #Necesario LO MUESTRA

window.close()