from CLASS_atril_andando import Atril
from CLASS_bolsa_andando import Bolsa


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


Atril_computadora = Atril(B.dameFichas(7))                      #Hay que darle un valor inicial pero este caso de testeo no pasa nada
Atril_jugador = Atril(B.dameFichas(7))       

#EJ_pc = Atril_computadora.getEstado()                          Veo el estado del atril, 

#lista_de_fichas_a_sacar = ["G", "A", "T", "A"]                 si puedo formar una palabra con (ej) 4 letras ["G", "A", "T", "A"],
#Atril_computadora.sacar_varias_fichas(lista_de_fichas_a_sacar) saco esas fichas del atril.


#Atril_computadora.agregar_varias_fichas(B.dameFichas(len(lista_de_fichas_a_sacar)))  Saco fichas de la bolsa y le doy la cantidad que le falta al atril para completarse 
                                                                                    #(SE HACE DESPUES DE CORROBORAR SI LA BOLSA ESTA VACIA Y DESPUES DE MOSTRAR EL ATRIL INCOMPLETO EN PANTALLA )


#------------------------------------------------------------------------------------------------------------------------
#Para mostrarlo en pantalla

DIC_J = Atril_jugador.getEstado()

LISTA_j = []
for elemento in DIC_J:                      #Hace una lista con las letras y sus repetidas (el proceso ".getLetras_disponibles()" lo hace)
    cant = DIC_J[elemento]["cantidad"]
    for i in range(cant):
        LISTA_j.append(elemento)



print(DIC_J)
print("-" * 30)
print(Atril_jugador.getLetras_disponibles())
print(LISTA_j)
print("-.,-.,"*20)


#------------------------------------------------------------------------------------------------------------------------
#Molina, Lucio Felipe - 15980/7