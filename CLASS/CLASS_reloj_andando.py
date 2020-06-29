class Reloj:
    
    #min y seg --> int
    #TERMINO --> boolean
    
    def __init__(self, min, seg, TERMINO=False):
        self.min = min
        self.seg = seg
        self.TERMINO = TERMINO
        self.aux_min = ""
        self.aux_seg = ""



    #cantActualizaciones --> int
    def temporizar(self,cantActualizaciones):
        
        """Cada 100 actualizaciones de los valores de la ventana, 
        decrementa el tiempo ingresado y lo devuelve formateado 
        para mostrarlo en pantalla"""

        if cantActualizaciones == 100:
            
            min = self.min                          #Auxiliares del estado del objeto
            seg = self.seg
            aux_min = self.aux_min
            aux_seg = self.aux_seg
            TERMINO = self.TERMINO

            
            aux_min = min                           #Uso los valores, achico el tiempo y lo formateo para mostrarlo en pantalla
            aux_seg = seg    

            if seg == 0:
                seg = 60
                aux_min= min
                min = min - 1
            
            if seg == 60:
                aux_seg= "00"
            
            elif seg == 59:
                aux_min = min 

            elif seg < 10:
                aux_seg = "0" + str(seg)
            
            else:    
                aux_seg = seg

            if  aux_min == 0 and aux_seg == "00":
                TERMINO=True

            seg = seg - 1

            self.min = min                          #Actualizo el estado del objeto
            self.seg = seg
            self.aux_min = aux_min
            self.aux_seg = aux_seg
            self.TERMINO = TERMINO

            cantActualizaciones = 0                 #Reinicio el contador
            return cantActualizaciones              #int
        else:

            return cantActualizaciones              #Retorno el contador como estaba (int)
        


    #====================================================================================================================
    #GETTERS
    
    def getMinutos(self):
        return self.aux_min                         #int

    def getSegundos(self):
        return self.aux_seg                         #int

    def getTERMINO(self):
        return self.TERMINO                         #boolean

    #====================================================================================================================




