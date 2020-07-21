import PySimpleGUI as sg
class Atril:
    
    #dic_de_letras --> diccionario de diccionarios (en formato especifico) EJ. {'A':{'cantidad':4,'valor':1} , 'B':{'cantidad':3,'valor':1}} (las cantidades suman 7)
    def __init__(self,dic_de_letras):    
        
        self.estado = dic_de_letras
        self.letras_disponibles = []
        self.__actualizar_estado_entero()

        for letra in self.estado:
            self.cant_fichas = self.cant_fichas + self.estado[letra]["cantidad"]


    def __actualizar_letra(self,letra):

        if  self.estado[letra]["cantidad"] == 0:
            del self.estado[letra]
        
        else:
            self.letras_disponibles.append(self.estado[letra])


    def __actualizar_estado_entero(self):
        
        for elemento in self.estado:
            self.__actualizar_letra(elemento)


    #======================================================================================================================================


    def getEstado(self):
        return self.estado                                          #EJ. {'A':{'cantidad':2,'valor':1} , 'B':{'cantidad':3,'valor':1}}


    #letra --> string EJ. "A"
    def sacar_ficha(self,letra):
        
        self.estado[letra]["cantidad"] = self.estado[letra]["cantidad"] - 1
        self.cant_fichas = self.cant_fichas - 1
        self.__actualizar_letra(letra)


    #lista_de_letras --> lista EJ. ["L", "C", "L", "K"]
    def sacar_varias_fichas(self, lista_de_letras):
        
        for letra in lista_de_letras:
            self.sacar_ficha(letra)


    #dic_de_ficha --> diccionario de diccionarios   EJ. {'A':{'cantidad':2,'valor':1} , 'G':{'cantidad':1,'valor':1}}
    def agregar_varias_fichas(self,dic_de_fichas):
        
        if dic_de_fichas:                                           #Si el diccionario no está vacio
            for letra in dic_de_fichas:
                self.estado[letra] = dic_de_fichas[letra]

        else:
            #POPUP DE BOLSA VACIA/////////////////////
            sg.popup("ESTE PROCESO NO TIENE QUE SER LLAMADO SI LA BOLSA ESTA VACIA")


        

