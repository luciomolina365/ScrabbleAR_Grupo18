import PySimpleGUI as sg
import random
import json

#from corroboro_y_puntuo import corroborarPalabra


def juego():
    sg.theme('Topanga')

    
    """En base a un diccionario predefinido, conseguir las 7 letras a usar por turnos,
    todo esto lo vamos a hacer o realizar con objetos, para que se instancien cada vez que sean necesario, y 
    la bolsa de letras se va a ir actualizando a medida de que vayamos retirando letras del abecedario tanto, 
    del jugador, como de la computadora"""


    def CreandoTablero(tableroD,cant):#areglar i,j o j,i        se crea el tablero recibiendo el tablero y la cantidad de filas y columnas 
        tablero=[]
        lista1=[]
        for i in range(cant):
            lista1.clear()
            for j in range(cant):
                if TableroD[(i,j)]["trampa"]==True:
                    if TableroD[(i,j)]["tipo_de_trampa"]=="-1":
                        lista1.append(sg.Button("",size=(2, 1),key=(i,j), pad=(2,3),button_color=('black','Dark grey'),image_filename='imagenes\menos 1.png',image_size=(25, 22)))
                    elif TableroD[(i,j)]["tipo_de_trampa"]=="-2":
                        lista1.append(sg.Button("",size=(2, 1),key=(i,j), pad=(2,3),button_color=('black','Dark grey'),image_filename='imagenes\menos 2.png',image_size=(25, 22)))
                    else:
                        lista1.append(sg.Button("",size=(2, 1),key=(i,j), pad=(2,3),button_color=('black','Dark grey'),image_filename='imagenes\menos 3.png',image_size=(25, 22)))
                elif TableroD[(i,j)]["recompensa"]==True:
                    if TableroD[(i,j)]["tipo_de_recompensa"]=="x2":
                        lista1.append(sg.Button("",size=(2, 1),key=(i,j), pad=(2,3),button_color=('black','Dark grey'),image_filename='imagenes\multiplicador x2.png',image_size=(25, 22)))
                    else:
                        lista1.append(sg.Button("",size=(2, 1),key=(i,j), pad=(2,3),button_color=('black','Dark grey'),image_filename='imagenes\multiplicador x3.png',image_size=(25, 22)))
                else:
                    lista1.append(sg.Button("",size=(2, 1),key=(i,j), pad=(2,3),button_color=('black','Dark grey'),image_filename='imagenes\GRIS.png',image_size=(25, 22)))
            lista1=[lista1]
            tablero=tablero+lista1
        return tablero



    TableroD = {}
    for i in range(19):
        for j in range(19):
            TableroD[(i,j)] = {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}  

    titulo =  [[sg.Text(' '*15)] + [sg.Text("ScrabbleAr", size=(10,1),key="menu")],
    [sg.Text('Tiempo restante'), sg.T(' '*1), sg.Text(size=(10,1), key='-TEMP OUT-')] , [sg.Exit()]]


            
            
    tabla=CreandoTablero(TableroD,19)


    def OTRO():
        layout = [sg.Button("-1" , key = "__-1__"),sg.Button("-2" , key = "__-2__"),sg.Button("-3" , key = "__-3__")],[sg.Button("x2" , key = "__x2__") , sg.Button("x3" , key = "__x3__")] ,[sg.Button("gris" , key = "__gris__")]

        window = sg.Window('ScrASD', layout, font='Courier 12')

        a_devolver = ""

        while True:
            event, values= window.read()
            print(event)
            if event != "":
                a_devolver = event
                window.close()
            break
        
        return a_devolver


    layout = titulo + tabla

    window = sg.Window('ScrabbleAr', layout, font='Courier 12')

    def escribirArchivo(datos):
        with open('tablero.json', 'w') as archivo:
            json.dump(datos, archivo)        
            archivo.close()

    def convertir_Datos_A_Json(datos):
        aux = {}
        for coor in datos["Tablero"]:
            aux[str(coor)] = datos["Tablero"][coor]
        
        datos["Tablero"] = aux
        return datos


    La_ficha=""
    tupla=""
    lista=[]

    
    while True:
        event, values= window.read()
        print("EVENTO  -., -,. - ,.")
        print(event)

        if event == "Exit":
            TableroD = convertir_Datos_A_Json({"Tablero":TableroD})
            escribirArchivo(TableroD)
            window.close()
            break

        elif event != "":
            CLAVE = event
            tipo = OTRO()

            if tipo == "__-1__":
                datos = {'letra': None, 'trampa': True, 'tipo_de_trampa': "-1", 'recompensa': False, 'tipo_de_recompensa': None}
                window[CLAVE].update("",disabled=False,image_filename='imagenes\menos 1.png',image_size=(25, 22))
            
            elif tipo == "__-2__":
                datos = {'letra': None, 'trampa': True, 'tipo_de_trampa': "-2", 'recompensa': False, 'tipo_de_recompensa': None}
                window[CLAVE].update("",disabled=False,image_filename='imagenes\menos 2.png',image_size=(25, 22))
            
            elif tipo == "__-3__":
                datos = {'letra': None, 'trampa': True, 'tipo_de_trampa': "-3", 'recompensa': False, 'tipo_de_recompensa': None}
                window[CLAVE].update("",disabled=False,image_filename='imagenes\menos 3.png',image_size=(25, 22))
            
            elif tipo == "__x2__":
                datos = {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': True, 'tipo_de_recompensa': "x2"}
                window[CLAVE].update("",disabled=False,image_filename='imagenes\multiplicador x2.png',image_size=(25, 22))
            
            elif tipo == "__x3__":
                datos = {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': True, 'tipo_de_recompensa': "x3"}
                window[CLAVE].update("",disabled=False,image_filename='imagenes\Multiplicador x3.png',image_size=(25, 22))
            elif tipo == "__gris__":
                datos = {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}
                window[CLAVE].update("",disabled=False,image_filename='imagenes\GRIS.png',image_size=(25, 22))
                
            TableroD[CLAVE] = datos

            print(TableroD[CLAVE])
    
    print("-.,-.,"*20)
    print(TableroD)
    print("-.,-.,"*20)
juego()

