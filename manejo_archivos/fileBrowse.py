import PySimpleGUI as sg
import json

def formatear_cadena_de_directorio(directorio):
    lista = directorio.split("/")
    nueva = []
    OK = False
    for directorio in lista:
        
        if directorio == "Archivos":
            OK = True
        
        if OK:    
            nueva.append(directorio)
            nueva.append("\\")
    
    nueva[len(nueva)-1] = ""
    direccion = ""
    for elemento in nueva:
        if elemento == "\\":
            elemento = elemento + "\\"
        direccion = direccion + elemento

    return str(direccion)

layout = [
    [sg.Input(visible=False, enable_events=True, key="_file_"), sg.FilesBrowse()],
    [sg.Exit()]
        ]



window = sg.Window('MODICAR DATOS DE JUGADOR').Layout(layout).Finalize()

while True:
    event, values = window.Read()

    if event is None or event == 'Exit':      
        break

    if event == "_file_":
        print(event)
        print(values)
        print(formatear_cadena_de_directorio(values[event]))
        
        
window.Close()







#archivo = open(values["_file_"] , "r")

#print(archivo.read())



