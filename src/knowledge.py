# Base de conocimiento simplificada de TransMilenio.
# Este modulo contiene estaciones, conexiones, lineas y reglas.

# Permite crear clases que almacenan datos de forma organizada.
from dataclasses import dataclass


@dataclass(frozen=True)
# Representa una conexion entre dos estaciones.
# origin: identificador de la estacion de origen.
# destination: identificador de la estacion de destino.
# line: letra de la linea de TransMilenio.
# minutes: tiempo estimado del trayecto entre estaciones.
class Connection:
    origin: str
    destination: str
    line: str
    minutes: int


# Hecho estacion(id, nombre): relaciona la clave usada por el programa
# con el nombre que se muestra al usuario.
STATIONS = {
    "portal_americas": "Portal Americas",
    "banderas": "Banderas",
    "mundo_avenida": "Mundo Aventura",
    "pradera": "Pradera",
    "americas": "Americas",
    "calle_13": "Calle 13",
    "sabana": "De la Sabana",
    "san_fa_centro": "San Victorino",
    "av_jimenez": "Avenida Jimenez",
    "museo_oro": "Museo del Oro",
    "las_aguas": "Las Aguas",
    "portal_norte": "Portal Norte",
    "toberin": "Toberin",
    "calle_127": "Calle 127",
    "pepe_sierra": "Pepe Sierra",
    "calle_100": "Calle 100",
    "calle_76": "Calle 76",
}


# Hechos conecta(origen, destino, linea, tiempo_estimado).
# Estas conexiones son una representacion academica y simplificada.
CONNECTIONS = [
    Connection("portal_americas", "banderas", "F", 4),
    Connection("banderas", "mundo_avenida", "F", 3),
    Connection("mundo_avenida", "pradera", "F", 3),
    Connection("pradera", "americas", "F", 3),
    Connection("americas", "calle_13", "F", 4),
    Connection("calle_13", "sabana", "F", 3),
    Connection("sabana", "san_fa_centro", "F", 3),
    Connection("san_fa_centro", "av_jimenez", "F", 3),
    Connection("av_jimenez", "museo_oro", "J", 3),
    Connection("museo_oro", "las_aguas", "J", 3),
    Connection("portal_norte", "toberin", "B", 4),
    Connection("toberin", "calle_127", "B", 4),
    Connection("calle_127", "pepe_sierra", "B", 3),
    Connection("pepe_sierra", "calle_100", "B", 4),
    Connection("calle_100", "calle_76", "B", 4),
    Connection("calle_76", "av_jimenez", "J", 9),
]


# Reglas logicas que explican como interpreta el sistema los hechos.
RULES = [
    "Si dos estaciones tienen una conexion, se puede viajar entre ellas.",
    "Si cambia la linea, se registra un transbordo.",
    "Si una ruta llega al destino, es una solucion candidata.",
    "Se prefiere la solucion con menor tiempo y menos transbordos.",
]


# Convierte los hechos de conexion en un grafo bidireccional.
# Aunque cada hecho se declara una sola vez, una persona puede desplazarse
# en ambos sentidos. Por eso se agrega la conexion original y la inversa.
def build_graph():
    # Se crea una lista vacia para cada estacion.
    graph = {station: [] for station in STATIONS}

    # Se agregan las conexiones de ida y de regreso.
    for connection in CONNECTIONS:
        graph[connection.origin].append(connection)
        graph[connection.destination].append(
            Connection(
                connection.destination,
                connection.origin,
                connection.line,
                connection.minutes,
            )
        )
    return graph
