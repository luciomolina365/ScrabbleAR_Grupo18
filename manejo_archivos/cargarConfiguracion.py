import json
import PySimpleGUI as sg

def obtenerConfiguracion(cargarPartida = False , numero_de_dificultad = 0):

    if cargarPartida and numero_de_dificultad == 0:
        
        try:
            
            direccion = "Archivos\\partidas\\partida_guardada_" + ".json"  
            with open(direccion, 'r') as archivo:
                datos = json.load(archivo)
                datos = convertir_Json_A_Datos(datos)
            return datos
        
        except FileNotFoundError:
            sg.popup("No hay partidas para continuar")
            return {}

    elif numero_de_dificultad != 0:
        
        direccion = "Archivos\\configuracion\\por_defecto_"  +  str(numero_de_dificultad) +  ".json"
        with open(direccion, 'r') as archivo:
            datos = json.load(archivo)
            datos = convertir_Json_A_Datos(datos)   
        return datos
        
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


def cambiarConfiguracion(configuracion):
    pass  



#========================================================
#DEMOSTRACION DE USO

datos = obtenerConfiguracion(True)              #Si pones 
                                                #-True  --> carga una partida no finalizada
                                                #-False 
if datos != {}:
    print(datos["Temporizador"])
else:
    print("No hay partidas a cargar")
    print("Crea una partida nueva")

#print(type(str((1,2))))
#print("-.,-.,-.,-.,-.,-,.")
#print(tuple("(1,2)"))







#------------------------------------------------------------------------------------------------------------------------
#Molina, Lucio Felipe - 15980/7