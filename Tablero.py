import PySimpleGUI as sg
import random
from Objetos import CLASS_atril
from Objetos import CLASS_bolsa
from Objetos import CLASS_temporizador
from Objetos import CLASS_tablero
from metodos_de_objetos import instanciar_objetos
from Archivos.metodos_de_archivos import guardar_partida
from corroboro.corroborarPalabra import __retorno_informacion

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


    def formatear(ficha):

        aux = []
        for LETRA in ficha:
            if not LETRA.isdecimal():
                aux.append(LETRA)

        nueva_cadena = ""
        for letra in aux: 
            nueva_cadena = nueva_cadena + letra

        return nueva_cadena
   
    
    Lista_j=OBJETOS["Atril_jugador"].getFichas_disponibles()
    Lista_c=OBJETOS["Atril_computadora"].getFichas_disponibles()
    if len(Lista_j)==0 and len(Lista_c)==0:
        OBJETOS["Atril_jugador"].agregar_varias_fichas(OBJETOS["Bolsa"].dameFichas(7))
        OBJETOS["Atril_computadora"].agregar_varias_fichas(OBJETOS["Bolsa"].dameFichas(7))


    def cant_fichas_tablero_jugador(Lista_j): #Seteo cant fichas
        fichas=[]
        for i in range(len(Lista_j)):
            fichas.append(sg.Button(Lista_j[i], pad=(10,5), key=i,button_color=('white', 'black'), size=(3, 1), font=("Helvetica", 16)))
        return fichas
    
    def cant_fichas_tablero_computadora(Lista_c): #Seteo cant fichas
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

    def actualizando_tablero(dic,Tablero,window,Lista_k):#Aca vuelven la tabla a su estado original si el jugador pone una palabra erronea
        for i in dic.keys():
                Tablero.setValorEnCoor(i,"")
                lugar=Tablero.getDatosEnCoor(i)
                print(i)
                print(lugar)
                if lugar["trampa"]==True: 
                    if lugar["tipo_de_trampa"]=="-1":
                        window[i].update("",disabled=False,image_filename='imagenes\menos 1.png',image_size=(25, 22))
                    elif lugar["tipo_de_trampa"]=="-2":
                        window[i].update("",disabled=False,image_filename='imagenes\menos 2.png',image_size=(25, 22))
                    else:
                        window[i].update("",disabled=False,image_filename='imagenes\menos 3.png',image_size=(25, 22))
                elif lugar["recompensa"]==True:
                    if lugar["tipo_de_recompensa"]=="x2":
                        window[i].update("",disabled=False,image_filename='imagenes\multiplicador x2.png',image_size=(25, 22))
                    else:
                        window[i].update("",disabled=False,image_filename='imagenes\multiplicador x3.png',image_size=(25, 22))
                else:
                    window[i].update("",disabled=False,image_filename='imagenes\GRIS.png',image_size=(25, 22))
        print(Lista_k)
        for i in Lista_k:
            window[i].update(disabled=False, button_color=('white', 'black'))


        #window[dic[i]["letra"]].update(disabled=False, button_color=('white', 'black'))


    def actualizar_fichas(lista_a_borrar,B,window,Atril,evento):#lista_K
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
            print("lista del pasar turno")
            print(lista_a_borrar)
                 
        Atril.sacar_varias_fichas(lista_a_borrar)

        Atril.agregar_varias_fichas(nuevas)
       
        listaNueva=[]
        for letra in nuevas:
            for i in range(nuevas[letra]["cantidad"]):#[a,a,b,b,c]
                listaNueva.append(letra)
                
        datos=Atril.getFichas_disponibles()
        for i in range(0,len(datos)):
            window[i].update(datos[i],disabled=False,button_color=('white', 'black'))
                



    # def Crear_diccionario(dic):
    #     nuevo={}
    #     for tupla in dic.keys():
    #         nuevo[tupla]=dic[tupla]["letra"]
    #     return nuevo     





    def cambiar_fichas(Atril,Window_principal,B,evento):
        Fichas=Atril.getFichas_disponibles()
        layout =[
                [sg.Button(Fichas[i], key=i,button_color=('white', 'black'), size=(3, 1), font=("Helvetica", 16)) for i in range(7)],
                [sg.Button("Confirmar",key="confirmar",font=("Helvetica", 9) ,button_color=('white','grey')),sg.Cancel(font=("Helvetica", 9) ,button_color=('white','grey'))]]
       
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
          if(event=="Cancel"):
            window.close()
            break  
          elif(event=="confirmar"):
              actualizar_fichas(Seleccionadas,B,Window_principal,Atril,evento)
              window.close()
              break




    titulo =  [[sg.Text(' '*15)] + [sg.Text("ScrabbleAr", size=(10,1),key="menu")],
    [sg.Text('Tiempo restante'), sg.T(' '*1), sg.Text(size=(10,1), key='-TEMP OUT-')]]


    if Configuracion["Dificultad"]==1:
        cant=19
    elif Configuracion["Dificultad"]==2:
        cant=17
    else:     
        cant=15 
    tabla=CreandoTablero(OBJETOS["Tablero"].getEstado(),cant)



    fichas_jugador = [fichasJ+[sg.Button("Poner",key="_poner_",font=("Helvetica", 9) ,button_color=('white','grey'),size=(6, 2))],
    [sg.Button(('Posponer partida!'),key="__save__",font=("Helvetica", 9) ,button_color=('white','grey')),sg.Button(("Terminar juego"), key="__exit__",font=("Helvetica", 9) ,button_color=('white','grey')),sg.Button(("REPARTIR NUEVAS FICHAS"),button_color=('white','grey'), key="__repartir__",font=("Helvetica", 9)),sg.Button('Pasar Turno',key="__pasar__",button_color=('black','white'), font=("Helvetica", 16))]]



    fichas_computadora = [fichasC] 


    layout = titulo + fichas_computadora + tabla + fichas_jugador

    window = sg.Window('ScrabbleAr', layout, font='Courier 12')
                        
    cantRead = 0                                    

    La_ficha=""
    tupla=""
    dic={}
    lista_a_borrar=[]
    puntaje_C=0
    puntaje_J=0
    Lista_k=[]
    Finalizada=False
    while not OBJETOS["Temporizador"].getTERMINO_Temporizador():
        event, values= window.read(timeout=10)
        cantRead = cantRead + 1  
        cantRead = OBJETOS["Temporizador"].avanzar_tiempo(cantRead)  
        window['-TEMP OUT-'].update(str(OBJETOS["Temporizador"].getMinutos()) + ":"+ str(OBJETOS["Temporizador"].getSegundos()) + ' min')       
        if type(event)== tuple and event!= '__TIMEOUT__' : 
            tupla=event
            
        if type(event)== int and event!= "_poner_" and event!= '__TIMEOUT__' :
            aux=event
            print(event)
            atril=OBJETOS["Atril_jugador"].getFichas_disponibles()
            dato=atril[event]
            La_ficha=formatear(dato)
            
        if event == "__exit__" and event!= '__TIMEOUT__' :
            window.close()
            break
        if event == "__save__" and event!= '__TIMEOUT__' :
            guardar_partida(OBJETOS["Bolsa"],OBJETOS["Tablero"],OBJETOS["Temporizador"],OBJETOS["Atril_jugador"],OBJETOS["Atril_computadora"],puntaje_J,puntaje_C,Finalizada)
            window.close()
            break
        if event == "_poner_" and La_ficha!="" and tupla!="" and event!= '__TIMEOUT__' :
            window[aux].update(disabled=True, button_color=('black','white'))
            window[tupla].update(La_ficha,disabled=True,button_color=('','white'),image_filename='', image_size=(23, 20))
            dic[tupla]=OBJETOS["Tablero"].getDatosEnCoor(tupla)
            dic[tupla]["letra"]=La_ficha
            Lista_k.append(aux)
            La_ficha=""
            tupla=""
        if event=="__repartir__"and event!= '__TIMEOUT__'and dic=={}:
            repartir=True
            cambiar_fichas(OBJETOS["Atril_jugador"],window,OBJETOS["Bolsa"],repartir)

        if event=="__pasar__" and event!= '__TIMEOUT__' and dic!={} :
            jugada = __retorno_informacion(dic,OBJETOS["Bolsa"].getBolsa())
            correcta= jugada[0]
            if(correcta==True):
                for i in dic.keys():
                   lista_a_borrar.append(dic[i]["letra"]) 
                #nuevo=Crear_diccionario(dic)
                puntaje = jugada[1]
                puntaje_J = puntaje_J + puntaje
                print("PUNTAAAAAJEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
                print(puntaje)
                repartir=False
                actualizar_fichas(lista_a_borrar,OBJETOS["Bolsa"],window,OBJETOS["Atril_jugador"],repartir)
                dic={}
                lista_a_borrar=[]
                Lista_k=[]
            else:
                actualizando_tablero(dic,OBJETOS["Tablero"],window,Lista_k)
                dic={}
                Lista_k=[]

    print(juego.__doc__)