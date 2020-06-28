import PySimpleGUI as sg
import random

abecedario="a,a,a,a,a,a,a,a,a,a,a,b,b,b,c,c,c,c,d,d,d,d,e,e,e,e,e,e,e,e,e,e,e,f,f,g,g,h,h,i,i,i,i,i,i,j,j,k,l,l,l,l,ll,m,m,m,n,n,n,n,n,ñ,o,o,o,o,o,o,o,o,p,p,q,r,r,r,r,rr,s,s,s,s,s,s,s,t,t,t,t,u,u,u,u,u,u,v,v,w,x,y,z"

print(abecedario)

abecedario=abecedario.split(",")

print(abecedario)

sg.theme('Topanga')

letras=[]

for i in range(1,8):
    a=random.randrange(1,len(abecedario))
    letras.append(abecedario[a])
print(letras)


header =  [[sg.Text('  ')] + [sg.Text("ScrabbleAr", size=(14,1),key="menu")]]

board =[[sg.Button("", size=(2, 1),key=(i,j), pad=(0,0)) for i in range(15)] for j in range(15)]



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



layout = header + board + fichas

window = sg.Window('ScrabbleAr', layout, font='Courier 12')







posicion=[]
ok=True

while ok:
    sg.popup("elige una ficha")
    eventNum = window.read()
    elegido=eventNum
    if eventNum == 'Exit':
        ok=False
        break
    elif eventNum is letras[0] or letras[1]or letras[2] or letras[3] or letras[4]or letras[5]:
        print(eventNum[0])
        window[eventNum[0]].update(disabled=True)
        sg.popup("elige una posicion")
        eventPos= window.read()
        print(eventPos[0])
        window[eventPos[0]].update(eventNum[0],disabled=True)
   
