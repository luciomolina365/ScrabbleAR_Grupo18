from random import randint,randrange
import pattern.text.es as pattern

abecedario="A,A,A,A,A,A,A,A,A,A,A,B,B,B,C,C,C,C,D,D,D,D,E,E,E,E,E,E,E,E,E,E,E,F,F,G,G,H,H,I,I,I,I,I,I,J,J,K,L,L,L,L,LL,M,M,M,N,N,N,N,N,Ñ,O,O,O,O,O,O,O,O,P,P,Q,R,R,R,R,RR,S,S,S,S,S,S,S,T,T,T,T,U,U,U,U,U,U,V,V,W,X,Y,Z"
abecedario=abecedario.split(",")

cantLetas = randint(2,7)

letras=[]
for i in range(1,8):
     a=randrange(1,len(abecedario))
     letras.append(abecedario[a])

print(letras)
letrasCopia = letras
palabra = []
x=7
print("letras "+str(cantLetas))
for i in range(cantLetas):
    pos=(randint(1,x)-1)
    print("pos "+ str(pos))
    palabra.append(letrasCopia[pos])
    print(palabra)
    letrasCopia.remove(letrasCopia[pos])
    print(letrasCopia)
    x = x-1

dir(pattern)

c = 0
for x in pattern.lexicon.keys():
    if x in pattern.spelling.keys():
        print(x, end=', ')
        c += 1

print('Cantidad de palabras en lexicon que no estan en spelling: ',c)