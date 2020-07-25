
from Archivos.metodos_de_archivos  import obtenerConfiguracion
from Objetos.CLASS_bolsa import Bolsa
from Objetos.CLASS_tablero import Tablero
from Objetos.CLASS_temporizador import Temporizador
from Objetos.CLASS_atril import Atril



def instanciar_objetos(Bol , Table , Temp , Atril_computadora , Atril_jugador , config):
    Bol = Bolsa(config["Bolsa"])
    Table = Tablero(config["Tablero"])
    Temp = Temporizador(config["Temporizador"]["minutos"] , config["Temporizador"]["segundos"])
    Atril_jugador = Atril(config["Atril_jugador"])
    Atril_computadora = Atril(config["Atril_computadora"])

    return {"Bolsa":Bol, "Tablero":Table, "Temporizador":Temp, "Atril_jugador":Atril_jugador, "Atril_computadora":Atril_computadora}

Bol = Bolsa
Table = Tablero
Temp = Temporizador
Atril_computadora = Atril
Atril_jugador =  Atril

config = obtenerConfiguracion("Archivos\\partidas\\partida_guardada_2.json")

OBJETOS = instanciar_objetos(Bol,Table,Temp,Atril_computadora,Atril_jugador,config)

print(OBJETOS["Bolsa"].getBolsa())



