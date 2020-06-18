#Armado en base a la entrada de una palabra

def puntuarJugador(palabra):
    puntuacionParcial=0
    palabra = palabra.upper()
    conjunto1=["A","E","O","S","I","U","N","T","L","R"]
    conjunto2=["C","D","G"]
    conjunto3=["M","B","P"]
    conjunto4=["F","H","V","Y"]
    conjunto6=["J"]
    conjunto8=["K","LL","Ñ","Q","RR","W","X"]
    conjunto10=["Z"]
    indice = 0
    while indice < len(palabra):
        caracter = palabra[indice]
        if((palabra[indice]=="L" and palabra[indice+1]=="L")or(palabra[indice]=="R" and palabra[indice+1]=="R")):
            puntuacionParcial=puntuacionParcial+8 #valorConjunto8
            indice=indice+1
        elif(caracter in conjunto1):
            puntuacionParcial = puntuacionParcial+1 #valorConjunto1
        elif(caracter in conjunto2):
            puntuacionParcial = puntuacionParcial+2 #valorConjunto2
        elif(caracter in conjunto3):
            puntuacionParcial = puntuacionParcial+3 #valorConjunto3
        elif(caracter in conjunto4):
            puntuacionParcial = puntuacionParcial+4 #valorConjunto4
        elif(caracter in conjunto6):
            puntuacionParcial = puntuacionParcial+6 #valorConjunto6
        elif(caracter in conjunto8):
            puntuacionParcial = puntuacionParcial+8 #valorConjunto8
        elif(caracter in conjunto10):
            puntuacionParcial = puntuacionParcial+10 #valorConjunto10
        indice = indice+1
    return puntuacionParcial

palabra = "ZoRrO"
print("El valor de esta palabra es: "+str(puntuarJugador(palabra))+".")