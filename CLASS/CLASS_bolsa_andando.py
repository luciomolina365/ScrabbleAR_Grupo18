import PySimpleGUI as sg
import random
class Bolsa:

    __TERMINO = False

    #dic_de_letras --> diccionario de diccionarios (en formato especifico) EJ. {'A':{'cantidad':11,'valor':1} , 'B':{'cantidad':3,'valor':1}}
    #letras_disponibles --> lista de strings(caracteres) EJ.  ["A","B","V", "Z"]

    def __init__(self, dic_de_letras):
        self.__bolsa = dic_de_letras
        self.__letras_disponibles = []
    

    def __actualizarLetrasDisponibles(self):
            
        for letra in self.__bolsa.keys():                                   #Cargo las letras disponibles 
            if self.__bolsa[letra] != 0:                                    #(POR SI ALGUNA LETRA TIENE CANTIDAD = 0 EN LA CONFIGURACION o PARTIDA CARGADA)
                self.__letras_disponibles.append(letra)
        

    #====================================================================================================================
    #GETTERS
                    
    def getLetrasDisponibles(self):
        return self.__letras_disponibles                                    #EJ.  ["A", "B", "V", "Z"]


    def getBolsa(self):
        return self.__bolsa                                                 #EJ.  {'A':{'cantidad':11,'valor':1} , 'B':{'cantidad':3,'valor':1}}


    def getCantFichasTotales(self):
        cant = 0
        for letra in self.__bolsa:
            cant = cant + self.__bolsa[letra]["cantidad"]

        return cant                                                         #int 


    def getTERMINO_Bolsa(self):
        return self.__TERMINO                                               #boolean


    #====================================================================================================================
    #METODOS

    #cant_fichas --> int
    def dameFichas(self, cant_fichas):

        """Devuelve un diccionario de diccionarios segun 
        la cantidad de fichas ingresada y actualiza la bolsa."""
    
        if cant_fichas > self.getCantFichasTotales():                                                   #Si no tengo suficientes fichas
            #POPUP SE TERMINA EL JUEGO POR FALTA DE FICHAS
            print(f"fichas pedidas = {cant_fichas} / total = {self.getCantFichasTotales()}")
            sg.popup("No hay suficientes fichas en la bolsa")                                           #Popup y devuelve un dic vacio
            self.__TERMINO = True
            return {}

        fichas = {}

        for i in range(cant_fichas):
            letra_random = random.choice(self.__letras_disponibles)                                     #Elegimos una letra 
            
            if letra_random not in fichas.keys():                                                       #Llenamos el diccionario de fichas para devolver
                fichas[letra_random] = {"cantidad": 1 , "valor": self.__bolsa[letra_random]["valor"]}   #Si es una letra nueva, la agrega al diccionario    
            else:
                fichas[letra_random]["cantidad"] = fichas[letra_random]["cantidad"] + 1                 #Si la letra ya existe, le suma 1 a la cantidad de esa letra
                

            self.__bolsa[letra_random]["cantidad"] = self.__bolsa[letra_random]["cantidad"] - 1         #Actualizamos la bolsa, a la cantidad de la letra que sacamos, le restamos 1 
            
            if self.__bolsa[letra_random]["cantidad"] == 0:                                             #Si es necesario, actualizamos las letras disponibles
                self.__letras_disponibles.remove(letra_random)

        return fichas                       #EJ.  {}  o   {'A':{'cantidad':4,'valor':1} , 'B':{'cantidad':3,'valor':1}}

    
    #dic_de_fichas  --> diccionario de diccionarios  EJ. {'A':{'cantidad':4,'valor':1} , 'B':{'cantidad':3,'valor':1}}
    def devolverFichas(self, dic_de_fichas):
        
        for letra in dic_de_fichas:
            self.__bolsa[letra]["cantidad"] = self.__bolsa[letra]["cantidad"] + dic_de_fichas[letra]["cantidad"]

        self.__actualizarLetrasDisponibles()


    #dic_a_intercambiar  --> diccionario de diccionarios  EJ. {'A':{'cantidad':4,'valor':1} , 'B':{'cantidad':3,'valor':1}}
    def intercambiar_fichas(self,dic_a_intercambiar):         
        
        cant = 0
        for letra in dic_a_intercambiar:                                                                #Contamos la cantidad de fichas a devolver
            cant = cant + dic_a_intercambiar[letra]["cantidad"]
        
        self.devolverFichas(dic_a_intercambiar)                                                         #Actualizamos el estadp interno del objeto

        return self.dameFichas(len(cant))                           #EJ.  {}  o   {'A':{'cantidad':4,'valor':1} , 'B':{'cantidad':3,'valor':1}}





#------------------------------------------------------------------------------------------------------------------------    
#Molina, Lucio Felipe - 15980/7        