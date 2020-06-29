from CLASS_bolsa_andando import Bolsa
import random

FICHAS = {
'A':{'cantidad':11,'valor':1},
'B':{'cantidad':3,'valor':1},
'C':{'cantidad':4,'valor':1},
'D':{'cantidad':4,'valor':1},
'E':{'cantidad':11,'valor':1},
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
'O':{'cantidad':8,'valor':1},
'P':{'cantidad':2,'valor':1},
'Q':{'cantidad':1,'valor':1},
'R':{'cantidad':4,'valor':1},
'RR':{'cantidad':1,'valor':1},
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

print(B.getBolsa())

print("-.,-.,"*25)
print(B.dameFichas(7))
print("-.,-.,"*25)

print(B.getBolsa())


