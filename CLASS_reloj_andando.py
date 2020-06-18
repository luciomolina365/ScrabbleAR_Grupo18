import PySimpleGUI as sg
from random import randint
        
class Reloj:
    
    def __init__(self, min, seg, TERMINO=False):
        self.min = min
        self.seg = seg
        self.TERMINO = TERMINO
        self.aux_min = ""
        self.aux_seg = ""

    def temporizar(self,cantActualizaciones):
        
        if cantActualizaciones == 100:
            
            min = self.min         #Auxiliares del estado del objeto
            seg = self.seg
            aux_min = self.aux_min
            aux_seg = self.aux_seg
            TERMINO = self.TERMINO
            
            
            
            aux_min = min          #Uso los valores y achico el tiempo
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

            self.min = min              #Actualizo el estado del objeto
            self.seg = seg
            self.aux_min = aux_min
            self.aux_seg = aux_seg
            self.TERMINO = TERMINO

            cantActualizaciones = 0     #Reinicio el contador
            return cantActualizaciones
        else:

            return cantActualizaciones  #Retorno el contador como estaba
        

    
    def getMinutos(self):
        return self.aux_min

    def getSegundos(self):
        return self.aux_seg

    def getTERMINO(self):
        return self.TERMINO





