from CLASS_tablero import Tablero

alto = 3
ancho = 3
T = Tablero(alto,ancho)

print(T.getEstado())

T.setDatosEnCoor((0,0) , 666, True)

T.setDoblePuntuacionEnCoor( (2,1) , True )

print("--"*70)

print(T.getDatosEnCoor( (2,1) ))


#print(T.getEstado())


