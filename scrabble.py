import PySimpleGUI as sg
import webbrowser as wb
import Tablero

def jugar():
    def menu():
        """Esto es un menu donde podras crear la partida segun la dificultad, cantidad de fichas o valor de las fichas, o
        en caso de tener alguna partida guardada, cargar la partida.
        En caso de querer ver el link del repositorio apretar el boton help"""

        sg.ChangeLookAndFeel('Topanga')
        fichas_predefinidas = {'A':{'cantidad':11,'valor':1},'B':{'cantidad':3,'valor':1},'C':{'cantidad':4,'valor':1},'D':{'cantidad':4,'valor':1},
        'E':{'cantidad':11,'valor':1},'F':{'cantidad':2,'valor':1},'G':{'cantidad':2,'valor':1},'H':{'cantidad':2,'valor':1},'I':{'cantidad':6,'valor':1},
        'J':{'cantidad':2,'valor':1},'K':{'cantidad':1,'valor':1},'L':{'cantidad':4,'valor':1},'LL':{'cantidad':1,'valor':1},'M':{'cantidad':3,'valor':1},
        'N':{'cantidad':5,'valor':1},'Ñ':{'cantidad':1,'valor':1},'O':{'cantidad':8,'valor':1},'P':{'cantidad':2,'valor':1},'Q':{'cantidad':1,'valor':1},
        'R':{'cantidad':4,'valor':1},'RR':{'cantidad':1,'valor':1},'S':{'cantidad':7,'valor':1},'T':{'cantidad':4,'valor':1},
        'U':{'cantidad':6,'valor':1},'V':{'cantidad':2,'valor':1},'W':{'cantidad':1,'valor':1},'X':{'cantidad':1,'valor':1},
        'Y':{'cantidad':1,'valor':1},'Z':{'cantidad':1,'valor':1}}  ##un dic con valores predefinidos

        fichas_propias=fichas_predefinidas  ##copio el dic fichas_predefinidas en caso de modificar varios valores de el dic

        # ------ Menu Definicion ------ #
        menu_def = [['&Help', ('Link del Repositorio')],
                    ]



        layout = [
            [sg.Menu(menu_def, tearoff=True)],
            [sg.Text('Configuracion del juego scrabble!', size=(40,1), justification='center', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE)],
            [sg.Text('Ingrese el nombre de la configuracion del nuevo juego ')],
            [sg.InputText('')],     
            [sg.Button(("Cargar partida previa"),key="cargar")],
            [sg.Frame(layout=[
            [sg.Checkbox('Datos predefinidos', size=(20,1),default=True,key="_predefinido_",enable_events=True),sg.Text("(Valores predefinidos para las letras)")],
            [sg.Radio('Dificultad facil  ', "RADIO1", default=True, size=(10,1)), sg.Radio('Dificultad Media!', "RADIO1"),sg.Radio('Dificultad Dificil', "RADIO1")]], title='Configuracion del juego',title_color='red', relief=sg.RELIEF_SUNKEN, tooltip='Use these to set flags')],
            [sg.Text("Tiempo de la partida"),sg.Slider(range=(1, 20), orientation='h', size=(13, 25), default_value=10,enable_events=False)],
            [sg.Frame('Puntuacion de letras',[[
                sg.InputOptionMenu(('A', 'B', 'C','D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'LL', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'RR', 'S', 'T', 'U', 'V', 'V', 'W', 'X', 'Y', 'Z'))],
                [sg.Text("Modificar cantidad"),sg.Slider(range=(1, 15), orientation='v', size=(10, 25), default_value=6,enable_events=False),sg.Text("Modificar valor"),sg.Slider(range=(1, 20), orientation='v', size=(10, 25), default_value=13,enable_events=False)],
                [sg.Button("Modificar",key="_modificar_")]
                ],visible=False,key="slider")],
            [sg.Text('_' * 80)],
            [sg.Button(("Top Ten"),key="topTeen")],                #para mostrar una lista con los top ten
            [sg.Button("Confirmar configuracion"), sg.Cancel("Cancel")],[sg.Button(("Jugar"),key="__jugar__")]]

        window = sg.Window('Menu', layout, default_element_size=(40, 1), grab_anywhere=False)
        while True:
            event, values = window.read()
            if values["_predefinido_"]==False:
                window["slider"].update(visible=True)       #si valores predefinidos es falso,mostrar tabla para modificar los valores y la cantidad.
            if values["_predefinido_"]==True:
                window["slider"].update(visible=False)      #si valores predefinidos es verdadero,no mostrar tabla.
            if(event=="_modificar_"):
                fichas_propias[values[6]]["cantidad"]=int(values[7])    #modifico la cantidad y el valor de las letras
                fichas_propias[values[6]]["valor"]=int(values[8])
            print("-"*60)
            print(fichas_propias)
            print("-"*60)
            print(event)
            print(values)

            # if event=="topTeen":
            #     mostrar la lista de los 10 mejores jugadores

            # if(event=="cargar"):
                    #Manejo de archivo


            if(event=="Link del Repositorio"):
                wb.open("https://github.com/luciomolina365/ScrabbleAR_Grupo18", new=0, autoraise=True)
            elif(event=="Cancel"):
                break
            elif(event == "__jugar__"):
                if(values["_predefinido_"==True]):
                    window.close()
                    Tablero.juego(fichas_predefinidas)
                else:
                    window.close()
                    Tablero.juego(fichas_propias)
            # if(event=="Confirmar configuracion"):
            
                # if values[2]==True:
                #     Dificultad="Facil"
                # elif values[3]==True:
                #     Dificultad="Medio"
                # else:
                #     Dificultad="Dificil"
                # tiempo=int(values[5])  
        window.close()
        print(menu.__doc__)
    menu()

jugar()


##https://pysimplegui.readthedocs.io/en/latest/#the-event-loop-callback-functions