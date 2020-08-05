from CLASS_atril import Atril
from CLASS_bolsa import Bolsa


FICHAS = {                                  #Es una configuracion que viene desde un archivo
'A':{'cantidad':11,'valor':1},
'B':{'cantidad':3,'valor':1},
'C':{'cantidad':4,'valor':1},
'D':{'cantidad':4,'valor':1},
'E':{'cantidad':11,'valor':6},
'F':{'cantidad':2,'valor':1},
'G':{'cantidad':2,'valor':1},
'H':{'cantidad':2,'valor':1},
'I':{'cantidad':6,'valor':1},
'J':{'cantidad':2,'valor':1},
'K':{'cantidad':1,'valor':1},
'L':{'cantidad':4,'valor':1},
'LL':{'cantidad':1,'valor':1},
'M':{'cantidad':3,'valor':1},
'N':{'cantidad':5,'valor':1},
'Ñ':{'cantidad':1,'valor':1},
'O':{'cantidad':8,'valor':9},
'P':{'cantidad':2,'valor':3},
'Q':{'cantidad':1,'valor':1},
'R':{'cantidad':4,'valor':1},
'RR':{'cantidad':1,'valor':20},
'S':{'cantidad':7,'valor':1},
'T':{'cantidad':4,'valor':1},
'U':{'cantidad':6,'valor':1},
'V':{'cantidad':2,'valor':1},
'W':{'cantidad':1,'valor':1},
'X':{'cantidad':1,'valor':1},
'Y':{'cantidad':1,'valor':1},
'Z':{'cantidad':1,'valor':1}
    }

B = Bolsa(FICHAS)


Atril_computadora = Atril(B.dameFichas(7))                      #El valor inicial viene de un archivo de config o partida guardada(en este caso usamos la bolsa)
Atril_jugador = Atril(B.dameFichas(7))       

#EJ_pc = Atril_computadora.getEstado()                          Veo el estado del atril, 

#lista_de_fichas_a_sacar = ["G", "A", "T", "A"]                 si puedo formar una palabra con (ej) 4 letras ["G", "A", "T", "A"],
#Atril_computadora.sacar_varias_fichas(lista_de_fichas_a_sacar) saco esas fichas del atril.


#Atril_computadora.agregar_varias_fichas(B.dameFichas(len(lista_de_fichas_a_sacar)))  Saco fichas de la bolsa y le doy la cantidad que le falta al atril para completarse 
                                                                                    #(SE HACE DESPUES DE CORROBORAR SI LA BOLSA ESTA VACIA Y DESPUES DE MOSTRAR EL ATRIL INCOMPLETO EN PANTALLA )


#------------------------------------------------------------------------------------------------------------------------
#Para mostrarlo en pantalla


print("-" * 30)
estado = Atril_jugador.getEstado()
print(estado)
print(Atril_jugador.getFichas_disponibles())

estado = {"casa" : 123}

print("-" * 30)
print(Atril_jugador.getEstado())
print(Atril_jugador.getFichas_disponibles())

print("-.,-.,"*20)


#------------------------------------------------------------------------------------------------------------------------
# Molina, Lucio Felipe - 15980/7