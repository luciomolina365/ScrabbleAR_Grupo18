import PySimpleGUI as sg
from random import randint
        
class Reloj:
    
    def __init__(self, min, seg, TERMINO=False):
        self.min = min
        self.seg = seg
        self.TERMINO = TERMINO
        self.aux_min = ""
        self.aux_seg = ""

    def temporizar(self):
        self.aux_min = self.min
        self.aux_seg = self.seg    

        if self.seg == 0:
            self.seg = 60
            self.aux_min= self.min
            self.min = self.min - 1
        
        if self.seg == 60:
            self.aux_seg= "00"
        
        elif self.seg == 59:
            self.aux_min = self.min 

        elif self.seg < 10:
            self.aux_seg = "0" + str(self.seg)
        
        else:    
            self.aux_seg = self.seg

        if  self.aux_min == 0 and self.aux_seg == "00":
            self.TERMINO=True

        self.seg = self.seg - 1

    
    def getMinutos(self):
        return self.aux_min

    def getSegundos(self):
        return self.aux_seg

    def getTERMINO(self):
        return self.TERMINO

#==========================================================================================================


sg.theme('Dark Blue 3')

layout = [  [sg.Text('Tiempo'), sg.T(' '*1), sg.Text(size=(8,1), key='-TEMP OUT-')],
            [sg.Button('Quit')]  ]

window = sg.Window('Reloj', layout, font='Default -24', return_keyboard_events=True, no_titlebar=True)

seg = 15
min = 1
TERMINO = False

R = Reloj(min,seg,TERMINO)

while not R.getTERMINO() :             # Event Loop
    event, values = window.read(timeout=1000)    # returns every 500 ms
    print(event, values) if event != sg.TIMEOUT_KEY else None       # a debug print
   
    if event in (sg.WIN_CLOSED, 'Quit'):
        break

    
    R.temporizar()

    window['-TEMP OUT-'].update(str(R.getMinutos()) + ":"+ str(R.getSegundos()) + ' C')

window.close()