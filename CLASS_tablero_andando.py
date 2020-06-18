class Tablero:
    estado={}

    def __init__(self,ancho,alto):
        for x in range(ancho+1):
            for y in range(alto+1):
                self.estado[(x,y)] = {"valor":"", "trampa":False , "doblePuntuacion":False}

    def getEstado(self):       #Devuelve un diccionario (que representa el tablero) del formato: 
        return self.estado     #{*tupla de int*: {"valor": *dato*  ,  "trampa": *boolean*  ,  "doblePuntuacion": *boolean*}}
        
    #====================================================================================================================
    #GETTERS

    def getDatosEnCoor(self, coordenada):
        return self.estado[coordenada]    #{"valor": *dato*  ,  "trampa": *boolean*  ,  "doblePuntuacion": *boolean*}
    
    def getValorEnCoor(self, coordenada):
        return self.estado[coordenada]["valor"]
    
    def getEsTrampaEnCoor(self, coordenada):
        return self.estado[coordenada]["trampa"]

    def getEsDoblePuntuacionEnCoor(self, coordenada):
        return self.estado[coordenada]["doblePuntuacion"]

    #====================================================================================================================
    #SETTERS
    
    def setDatosEnCoor(self,coordenada, valor, trampa=False, doblePuntuacion=False):
        self.estado[coordenada]["valor"] = valor
        self.estado[coordenada]["trampa"] = trampa
        self.estado[coordenada]["doblePuntuacion"] = doblePuntuacion

    def setValorEnCoor(self, coordenada, valor):
        self.estado[coordenada]["valor"] = valor
    
    def setTrampaEnCoor(self, coordenada, trampa):
        self.estado[coordenada]["trampa"] = trampa

    def setDoblePuntuacionEnCoor(self, coordenada, doblePuntuacion):
        self.estado[coordenada]["doblePuntuacion"] = doblePuntuacion

    #====================================================================================================================





    