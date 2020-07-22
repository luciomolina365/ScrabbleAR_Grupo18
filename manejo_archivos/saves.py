import json

def escribirArchivo(values):
    with open("ListaDeJugadores.json","w") as archivo:
        json.dump(values,archivo)


def leerArchivo():
        with open("ListaDeJugadores.json","r") as archivo:
            datos=json.load(archivo)
        return datos

  ##     try:
    #         saves.leerArchivo()  //en el menu
    #     except FileNotFoundError:
    #         sg.popup("No existen partidas previas")
  
        
