
from Archivos.metodos_de_archivos  import cargarPartida
from Archivos.metodos_de_archivos  import guardar_partida
from Objetos.CLASS_bolsa import Bolsa
from Objetos.CLASS_tablero import Tablero
from Objetos.CLASS_temporizador import Temporizador
from Objetos.CLASS_atril import Atril



def instanciar_objetos(Bol , Table , Temp , Atril_jugador , Atril_computadora , config):

    """Recibe los datos en diccionarios e instancia los objetos para su uso."""
    Bol = Bolsa(config["Bolsa"])
    Table = Tablero(config["Tablero"])
    Temp = Temporizador(int(config["Temporizador"]["minutos"]) , int(config["Temporizador"]["segundos"]))
    Atril_jugador = Atril(config["Atril_jugador"])
    Atril_computadora = Atril(config["Atril_computadora"])

    return {"Bolsa":Bol, "Tablero":Table, "Temporizador":Temp, "Atril_jugador":Atril_jugador, "Atril_computadora":Atril_computadora}


#------------------------------------------------------------------------------------------------------------------------
# Molina, Lucio Felipe - 15980/7



