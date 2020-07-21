from CLASS_atril_andando import Atril
from CLASS_bolsa_andando import Bolsa


FICHAS = {
'A':{'cantidad':1,'valor':1},
'B':{'cantidad':1,'valor':1},
'C':{'cantidad':1,'valor':1},
'D':{'cantidad':1,'valor':1},
'E':{'cantidad':1,'valor':1},
'F':{'cantidad':1,'valor':1},
'G':{'cantidad':1,'valor':1},
'H':{'cantidad':1,'valor':1},
'I':{'cantidad':1,'valor':1},
'J':{'cantidad':1,'valor':1},
'K':{'cantidad':1,'valor':1},
'L':{'cantidad':1,'valor':1},
'LL':{'cantidad':1,'valor':1},
'M':{'cantidad':1,'valor':1},
'N':{'cantidad':1,'valor':1},
'Ñ':{'cantidad':1,'valor':1},
'O':{'cantidad':1,'valor':1},
'P':{'cantidad':1,'valor':1},
'Q':{'cantidad':1,'valor':1},
'R':{'cantidad':1,'valor':1},
'RR':{'cantidad':1,'valor':1},
'S':{'cantidad':1,'valor':1},
'T':{'cantidad':1,'valor':1},
'U':{'cantidad':1,'valor':1},
'V':{'cantidad':1,'valor':1},
'W':{'cantidad':1,'valor':1},
'X':{'cantidad':1,'valor':1},
'Y':{'cantidad':1,'valor':1},
'Z':{'cantidad':1,'valor':1}
}

B = Bolsa(FICHAS)

Atril_computadora = Atril({})
Atril_jugador = Atril({})

Atril_computadora.agregar_varias_fichas(B.dameFichas(7))

Atril_jugador.agregar_varias_fichas(B.dameFichas(7))

DIC_J = Atril_jugador.getEstado()

LISTA_j = []
for elemento in DIC_J:
    LISTA_j.append(elemento)


print(DIC_J)
print("-" * 30)
print(LISTA_j)