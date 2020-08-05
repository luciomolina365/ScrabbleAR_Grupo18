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

print("_______"*20)
Atril_computadora = Atril(B.dameFichas(7))                      #El valor inicial viene de un archivo de config o partida guardada(en este caso usamos la bolsa)
Atril_jugador = Atril(B.dameFichas(7))       


def test(lista):
    lista["A"]["cantidad"] = "YO NO DEBERIA ESTAR ACA"

print(Atril_computadora.getEstado())

test(Atril_computadora.getEstado())

print(Atril_computadora.getEstado())

EJ_pc = Atril_computadora.getEstado()
#print(EJ_pc)                                                    #PRIMER ESTADO
print("_______"*20)                          





#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
lista_de_fichas_a_sacar = []                                    #Apartir de estado genero lista de letras random a sacar
for elemento in EJ_pc:                                          #En este caso saco las letras que aparecen 2 veces
    if EJ_pc[elemento]["cantidad"] == 2:
        lista_de_fichas_a_sacar.append(elemento)
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////





print(f"letras a sacar {lista_de_fichas_a_sacar}")
print("_______"*20)

Atril_computadora.sacar_varias_fichas(lista_de_fichas_a_sacar) 

print(Atril_computadora.getEstado())                            #SEGUNDO ESTADO (SACANDO VARIAS FICHAS)
print("_______"*20)

Atril_computadora.agregar_varias_fichas({'A':{'cantidad':5,'valor':1} , 'G':{'cantidad':1,'valor':1}, "B":{'cantidad':1,'valor':1}})

lista=["A","B","G","G"]
Atril_computadora.sacar_varias_fichas(lista) 

print(Atril_computadora.getEstado())                            #TERCER ESTADO (AGREGANDO VARIAS FICHAS)





#------------------------------------------------------------------------------------------------------------------------
# Molina, Lucio Felipe - 15980/7