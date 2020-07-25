from CLASS_atril import Atril
from CLASS_bolsa import Bolsa
from CLASS_tablero import Tablero
from CLASS_temporizador import Temporizador

def instanciar_objetos(Bol , Table , Temp , Atril_computadora , Atril_jugador , config):
    Bol = Bolsa(config["Bolsa"])
    Table = Tablero(config["Tablero"])
    Temp = Temporizador(config["Temporizador"]["minutos"] , config["Temporizador"]["segundos"])
    Atril_jugador = Atril(config["Atril_jugador"])
    Atril_computadora = Atril(config["Atril_computadora"])



