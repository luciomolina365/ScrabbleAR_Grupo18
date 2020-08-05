import copy


class Tablero:
    __estado={}

    #ancho y alto --> int 
    #estado_a_cargar --> diccionario de diccionarios  EJ. #{*tupla de int*: {"letra": *string* , "trampa": *boolean*, "tipo_de_trampa": *int o None*, "recompensa": *boolean*, "tipo_de_recompensa": *int o None*} , *tupla de int*: {"letra": ...}}
    def __init__(self, estado_a_cargar):
        self.__estado = estado_a_cargar
    

    def getEstado(self):
        """Retorna una copia del estado del tablero en el momento que es llamado este metodo."""
        dic = copy.deepcopy(self.__estado)                      #Devuelve un diccionario de diccionarios (que representa el tablero) del formato:                       
        return dic                                              #{*tupla de int*: {"letra": *string* , "trampa": *boolean*, "tipo_de_trampa": *int o None*, "recompensa": *boolean*, "tipo_de_recompensa": *int o None*} , *tupla de int*: {"letra": ...}}                                     
                                           
        
    #====================================================================================================================
    #GETTERS
    #coordenada --> tupla de int , EJ. (1,2)
    
    def getDatosEnCoor(self, coordenada):
        """Recibe una tupla de interos(coordenada) y retorna un diccionario con los datos en la coordenada."""
        dic = copy.deepcopy(self.__estado[coordenada])                                 
        return dic                       #EJ. {"letra": *string* , "trampa": *boolean*, "tipo_de_trampa": *int o None*, "recompensa": *boolean*, "tipo_de_recompensa": *int o None*}
    

    #====================================================================================================================
    #SETTERS
    
    #coordenada --> tupla de int , EJ. (1,2)
    #valor --> string , EJ. "A"

    def setValorEnCoor(self, coordenada, letra):
        """Recibe una tupla de interos(coordenada) y un string(letra), y pone el la letra ingresada en la coordenada ingresada."""
        self.__estado[coordenada]["letra"] = letra


    #====================================================================================================================




#------------------------------------------------------------------------------------------------------------------------
# Molina, Lucio Felipe - 15980/7    