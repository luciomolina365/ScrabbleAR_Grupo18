import PySimpleGUI as sg

sg.theme('Dark Brown 1')


header =  [[sg.Text('  ')] + [sg.Text("ScrabbleAr", size=(14,1))]]

input_rows = [[sg.Input(size=(2,1), pad=(1,1)) for col in range(15)] for row in range(15)]

buttons = [[sg.Button('Save'), sg.Button('Exit')]]

layout = header + input_rows + buttons

window = sg.Window('ScrabbleAr', layout, font='Courier 12')




pos_ban = []
while True:
    event, dic = window.read()
    
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