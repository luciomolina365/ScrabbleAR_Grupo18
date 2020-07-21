import webbrowser as web
import PySimpleGUI as sg

#web.open("https://github.com/luciomolina365/ScrabbleAR_Grupo18", new=0, autoraise=True)

directorio = dir(sg)

for x in range(0,len(directorio)):
    print(directorio[x]+"\b")