import PySimpleGUI as sg
from time import sleep
import random

abecedario="a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z"
print(abecedario)
abecedario=abecedario.split(",")
print(abecedario)
sg.theme('Dark Brown 1')
letras=[]
for i in range(1,8):
    a=random.randrange(1,len(abecedario))
    letras.append(abecedario[a])
print(letras)

header =  [[sg.Text('  ')] + [sg.Text("ScrabbleAr", size=(14,1))]]

input_rows = [[sg.Button(size=(2,1), pad=(1,1)) for col in range(15)] for row in range(15)]


fichas = [
    [sg.Button(letras[0], button_color=('white', 'black'), size=(3, 1), font=("Helvetica", 20)),
    sg.Button(letras[1], button_color=('white', 'black'), size=(3, 1), font=("Helvetica", 20)),
    sg.Button(letras[2], button_color=('white', 'black'), size=(3, 1), font=("Helvetica", 20)),
    sg.Button(letras[3], button_color=('white', 'black'), size=(3, 1), font=("Helvetica", 20)),
    sg.Button(letras[4], button_color=('white', 'black'), size=(3, 1), font=("Helvetica", 20)),
    sg.Button(letras[5], button_color=('white', 'black'), size=(3, 1), font=("Helvetica", 20)),
    sg.Button(letras[6], button_color=('white', 'black'), size=(3, 1), font=("Helvetica", 20))],
    [sg.Button('Save'),sg.Button("Exit")]
      ]

layout = header + input_rows + fichas

window = sg.Window('ScrabbleAr', layout, font='Courier 12')

pos_ban = []
ok=True
while ok:
    sg.popup("elige una ficha")
    eventNum, dic = window.read()
    elegido=eventNum
    if eventNum == 'Exit':
        ok=False
        break
    elif eventNum is letras[0] or letras[1]or letras[2] or letras[3] or letras[4]or letras[5]:
        print(eventNum[0])
        sg.popup("elige una posicion")
        eventPos= window.read()
        print(eventPos[0])
    





      
        


