import random
class Bolsa:

    #dic_de_letras --> diccionario de diccionarios (en formato especifico) EJ. {'A':{'cantidad':11,'valor':1} , 'B':{'cantidad':3,'valor':1}}
    #letras_disponibles --> lista de strings(caracteres) EJ.  ["A","B","V", "Z"]

    def __init__(self, dic_de_letras):
        self.bolsa = dic_de_letras
        self.letras_disponibles = []
            
        for letra in self.bolsa.keys():                             #Cargo las letras disponibles 
            if self.bolsa[letra] != 0:                              #(POR SI ALGUNA LETRA TIENE CANTIDAD = 0 EN LA CONFIGURACION o PARTIDA CARGADA)
                self.letras_disponibles.append(letra)
                    

                    
    def getLetrasDisponibles(self):
        return self.letras_disponibles                                  #EJ.  ["A", "B", "V", "Z"]

    def getBolsa(self):
        return self.bolsa                                               #EJ.  {'A':{'cantidad':11,'valor':1} , 'B':{'cantidad':3,'valor':1}}

    def getCantFichasTotales(self):
        return len(self.letras_disponibles)                             #int 

    #cant_fichas --> int
    def dameFichas(self, cant_fichas):

        """Devuelve un diccionario de diccionarios segun 
        la cantidad de fichas ingresada y actualiza la bolsa."""
        
        if cant_fichas == 0:                        ###=====================================HACER CLASS JUGADOR=====================================###
            return {}

        fichas = {}

        for i in range(cant_fichas):
            letra_random = random.choice(self.letras_disponibles)                                   #Elegimos una letra 
            
            if letra_random not in fichas.keys():                                                   #Llenamos el diccionario de fichas para devolver
                fichas[letra_random] = {"cantidad": 1 , "valor": self.bolsa[letra_random]["valor"]}      
            else:
                fichas[letra_random]["cantidad"] = fichas[letra_random]["cantidad"] + 1
                

            self.bolsa[letra_random]["cantidad"] = self.bolsa[letra_random]["cantidad"] - 1         #Actualizamos la bolsa     
            
            if self.bolsa[letra_random]["cantidad"] == 0:                                           #Si es necesario, actualizamos las letras disponibles
                self.letras_disponibles.remove(letra_random)

        return fichas                                                   #EJ.  {}  o   {'A':{'cantidad':4,'valor':1} , 'B':{'cantidad':3,'valor':1}}
        