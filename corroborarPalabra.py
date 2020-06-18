#Funcion para ordenar la palabra que ingresa
#despues corroborar con pattern y puntuacion

dic = {(8, 7): 'S', (6, 7): 'C', (7, 7): 'A', (9, 7): 'A'}
print(dic)
print(dict(sorted(dic.items(), key = lambda diccio: diccio[0])))