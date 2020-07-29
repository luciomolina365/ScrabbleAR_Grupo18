import json
import PySimpleGUI as sg
from os import rename
from os import remove

def cargarConfiguracionPorDefecto(dificultad):
    direccion = "Archivos\\configuracion\\por_defecto_" + str(dificultad) +".json"
    datos = cargarPartida(direccion)
    return datos

def cargarPartida(direccion):

        """Lee un archivo mediante direccion, le da formato útil a los datos y los retorna.
        (sirve para cargar una partida guardada y para cargar los datos por defecto)."""

        with open(direccion, 'r') as archivo:
            datos = json.load(archivo , encoding='utf-8')
            datos = convertir_Json_A_Datos(datos)
            archivo.close()   
        return datos


def cant_partidas(Finalizada = False):

    if Finalizada:
        direccion = "Archivos\\partidas_FINALIZADAS\\cant_partidas.txt"
    else:
        direccion = "Archivos\\partidas\\cant_partidas.txt"

    f = open(direccion,"r")
    aux = f.readlines()
    f.close()
    return int(aux[0])


def hay_partidas_a_cargar():                                        #Lee el archivo de cantidad de partidas y retorna un booleano
    
    cant = cant_partidas()

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
            print(direccion)

            with open(direccion, 'r') as archivo:
                datos = json.load(archivo,encoding='utf-8')
                datos = convertir_Json_A_Datos(datos)
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
    
def convertir_Datos_A_Json(datos):
    aux = {}
    for coor in datos["Tablero"]:
        aux[str(coor)] = datos["Tablero"][coor]
    
    datos["Tablero"] = aux
    return datos
    

def convertir_Json_A_Datos(datos):
    aux = {}

    for coor in datos["Tablero"]:
        
        aux[eval(coor)] = datos["Tablero"][coor]
    
    datos["Tablero"] = aux
    return datos

#========================================================        

def estaFinalizada(datos):
    return datos["Finalizada"]


def __TEST_GUARDAR(Bolsa , Tablero, Temporizador , Atril_jugador , Atril_computadora , puntaje_J , puntaje_C , dificultad , Finalizada = False):
    actualizar_cant_partidas_guardadas(Finalizada)

    if Finalizada:
        indice = cant_partidas(Finalizada)
        direccion = "Archivos\\partidas_FINALIZADAS\\partida_guardada_FINALIZADA_" + str(indice+1) +".json"
    
    else:
        indice = cant_partidas()
        direccion = "Archivos\\partidas\\partida_guardada_" +  str(indice+1)  +".json"    

    datos={}

    datos["Tablero"] = Tablero
    datos["Bolsa"] = Bolsa
    datos["Temporizador"] = Temporizador
    datos["Atril_jugador"] = Atril_jugador
    datos["Atril_computadora"] = Atril_computadora
    datos["Puntaje_jugador"] = puntaje_J
    datos["Puntaje_computadora"] = puntaje_C
    datos["Dificultad"] = dificultad
    datos["Finalizada"] = Finalizada

    datos = convertir_Datos_A_Json(datos)

    with open(direccion, 'w') as archivo:
            json.dump(datos, archivo)        
            archivo.close()

    actualizar_cant_partidas_guardadas(Finalizada)

#Bolsa , Tablero, Temporizador , Atril_jugador , Atril_computadora --> Objetos
#puntaje_J , puntaje_C --> int
#dificultad --> int del 1 al 3
#Finalizada --> boolean
def guardar_partida(Bolsa , Tablero, Temporizador , Atril_jugador , Atril_computadora , puntaje_J , puntaje_C , dificultad , Finalizada = False):   
    
    """Guarda los datos de la partida, en la carpeta "Archivos\\partidas_FINALIZADAS" si la partida terminó o en "Archivos\\partidas" si la partida se puede continuar - - - 
    También actualiza "cant_partidas.txt" de la carpeta correspondiente."""
    
    actualizar_cant_partidas_guardadas(Finalizada)

    if Finalizada:
        indice = cant_partidas(Finalizada)
        direccion = "Archivos\\partidas_FINALIZADAS\\partida_guardada_FINALIZADA_" + str(indice+1) +".json"
    
    else:
        indice = cant_partidas()
        direccion = "Archivos\\partidas\\partida_guardada_" +  str(indice+1)  +".json"    

    datos={}

    datos["Tablero"] = Tablero.getEstado()
    datos["Bolsa"] = Bolsa.getBolsa()
    datos["Temporizador"] = Temporizador.getTiempo()
    datos["Atril_jugador"] = Atril_jugador.getEstado()
    datos["Atril_computadora"] = Atril_computadora.getEstado()
    datos["Puntaje_jugador"] = puntaje_J
    datos["Puntaje_computadora"] = puntaje_C
    datos["Dificultad"] = dificultad
    datos["Finalizada"] = Finalizada

    datos = convertir_Datos_A_Json(datos)

    with open(direccion, 'w') as archivo:
            json.dump(datos, archivo)        
            archivo.close()

    actualizar_cant_partidas_guardadas(Finalizada)

  
#datos_del_menu --> {"minutos": * int positivo * , "dificultad" : * int del 1 al 3 * ,  "letras":  {'A':{'cantidad':11,'valor':1} , ...} }
def definir_configuracion(datos_del_menu):
    
    """Despues que se confirme la configuracion personalizada en el menu, se modifica la dificultad seleccionada.
    Desde este punto, los datos se usan en metodos y para instanciar objetos.
    (Esta configuracion se persiste en un archivo cuando termine la partida o se guarde)"""
      
    config_por_defecto = cargarConfiguracionPorDefecto(datos_del_menu["dificultad"])                        #Cargamos una dificultad
    
    config_por_defecto["Dificultad"] = datos_del_menu["dificultad"]
    config_por_defecto["Temporizador"]["minutos"] = datos_del_menu["minutos"]                               #Seteamos los cambios                            
    config_por_defecto["Bolsa"] = datos_del_menu["letras"]

    return config_por_defecto


def main():
    #facil = 1
    #medio = 2
    dificil = 3

    datos = cargarConfiguracionPorDefecto(dificil)         
                                                
    if datos != {}:
        #ESTE TEST NO ES LO QUE HAY QUE HACER (ES UN EJEMPLO PARA USARLO EN EL MOMENTO)
        __TEST_GUARDAR(datos["Bolsa"] , datos["Tablero"] , datos["Temporizador"] , datos["Atril_jugador"] , datos["Atril_computadora"] , 123 , 321 , datos["Dificultad"] , True)
        
        # OBJETOS = instanciar_objetos(Bol,Table,Temp,Atril_computadora,Atril_jugador,config)
        # SE USAN LOS OBJETOS
        # guardar_partida(OBJETOS["Bolsa"] , OBJETOS["Tablero"] , OBJETOS["Temporizador"] , OBJETOS["Atril_jugador"] , OBJETOS["Atril_computadora"], 666 , 999, True)




    else:
        print("No hay partidas a cargar")
        print("Crea una partida nueva")


#========================================================
#DEMOSTRACION DE USO


if __name__ == "__main__":
    main()
    print("LISTO")
    print("Cantidad de partidas actualizada")
    
    
    if hay_partidas_a_cargar():
        print("Hay partidas para cargar")
    else:
        print("---NO--- HAY PARTIDAS A CARGAR")

    print("ACA DEBERIA USAR EL BOOLEAN PARA QUE SE MUESTRE O NO EL BOTON DE CARGAR PARTIDA")
    sg.popup("ACA DEBERIA USAR EL BOOLEAN PARA QUE SE MUESTRE O NO EL BOTON DE CARGAR PARTIDA")

#------------------------------------------------------------------------------------------------------------------------
#Molina, Lucio Felipe - 15980/7
