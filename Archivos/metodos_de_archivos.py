import json
import PySimpleGUI as sg
from os import rename
from os import remove
def obtenerConfiguracion(direccion):                                #Lee un archivo mediante direccion y le da formato util a los datos
        with open(direccion, 'r') as archivo:
            datos = json.load(archivo , encoding='utf-8')
            datos = convertir_Json_A_Datos(datos)
            archivo.close()   
        return datos


def cant_partidas():
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
        

def actualizar_cant_partidas_guardadas():

    """Actualiza cant_partidas.txt, para, segun sus datos, permitir o no cargar partida"""

    i = 1
    while True:                                                     #Cuenta los archivos de partida NO FINALIZADAS 

        try:
            predef = "Archivos\\partidas\\partida_guardada_"
            direccion = predef + str(i) + ".json"
            with open(direccion, 'r') as archivo:
                datos = json.load(archivo,encoding='utf-8')
                datos = convertir_Json_A_Datos(datos)
                archivo.close()

            if estaFinalizada(datos):
                nuevo_nombre = predef + "FINALIZADA" + ".json"
                
                try:
                    rename(direccion, nuevo_nombre)
                except FileExistsError:
                    remove(direccion)
                
                    
            else:
                i = i + 1  
                
        except FileNotFoundError:
            break
    
    direccion = "Archivos\\partidas\\cant_partidas.txt"             #Actualiza la cantidad de partidad disponibles
    f = open(direccion,"w")
    i = i - 1
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
        

def guardar_partida(Bolsa , Tablero, Temporizador , Atril_jugador , Atril_computadora , puntaje_J , puntaje_C , Finalizada = False):   #RECIBO LOS DATOS DE LOS OBJETOS Y DEMAS
    actualizar_cant_partidas_guardadas()
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
    datos["Finalizada"] = Finalizada

    datos = convertir_Datos_A_Json(datos)

    with open(direccion, 'w') as archivo:
            json.dump(datos, archivo)        
            archivo.close()

    actualizar_cant_partidas_guardadas()
    



    
#datos_del_menu --> {"minutos": * int positivo * , "dificultad" : * int del 1 al 3 * ,  "letras":  {'A':{'cantidad':11,'valor':1} , ...} }
def definir_configuracion(datos_del_menu):
    
    """Despues que se confirme la configuracion personalizada en el menu, se modifica la dificultad seleccionada.
    Desde este punto, los datos se usan en metodos e instanciar los objetos.
    (Esta configuracion se pasa a un archivo cuando termine la partida o se guarde)"""



    direccion = "Archivos\\configuracion\\por_defecto_" +  str(datos_del_menu["dificultad"])   +  ".json"        #Cargamos una dificultad
    config_por_defecto = obtenerConfiguracion(direccion)        
    
    config_por_defecto["Dificultad"] = datos_del_menu["dificultad"]
    config_por_defecto["Temporizador"]["minutos"] = datos_del_menu["minutos"]                               #Seteamos los cambios                            
    config_por_defecto["Bolsa"] = datos_del_menu["letras"]

    return config_por_defecto




#========================================================
#DEMOSTRACION DE USO


def main():
    datos = obtenerConfiguracion("Archivos\\configuracion\\por_defecto_1.json")          
                                                
    if datos != {}:
        print("Muestra de que se levantaron los datos desde un archivo:  ")
        print(datos["Bolsa"])
    else:
        print("No hay partidas a cargar")
        print("Crea una partida nueva")

    #print(type(str((1,2))))
    #print("-.,-.,-.,-.,-.,-,.")
    #print(tuple("(1,2)"))

    actualizar_cant_partidas_guardadas()


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
