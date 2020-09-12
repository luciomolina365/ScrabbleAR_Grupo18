
import PySimpleGUI as sg
import random
import copy

class Bolsa:

    __TERMINO = False

    #dic_de_letras --> diccionario de diccionarios (en formato especifico) EJ. {'A':{'cantidad':11,'valor':1} , 'B':{'cantidad':3,'valor':1}}
    #letras_disponibles --> lista de strings(caracteres) EJ.  ["A","B","V", "Z"]
    def __init__(self, dic_de_letras):
        self.__bolsa = dic_de_letras
        self.__letras_disponibles = []
        self.__actualizarLetrasDisponibles()
    

    def __actualizarLetrasDisponibles(self):
        self.__letras_disponibles.clear()
        for letra in self.__bolsa.keys():                                   # Cargo las letras disponibles 
            if self.__bolsa[letra]["cantidad"] != 0:                        # (POR SI ALGUNA LETRA TIENE CANTIDAD = 0 EN LA CONFIGURACION o PARTIDA CARGADA)
                self.__letras_disponibles.append(letra)
        

    #====================================================================================================================
    #GETTERS
                    
    def getLetrasDisponibles(self):

        """Devuelve una lista que representa las fichas de la bolsa."""
        
        lista = copy.deepcopy(self.__letras_disponibles)
        return lista                                                        #EJ.  ["A", "B", "V", "Z"]
          


    def getBolsa(self):

        """Devuelve un diccionario que representa las letras de la bolsa, con sus cantidades y valores."""

        dic = copy.deepcopy(self.__bolsa)
        return dic                                                          #EJ.  {'A':{'cantidad':11,'valor':1} , 'B':{'cantidad':3,'valor':1}}


    def __getCantFichasTotales(self):

        return  self.__contar_fichas(self.__bolsa)                          #int 


    def getTERMINO_Bolsa(self):

        """Retorna un True en caso que la bolsa este vacia, en caso contrario devuelve False."""

        return self.__TERMINO                                               #boolean


    #====================================================================================================================
    #METODOS

    #cant_fichas --> int
    def dameFichas(self, cant_fichas):

        """Devuelve un diccionario de diccionarios segun 
        la cantidad de fichas ingresada y actualiza la bolsa."""
    
        if cant_fichas > self.__getCantFichasTotales():                                                 #Si no tengo suficientes fichas                                            
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

        """Devuelve a la Bolsa las fichas pasadas por parametro."""
        
        for letra in dic_de_fichas:
            self.__bolsa[letra]["cantidad"] = self.__bolsa[letra]["cantidad"] + dic_de_fichas[letra]["cantidad"]

        


    #dic_a_intercambiar  --> diccionario de diccionarios  EJ. {'A':{'cantidad':4,'valor':1} , 'B':{'cantidad':3,'valor':1}}
    # ó
    #dic_a_intercambiar  --> lista de strings EJ. ["A","A","F","B"]
    def intercambiar_fichas(self,dic_a_intercambiar):

        """Recibe un diccionario o una lista de fichas y retorna un diccionario con la misma cantidad de fichas."""  

        if type(dic_a_intercambiar) == list:                                                            #Si recibe una lista, la convierte a diccionario para procesarla
            estado = self.getBolsa()
            dic = {}
            for letra in dic_a_intercambiar:
                if letra in dic.keys():
                    dic[letra]["cantidad"] = dic[letra]["cantidad"]+1
                else:
                    dic[letra] = {"cantidad":1,"valor":estado[letra]["valor"]}
            
            
      

        self.devolverFichas(dic) 

        cant = self.__contar_fichas(dic)                                                                #Contamos la cantidad de fichas a dar                                                    
        
        self.__actualizarLetrasDisponibles()                                                         

        return self.dameFichas(cant)                           #EJ.  {}  o   {'A':{'cantidad':4,'valor':1} , 'B':{'cantidad':3,'valor':1}}


    #dic --> diccionario de diccionarios  EJ. {'A':{'cantidad':4,'valor':1} , 'B':{'cantidad':3,'valor':1}}
    def __contar_fichas(self, dic):
        cant = 0
        for letra in dic:                                                                             
            cant = cant + dic[letra]["cantidad"]

        return cant                                             #int



#------------------------------------------------------------------------------------------------------------------------    
# Molina, Lucio Felipe - 15980/7        