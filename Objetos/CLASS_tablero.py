class Tablero:
    __estado={}

    #ancho y alto --> int 
    #estado_a_cargar --> diccionario de diccionarios  EJ. #{*tupla de int*: {"letra": *string* , "trampa": *boolean*, "tipo_de_trampa": *int o None*, "recompensa": *boolean*, "tipo_de_recompensa": *int o None*} , *tupla de int*: {"letra": ...}}
    def __init__(self, estado_a_cargar):
        self.__estado = estado_a_cargar
    

    def getEstado(self):                                        #Devuelve un diccionario de diccionarios (que representa el tablero) del formato: 
        return self.__estado                                    #{*tupla de int*: {"letra": *string* , "trampa": *boolean*, "tipo_de_trampa": *int o None*, "recompensa": *boolean*, "tipo_de_recompensa": *int o None*} , *tupla de int*: {"letra": ...}}
        
    #====================================================================================================================
    #GETTERS
    #coordenada --> tupla de int , EJ. (1,2)
    
    def getDatosEnCoor(self, coordenada):                           
        return self.__estado[coordenada]                        #EJ. {"letra": *string* , "trampa": *boolean*, "tipo_de_trampa": *int o None*, "recompensa": *boolean*, "tipo_de_recompensa": *int o None*}
    

    #====================================================================================================================
    #SETTERS
    
    #coordenada --> tupla de int , EJ. (1,2)
    #valor --> string , EJ. "A"

    def setValorEnCoor(self, coordenada, letra):
        self.__estado[coordenada]["letra"] = letra


    #====================================================================================================================




#------------------------------------------------------------------------------------------------------------------------
#Molina, Lucio Felipe - 15980/7    