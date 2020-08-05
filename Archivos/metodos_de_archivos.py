import json
import PySimpleGUI as sg
from os import rename
from os import remove
from datetime import date


#dificultad --> int del 1 al 3
def __cargarConfiguracionPorDefecto(dificultad):

    """Devuelve los datos de una configuracion por defecto dependiendo de la dificultad que recibe por parametro"""

    direccion = "Archivos\\configuracion\\por_defecto_" + str(dificultad) +".json"
    datos = cargarPartida(direccion)
    
    return datos


def cargarPartida(direccion):

        """Lee un archivo mediante direccion, le da formato útil a los datos y los retorna.
        (sirve para cargar una partida guardada y para cargar los datos por defecto)."""

        with open(direccion, 'r') as archivo:
            datos = json.load(archivo , encoding='utf-8')
            datos = __convertir_Json_A_Datos(datos)
            archivo.close()   
        return datos


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

def __cant_partidas(Finalizada = False):

    if Finalizada:
        direccion = "Archivos\\partidas_FINALIZADAS\\cant_partidas.txt"
    else:
        direccion = "Archivos\\partidas\\cant_partidas.txt"

    f = open(direccion,"r")
    aux = f.readlines()
    f.close()
    return int(aux[0])


def hay_partidas_a_cargar():

    """Lee el archivo de cantidad de partidas y retorna un booleano. Para mostrar o no el boton de cargar partida."""                                        
    
    cant = __cant_partidas()

    if cant == 0:
        return False
    else:
        return True 
        

def actualizar_cant_partidas_guardadas(Finalizada = False):

    """Actualiza cant_partidas.txt, para, segun sus datos, permitir o no cargar partida."""

    predef = "Archivos\\partidas"
    if Finalizada:                                                  
        predef =  predef + "_FINALIZADAS\\partida_guardada_" + "FINALIZADA_"
    else:
        predef = predef + "\\partida_guardada_"

    i = 1
    while True:                                                     #Cuenta los archivos de partida NO FINALIZADAS 

        try:
            
            direccion = predef + str(i) + ".json"
            #print(direccion)

            with open(direccion, 'r') as archivo:
                
                datos = json.load(archivo,encoding='utf-8')
                
                if Finalizada == False:
                    datos = __convertir_Json_A_Datos(datos) 

                archivo.close()

            i = i + 1  
                
        except FileNotFoundError:
            break
    

    if Finalizada:                                                  #Actualiza la cantidad de partidad disponibles
        direccion = "Archivos\\partidas_FINALIZADAS\\cant_partidas.txt"
    else:
        direccion = "Archivos\\partidas\\cant_partidas.txt"

    i = i - 1             
    f = open(direccion,"w")
    f.write((str(i)))
    f.close()
    

#========================================================        
                                                        #
                                                        #
def __convertir_Datos_A_Json(datos):                    #
    aux = {}                                            #
    for coor in datos["Tablero"]:
        aux[str(coor)] = datos["Tablero"][coor]
    
    datos["Tablero"] = aux
    return datos
    

def __convertir_Json_A_Datos(datos):
    aux = {}

    for coor in datos["Tablero"]:
        
        aux[eval(coor)] = datos["Tablero"][coor]
    
    datos["Tablero"] = aux
    return datos


#========================================================        


#Bolsa , Tablero, Temporizador , Atril_jugador , Atril_computadora --> Objetos
#puntaje_J , puntaje_C --> int
#dificultad --> int del 1 al 3
def guardar_partida(Bolsa , Tablero, Temporizador , Atril_jugador , Atril_computadora , puntaje_J , puntaje_C , dificultad):   
    
    """Guarda los datos de la partida, en la carpeta "Archivos\\partidas" para poder seguirla en otro momento  - - - 
    También actualiza "cant_partidas.txt" de la carpeta correspondiente."""
    
    datos={}

    datos["Tablero"] = Tablero.getEstado()
    datos["Bolsa"] = Bolsa.getBolsa()
    datos["Temporizador"] = Temporizador.getTiempo()
    datos["Atril_jugador"] = Atril_jugador.getEstado()
    datos["Atril_computadora"] = Atril_computadora.getEstado()
    datos["Puntaje_jugador"] = puntaje_J
    datos["Puntaje_computadora"] = puntaje_C
    datos["Dificultad"] = dificultad

    datos = __convertir_Datos_A_Json(datos)
    
    actualizar_cant_partidas_guardadas()
    indice = __cant_partidas()
    direccion = "Archivos\\partidas\\partida_guardada_" +  str(indice+1)  + ".json" 
    
    with open(direccion, 'w') as archivo:
            json.dump(datos, archivo)        
            archivo.close()


#puntaje_J --> int
#dificultad --> int del 1 al 3
#nombre --> String
def guardar_partida_finalizada(puntaje_J , dificultad , nombre):

    """Guarda los datos de la partida, en la carpeta "Archivos\\partidas_FINALIZADAS" para mostrar el Top 10 de los mejores jugadores y sus datos - - - 
    También actualiza "cant_partidas.txt" de la carpeta correspondiente."""

    actualizar_cant_partidas_guardadas(True)
    indice = __cant_partidas(True)
    direccion = "Archivos\\partidas_FINALIZADAS\\partida_guardada_FINALIZADA_" + str(indice+1) +".json"
    
    datos = {}

    datos["Puntaje_jugador"] = puntaje_J
    datos["Dificultad"] = dificultad
    datos["Nombre"] = nombre
    datos["Fecha"] = str(date.today())

    with open(direccion, 'w') as archivo:
            json.dump(datos, archivo)        
            archivo.close()

  
#datos_del_menu --> {"minutos": * int positivo * , "dificultad" : * int del 1 al 3 * ,  "letras":  {'A':{'cantidad':11,'valor':1} , ... } }
def definir_configuracion(datos_del_menu):
    
    """Despues que se confirme la configuracion personalizada en el menu, se modifica la dificultad seleccionada.
    Desde este punto, los datos se usan en metodos y para instanciar objetos.
    (Esta configuracion se persiste en un archivo cuando termine la partida o la guarde el usuario)"""
      
    config_por_defecto = __cargarConfiguracionPorDefecto(datos_del_menu["dificultad"])                      #Cargamos una dificultad
    
    config_por_defecto["Dificultad"] = datos_del_menu["dificultad"]
    config_por_defecto["Temporizador"]["minutos"] = datos_del_menu["minutos"]                               #Seteamos los cambios                            
    
    if datos_del_menu["letras"] != {}:
        
        for letra in datos_del_menu["letras"]:
            config_por_defecto["Bolsa"][letra] = datos_del_menu["letras"][letra]

    return config_por_defecto


#dificultad --> int del 1 al 3
def TopTen_de_jugadores(dificultad):

    """Lee los datos de las partidas guardadas y muestra un Top 10 de los mejores jugadores, según su puntaje"""

    actualizar_cant_partidas_guardadas(True)
    cant = __cant_partidas(True)
    
    lista = []
    for i in range(1,cant+1):                                           

        direccion = "Archivos\\partidas_FINALIZADAS\\partida_guardada_FINALIZADA_" + str(i) + ".json"

        with open(direccion, 'r') as archivo:
            datos = json.load(archivo , encoding='utf-8')
            archivo.close()

        if datos["Dificultad"] == dificultad:
            lista.append({"Nombre":datos["Nombre"] , "Puntaje":datos["Puntaje_jugador"] , "Dificultad":datos["Dificultad"] , "Fecha":datos["Fecha"]})

    Todos = list(sorted(lista , key = lambda top: top["Puntaje"] , reverse=True))
    
    ret = []
    for elemento in Todos:
        nombre = elemento["Nombre"]
        puntaje = datos["Puntaje_jugador"]
        if datos["Dificultad"] == 1:
            dificultad = "Facil"
        elif datos["Dificultad"] == 2:
            dificultad = "Medio"
        else:
            dificultad = "Dificil"

        fecha = datos["Fecha"]
        ret.append(f">>{nombre} // {puntaje}pts // Dificultad {dificultad} // {fecha}")

    if len(ret) >= 10:
        return ret[:10]
    
    else:
        return ret
    

def lista_de_partidas_a_cargar():

    """Genera una lista de las direcciones de las partidas guardadas."""
    
    lista = []
    i = 1
    while True:                                                     

        try:
            
            direccion = "Archivos\\partidas\\partida_guardada_" + str(i) + ".json"
            #print(direccion)

            with open(direccion, 'r') as archivo:
                archivo.close()

            lista.append(direccion)
            i = i + 1
                
        except FileNotFoundError:
            break
    
    return lista



# OBJETOS = instanciar_objetos(Bol,Table,Temp,Atril_computadora,Atril_jugador,config)
# SE USAN LOS OBJETOS
# guardar_partida(OBJETOS["Bolsa"] , OBJETOS["Tablero"] , OBJETOS["Temporizador"] , OBJETOS["Atril_jugador"] , OBJETOS["Atril_computadora"], 666 , 999, 1)

# print(lista_de_partidas_a_cargar())

#------------------------------------------------------------------------------------------------------------------------
# Molina, Lucio Felipe - 15980/7
