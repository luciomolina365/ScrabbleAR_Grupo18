import json

def obtenerConfiguracion(cargarPartida = False , numero_de_dificultad = 0):

    if cargarPartida and numero_de_dificultad == 0:
        
        with open("partidas\partida_guardada.json", 'r') as archivo:
            datos = json.load(archivo)
            datos = convertir_Json_A_Datos(datos)
        return datos

    elif numero_de_dificultad != 0:
        
        direccion = "configuracion\por_defecto_"  +  str(numero_de_dificultad) +  ".json"
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
    
#========================================================

datos = obtenerConfiguracion(True)

print(datos["Temporizador"])

#print(type(str((1,2))))
#print("-.,-.,-.,-.,-.,-,.")
#print(tuple("(1,2)"))


def cambiarConfiguracion():
    pass 

