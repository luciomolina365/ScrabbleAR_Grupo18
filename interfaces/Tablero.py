import PySimpleGUI as sg

from ScrabbleAR import Menu_principal

import random

from Objetos import CLASS_atril, CLASS_bolsa, CLASS_temporizador, CLASS_tablero
from Objetos.metodos_de_objetos import instanciar_objetos

from Archivos.metodos_de_archivos import guardar_partida
from Archivos.metodos_de_archivos import guardar_partida_finalizada

from jugabilidad.corroborarPalabra import __retorno_informacion
from jugabilidad.jugarComputadora import __juega_IA, __fichas_a_intercambiar

import os

import platform
sistema = platform.system()

def juego(Configuracion):
    sg.theme('DarkPurple3')

    
    """En base a la configuracion,obtendremos todos los datos necesarios para jugar,como la dificultad, el tiempo, 
    la bolsa y el tablero. En caso de cargar partida tambien obtendremos el atril del jugador y de la IA.
    Todo esto lo vamos a hacer o realizar con objetos, para que se instancien cada vez que sean necesario, y 
    la bolsa de letras se va a ir actualizando a medida de que vayamos retirando letras del abecedario tanto, 
    del jugador, como de la computadora"""


    

#metodos utilizados en momentos
#------------------------------------------------------------------------------------------------- 

    def formatear(ficha):
        """Esto es en el caso de que hayan varias letras similares,consigue solamente la letra ya que 
        si hay varias letras similares como 2 A, una de las A tendra como valor A2"""

        aux = []
        for LETRA in ficha:
            if not LETRA.isdecimal():
                aux.append(LETRA)

        nueva_cadena = ""
        for letra in aux: 
            nueva_cadena = nueva_cadena + letra

        return nueva_cadena

    def mitad_tablero(dificultad):
        """metodo para saber cual es el medio dependiendo la dificultad"""
        
        if(dificultad == 1):
            medio = (9,9)
        else:
            medio = (8,8)
        
        return(medio) 

   #------------------------------------------------------------------------------------------------- 


   #Creando tablero primera vez o al cargar
   #------------------------------------------------------------------------------------------------- 

    if(sistema == "Linux"):
        tam_letras_atril = (2, 1)
    else:
        tam_letras_atril = (3, 1)

    def cant_fichas_tablero_jugador(Lista_j): #Seteo cant fichas jugador
        """Se crea los botones del atril del jugador"""
        fichas = []
        for i in range(len(Lista_j)):
            fichas.append(sg.Button(Lista_j[i], pad=(10,5), key=i,button_color=('white', 'black'), size=tam_letras_atril, font=("Helvetica", 16)))
        return fichas
    

    def cant_fichas_tablero_computadora(Lista_c): #Seteo cant fichas computadora
        """Se crea los botones del atril de la IA con un signo de interrogacion para que el jugador no sepa las 
        fichas de la IA"""
        fichas = []
        for i in Lista_c:
            fichas.append(sg.Button("?", pad=(10,5), button_color=('white', 'black'), size=tam_letras_atril, font=("Helvetica", 16),disabled=True))
        return fichas
    
    
    def CreandoTablero(TableroD,cant,medio):# 
        """Se crea el tablero recibiendo el tablero y la cantidad de filas y columnas,en caso de que sea una partida
        guardada, se cargara las letras en las posiciones donde se formaron palabras correctas"""
        tablero = []
        lista1 = []
        for i in range(cant):
            lista1.clear()
            for j in range(cant):
                if (TableroD[(i,j)]["letra"] != None):
                    lista1.append(sg.Button(TableroD[(i,j)]["letra"],disabled=True,size=(2,1),key=(i,j), pad=(2,3),button_color=('grey','white'), image_filename='', image_size=(25, 22)))
                else:
                    if((i,j)==medio):
                        lista1.append(sg.Button("",size=(2, 1),key=(i,j), pad=(2,3),button_color=('black','Dark grey'),image_filename=os.path.join("imagenes","estrella_con_cara.png"),image_size=(25, 22)))
                    else:
                        if TableroD[(i,j)]["trampa"]==True:
                            if TableroD[(i,j)]["tipo_de_trampa"]=="-1":
                                lista1.append(sg.Button("",size=(2, 1),key=(i,j), pad=(2,3),button_color=('black','Dark grey'),image_filename=os.path.join("imagenes","menos 1.png"),image_size=(25, 22)))
                            elif TableroD[(i,j)]["tipo_de_trampa"]=="-2":
                                lista1.append(sg.Button("",size=(2, 1),key=(i,j), pad=(2,3),button_color=('black','Dark grey'),image_filename=os.path.join("imagenes","menos 2.png"),image_size=(25, 22)))
                            else:
                                lista1.append(sg.Button("",size=(2, 1),key=(i,j), pad=(2,3),button_color=('black','Dark grey'),image_filename=os.path.join("imagenes","menos 3.png"),image_size=(25, 22)))
                        elif TableroD[(i,j)]["recompensa"]==True:
                            if TableroD[(i,j)]["tipo_de_recompensa"]=="x2":
                                lista1.append(sg.Button("",size=(2, 1),key=(i,j), pad=(2,3),button_color=('black','Dark grey'),image_filename=os.path.join("imagenes",'multiplicador x2.png'),image_size=(25, 22)))
                            elif TableroD[(i,j)]["tipo_de_recompensa"]=="x3":
                                lista1.append(sg.Button("",disabled=False,pad=(2,3),key=(i,j),image_filename=os.path.join("imagenes",'multiplicador x3.png'),image_size=(25, 22)))  
                            elif TableroD[(i,j)]["tipo_de_recompensa"]=="Px2":
                                lista1.append(sg.Button("",disabled=False,pad=(2,3),key=(i,j),image_filename=os.path.join("imagenes",'palabra x2.png'),image_size=(25, 22)))
                            else:
                                lista1.append(sg.Button("",disabled=False,pad=(2,3),key=(i,j),image_filename=os.path.join("imagenes",'palabra x3.png'),image_size=(25, 22)))
                        else:
                            lista1.append(sg.Button("",size=(2, 1),key=(i,j), pad=(2,3),button_color=('black','Dark grey'),image_filename=os.path.join("imagenes",'GRIS.png'),image_size=(25, 22)))
            lista1 = [lista1]
            tablero = tablero + lista1
        return tablero

#---------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------
#FINALIZANDO
    def nombreFinalizada():         #se llama al metodo para q el jugador ingrese su nombre para que este registrado su nombre en el posible Top Ten
        """Cuando la partida termina porque la bolsa no tiene mas fichas o se termino el tiempo, se guarda el nombre 
        del jugador para registrar el nombre en el Top Ten"""
        layout=[[sg.Text("Ingrese su nombre para registrar su partida finalizada")],
        [sg.Input(default_text="",key="nombre")],
        [sg.Button("Confirmar",key="confirmar")]]
        

        window = sg.Window('Guardar partida', layout, font='Courier 12',disable_close=True, no_titlebar = True , disable_minimize=True)

        while True:
            event, values = window.Read()
            if event == "confirmar" and "nombre"!="":
                window.Close()
                return values["nombre"]

#---------------------------------------------------------------------------------------------------



    #ACTUALIZAR TABLERO
    #Con este IF resolvemos problemas de tamaños en el tablero por conflictos entre Windows y Linux
    if(sistema == "Linux"):
        size_image=(1, 12)
    else:
        size_image=(23, 20)

#---------------------------------------------------------------------------------------------------

    def actualizando_tablero(dic,Tablero,window,Lista_k,medio):
            """Aca vuelve el tablero a su estado anterior en caso de que el jugador forma una palabra erronea"""
            for i in dic.keys():
                    Tablero.setValorEnCoor(i,None)
                    lugar=Tablero.getDatosEnCoor(i)
                    if i==medio:
                        window[i].update("",disabled=False,image_filename=os.path.join("imagenes","estrella_con_cara.png"),image_size=(25, 22))
                    else:
                        if lugar["trampa"]==True: 
                            if lugar["tipo_de_trampa"]=="-1":
                                window[i].update("",disabled=False,image_filename=os.path.join("imagenes","menos 1.png"),image_size=(25, 22))
                            elif lugar["tipo_de_trampa"]=="-2":
                                window[i].update("",disabled=False,image_filename=os.path.join("imagenes","menos 2.png"),image_size=(25, 22))
                            else:
                                window[i].update("",disabled=False,image_filename=os.path.join("imagenes","menos 3.png"),image_size=(25, 22))
                        elif lugar["recompensa"]==True:
                            if lugar["tipo_de_recompensa"]=="x2":
                                window[i].update("",disabled=False,image_filename=os.path.join("imagenes",'multiplicador x2.png'),image_size=(25, 22))
                            if lugar["tipo_de_recompensa"]=="x3":
                                window[i].update("",disabled=False,image_filename=os.path.join("imagenes",'multiplicador x3.png'),image_size=(25, 22))   
                            if lugar["tipo_de_recompensa"]=="Px2":
                                window[i].update("",disabled=False,image_filename=os.path.join("imagenes",'palabra x2.png'),image_size=(25, 22))
                            if lugar["tipo_de_recompensa"]=="Px3":
                                window[i].update("",disabled=False,image_filename=os.path.join("imagenes",'palabra x3.png'),image_size=(25, 22))
                        else:
                            window[i].update("",disabled=False,image_filename=os.path.join("imagenes",'GRIS.png'),image_size=(25, 22))

            for i in Lista_k:
                window[i].update(disabled=False, button_color=('white', 'black'), image_size=size_image)



    def cambiar_fichas(Atril,Window_principal,B,evento,jugador):
        """este metodo se llamara en el caso de q se pida fichas a 
        la bolsa para intercambiar y a partir de ahi llama a actualizar_fichas.
        Se muestra una nueva ventana para elegir las fichas que el jugador quiere intercambiar"""
        Fichas = Atril.getFichas_disponibles()
        layout =[[sg.Button(Fichas[i], key=i,button_color=('white', 'black'), size=tam_letras_atril, font=("Helvetica", 16)) for i in range(7)],
                [sg.Button("Confirmar",key="confirmar",font=("Helvetica", 9) ,button_color=('white','grey'))]]
       
        window = sg.Window('Seleccione las fichas a cambiar', layout, font='Courier 12',disable_close=True, no_titlebar = True)
        Seleccionadas = []

        while True:
            event, values = window.Read()
          
            if type(event)==int: 
                aux = event
                dato = Fichas[event]
                ficha_a_cambiar = formatear(dato)
                window[event].update(disabled=True, button_color=('black','white'))
                Seleccionadas.append(ficha_a_cambiar)
          
            elif(event == "confirmar") and len(Seleccionadas) > 0:
                actualizar_fichas(Seleccionadas,B,Window_principal,Atril,evento,jugador)
                window.Close()
                break


  #una variable q sea jugador o computadora
    def actualizar_fichas(lista_a_borrar,Bolsa,window,Atril,evento,jugador):
        """Este metodo se usa en caso de q coloques una palabra correcta o q requieras devolver letras a la bolsa,
        si es en el caso de que alguno de que alguno formo una palabra correcta,se pide la cantidad de letras que 
        se utilizo para formar la plabra a la bolsa.
        En caso de que el evento fue repartir,intercambio las fichas de la bolsa
        En cualquiera de los dos casos, si lo hizo el jugador, se hara el update del atril"""
        #evento = si es repartir
        #jugador = si es la maquina o el jugador
        if evento == True:
            #significa q el evento fue repartir
                        
            nuevas = Bolsa.intercambiar_fichas(lista_a_borrar)
        else: #sino el evento fue pasar turno y era una palabra correcta
            nuevas = Bolsa.dameFichas(len(lista_a_borrar))
        
        Atril.sacar_varias_fichas(lista_a_borrar)

        Atril.agregar_varias_fichas(nuevas)
       
        listaNueva = []
        for letra in nuevas:
            for i in range(nuevas[letra]["cantidad"]):#[a,a,b,b,c]
                listaNueva.append(letra)
                
        datos = Atril.getFichas_disponibles()
        if jugador == 0:
            for i in range(0,len(datos)):
                window[i].update(datos[i],disabled=False,button_color=('white', 'black'))


#---------------------------------------------------------------------------------------------------


#---------------------------------------------------------------------------------------------------
# Cargamos configuraciones

    Bol = CLASS_bolsa.Bolsa                             #Creamos los objetos
    Table = CLASS_tablero.Tablero
    Temp = CLASS_temporizador.Temporizador
    Atril_computadora = CLASS_atril.Atril
    Atril_jugador =  CLASS_atril.Atril

    OBJETOS = instanciar_objetos(Bol, Table, Temp, Atril_jugador, Atril_computadora, Configuracion)

    Turno = None
    if len(OBJETOS["Atril_jugador"].getFichas_disponibles()) == 0 and len(OBJETOS["Atril_computadora"].getFichas_disponibles()) == 0:
        
        OBJETOS["Atril_jugador"].agregar_varias_fichas(OBJETOS["Bolsa"].dameFichas(7))
        OBJETOS["Atril_computadora"].agregar_varias_fichas(OBJETOS["Bolsa"].dameFichas(7))
        primer_turno = True
        palabras_armadas = []
    else:
        Turno = 0
        primer_turno = False
        palabras_armadas = Configuracion['Jugadas']

    Lista_j = OBJETOS["Atril_jugador"].getFichas_disponibles()
    Lista_c = OBJETOS["Atril_computadora"].getFichas_disponibles()

    puntaje_J = Configuracion["Puntaje_jugador"]
    puntaje_C = Configuracion["Puntaje_computadora"]
    
    fichasJ = cant_fichas_tablero_jugador(Lista_j)
    fichasC = cant_fichas_tablero_computadora(Lista_c)

#---------------------------------------------------------------------------------------------------
#Creando ventana de juego
    medio = mitad_tablero(Configuracion['Dificultad'])

    num_dif = Configuracion['Dificultad']

    if(num_dif == 1):
        dificultad = 'Facil'
    elif(num_dif == 2):
        dificultad = 'Medio'
    else:
        dificultad = 'Dificil'

    headings = ['JUGADOR', ' IA '+dificultad]
    header =  [[sg.T(' '*13),sg.Text('')] + [sg.Text(h, size=(11,1)) for h in headings]]

    input_rows = [[sg.T(' '*18),sg.Text("",size=(14,1), pad=(0,0),key="-player-"),sg.Text("",size=(11,1), pad=(0,0),key="-compu-")]]

    puntua = header + input_rows

    titulo =  [
    [sg.Text(size=(50,1), key='-OUT-')],
    [sg.Text('Tiempo restante'), sg.T(' '*1), sg.Text(size=(10,1), key='-TEMP OUT-')]
    ]

    if Configuracion["Dificultad"]==1:
        cant=19
        size_poner=(13, 1)
        size_repartir=(40,2)
        size_pasar=(40,2)
        font_size_fichas_jugador=9

    else:     
        cant=17 
        size_poner=(7, 1)
        size_repartir=(25,1)
        size_pasar=(25,1)
        font_size_fichas_jugador=10

    if(sistema == "Linux"):
        size_image=(1, 12)
        if Configuracion["Dificultad"]==1:
            size_listbox=(25,39)
        
        else:
            size_listbox=(25,36)
    else:
        size_image=(23, 20)
        if Configuracion["Dificultad"]==1:
            size_listbox=(20,39)

        else:     
            size_listbox=(20,36)

    tabla = CreandoTablero(OBJETOS["Tablero"].getEstado(),cant,medio)  #dependiendo la dificultad, creo un tablero de determinada cantidad



    fichas_jugador = [fichasJ+[sg.Button("Poner",key="_poner_",font=("Helvetica", 14) ,button_color=('white','grey'),size=size_poner)],
    [sg.Button(("Repartir Nuevas Fichas"),button_color=('white','grey'),size=size_repartir, key="__repartir__",font=("Helvetica", font_size_fichas_jugador)),sg.Button('Pasar Turno',key="__pasar__",button_color=('black','white'),size=size_pasar, font=("Helvetica", font_size_fichas_jugador))]]


    fichas_computadora = [fichasC] 

    tablero = titulo + puntua + fichas_computadora + tabla + fichas_jugador

    columna2 = [ 
            [sg.Text("Palabras armadas!",justification='right')],
            [sg.Listbox(values=(palabras_armadas),size=size_listbox,select_mode=False,key="__lista_pal_armadas__",enable_events=False)],
            [sg.Button(('Posponer'),key="__save__",font=("Helvetica", 10),size=(10,1) ,button_color=('white','grey')),sg.Button(("Finalizar"), key="__exit__",font=("Helvetica", 10),size=(10,1) ,button_color=('white','grey'))]
            ]

    diseño = [
            [sg.Column(tablero), sg.Column(columna2)]
             ]

    window = sg.Window('ScrabbleAr', diseño, font='Courier 12')

    
   #JUEGO 
#---------------------------------------------------------------------------------------------------
                    
    cantRead = 0                                    
    cant_letras = 0
    La_ficha = ""
    tupla = ""
    dic = {}
    lista_a_borrar = []
    Lista_k = []

    window.Read(timeout = 10)
    window['-player-'].update(puntaje_J)
    window['-compu-'].update(puntaje_C)
    window['-OUT-'].update("Buena suerte!!")

    if Turno == None:
        Turno = random.randint(0,1)       #Si es 1 es la IA si es 0 es el jugador

    
    if(Turno == 1):
        window['-OUT-'].update("Buena suerte! El turno es de la IA.")
    else:
        window['-OUT-'].update("Buena suerte! El turno es del jugador.")

    no_jugada = 0

    TERMINO = False

    while not OBJETOS["Temporizador"].getTERMINO_Temporizador() and not OBJETOS["Bolsa"].getTERMINO_Bolsa():#Si el tiempo no termina y no se termino la bolsa

        event, values= window.Read(timeout=10)
        cantRead = cantRead + 1  
        cantRead = OBJETOS["Temporizador"].avanzar_tiempo(cantRead)  
        window['-TEMP OUT-'].update(str(OBJETOS["Temporizador"].getMinutos()) + ":"+ str(OBJETOS["Temporizador"].getSegundos()) + ' min') 

        if event!= '__TIMEOUT__' and event == sg.WIN_CLOSED:
            window.Close()
            break      
        
        else:
            
            if type(event)== tuple and event!= '__TIMEOUT__' : 
                tupla=event 

            if type(event)== int and event!= "_poner_" and event!= '__TIMEOUT__' :
                aux = event
                atril = OBJETOS["Atril_jugador"].getFichas_disponibles()
                dato = atril[event]
                La_ficha = formatear(dato)

            if event == "__exit__" and event!= '__TIMEOUT__' and Turno==0:
                window.Close()
                TERMINO = True
                break

            if event == "__save__" and event!= '__TIMEOUT__' and Turno==0 :
                guardar_partida(OBJETOS["Bolsa"],OBJETOS["Tablero"],OBJETOS["Temporizador"],OBJETOS["Atril_jugador"],OBJETOS["Atril_computadora"],puntaje_J,puntaje_C,Configuracion["Dificultad"],palabras_armadas)
                window.Close()
                sg.Popup("Se guardo la partida correctamente!",title="Guardar Partida")
                break

            if event == "_poner_" and La_ficha!="" and tupla!="" and event!= '__TIMEOUT__' :
                window[aux].update(disabled=True, button_color=('white','black'))
                window[tupla].update(La_ficha,disabled=True,button_color=('black','white'),image_filename='', image_size=size_image)
                cant_letras = cant_letras +1
                dic[tupla] = OBJETOS["Tablero"].getDatosEnCoor(tupla)
                dic[tupla]["letra"] = La_ficha
                Lista_k.append(aux)
                La_ficha = ""
                tupla = ""
            
            if event == "__repartir__" and event != '__TIMEOUT__' and dic == {} and Turno == 0:
                repartir = True
                
                cambiar_fichas(OBJETOS["Atril_jugador"],window,OBJETOS["Bolsa"],repartir,Turno)
                
                Turno=1

            if event == "__repartir__" and event != '__TIMEOUT__'and dic != {} and Turno == 0 :
                window['-OUT-'].update("Ya has seleccionado una posicion en el tablero")

            if event == "__pasar__" and event != '__TIMEOUT__' and dic == {} and Turno == 0 :
                window['-OUT-'].update("Debes colocar las fichas en el tablero")

            if Turno == 1:        #jugada de la IA
                jugada_IA = __juega_IA(Configuracion['Dificultad'],OBJETOS["Tablero"].getEstado(),OBJETOS["Atril_computadora"].getFichas_disponibles(),primer_turno,OBJETOS['Bolsa'].getBolsa())
                
                if(jugada_IA[0] == True):
                    puntaje = jugada_IA[1]
                    jugada = jugada_IA[2]
                    puntaje_C = puntaje_C + puntaje
                    repartir = False
                    lista_computadora_a_cambiar = jugada_IA[3]
                    actualizar_fichas(lista_computadora_a_cambiar,OBJETOS['Bolsa'],window,OBJETOS['Atril_computadora'],repartir,Turno)
                    
                    for i in jugada.keys():
                        window[i].update(jugada[i]["letra"],disabled=True,button_color=('grey','white'),image_filename='', image_size=size_image)
                        OBJETOS["Tablero"].setValorEnCoor(i,jugada[i]["letra"])

                    window['-compu-'].update(puntaje_C)
                    window['-OUT-'].update("La maquina ha formado una palabra")
                    palabras_armadas.append(f"La IA formo - {jugada_IA[3]}")
                    window['__lista_pal_armadas__'].update(palabras_armadas)
                    primer_turno = False
                
                else:
                    window['-OUT-'].update("La maquina no ha formado una palabra") 
                    jugada = jugada_IA[2]
                    no_jugada = no_jugada +1
                    if(no_jugada == 2):    #Esto es para cuando la IA no pudo formar palabras en 2 turnos seguidos, cambia sus fichas
                        letras_a_intercambiar = __fichas_a_intercambiar(OBJETOS['Atril_computadora'].getFichas_disponibles())
                        repartir = True
                        actualizar_fichas(letras_a_intercambiar,OBJETOS['Bolsa'],window,OBJETOS['Atril_computadora'],repartir,Turno)
                        
                        for i in jugada.keys():
                            OBJETOS["Tablero"].setValorEnCoor(i,None)

                        no_jugada = 0

                Turno = 0       # pasa al turno del jugador        


            if event == "__pasar__" and event != '__TIMEOUT__' and dic != {} and Turno == 0 :
                mal = False
                Bien = False
                
                if(len(Lista_k)>1):
                    if(medio in dic.keys()):
                        es_ok = True
                    else:
                        es_ok = False
                    info = __retorno_informacion(dic,OBJETOS['Bolsa'].getBolsa(),Configuracion['Dificultad'])
                    ok_J = info[0]
                    if(ok_J == True):
                        Bien = True
                        if primer_turno == True and es_ok == False :
                            mal = True
                            Bien = False
                    else:
                        mal = True
                else:
                    mal = True
                
                if(Bien == True):
                    
                    for i in dic.keys():
                        OBJETOS["Tablero"].setValorEnCoor(i,dic[i]["letra"])
                        lista_a_borrar.append(dic[i]["letra"]) 

                    puntaje = info[1]
                    puntaje_J = puntaje_J+puntaje
                    repartir = False
                    actualizar_fichas(lista_a_borrar,OBJETOS["Bolsa"],window,OBJETOS["Atril_jugador"],repartir,Turno)
                    window['-OUT-'].update("Felicitaciones, armaste una palabra correcta!")
                    palabras_armadas.append(f"Formaste - {info[2]}")
                    window['__lista_pal_armadas__'].update(palabras_armadas)
                    window['-player-'].update(puntaje_J)
                    dic = {}
                    lista_a_borrar.clear()
                    Lista_k.clear()
                    Turno = 1
                    primer_turno = False
                if(mal == True):
                    actualizando_tablero(dic,OBJETOS["Tablero"],window,Lista_k,medio)
                    window['-OUT-'].update("Le erraste, buena suerte para el proximo turno!")
                    dic = {}
                    Lista_k.clear()
                    Turno = 1

    if OBJETOS["Bolsa"].getTERMINO_Bolsa() or OBJETOS["Temporizador"].getTERMINO_Temporizador() or TERMINO:
        if(OBJETOS["Bolsa"].getTERMINO_Bolsa()):
            sg.popup("Se terminaron las fichas en la bolsa, fin del juego.")
            window.Close()
        elif OBJETOS["Temporizador"].getTERMINO_Temporizador():
            sg.popup("Se termino el tiempo, fin del juego.")
            window.Close()

        nombre = nombreFinalizada()
        guardar_partida_finalizada(puntaje_J , Configuracion["Dificultad"] , nombre)
        window.Close()

    Menu_principal()

#----------------------------------------------------------------------------------------------------------------------------------

#   Ajenjo, Tobias Adrian   -   16286/5