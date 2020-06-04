import PySimpleGUI as sg
import time
sg.theme('Dark Brown 1')


header =  [[sg.Text('  ')] + [sg.Text("ScrabbleAr", size=(14,1))]]

input_rows = [[sg.Button(size=(2,1), pad=(1,1)) for col in range(15)] for row in range(15)]


fichas = [ [sg.Button('1', button_color=('white', 'blue'), size=(5, 1), font=("Helvetica", 20)),
     sg.Button('letra1', button_color=('white', 'blue'), size=(5, 1), font=("Helvetica", 20)),
     sg.Button('letra2', button_color=('white', 'blue'), size=(5, 1), font=("Helvetica", 20)),
     sg.Button('letra3', button_color=('white', 'blue'), size=(5, 1), font=("Helvetica", 20)),
     sg.Button('letra4', button_color=('white', 'blue'), size=(5, 1), font=("Helvetica", 20)),
     sg.Button('letra5', button_color=('white', 'blue'), size=(5, 1), font=("Helvetica", 20))],
      [sg.Exit()]]

layout = header + input_rows + fichas

window = sg.Window('ScrabbleAr', layout, font='Courier 12')



time=10
pos_ban = []
while True:
    event, dic = window.read()
    window['text'].update('{}'.format((time -1 )))
    print(event)
    if event == 'Save':
        palabra = [] 
        i = 0  
        for elemento in dic.values():    
            if elemento != '' and i not in pos_ban:
                palabra.append(str(elemento))
                pos_ban.append(i)
                print(elemento)
            i= i + 1

        print(palabra)
        print(pos_ban)

    elif event == 'Exit':
        break

print(dic)


