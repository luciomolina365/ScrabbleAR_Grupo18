from CLASS_tablero_andando import Tablero


#estado_a_cargar = {*tupla de int*: {"letra": *string* , "trampa": *boolean*, "tipo_de_trampa": *int o None*, "recompensa": *boolean*, "tipo_de_recompensa": *int o None*} , *tupla de int*: {"letra": ...}}
estado_a_cargar = {}
for x in range(16):
    for y in range(16):
        estado_a_cargar[(x,y)] = {"letra": "A" , "trampa": False, "tipo_de_trampa": None, "recompensa": True, "tipo_de_recompensa": 3}

print(estado_a_cargar)

T = Tablero(estado_a_cargar)

T.setValorEnCoor((15,15) , "GGG")           #Cuando esta corroborada la palabra, agregas de a un valor    

print("-.,-.,"*20)
print(T.getEstado())
print("-.,-.,"*20)
print(T.getDatosEnCoor((15,15)))
