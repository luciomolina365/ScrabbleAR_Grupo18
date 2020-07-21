class Tablero:
    estado={}

    #ancho y alto --> int 

    def __init__(self,ancho,alto, estado_a_cargar):
        
        self.estado = estado_a_cargar
    

    def getEstado(self):                                        #Devuelve un diccionario de diccionarios (que representa el tablero) del formato: 
        return self.estado                                      #{*tupla de int*: {"valor": *string* , "trampa": *boolean*, "tipo_de_trampa": *int o None*, "recompensa": *boolean*, "tipo_de_recompensa": *int o None*} , *tupla de int*: {"valor": ...}}
        
    #====================================================================================================================
    #GETTERS
    #coordenada --> tupla de int , EJ. (1,2)
    
    def getDatosEnCoor(self, coordenada):
        return self.estado[coordenada]                          #EJ. {"valor": *string* , "trampa": *boolean*, "tipo_de_trampa": *int o None*, "recompensa": *boolean*, "tipo_de_recompensa": *int o None*}
    

    #====================================================================================================================
    #SETTERS
    
    #coordenada --> tupla de int , EJ. (1,2)
    #valor --> string , EJ. "A"

    def setValorEnCoor(self, coordenada, valor):
        self.estado[coordenada]["valor"] = valor


    #====================================================================================================================





    