#Facil 19x19 medio(9,9) . Medio 17x17 medio(8,8) . Dificil 15x15 medio(7,7)
from random import randint,randrange
from corroboro.corroborarPalabra import __retorno_informacion
#from Objetos import CLASS_tablero
#from Objetos import CLASS_atril
#from Objetos import CLASS_bolsa

__configuracion = {'A':{'cantidad':11,'valor':1}, 'B':{'cantidad':3,'valor':1}, 'C':{'cantidad':4,'valor':1}, 'D':{'cantidad':4,'valor':1}, 
'E':{'cantidad':11,'valor':2}, 'F':{'cantidad':2,'valor':1}, 'G':{'cantidad':2,'valor':1}, 'H':{'cantidad':2,'valor':1}, 'I':{'cantidad':6,'valor':1}, 
'J':{'cantidad':2,'valor':1}, 'K':{'cantidad':1,'valor':1}, 'L':{'cantidad':4,'valor':1}, 'LL':{'cantidad':1,'valor':1}, 'M':{'cantidad':3,'valor':1}, 
'N':{'cantidad':5,'valor':1}, 'Ñ':{'cantidad':1,'valor':1}, 'O':{'cantidad':8,'valor':2}, 'P':{'cantidad':2,'valor':2}, 'Q':{'cantidad':1,'valor':1}, 
'R':{'cantidad':4,'valor':1}, 'RR':{'cantidad':1,'valor':8}, 'S':{'cantidad':7,'valor':1}, 'T':{'cantidad':4,'valor':1}, 'U':{'cantidad':6,'valor':1},
'V':{'cantidad':2,'valor':1}, 'W':{'cantidad':1,'valor':1}, 'X':{'cantidad':1,'valor':1}, 'Y':{'cantidad':1,'valor':1}, 'Z':{'cantidad':1,'valor':2}}

__tablero = {(0, 0): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": True, "tipo_de_recompensa": "x3"},
            (0, 1): {"letra": "", "trampa": True, "tipo_de_trampa": "-3", "recompensa": False, "tipo_de_recompensa": ""},
            (0, 2): {"letra": "", "trampa": True, "tipo_de_trampa": "-1", "recompensa": False, "tipo_de_recompensa": ""},
            (0, 3): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (0, 4): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (0, 5): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (0, 6): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (0, 7): {"letra": "", "trampa": True, "tipo_de_trampa": "-2", "recompensa": False, "tipo_de_recompensa": ""},
            (0, 8): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (0, 9): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (0, 10): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (0, 11): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (0, 12): {"letra": "", "trampa": True, "tipo_de_trampa": "-1", "recompensa": False, "tipo_de_recompensa": ""},
            (0, 13): {"letra": "", "trampa": True, "tipo_de_trampa": "-3", "recompensa": False, "tipo_de_recompensa": ""},
            (0, 14): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": True, "tipo_de_recompensa": "x3"},
            (1, 0): {"letra": "", "trampa": True, "tipo_de_trampa": "-3", "recompensa": False, "tipo_de_recompensa": ""},
            (1, 1): {"letra": "", "trampa": True, "tipo_de_trampa": "-1", "recompensa": False, "tipo_de_recompensa": ""},
            (1, 2): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (1, 3): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (1, 4): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (1, 5): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (1, 6): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (1, 7): {"letra": "", "trampa": True, "tipo_de_trampa": "-2", "recompensa": False, "tipo_de_recompensa": ""},
            (1, 8): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (1, 9): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (1, 10): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (1, 11): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (1, 12): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (1, 13): {"letra": "", "trampa": True, "tipo_de_trampa": "-1", "recompensa": False, "tipo_de_recompensa": ""},
            (1, 14): {"letra": "", "trampa": True, "tipo_de_trampa": "-3", "recompensa": False, "tipo_de_recompensa": ""},
            (2, 0): {"letra": "", "trampa": True, "tipo_de_trampa": "-1", "recompensa": False, "tipo_de_recompensa": ""},
            (2, 1): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (2, 2): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": True, "tipo_de_recompensa": "x2"},
            (2, 3): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (2, 4): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (2, 5): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (2, 6): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (2, 7): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (2, 8): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (2, 9): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (2, 10): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (2, 11): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (2, 12): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": True, "tipo_de_recompensa": "x2"},
            (2, 13): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (2, 14): {"letra": "", "trampa": True, "tipo_de_trampa": "-1", "recompensa": False, "tipo_de_recompensa": ""},
            (3, 0): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (3, 1): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (3, 2): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (3, 3): {"letra": "", "trampa": True, "tipo_de_trampa": "-3", "recompensa": False, "tipo_de_recompensa": ""},
            (3, 4): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (3, 5): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (3, 6): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (3, 7): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (3, 8): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (3, 9): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (3, 10): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (3, 11): {"letra": "", "trampa": True, "tipo_de_trampa": "-3", "recompensa": False, "tipo_de_recompensa": ""},
            (3, 12): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (3, 13): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (3, 14): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (4, 0): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": True, "tipo_de_recompensa": "x2"},
            (4, 1): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (4, 2): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (4, 3): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (4, 4): {"letra": "", "trampa": True, "tipo_de_trampa": "-2", "recompensa": False, "tipo_de_recompensa": ""},
            (4, 5): {"letra": "", "trampa": True, "tipo_de_trampa": "-1", "recompensa": False, "tipo_de_recompensa": ""},
            (4, 6): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (4, 7): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": True, "tipo_de_recompensa": "x2"},
            (4, 8): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (4, 9): {"letra": "", "trampa": True, "tipo_de_trampa": "-1", "recompensa": False, "tipo_de_recompensa": ""},
            (4, 10): {"letra": "", "trampa": True, "tipo_de_trampa": "-2", "recompensa": False, "tipo_de_recompensa": ""},
            (4, 11): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (4, 12): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (4, 13): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (4, 14): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": True, "tipo_de_recompensa": "x3"},
            (5, 0): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (5, 1): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (5, 2): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (5, 3): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (5, 4): {"letra": "", "trampa": True, "tipo_de_trampa": "-1", "recompensa": False, "tipo_de_recompensa": ""},
            (5, 5): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (5, 6): {"letra": "", "trampa": True, "tipo_de_trampa": "-2", "recompensa": False, "tipo_de_recompensa": ""},
            (5, 7): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (5, 8): {"letra": "", "trampa": True, "tipo_de_trampa": "-2", "recompensa": False, "tipo_de_recompensa": ""},
            (5, 9): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (5, 10): {"letra": "", "trampa": True, "tipo_de_trampa": "-1", "recompensa": False, "tipo_de_recompensa": ""},
            (5, 11): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (5, 12): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (5, 13): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (5, 14): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (6, 0): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (6, 1): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (6, 2): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (6, 3): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (6, 4): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (6, 5): {"letra": "", "trampa": True, "tipo_de_trampa": "-2", "recompensa": False, "tipo_de_recompensa": ""},
            (6, 6): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (6, 7): {"letra": "", "trampa": True, "tipo_de_trampa": "-1", "recompensa": False, "tipo_de_recompensa": ""},
            (6, 8): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (6, 9): {"letra": "", "trampa": True, "tipo_de_trampa": "-2", "recompensa": False, "tipo_de_recompensa": ""},
            (6, 10): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (6, 11): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (6, 12): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (6, 13): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (6, 14): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (7, 0): {"letra": "", "trampa": True, "tipo_de_trampa": "-1", "recompensa": False, "tipo_de_recompensa": ""},
            (7, 1): {"letra": "", "trampa": True, "tipo_de_trampa": "-1", "recompensa": False, "tipo_de_recompensa": ""},
            (7, 2): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (7, 3): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (7, 4): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": True, "tipo_de_recompensa": "x2"},
            (7, 5): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (7, 6): {"letra": "", "trampa": True, "tipo_de_trampa": "-1", "recompensa": False, "tipo_de_recompensa": ""},
            (7, 7): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": True, "tipo_de_recompensa": "x3"},
            (7, 8): {"letra": "", "trampa": True, "tipo_de_trampa": "-1", "recompensa": False, "tipo_de_recompensa": ""},
            (7, 9): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (7, 10): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": True, "tipo_de_recompensa": "x2"},
            (7, 11): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (7, 12): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (7, 13): {"letra": "", "trampa": True, "tipo_de_trampa": "-1", "recompensa": False, "tipo_de_recompensa": ""},
            (7, 14): {"letra": "", "trampa": True, "tipo_de_trampa": "-1", "recompensa": False, "tipo_de_recompensa": ""},
            (8, 0): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (8, 1): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (8, 2): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (8, 3): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (8, 4): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (8, 5): {"letra": "", "trampa": True, "tipo_de_trampa": "-2", "recompensa": False, "tipo_de_recompensa": ""},
            (8, 6): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (8, 7): {"letra": "", "trampa": True, "tipo_de_trampa": "-1", "recompensa": False, "tipo_de_recompensa": ""},
            (8, 8): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (8, 9): {"letra": "", "trampa": True, "tipo_de_trampa": "-2", "recompensa": False, "tipo_de_recompensa": ""},
            (8, 10): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (8, 11): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (8, 12): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (8, 13): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (8, 14): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (9, 0): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""}, 
            (9, 1): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (9, 2): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (9, 3): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (9, 4): {"letra": "", "trampa": True, "tipo_de_trampa": "-1", "recompensa": False, "tipo_de_recompensa": ""},
            (9, 5): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (9, 6): {"letra": "", "trampa": True, "tipo_de_trampa": "-2", "recompensa": False, "tipo_de_recompensa": ""},
            (9, 7): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (9, 8): {"letra": "", "trampa": True, "tipo_de_trampa": "-2", "recompensa": False, "tipo_de_recompensa": ""},
            (9, 9): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (9, 10): {"letra": "", "trampa": True, "tipo_de_trampa": "-1", "recompensa": False, "tipo_de_recompensa": ""},
            (9, 11): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (9, 12): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (9, 13): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (9, 14): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (10, 0): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": True, "tipo_de_recompensa": "x3"},
            (10, 1): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (10, 2): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (10, 3): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (10, 4): {"letra": "", "trampa": True, "tipo_de_trampa": "-2", "recompensa": False, "tipo_de_recompensa": ""},
            (10, 5): {"letra": "", "trampa": True, "tipo_de_trampa": "-1", "recompensa": False, "tipo_de_recompensa": ""},
            (10, 6): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (10, 7): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": True, "tipo_de_recompensa": "x2"},
            (10, 8): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (10, 9): {"letra": "", "trampa": True, "tipo_de_trampa": "-1", "recompensa": False, "tipo_de_recompensa": ""},
            (10, 10): {"letra": "", "trampa": True, "tipo_de_trampa": "-2", "recompensa": False, "tipo_de_recompensa": ""},
            (10, 11): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (10, 12): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (10, 13): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (10, 14): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": True, "tipo_de_recompensa": "x2"},
            (11, 0): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (11, 1): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (11, 2): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (11, 3): {"letra": "", "trampa": True, "tipo_de_trampa": "-3", "recompensa": False, "tipo_de_recompensa": ""},
            (11, 4): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (11, 5): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (11, 6): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (11, 7): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (11, 8): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (11, 9): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (11, 10): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (11, 11): {"letra": "", "trampa": True, "tipo_de_trampa": "-3", "recompensa": False, "tipo_de_recompensa": ""},
            (11, 12): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (11, 13): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (11, 14): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (12, 0): {"letra": "", "trampa": True, "tipo_de_trampa": "-1", "recompensa": False, "tipo_de_recompensa": ""},
            (12, 1): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (12, 2): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": True, "tipo_de_recompensa": "x2"},
            (12, 3): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (12, 4): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (12, 5): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (12, 6): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (12, 7): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (12, 8): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (12, 9): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (12, 10): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (12, 11): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (12, 12): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": True, "tipo_de_recompensa": "x2"},
            (12, 13): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (12, 14): {"letra": "", "trampa": True, "tipo_de_trampa": "-1", "recompensa": False, "tipo_de_recompensa": ""},
            (13, 0): {"letra": "", "trampa": True, "tipo_de_trampa": "-3", "recompensa": False, "tipo_de_recompensa": ""},
            (13, 1): {"letra": "", "trampa": True, "tipo_de_trampa": "-1", "recompensa": False, "tipo_de_recompensa": ""},
            (13, 2): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (13, 3): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (13, 4): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (13, 5): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (13, 6): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (13, 7): {"letra": "", "trampa": True, "tipo_de_trampa": "-2", "recompensa": False, "tipo_de_recompensa": ""},
            (13, 8): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (13, 9): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (13, 10): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (13, 11): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (13, 12): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (13, 13): {"letra": "", "trampa": True, "tipo_de_trampa": "-1", "recompensa": False, "tipo_de_recompensa": ""},
            (13, 14): {"letra": "", "trampa": True, "tipo_de_trampa": "-3", "recompensa": False, "tipo_de_recompensa": ""},
            (14, 0): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": True, "tipo_de_recompensa": "x3"},
            (14, 1): {"letra": "", "trampa": True, "tipo_de_trampa": "-3", "recompensa": False, "tipo_de_recompensa": ""},
            (14, 2): {"letra": "", "trampa": True, "tipo_de_trampa": "-1", "recompensa": False, "tipo_de_recompensa": ""},
            (14, 3): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (14, 4): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (14, 5): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (14, 6): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (14, 7): {"letra": "", "trampa": True, "tipo_de_trampa": "-2", "recompensa": False, "tipo_de_recompensa": ""},
            (14, 8): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (14, 9): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (14, 10): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (14, 11): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": False, "tipo_de_recompensa": ""},
            (14, 12): {"letra": "", "trampa": True, "tipo_de_trampa": "-1", "recompensa": False, "tipo_de_recompensa": ""},
            (14, 13): {"letra": "", "trampa": True, "tipo_de_trampa": "-3", "recompensa": False, "tipo_de_recompensa": ""},
            (14, 14): {"letra": "", "trampa": False, "tipo_de_trampa": "", "recompensa": True, "tipo_de_recompensa": "x3"}}

#Al llamar la jugabilidad, le pasaremos el tablero, el atril de la computadora y la bolsa de fichas

#La dificultad entra al llamar la jugabilidad de la IA
atril = ["O","S","O","S","O","S","O"] #CLASS_atril.Atril.getFichas_disponibles()
#"__tablero = tablero entero"
#"__configuracion = configuracion del scrabble"

#Si el turno es False = empieza el jugador, si es True, empieza la IA, esto se maneja afuera para que si, le toca el primer turno, despues se lo cambia y se pone optimo a jugar
def __dificultad_IA(dificultad):

    #Reviso la dificultad que entra de la configuracion
    #Seteo valores de cantidad de jugadas y los puntos medios de la IA por si empieza a jugar
    if(dificultad==1):
        cant = 5
        medio = (9, 9)
    elif(dificultad==2):
        cant = 10
        medio = (8, 8)
    else:
        cant = 15
        medio = (7, 7)

    return(cant,medio)

#Formo la palabra en base al atril actual de la IA
def __armo_palabra_IA(atril,cantLetras):
    letras=[0,1,2,3,4,5,6]
    
    
    copia_atril = atril[:]
    copia_letras = letras[:]
    
    palabra_armada = []
    
    for i in range(cantLetras):
        
        pos = randint(0,(len(letras)-1))
        
        palabra_armada.append(atril[letras[pos]])
        
        del letras[pos]
        
        del copia_atril[pos]
        
    atril = copia_atril[:]
    letras = copia_letras[:]
    
    return palabra_armada
#----------------------------------------------------------------------------------------------------------------------------------

def __posicion_inicio(dificultad):
    
    if(dificultad==1):
        x = randint(0,18)
        y = randint(0,18)
        pos = (x, y)
    elif(dificultad==2):
        x = randint(0,16)
        y = randint(0,16)
        pos = (x, y)
    else:
        x = randint(0,14)
        y = randint(0,14)
        pos = (x, y)
    
    return pos


#----------------------------------------------------------------------------------------------------------------------------------
#Seteo booleano para ver si: en base a la cantidad de letras, puede insertar la palabra
#Una lista de direcciones que representan, de un punto, avanzar hacia la derecha o izquierda o hacia arriba o abajo
#Creamos una variable d para las direcciones, que iremos revisando 1 por 1 ya que la idea es darle mas oportunidades a la IA
#En que pueda generar una palabra correcta
#Si ok es False, no puede insertar la cantidad de letras que se eligieron para la IA, y se vuelve a hacer todo devuelta
#La idea es que segun la dificultad que se eligio, la IA tenga mas posibilidades
#En facil, tendra 3 oportunidades de crear una palabra en base a la cantidad de letras que se eligieron
#En medio, seran 6 oportunidades
#En dificil, seran 10 oportunidades

#pos es una tupla de posiciones = (x , y)
def __pos_valida_IA(pos,palabra,dificultad,__tablero):
    
    direcciones = ["derecha","abajo"]
    
    posible_sentido = len(direcciones)-1
    
    direFinal = "nada"
    
    if(dificultad==1):
        fin_tablero = 18
    
    elif(dificultad==2):
        fin_tablero = 16
    
    else:
        fin_tablero = 14

    
    for dire in range(len(direcciones)):
        ok = True
        sigo=True
        #esto lo hago 1 vez para ver que direccion tomo, si por X ascendente o descendente o lo mismo pero por Y
        pos_dir = randint(0 , posible_sentido)
        
        #if(direcciones[pos_dir]=="arriba"):
        #    
        #    #me muevo en el eje Y de manera ascendente
        #    for i in range(len(palabra)):
        #        if((pos[0]-i>=0) and sigo ):
        #            if(__tablero[(pos[0]-i,pos[1])]['letra'] != ""):
        #            #if(tablero.getDatosEnCoor((pos[0]-i,pos[1]))['letra'] !=""):
        #                sigo=False
        #        else:
        #            sigo=False
        #            break
        #    if(sigo==True):
        #        direFinal = "arriba"
        #    else:
        #        direFinal = "nada"
        #        ok=False
        if(direcciones[pos_dir]=="derecha"):
            
            #me muevo en el X de manera ascendente
            for i in range(len(palabra)):
                if((pos[1]+i<=fin_tablero) and sigo ):
                    if(__tablero[(pos[0],pos[1]+i)]['letra'] !=""):
                    #if(tablero.getDatosEnCoor((pos[0]+i,pos[1]))['letra'] !=""):
                        sigo=False
                else:
                    sigo = False
                    break
            if(sigo==True):
                direFinal = "derecha"
            else:
                direFinal = "nada"
                ok=False
        
        elif(direcciones[pos_dir]=="abajo"):
            
            #me muevo por el eje Y de manera descendente
            for i in range(len(palabra)):
                if((pos[0]+i<=fin_tablero) and sigo):
                    if(__tablero[(pos[0]+i,pos[1])]['letra'] !=""):
                    #if(tablero.getDatosEnCoor((pos[0],pos[1]-i))['letra'] !=""):
                        sigo=False
                else:
                    sigo=False
                    break
            if(sigo==True):
                direFinal = "abajo"
            else:
                direFinal = "nada"
                ok=False
        
        #elif(direcciones[pos_dir]=="izquierda"):
        #    
        #    #me muevo en el eje X de manera descentende
        #    for i in range(len(palabra)):
        #        if((pos[1]-i>=0) and sigo):
        #            if(__tablero[(pos[0],pos[1]-i)]['letra']!=""):
        #            #if(tablero.getDatosEnCoor((pos[0]-i,pos[1]))['letra'] !=""):
        #                sigo=False
        #        else:
        #            sigo=False
        #            break
        #    if(sigo==True):
        #        direFinal = "izquierda"
        #    else:
        #        direFinal = "nada"
        #        ok=False
        
        if(direFinal!="nada"):
            break
        else:
            direcciones.pop(pos_dir)
            posible_sentido = posible_sentido - 1


    return(ok,direFinal)
#-----------------------------------------------------------------------------------------------------------------------------------

def __armo_estructura_IA(palabra,pos,direccion,__tablero):
    dic_IA = {}
    #if(direccion=="arriba"):
    #    for i in range(len(palabra)):
    #        dic_IA[(pos[0]-i,pos[1])] = __tablero[(pos[0]-i,pos[1])]
    #        dic_IA[(pos[0]-i,pos[1])]['letra']=palabra[i]
    if(direccion=="derecha"):
        for i in range(len(palabra)):
            dic_IA[(pos[0],pos[1]+i)] = __tablero[(pos[0],pos[1]+i)]
            dic_IA[(pos[0],pos[1]+i)]['letra']=palabra[i]
    elif(direccion=="abajo"):
        for i in range(len(palabra)):
            dic_IA[(pos[0]+i,pos[1])] = __tablero[(pos[0]+i,pos[1])]
            dic_IA[(pos[0]+i,pos[1])]['letra']=palabra[i]
    #elif(direccion=="izquierda"):
    #    for i in range(len(palabra)):
    #        dic_IA[(pos[0],pos[1]-i)] = __tablero[(pos[0],pos[1]-i)]
    #        dic_IA[(pos[0],pos[1]-i)]['letra']=palabra[i]
    
    print("diccionario IA TERMINADO")
    print(dic_IA)

    return(dic_IA)

#----------------------------------------------------------------------------------------------------------------------------------

#def __pongo_letras_IA(pos,direccion,palabra):
#    
#    if(direccion==1):
#        for i in range(0,len(palabra),1):
#            __palabra.setValorEnCoor((pos[0],pos[1]+i),palabra[i])
#    elif(direccion==2):
#        for i in range(0,len(palabra),1):
#            __palabra.setValorEnCoor((pos[0]+i,pos[1]),palabra[i])
#    elif(direccion==3):
#        for i in range(0,len(palabra),1):
#            __palabra.setValorEnCoor((pos[0],pos[1]-i),palabra[i])
#    else:
#        for i in range(0,len(palabra),1):
#            __palabra.setValorEnCoor((pos[0]-1,pos[1]),palabra[i])

        
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def __juega_IA(dificultad,__tablero,__atril,__primer_turno):
    cantLetras = randint(2,7)
    if(__primer_turno == True):
        
        #Esto es por si empieza pa IA
        dif = __dificultad_IA(dificultad)
        
        #dif[0] me retorna la cantidad de veces que tendra que armar la palabra
        veces = dif[0]
        
        #dif[1] me retorna si el turno arranca por la IA, la pos del medio del tablero dependiendo la dificultad
        pos = dif[1]

        #armo la palabra en base a la cantidad de letras que se elige, esto le da mas posibilidades de armar palabras cortas o lagras, de la misma cantidad de letras
        palabra = __armo_palabra_IA(__atril, cantLetras)

        #empiezo a preguntar por las posiciones, para armar la estructura que enviare a corroboro palabra
        posiciones = __pos_valida_IA(pos,palabra,dificultad,__tablero)

        #posiciones[0] me retorna si habia lugar para insertar la palabra en 4 direcciones distintas
        pos_ok = posiciones[0]

        #posiciones[1] me retorna la direccion hacia donde encontro el lugar para insertar esta palabra
        direccion = posiciones[1]

        #empezamos a corroborar la palabra armada
        for intento in range(veces):
            
            #armo la jugada de la IA, esto me arma la estructura para enviar toda la informacion hacia corroboro palabra
            jugada_IA = __armo_estructura_IA(palabra,pos,direccion,__tablero)

            #Mando la informacion a corroboro palabra
            sigue = __retorno_informacion(jugada_IA,__configuracion,dificultad)

            #sigue[0] me retorna un booleano de si pudo o no corroborar toda la info
            ok = sigue[0]

            #sigue[1] me retorna el puntaje obtenido por la palabra enviada
            puntaje = sigue[1]

            #Si el booleano que me retorna sigue, es True, envio el puntaje obtenido y corto el for
            if(ok==True):
                print(puntaje)
                return(puntaje)

            else:
                palabra = __armo_palabra_IA(__atril,cantLetras)
                if(intento == veces):
                    print(puntaje)
                    return(puntaje)
    
    else:

        #Esto es por si empieza pa IA
        dif = __dificultad_IA(dificultad)
        
        #dif[0] me retorna la cantidad de veces que tendra que armar la palabra
        veces = dif[0]
        
        #armo la palabra en base a la cantidad de letras que se elige, esto le da mas posibilidades de armar palabras cortas o lagras, de la misma cantidad de letras
        palabra = __armo_palabra_IA(__atril, cantLetras)

        pos_valida = False
        #empezamos a corroborar la palabra armada

        while(pos_valida == False):
                #Obtengo una pos de inicio de manera aleatoria
                pos = __posicion_inicio(dificultad)

                #empiezo a preguntar por las posiciones, para armar la estructura que enviare a corroboro palabra
                posiciones = __pos_valida_IA(pos,palabra,dificultad,__tablero)

                #posiciones[0] me retorna si habia lugar para insertar la palabra en 4 direcciones distintas
                pos_ok = posiciones[0]

                print("possssss")
                print(pos)


                if(pos_ok == True):
                    pos_valida = True
                    
                    #posiciones[1] me retorna la direccion hacia donde encontro el lugar para insertar esta palabra
                    direccion = posiciones[1]
                    print("direccion")
                    print(direccion)

        for intento in range(veces):
                   
            #armo la jugada de la IA, esto me arma la estructura para enviar toda la informacion hacia corroboro palabra
            jugada_IA = __armo_estructura_IA(palabra,pos,direccion,__tablero)

            #Mando la informacion a corroboro palabra
            sigue = __retorno_informacion(jugada_IA,__configuracion,dificultad)

            #sigue[0] me retorna un booleano de si pudo o no corroborar toda la info
            ok = sigue[0]

            #sigue[1] me retorna el puntaje obtenido por la palabra enviada
            puntaje = sigue[1]

            #Si el booleano que me retorna sigue, es True, envio el puntaje obtenido y corto el for
            if(ok==True):
                print(puntaje)
                return(puntaje)

            else:
                palabra = __armo_palabra_IA(__atril,cantLetras)
                if(intento == veces):
                    print(puntaje)
                    return(puntaje)


jugada = __juega_IA(3,__tablero,atril,False)

print(jugada)

#diccionario 