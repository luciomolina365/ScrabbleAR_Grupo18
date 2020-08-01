import PySimpleGUI as sg
import random
from Objetos import CLASS_atril
from Objetos import CLASS_bolsa
from Objetos import CLASS_temporizador
from Objetos import CLASS_tablero
from metodos_de_objetos import instanciar_objetos
import random
from Archivos.metodos_de_archivos import guardar_partida
from Archivos.metodos_de_archivos import guardar_partida_finalizada
from corroboro.corroborarPalabra import __retorno_informacion
from jugarComputadora import __juega_IA

#{"minutos": * int positivo * , "dificultad" : * int del 1 al 3 * ,  "letras": 

def juego(Configuracion):
    sg.theme('Topanga')

    
    """En base a un diccionario predefinido, conseguir las 7 letras a usar por turnos,
    todo esto lo vamos a hacer o realizar con objetos, para que se instancien cada vez que sean necesario, y 
    la bolsa de letras se va a ir actualizando a medida de que vayamos retirando letras del abecedario tanto, 
    del jugador, como de la computadora"""


    Bol = CLASS_bolsa.Bolsa
    Table = CLASS_tablero.Tablero
    Temp = CLASS_temporizador.Temporizador
    Atril_computadora = CLASS_atril.Atril
    Atril_jugador =  CLASS_atril.Atril

    OBJETOS = instanciar_objetos(Bol,Table,Temp,Atril_computadora,Atril_jugador,Configuracion)

#metodos utilizados en momentos
#------------------------------------------------------------------------------------------------- 

    def formatear(ficha):

        aux = []
        for LETRA in ficha:
            if not LETRA.isdecimal():
                aux.append(LETRA)

        nueva_cadena = ""
        for letra in aux: 
            nueva_cadena = nueva_cadena + letra

        return nueva_cadena
   #------------------------------------------------------------------------------------------------- 


   #Creando tablero primera vez o al cargar
   #------------------------------------------------------------------------------------------------- 
    Lista_j=OBJETOS["Atril_jugador"].getFichas_disponibles()
    Lista_c=OBJETOS["Atril_computadora"].getFichas_disponibles()
    Turno=None
    if len(Lista_j)==0 and len(Lista_c)==0:
        OBJETOS["Atril_jugador"].agregar_varias_fichas(OBJETOS["Bolsa"].dameFichas(7))
        OBJETOS["Atril_computadora"].agregar_varias_fichas(OBJETOS["Bolsa"].dameFichas(7))
    else:
        Turno=0
    
    puntaje_J=Configuracion["Puntaje_jugador"]
    puntaje_C=Configuracion["Puntaje_computadora"]

    def cant_fichas_tablero_jugador(Lista_j): #Seteo cant fichas jugador
        fichas=[]
        for i in range(len(Lista_j)):
            fichas.append(sg.Button(Lista_j[i], pad=(10,5), key=i,button_color=('white', 'black'), size=(3, 1), font=("Helvetica", 16)))
        return fichas
    
    def cant_fichas_tablero_computadora(Lista_c): #Seteo cant fichas computadora
        fichas=[]
        for i in Lista_c:
            fichas.append(sg.Button("?", pad=(10,5), button_color=('white', 'black'), size=(3, 1), font=("Helvetica", 16),disabled=True))
        return fichas
    
    fichasJ = cant_fichas_tablero_jugador(Lista_j)
    fichasC = cant_fichas_tablero_computadora(Lista_c)

    
    def CreandoTablero(TableroD,cant):#  se crea el tablero recibiendo el tablero y la cantidad de filas y columnas 
        tablero=[]
        lista1=[]
        for i in range(cant):
            lista1.clear()
            for j in range(cant):
                if (TableroD[(i,j)]["letra"] != None):
                    lista1.append(sg.Button(TableroD[(i,j)]["letra"],disabled=True,size=(2,1),key=(i,j), pad=(2,3),button_color=('grey','white'), image_filename='', image_size=(25, 22)))
                else:
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
                        elif TableroD[(i,j)]["tipo_de_recompensa"]=="x3":
                            lista1.append(sg.Button("",disabled=False,pad=(2,3),key=(i,j),image_filename='imagenes\multiplicador x3.png',image_size=(25, 22)) )  
                        elif TableroD[(i,j)]["tipo_de_recompensa"]=="Px2":
                            lista1.append(sg.Button("",disabled=False,pad=(2,3),key=(i,j),image_filename='imagenes\palabra x2.png',image_size=(25, 22)))
                        else:
                            lista1.append(sg.Button("",disabled=False,pad=(2,3),key=(i,j),image_filename='imagenes\palabra x3.png',image_size=(25, 22)))
                    else:
                        lista1.append(sg.Button("",size=(2, 1),key=(i,j), pad=(2,3),button_color=('black','Dark grey'),image_filename='imagenes\GRIS.png',image_size=(25, 22)))
            lista1=[lista1]
            tablero=tablero+lista1
        return tablero

#---------------------------------------------------------------------------------------------------
                


#---------------------------------------------------------------------------------------------------
#FINALIZANDO
    def nombreFinalizada():         #se llama al metodo para q el jugador ingrese su nombre para que este registrado su nombre en el posible Top Ten
        layout=[[sg.Text("Ingrese su nombre para registrar su partida finalizada")],
        [sg.Input(default_text="",key="nombre")],
        [sg.Button("Confirmar",key="confirmar")]]
        

        window = sg.Window('Seleccione las fichas a cambiar', layout, font='Courier 12',disable_close=True, disable_minimize=True)

        while True:
            event, values= window.read()
            if event=="confirmar" and "nombre"!="":
                window.close()
                return values["nombre"]

#---------------------------------------------------------------------------------------------------



#ACTUALIZAR TABLERO
#---------------------------------------------------------------------------------------------------

    def actualizando_tablero(dic,Tablero,window,Lista_k):#Aca vuelven la tabla a su estado original si el jugador pone una palabra erronea
            for i in dic.keys():
                    Tablero.setValorEnCoor(i,"")
                    lugar=Tablero.getDatosEnCoor(i)
                    if lugar["trampa"]==True: 
                        if lugar["tipo_de_trampa"]=="-1":
                            window[i].update("",disabled=False,image_filename='imagenes\menos 1.png',image_size=(23, 20))
                        elif lugar["tipo_de_trampa"]=="-2":
                            window[i].update("",disabled=False,image_filename='imagenes\menos 2.png',image_size=(25, 22))
                        else:
                            window[i].update("",disabled=False,image_filename='imagenes\menos 3.png',image_size=(25, 22))
                    elif lugar["recompensa"]==True:
                        if lugar["tipo_de_recompensa"]=="x2":
                            window[i].update("",disabled=False,image_filename='imagenes\multiplicador x2.png',image_size=(25, 22))
                        if lugar["tipo_de_recompensa"]=="x3":
                            window[i].update("",disabled=False,image_filename='imagenes\multiplicador x3.png',image_size=(25, 22))   
                        if lugar["tipo_de_recompensa"]=="Px2":
                            window[i].update("",disabled=False,image_filename='imagenes\palabra x2.png',image_size=(25, 22))
                        else:
                            window[i].update("",disabled=False,image_filename='imagenes\palabra x3.png',image_size=(25, 22))
                            
            print(Lista_k)
            for i in Lista_k:
                window[i].update(disabled=False, button_color=('white', 'black'))



    def cambiar_fichas(Atril,Window_principal,B,evento,jugador):#este metodo se llamara en el caso de q se pida fichas a la bolsa para intercambiar y a partir de ahi llama a actualizar_fichas
        Fichas=Atril.getFichas_disponibles()
        layout =[
                [sg.Button(Fichas[i], key=i,button_color=('white', 'black'), size=(3, 1), font=("Helvetica", 16)) for i in range(7)],
                [sg.Button("Confirmar",key="confirmar",font=("Helvetica", 9) ,button_color=('white','grey'))]]
       
        window = sg.Window('Seleccione las fichas a cambiar', layout, font='Courier 12',disable_close=True, disable_minimize=True)
        Seleccionadas=[]
        while True:
          event, values= window.read()
          if type(event)==int: 
                aux=event
                dato=Fichas[event]
                ficha_a_cambiar=formatear(dato)
                window[event].update(disabled=True, button_color=('black','white'))
                Seleccionadas.append(ficha_a_cambiar)
          elif(event=="confirmar"):
              actualizar_fichas(Seleccionadas,B,Window_principal,Atril,evento,jugador)
              window.close()
              break



  #una variable q sea jugador o computadora
    def actualizar_fichas(lista_a_borrar,B,window,Atril,evento,jugador):#Este metodo se usa en caso de q coloques una palabra correcta o q requieras devolver letras a la bolsa
        if evento==True:#significa q el evento fue repartir
            estado=Atril.getEstado()
            dic={}
            for letra in lista_a_borrar:
                if letra in dic.keys():
                    dic[letra]["cantidad"]=dic[letra]["cantidad"]+1
                else:
                    dic[letra]={"cantidad":1,"valor":estado[letra]["valor"]}
            
            nuevas=B.intercambiar_fichas(dic)
        else: #sino el evento fue pasar turno y era una palabra correcta
            nuevas=B.dameFichas(len(lista_a_borrar))
                 
        Atril.sacar_varias_fichas(lista_a_borrar)

        Atril.agregar_varias_fichas(nuevas)
       
        listaNueva=[]
        for letra in nuevas:
            for i in range(nuevas[letra]["cantidad"]):#[a,a,b,b,c]
                listaNueva.append(letra)
                
        datos=Atril.getFichas_disponibles()
        if jugador ==0:
            for i in range(0,len(datos)):
                window[i].update(datos[i],disabled=False,button_color=('white', 'black'))


#---------------------------------------------------------------------------------------------------

##Creando la ventana de juego
#---------------------------------------------------------------------------------------------------

    headings = ['JUGADOR', ' IA']
    header =  [[sg.T(' '*15),sg.Text('')] + [sg.Text(h, size=(8,1)) for h in headings]]

    input_rows = [[sg.T(' '*20),sg.Text("",size=(7,1), pad=(0,0),key="-player-"),sg.Text("",size=(8,1), pad=(0,0),key="-compu-")]]

    puntua= header + input_rows

    titulo =  [
    [sg.Text(size=(50,1), key='-OUT-')],
    [sg.Text('Tiempo restante'), sg.T(' '*1), sg.Text(size=(10,1), key='-TEMP OUT-')]]


    if Configuracion["Dificultad"]==1:
        cant=19
    elif Configuracion["Dificultad"]==2:
        cant=17
    else:     
        cant=15 
    tabla=CreandoTablero(OBJETOS["Tablero"].getEstado(),cant)  #dependiendo la dificultad, creo un tablero de determinada cantidad



    fichas_jugador = [fichasJ+[sg.Button("Poner",key="_poner_",font=("Helvetica", 9) ,button_color=('white','grey'),size=(6, 2))],
    [sg.Button(('Posponer partida!'),key="__save__",font=("Helvetica", 9) ,button_color=('white','grey')),sg.Button(("Terminar juego"), key="__exit__",font=("Helvetica", 9) ,button_color=('white','grey')),sg.Button(("Repartir Nuevas Fichas"),button_color=('white','grey'), key="__repartir__",font=("Helvetica", 9)),sg.Button('Pasar Turno',key="__pasar__",button_color=('black','white'), font=("Helvetica", 16))]]


    fichas_computadora = [fichasC] 

    layout = titulo + puntua + fichas_computadora + tabla + fichas_jugador

    window = sg.Window('ScrabbleAr', layout, font='Courier 12')

    
#---------------------------------------------------------------------------------------------------
                        
    cantRead = 0                                    

    La_ficha=""
    tupla=""
    dic={}
    lista_a_borrar=[]
    Lista_k=[]
    window.read(timeout=10)
    window['-player-'].update(puntaje_J)
    window['-compu-'].update(puntaje_C)
    window['-OUT-'].update("Buena suerte!!")
    primer_turno=True
    if Turno==None:
        Turno=random.randint(0,1)       #Si es 1 es la IA si es 0 es el jugador
    print(Turno)
    if(Turno==1):
       print("El turno es de la IA ")
    else:
       print("el turno es de el jugador")
    no_jugada = 0


    while not OBJETOS["Temporizador"].getTERMINO_Temporizador():
        event, values= window.read(timeout=10)
        cantRead = cantRead + 1  
        cantRead = OBJETOS["Temporizador"].avanzar_tiempo(cantRead)  
        window['-TEMP OUT-'].update(str(OBJETOS["Temporizador"].getMinutos()) + ":"+ str(OBJETOS["Temporizador"].getSegundos()) + ' min')       
        if type(event)== tuple and event!= '__TIMEOUT__' : 
            tupla=event 
            print(tupla)
        if type(event)== int and event!= "_poner_" and event!= '__TIMEOUT__' :
            aux=event
            atril=OBJETOS["Atril_jugador"].getFichas_disponibles()
            dato=atril[event]
            La_ficha=formatear(dato)
            print(La_ficha)
            
        if event == "__exit__" and event!= '__TIMEOUT__' Turno==0:
            window.close()
            nombre=nombreFinalizada()
            guardar_partida_finalizada(puntaje_J , Configuracion["Dificultad"],nombre)
            break
        if event == "__save__" and event!= '__TIMEOUT__' Turno==0 :
            guardar_partida(OBJETOS["Bolsa"],OBJETOS["Tablero"],OBJETOS["Temporizador"],OBJETOS["Atril_jugador"],OBJETOS["Atril_computadora"],puntaje_J,puntaje_C,Configuracion["Dificultad"])
            window.close()
            break
        if event == "_poner_" and La_ficha!="" and tupla!="" and event!= '__TIMEOUT__' :
            window[aux].update(disabled=True, button_color=('black','white'))
            window[tupla].update(La_ficha,disabled=True,button_color=('grey','white'),image_filename='', image_size=(23, 20))
            dic[tupla]=OBJETOS["Tablero"].getDatosEnCoor(tupla)
            dic[tupla]["letra"]=La_ficha
            Lista_k.append(aux)
            La_ficha=""
            tupla=""
        if event=="__repartir__"and event!= '__TIMEOUT__'and dic=={} and Turno==0:
            repartir=True
            cambiar_fichas(OBJETOS["Atril_jugador"],window,OBJETOS["Bolsa"],repartir,Turno)
            Turno=1

        if event=="__repartir__"and event!= '__TIMEOUT__'and dic!={} and Turno==0 :
           window['-OUT-'].update("Ya has seleccionado una posicion en el tablero")

        if event=="__pasar__" and event!= '__TIMEOUT__' and dic=={} and Turno==0 :
            window['-OUT-'].update("Debes colocar las fichas en el tablero")

        
        if Turno==1:
            jugada_IA = __juega_IA(Configuracion['Dificultad'],OBJETOS["Tablero"].getEstado(),OBJETOS["Atril_computadora"].getFichas_disponibles(),primer_turno,OBJETOS['Bolsa'].getBolsa())
            if(jugada_IA[0] == True):
                puntaje = jugada_IA[1]
                jugada = jugada_IA[2]
                puntaje_C = puntaje_C + puntaje
                repartir = False
                lista_computadora_a_cambiar = jugada_IA[3]
                actualizar_fichas(lista_computadora_a_cambiar,OBJETOS['Bolsa'],window,OBJETOS['Atril_computadora'],repartir,Turno)
                for i in jugada.keys():
                    window[i].update(jugada[i]["letra"],disabled=True,button_color=('grey','white'),image_filename='', image_size=(23, 20))
                primer_turno = False
                window['-compu-'].update(puntaje_C)
                window['-OUT-'].update("La maquina a formado una palabra")
            else:
                window['-OUT-'].update("La maquina no a formado una palabra")
                no_jugada = no_jugada +1
                if(no_jugada == 2):
                    cant_fichas = random.randint(1,7)
                    lista_computadora_a_cambiar = OBJETOS["Atril_computadora"].getEstado()
                    lista_computadora_a_cambiar = lista_computadora_a_cambiar[:cant_fichas]
                    repartir=True
                    actualizar_fichas(lista_computadora_a_cambiar,OBJETOS['Bolsa'],window,OBJETOS['Atril_computadora'],repartir,Turno)
                    no_jugada = 0
            Turno = 0       # pasa al turno del jugador        


        if event=="__pasar__" and event!= '__TIMEOUT__' and dic!={} and Turno==0 :
            correcta=True
            if(correcta==True):
                for i in dic.keys():
                  lista_a_borrar.append(dic[i]["letra"]) 
                puntaje=corroborarPalabra.puntuacion() 
                puntaje_J=puntaje_J+puntaje
                repartir=False
                actualizar_fichas(lista_a_borrar,OBJETOS["Bolsa"],window,OBJETOS["Atril_jugador"],repartir,Turno)
                window['-OUT-'].update("Bien hecho bro")
                window['-player-'].update(puntaje_J)
                dic={}
                lista_a_borrar=[]
                Lista_k=[]
               
            else:
                actualizando_tablero(dic,OBJETOS["Tablero"],window,Lista_k)
                window['-OUT-'].update("Mal ahi bro le erraste ")
                dic={}
                Lista_k=[]
            Turno=1

    print(juego.__doc__)
