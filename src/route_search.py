"""Busqueda de la mejor ruta usando una cola de prioridad.

Se utiliza una variante de Dijkstra, tambien conocida como busqueda de costo
uniforme, porque siempre se explora primero el estado con menor puntaje.
"""

import heapq
from dataclasses import dataclass

from knowledge import STATIONS, build_graph


# Penalizacion academica para que el sistema prefiera rutas con menos cambios
# de linea. No representa necesariamente el tiempo real de TransMilenio.
TRANSFER_PENALTY = 8


@dataclass
class RouteResult:
    """Almacena la solucion encontrada por el algoritmo."""

    origin: str
    destination: str
    stations: list[str]
    lines: list[str]
    minutes: int
    transfers: int
    score: int


def best_route(origin: str, destination: str) -> RouteResult:
    """Encuentra la ruta con menor puntaje desde origen hasta destino.

    El puntaje es tiempo de viaje mas ocho minutos por cada transbordo.
    Incluir la ultima linea en el estado permite contar los transbordos.
    """
    # Validacion de los datos ingresados por el usuario.
    if origin not in STATIONS or destination not in STATIONS:
        raise ValueError("La estacion de origen o destino no existe.")

    # Si origen y destino son iguales, no hay trayecto ni transbordos.
    if origin == destination:
        return RouteResult(origin, destination, [origin], [], 0, 0, 0)

    # Cada elemento de la cola contiene:
    # puntaje, minutos, estacion actual, ultima linea, camino y lineas usadas.
    graph = build_graph()
    queue = [(0, 0, origin, None, [origin], [])]
    visited = {}

    # La cola de prioridad permite procesar primero la opcion mas economica.
    while queue:
        score, minutes, station, last_line, path, lines = heapq.heappop(queue)
        state = (station, last_line)

        # Evita volver a procesar un estado si ya se encontro una opcion mejor.
        if state in visited and visited[state] <= score:
            continue
        visited[state] = score

        # Al llegar al destino se calcula el numero de transbordos y se devuelve
        # la primera solucion, que es la de menor puntaje.
        if station == destination:
            transfers = sum(
                1 for previous, current in zip(lines, lines[1:])
                if previous != current
            )
            return RouteResult(
                origin, destination, path, lines, minutes, transfers, score
            )

        # Se revisan todas las conexiones posibles desde la estacion actual.
        for edge in graph[station]:
            # Hay transbordo cuando cambia la linea utilizada.
            transfer = last_line is not None and edge.line != last_line
            new_score = score + edge.minutes
            if transfer:
                new_score += TRANSFER_PENALTY

            # Se agrega a la cola una nueva posibilidad de recorrido.
            heapq.heappush(
                queue,
                (
                    new_score,
                    minutes + edge.minutes,
                    edge.destination,
                    edge.line,
                    path + [edge.destination],
                    lines + [edge.line],
                ),
            )

    # Este punto se alcanza si el grafo no tiene un camino al destino.
    raise ValueError("No existe una ruta entre las estaciones indicadas.")


def format_route(result: RouteResult) -> str:
    """Prepara el resultado para mostrarlo en consola.

    Convierte las claves internas de las estaciones en nombres comprensibles
    para el usuario y presenta los indicadores de la ruta.
    """
    station_names = " -> ".join(STATIONS[key] for key in result.stations)
    lines = ", ".join(result.lines) if result.lines else "Ninguna"
    return (
        f"Ruta: {station_names}\n"
        f"Lineas: {lines}\n"
        f"Tiempo estimado: {result.minutes} minutos\n"
        f"Transbordos: {result.transfers}\n"
        f"Puntaje: {result.score}"
    )
