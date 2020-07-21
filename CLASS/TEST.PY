from CLASS_atril_andando import Atril
from CLASS_bolsa_andando import Bolsa


FICHAS = {
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

Atril_computadora = Atril({})               #Hay que darle un valor inicial pero este caso de testeo no pasa nada
Atril_jugador = Atril({})       

Atril_computadora.agregar_varias_fichas(B.dameFichas(7))

Atril_jugador.agregar_varias_fichas(B.dameFichas(7))

DIC_J = Atril_jugador.getEstado()

LISTA_j = []
for elemento in DIC_J:                      #Hace una lista con las letras y sus repetidas
    cant = DIC_J[elemento]["cantidad"]
    for i in range(cant):
        LISTA_j.append(elemento)

print(DIC_J)
print("-" * 30)
print(LISTA_j)
print("-.,-.,"*20)