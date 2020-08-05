from CLASS_tablero import Tablero


#estado_a_cargar = {*tupla de int*: {"letra": *string* , "trampa": *boolean*, "tipo_de_trampa": *int o None*, "recompensa": *boolean*, "tipo_de_recompensa": *int o None*} , *tupla de int*: {"letra": ...}}
estado_a_cargar = {}
for x in range(16):
    for y in range(16):
        estado_a_cargar[(x,y)] = {"letra": None , "trampa": False, "tipo_de_trampa": None, "recompensa": False, "tipo_de_recompensa": None}

print(estado_a_cargar)


T = Tablero(estado_a_cargar)

T.setValorEnCoor((15,15) , "GGG")           #Cuando esta corroborada la palabra, agregas de a un valor    

def test(dic):
    dic[(0,0)] = "YO NO DEBERIA ESTAR ACA"
# print("-.,-.,"*20)
# print(T.getEstado())
# print("-.,-.,"*20)
print(T.getDatosEnCoor((15,15)))
print("-.,-.,"*20)
print(T.getEstado())
print("-.,-.,"*20)

test(T.getEstado())

print("-.,-.,"*20)
print(T.getEstado())
print("-.,-.,"*20)










#------------------------------------------------------------------------------------------------------------------------
# Molina, Lucio Felipe - 15980/7