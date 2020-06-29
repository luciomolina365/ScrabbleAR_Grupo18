from CLASS_tablero_andando import Tablero

alto = 3
ancho = 3
T = Tablero(alto,ancho)

print(T.getEstado())

T.setDatosEnCoor((0,0) , "K", True)

T.setDoblePuntuacionEnCoor( (2,1) , True )

print("--"*70)

print(T.getDatosEnCoor( (0,0) ))


#print(T.getEstado())


