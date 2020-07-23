import json

def obtenerConfig(cargarPartida = False , numero_de_dificultad = 0):

    AUX = {"Tablero": {(0, 0): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (0, 1): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (0, 2): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (0, 3): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (0, 4): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (0, 5): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (0, 6): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (0, 7): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (0, 8): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (0, 9): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (0, 10): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (0, 11): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (0, 12): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (0, 13): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (0, 14): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (0, 15): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (1, 0): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (1, 1): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (1, 2): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (1, 3): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (1, 4): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (1, 5): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (1, 6): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (1, 7): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (1, 8): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (1, 9): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (1, 10): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (1, 11): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (1, 12): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (1, 13): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (1, 14): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (1, 15): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (2, 0): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (2, 1): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (2, 2): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (2, 3): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (2, 4): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (2, 5): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (2, 6): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (2, 7): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (2, 8): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (2, 9): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (2, 10): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (2, 11): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (2, 12): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (2, 13): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (2, 14): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (2, 15): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (3, 0): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 
'tipo_de_recompensa': None}, (3, 1): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (3, 2): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (3, 3): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (3, 4): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (3, 5): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (3, 6): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (3, 7): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (3, 8): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (3, 9): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (3, 10): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (3, 11): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (3, 12): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (3, 13): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (3, 14): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (3, 15): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (4, 0): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (4, 1): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (4, 2): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (4, 3): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (4, 4): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (4, 5): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (4, 6): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (4, 7): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (4, 8): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (4, 9): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (4, 10): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (4, 11): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (4, 12): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (4, 13): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (4, 14): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (4, 15): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (5, 0): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (5, 1): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (5, 2): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (5, 3): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (5, 4): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (5, 5): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (5, 6): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (5, 7): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (5, 8): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (5, 9): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (5, 10): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (5, 11): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (5, 12): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (5, 13): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (5, 14): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (5, 15): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (6, 0): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (6, 1): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (6, 2): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (6, 3): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (6, 4): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (6, 5): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (6, 6): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (6, 7): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (6, 8): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (6, 9): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (6, 10): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (6, 11): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (6, 12): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (6, 13): {'letra': None, 
'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (6, 14): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (6, 15): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (7, 0): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (7, 1): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (7, 2): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (7, 3): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (7, 4): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (7, 5): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (7, 6): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (7, 7): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (7, 8): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (7, 9): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (7, 10): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (7, 11): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (7, 12): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (7, 13): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (7, 14): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (7, 15): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (8, 0): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (8, 1): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (8, 2): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (8, 3): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (8, 4): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (8, 5): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (8, 6): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (8, 7): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (8, 8): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (8, 9): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (8, 10): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (8, 11): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (8, 12): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (8, 13): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (8, 14): {'letra': None, 'trampa': False, 
'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (8, 15): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (9, 0): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (9, 1): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (9, 2): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (9, 3): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (9, 4): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (9, 5): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (9, 6): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (9, 7): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (9, 8): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (9, 9): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (9, 10): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (9, 11): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (9, 12): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (9, 13): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (9, 14): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (9, 15): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (10, 0): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (10, 1): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (10, 2): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (10, 3): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (10, 4): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (10, 5): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (10, 6): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (10, 7): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (10, 8): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (10, 9): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (10, 10): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (10, 11): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (10, 12): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (10, 13): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (10, 14): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (10, 15): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (11, 0): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (11, 1): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (11, 2): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (11, 3): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (11, 4): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (11, 5): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (11, 6): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (11, 7): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (11, 8): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (11, 9): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (11, 10): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, 
(11, 11): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (11, 12): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (11, 13): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (11, 14): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (11, 15): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (12, 0): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (12, 1): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (12, 2): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (12, 3): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (12, 4): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (12, 5): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (12, 6): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (12, 7): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (12, 8): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (12, 9): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (12, 10): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (12, 11): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (12, 12): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (12, 13): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (12, 14): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (12, 15): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (13, 0): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (13, 1): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (13, 2): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (13, 3): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (13, 4): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (13, 5): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (13, 6): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (13, 7): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, 
(13, 8): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (13, 9): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': 
None}, (13, 10): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (13, 11): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (13, 12): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (13, 13): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (13, 14): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (13, 15): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (14, 0): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (14, 1): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (14, 2): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (14, 3): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (14, 4): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (14, 5): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (14, 6): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (14, 7): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (14, 8): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (14, 9): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (14, 10): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (14, 11): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (14, 12): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (14, 13): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (14, 14): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (14, 15): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (15, 0): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (15, 1): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (15, 2): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (15, 3): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (15, 4): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (15, 5): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (15, 6): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (15, 7): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (15, 8): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (15, 9): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (15, 10): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (15, 11): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (15, 12): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (15, 13): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (15, 14): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}, (15, 15): {'letra': None, 'trampa': False, 'tipo_de_trampa': None, 'recompensa': False, 'tipo_de_recompensa': None}}   ,  
"Bolsa": {
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
    }   , 
"Temporizador": {"minutos": 0 , "segundos": 0}  ,  
"Atril_jugador": {}   ,   
"Atril_computadora": {}   ,   
"Puntaje_jugador": 0  ,  
"Puntaje_computadora": 0   ,
"Finalizada": False
}    







    if cargarPartida and numero_de_dificultad == 0:
        with open("partidas\partida_guardada.json", 'r') as archivo:
            datos = json.load(archivo)
            datos = convertir_Json_A_Datos(datos)

        return datos
    elif numero_de_dificultad == 1:

        try:
            with open("configuracion\por_defecto_TEST.json", 'r') as archivo:
                datos = json.load(archivo)
            return datos    
        except FileNotFoundError:
            with open("configuracion\por_defecto_TEST.json", 'w') as archivo:
                
                datos = convertir_Datos_A_Json(AUX)

                json.dump(datos,archivo)

                

            return datos
        
    
def convertir_Datos_A_Json(datos):
    aux = {}
    for coor in datos["Tablero"]:
        aux[str(coor)] = datos["Tablero"][coor]
    
    datos["Tablero"] = aux
    return datos
    

def convertir_Json_A_Datos(datos):
    aux = {}
    x = 0
    y = 0
    for coor in datos["Tablero"]:
        aux_coor = coor
        y = y + 1
        #print(type(coor))
        coor = tuple(coor)
        print("coordenada que entra con el for")
        print(coor)
        
        if(x <11 and y < 11):
            coor = (  int(coor[1])  , int(coor[4])  )
            print("coordenada que x e y menor a 10")
            print(coor)
        
        elif( x < 11 and ( y>=11 and y<=16)):
            y1=coor[4]
            y2=coor[5]
            coorY=y1+y2
            coorY=int(coorY)
            
            coor = (  int(coor[1])  , coorY )
            print("coordenada que x menor a 10 e y mayor a 9")
            print(coor)
            if(y==16):
                y = 0
                x = x + 1
            #print("aca entra cuando y se va a la bosta")

        elif( ( x >= 11 and x <= 16 ) and y < 11):
            print("entro x mayor a 10")
            x1=coor[1]
            x2=coor[2]
            coorX=x1+x2
            coorX=int(coorX)
            
            coor = (  coorX  , int(coor[5]))
            print("coordenada que x mayor a 9 e y menor a 10")
            print(coor)

        elif(( x >= 11 and x <= 16) and ( y >= 11 and y <= 16 )):
            x1=coor[1]
            x2=coor[2]
            coorX=x1+x2
            coorX=int(coorX)
            
            y1=coor[5]
            y2=coor[6]
            coorY=y1+y2
            coorY=int(coorY)
            if(y==16):
                y = 0
            coor = ( coorX  , coorY )
            print("coordenada que x mayor a 9 e y mayor a 9")
            print(coor)
        print('X')
        print(x)
        print('Y')
        print(y)
        aux[coor] = datos["Tablero"][aux_coor]
    
    datos["Tablero"] = aux
    return datos





datos = obtenerConfig(True)

print(datos)

#print(type(str((1,2))))
#print("-.,-.,-.,-.,-.,-,.")
#print(tuple("(1,2)"))





def cambiarConfiguracion():
    pass 