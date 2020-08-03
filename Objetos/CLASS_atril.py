import PySimpleGUI as sg
class Atril:
    
    #dic_de_letras --> diccionario de diccionarios (en formato especifico) EJ. {'A':{'cantidad':4,'valor':1} , 'B':{'cantidad':3,'valor':1}} (las cantidades suman 7)
    def __init__(self,dic_de_letras):    
        
        self.__estado = dic_de_letras
        self.__fichas_disponibles = []
        self.__cant_fichas = 0
        self.__actualizar_estado_entero()
        

        for letra in self.__estado:
            self.__cant_fichas = self.__cant_fichas + self.__estado[letra]["cantidad"]


    def __actualizar_letra(self,letra):

        if  self.__estado[letra]["cantidad"] == 0:                    #Saca la ficha que ya no esta
            del self.__estado[letra]

            
    def __actualizar_estado_entero(self):
        
        for elemento in self.__estado:                                #Bucle para sacar las fichas con cantidad == 0
            self.__actualizar_letra(elemento)

        self.__fichas_disponibles.clear()                             #Actualiza las letras disponibles
        for elemento in self.__estado:                            
            cant = self.__estado[elemento]["cantidad"]
            for i in range(cant):
                self.__fichas_disponibles.append(elemento)


    #======================================================================================================================================
    #GETTERS

    def getEstado(self):
        dic = {**self.__estado}
        return dic                                                    #EJ. {'A':{'cantidad':2,'valor':1} , 'B':{'cantidad':3,'valor':1}}                                           

    def getFichas_disponibles(self):
        return self.__fichas_disponibles                              #EJ. ["T", "O", "P", "O"]

    #======================================================================================================================================
    #METODOS

    #letra --> string EJ. "A"
    def sacar_ficha(self,letra):
        
        self.__estado[letra]["cantidad"] = self.__estado[letra]["cantidad"] - 1
        self.__cant_fichas = self.__cant_fichas - 1
        self.__fichas_disponibles.remove(letra)
        self.__actualizar_letra(letra)


    #lista_de_letras --> lista EJ. ["L", "C", "L", "K"]
    def sacar_varias_fichas(self, lista_de_letras):

        """Le SACA las fichas pasadas por parametro al Atril y lo actualiza"""
        
        for letra in lista_de_letras:
            self.sacar_ficha(letra)


    #dic_de_ficha --> diccionario de diccionarios   EJ. {'A':{'cantidad':2,'valor':1} , 'G':{'cantidad':1,'valor':1}}
    def agregar_varias_fichas(self,dic_de_fichas):

        """Le AGREGA las fichas pasadas por parametro al Atril y lo actualiza"""
        
        if dic_de_fichas:                                           #Si el diccionario no está vacio
            
            for letra in dic_de_fichas:
                
                if letra not in self.__estado.keys():
                    self.__estado[letra] = dic_de_fichas[letra]    
                
                else:            
                    self.__estado[letra]["cantidad"] = self.__estado[letra]["cantidad"] + dic_de_fichas[letra]["cantidad"]
            
            self.__actualizar_estado_entero()

        else:
            #POPUP DE BOLSA VACIA (DEBUG) /////////////////////
            sg.popup("ESTE PROCESO NO TIENE QUE SER LLAMADO SI LA BOLSA ESTA VACIA")  


        
#------------------------------------------------------------------------------------------------------------------------
# Molina, Lucio Felipe - 15980/7