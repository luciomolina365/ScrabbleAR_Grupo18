from CLASS_bolsa_andando import Bolsa
import random

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

print(B.getBolsa())

print("-.,-.,"*25)
print(B.dameFichas(28))
print("-.,-.,"*25)

print(B.getBolsa())

print("-.,-.,"*25)
print(B.dameFichas(2))   #NO HAY SUFICIENTES FICHAS
print("-.,-.,"*25)

print(B.getBolsa())