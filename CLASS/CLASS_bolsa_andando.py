import random
class Bolsa:

    def __init__(self, dic_de_letras, letras_disponibles = []):
        self.bolsa = dic_de_letras
        self.letras_disponibles = letras_disponibles            #Para continuar la partida
        
        if len(self.letras_disponibles) == 0:                   #Si no se cargo ninguna partida
            
            for letra in self.bolsa.keys():                   #Cargo las letras disponibles 
                if self.bolsa[letra] != 0:                    #(POR SI ALGUNA LETRA TIENE CANTIDAD = 0 EN LA CONFIGURACION)
                    self.letras_disponibles.append(letra)
                    
    def getLetrasDisponibles(self):
        return self.letras_disponibles

    def getBolsa(self):
        return self.bolsa

    def getCantFichasTotales(self):
        return len(self.letras_disponibles)


    def dameFichas(self, cant_fichas):
        if cant_fichas == 0:            #CLASS JUEGO
            return {}

        fichas = {}

        for i in range(cant_fichas):
            letra_random = random.choice(self.letras_disponibles)               #Elegimos una letra 
            
            if letra_random not in fichas.keys():                               #Llenamos el diccionario de fichas para devolver
                fichas[letra_random] = {"cantidad": 1 , "valor": self.bolsa[letra_random]["valor"]}      
            else:
                fichas[letra_random]["cantidad"] = fichas[letra_random]["cantidad"] + 1
                

            self.bolsa[letra_random]["cantidad"] = self.bolsa[letra_random]["cantidad"] - 1     #Actualizamos la bolsa     
            
            if self.bolsa[letra_random]["cantidad"] == 0:                                       #Si es necesario, actualizamos las letras disponibles
                self.letras_disponibles.remove(letra_random)

        return fichas
        