import json
import PySimpleGUI as sg

def obtenerConfiguracion(direccion):
        with open(direccion, 'r') as archivo:
            datos = json.load(archivo)
            datos = convertir_Json_A_Datos(datos)
            archivo.close()   
        return datos

def hay_partidas_a_cargar():
    direccion = "Archivos\\partidas\\cant_partidas.txt"
    f = open(direccion,"r")
    aux = f.readlines()
    f.close()

    if aux == 0:
        return False
    else:
        return True 
        

def actualizar_cant_partidas_guardadas():
    i = 1
    while True:

        try:
            direccion = "Archivos\\partidas\\partida_guardada_" + str(i) + ".json"
            with open(direccion, 'r') as archivo:
                archivo.close()
            i = i + 1
        except FileNotFoundError:
            break
    
    direccion = "Archivos\\partidas\\cant_partidas.txt"
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


def estaFinalizada(datos):
    return datos["Finalizada"]
        
    

def cambiarConfiguracion(configuracion):                    #-.,-,.-.,-.,-.,-.,-.,-,.-.,HACERRRRRR-.,-.,-,.-.,-.,-.,-.,-.,-.,-.,-,.
    pass                                                    #-.,-,.-.,-.,-.,-.,-.,-,.-.,HACERRRRRR-.,-.,-,.-.,-.,-.,-.,-.,-.,-.,-,.



#========================================================
#DEMOSTRACION DE USO


def main():
    datos = obtenerConfiguracion("Archivos\\partidas\\partida_guardada_1.json")          
                                                
    if datos != {}:
        print("Muestra de que se levantaron los datos desde un archivo:  ")
        print(datos["Temporizador"])
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
        print("ACA DEBERIA MANDAR UN BOOLEAN PARA QUE SE MUESTRE O NO EL BOTON DE CARGAR PARTIDA")
        sg.popup("ACA DEBERIA MANDAR UN BOOLEAN PARA QUE SE MUESTRE O NO EL BOTON DE CARGAR PARTIDA")



#------------------------------------------------------------------------------------------------------------------------
#Molina, Lucio Felipe - 15980/7
