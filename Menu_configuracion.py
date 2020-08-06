import PySimpleGUI as sg
import webbrowser as wb
import Tablero
from Archivos.metodos_de_archivos import definir_configuracion,leer_reglas

def jugar():
    def menu():
        """Esto es el menu de configuracion donde podras crear la partida segun la dificultad, 
        cantidad de fichas o valor de las fichas.
        En caso de querer ver el link del repositorio apretar el boton help.
            Esta funcion del menu no anda en la maquina virtual ya que no tiene un navegador por defecto"""

        sg.ChangeLookAndFeel('DarkGrey6')

        fichas_propias = {}  #creo un dic para saber si el jugador modifica el valor o la cantidad de una letra

        # ------ Menu Definicion ------ #
        menu_def = [['&Help', ('Link del Repositorio'),("Reglas del juego")],
                    ]


        
        layout = [
            [sg.Menu(menu_def, tearoff=True)],
            [sg.Text('Configuracion del juego scrabble!', size=(26,1), justification='center', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE)],
            [sg.Frame(layout=[
            [sg.Checkbox('Datos predefinidos', size=(29,1),default=True,key="_predefinido_",enable_events=True),sg.Text("(Valores predefinidos para las letras)")],
            [sg.Radio('Dificultad facil  ', "Dificultad", default=True, size=(10,1)), sg.Radio('Dificultad Media!', "Dificultad"),sg.Radio('Dificultad Dificil', "Dificultad")]], title='Configuracion del juego', relief=sg.RELIEF_SUNKEN, tooltip='Use these to set flags')],
            [sg.Text("Tiempo de la partida"),sg.Slider(range=(1, 20), orientation='h', size=(13, 25), default_value=10,enable_events=False)],
            [sg.Frame('Puntuacion de letras',[[
                sg.InputOptionMenu(('A', 'B', 'C','D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'LL', 'M', 'N', 'O', 'P', 'Q', 'R', 'RR', 'S', 'T', 'U', 'V', 'V', 'W', 'X', 'Y', 'Z'))],
                [sg.Text("Modificar cantidad"),sg.Slider(range=(1, 15), orientation='v', size=(10, 25), default_value=6,enable_events=False),sg.Text("Modificar valor"),sg.Slider(range=(1, 20), orientation='v', size=(10, 25), default_value=6,enable_events=False)],
                [sg.Button("Modificar",key="_modificar_")]
                ],visible=False,key="slider")],
            [sg.Text('_' * 70)],
            [sg.Button(("Confirmar configuracion"),key="__jugar__") ,sg.Cancel("Cancel")]]




        window = sg.Window('Menu', layout, default_element_size=(40, 1), grab_anywhere=False)


        while True:
            event, values = window.Read()
            
            if event == sg.WIN_CLOSED:
                window.Close()
                break
            else:
            
                if values["_predefinido_"] == False:
                    window["slider"].update(visible=True)       #si valores predefinidos es falso,mostrar tabla para modificar los valores y la cantidad.
                
                if values["_predefinido_"] == True:
                    window["slider"].update(visible=False)      #si valores predefinidos es verdadero,no mostrar tabla.
                
                if(event=="_modificar_"):
                    fichas_propias[values[5]] = {"cantidad" : int(values[6]) , "valor" : int(values[7])}    #modifico la cantidad y el valor de las letras
            
    
                if(event=="Link del Repositorio"):         #lleva al link del repositorio si se apreta help y link del repositorio
                    wb.open("https://github.com/luciomolina365/ScrabbleAR_Grupo18", new=0, autoraise=True)
                
                if event=="Reglas del juego":
                    texto=leer_reglas()
                    print(texto)
    
                elif(event=="Cancel"):
                    break
                
                elif(event == "__jugar__"):        #indico en una variable q dificultad va a tener el juego
                    if values[1] == True:
                        Dificultad_final = 1
                    elif values[2] == True:
                        Dificultad_final = 2
                    else:
                        Dificultad_final = 3
                        
                    if(values["_predefinido_" == True]):      #esto guarda en fichas_finales las fichas que se utilizaran
                        fichas_finales = {}
                    else:
                        fichas_finales = fichas_propias
                    
                    Configuracion = {}
                    Configuracion["minutos"] = values[4]
                    Configuracion["dificultad"] = Dificultad_final
                    Configuracion["letras"] = fichas_finales
                    Configuracion["Puntaje_jugador"] = 0
                    Configuracion["Puntaje_computadora"] = 0
    
                    Config = definir_configuracion(Configuracion)    #se carga la configuracion para poder mandar correctamente todos los datos al tablero
                    window.Close() 
                    Tablero.juego(Config)
                    break

        window.Close()
    menu()

#----------------------------------------------------------------------------------------------------------------------------------

#   Ajenjo, Tobias Adrian   -   16286/5