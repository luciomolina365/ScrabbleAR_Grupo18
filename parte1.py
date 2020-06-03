import PySimpleGUI as sg
import pattern.text.es

m=[] #Creo matriz

fila=6 #seteo cantidad filas de tablero
columna=6 #seteo cantidad columnas de tablero

#ARMO LA MATRIZ EN BASE A FILAS COLUMNAS ELEGIDAS
num = 0
for f in range(fila):
    m.append([])
    for c in range(columna):
        m[f].append(None)
        print(m[f][c],end=" ")
    print()
print("--------------------------")

m[0][0]=0
m[0][1]=1
m[0][2]=2
m[0][3]=3
m[0][4]=4
m[0][5]=5
m[1][0]="a"
m[2][0]="b"
m[3][0]="c"
m[4][0]="d"
m[5][0]="e"

print("--------------------------")
for f in range(fila):
    for c in range(columna):
        if(f==0):
            print(m[f][c],end="     ")
        else:
            print(m[f][c],end="  ")
    print()
print("--------------------------")
for f in m:
    if(f==0):
        print(f,end="    ")
    else:
        print(f)
#CONFIGURACION

