
from Archivos.metodos_de_archivos  import cargarPartida
from Archivos.metodos_de_archivos  import guardar_partida
from Objetos.CLASS_bolsa import Bolsa
from Objetos.CLASS_tablero import Tablero
from Objetos.CLASS_temporizador import Temporizador
from Objetos.CLASS_atril import Atril



def instanciar_objetos(Bol , Table , Temp , Atril_jugador , Atril_computadora , config):
    Bol = Bolsa(config["Bolsa"])
    Table = Tablero(config["Tablero"])
    Temp = Temporizador(int(config["Temporizador"]["minutos"]) , int(config["Temporizador"]["segundos"]))
    Atril_jugador = Atril(config["Atril_jugador"])
    Atril_computadora = Atril(config["Atril_computadora"])

    return {"Bolsa":Bol, "Tablero":Table, "Temporizador":Temp, "Atril_jugador":Atril_jugador, "Atril_computadora":Atril_computadora}


#=============================================================

# Bol = Bolsa
# Table = Tablero
# Temp = Temporizador
# Atril_computadora = Atril
# Atril_jugador =  Atril

# config = cargarPartida("Archivos\\partidas\\partida_guardada_1.json")
# print(config)

# OBJETOS = instanciar_objetos(Bol,Table,Temp,Atril_computadora,Atril_jugador,config)

# guardar_partida(OBJETOS["Bolsa"] , OBJETOS["Tablero"] , OBJETOS["Temporizador"] , OBJETOS["Atril_jugador"] , OBJETOS["Atril_computadora"], 666 , 999, True)

# print(OBJETOS["Bolsa"].getBolsa())


#------------------------------------------------------------------------------------------------------------------------
# Molina, Lucio Felipe - 15980/7



