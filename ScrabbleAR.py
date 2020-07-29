import PySimpleGUI as sg
import webbrowser as wb
import Tablero
from Archivos.metodos_de_archivos import definir_configuracion

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
            [sg.Frame(layout=[
            [sg.Checkbox('Datos predefinidos', size=(20,1),default=True,key="_predefinido_",enable_events=True),sg.Text("(Valores predefinidos para las letras)")],
            [sg.Radio('Dificultad facil  ', "Dificultad", default=True, size=(10,1)), sg.Radio('Dificultad Media!', "Dificultad"),sg.Radio('Dificultad Dificil', "Dificultad")]], title='Configuracion del juego',title_color='red', relief=sg.RELIEF_SUNKEN, tooltip='Use these to set flags')],
            [sg.Text("Tiempo de la partida"),sg.Slider(range=(1, 20), orientation='h', size=(13, 25), default_value=10,enable_events=False)],
            [sg.Frame('Puntuacion de letras',[[
                sg.InputOptionMenu(('A', 'B', 'C','D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'LL', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'RR', 'S', 'T', 'U', 'V', 'V', 'W', 'X', 'Y', 'Z'))],
                [sg.Text("Modificar cantidad"),sg.Slider(range=(1, 15), orientation='v', size=(10, 25), default_value=6,enable_events=False),sg.Text("Modificar valor"),sg.Slider(range=(1, 20), orientation='v', size=(10, 25), default_value=6,enable_events=False)],
                [sg.Button("Modificar",key="_modificar_")]
                ],visible=False,key="slider")],
            [sg.Text('_' * 80)],
            [sg.Button(("Top Ten"),key="topTeen")],                #para mostrar una lista con los top ten
            [sg.Button(("Confirmar configuracion"),key="__jugar__") ,sg.Cancel("Cancel")]]




        window = sg.Window('Menu', layout, default_element_size=(40, 1), grab_anywhere=False)


        while True:
            event, values = window.read()
            if values["_predefinido_"]==False:
                window["slider"].update(visible=True)       #si valores predefinidos es falso,mostrar tabla para modificar los valores y la cantidad.
            if values["_predefinido_"]==True:
                window["slider"].update(visible=False)      #si valores predefinidos es verdadero,no mostrar tabla.
            if(event=="_modificar_"):
                fichas_propias[values[5]]["cantidad"]=int(values[6])    #modifico la cantidad y el valor de las letras
                fichas_propias[values[5]]["valor"]=int(values[7])
            
             #{0: None, '_predefinido_': True, 1: True, 2: False, 3: False, 4: 10.0, 5: 'A', 6: 6.0, 7: 6.0}

            # if event=="topTeen":
            #     mostrar la lista de los 10 mejores jugadores



            if(event=="Link del Repositorio"):
                wb.open("https://github.com/luciomolina365/ScrabbleAR_Grupo18", new=0, autoraise=True)
            elif(event=="Cancel"):
                break
            elif(event == "__jugar__"):        #indico en una variable q dificultad va a tener el juego
                if values[1]==True:
                    Dificultad_final=1
                elif values[2]==True:
                    Dificultad_final=2
                else:
                    Dificultad_final=3
                if(values["_predefinido_"==True]):
                    fichas_finales=fichas_predefinidas
                else:
                    fichas_finales=fichas_propias
            #{"minutos": * int positivo * , "dificultad" : * int del 1 al 3 * ,  "letras":    
                Configuracion={}
                Configuracion["minutos"]=values[4]
                Configuracion["dificultad"]=Dificultad_final
                Configuracion["letras"]=fichas_finales
                print("/"*80)
                Config=definir_configuracion(Configuracion)
                Tablero.juego(Config)
                window.close()
        window.close()
        print(menu.__doc__)
    menu()

jugar()


##https://pysimplegui.readthedocs.io/en/latest/#the-event-loop-callback-functions