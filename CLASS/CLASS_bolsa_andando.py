import random
class Bolsa:

    def __init__(self,dic_de_letras):
        self.valores = dic_de_letras
        self.letras_disponibles = []
        for letra in self.valores.keys():                   #Letras disponibles (POR SI ALGUNA LETRA TIENE CANTIDAD = 0 EN LA CONFIGURACION)
            if self.valores[letra] != 0:
                self.letras_disponibles.append(letra)


    def getLetrasDisponibles(self):
        return self.letras_disponibles

    def getBolsa(self):
        return self.valores




    def dameFichas(self, cant_fichas):
        fichas = {}

        for i in range(cant_fichas):
            letra_random = random.choice(self.letras_disponibles)
            
            if letra_random not in fichas.keys():                               #Llenamos el diccionario de fichas para devolver
                fichas[letra_random] = 1    
            else:
                fichas[letra_random] = fichas[letra_random] + 1
                

            self.valores[letra_random] = self.valores[letra_random] - 1         #Elegimos una letra actualizamos la bolsa y, si es necesario,
            if self.valores[letra_random] == 0:                                 #actualizamos las letras disponibles
                self.letras_disponibles.remove(letra_random)

        return fichas
        