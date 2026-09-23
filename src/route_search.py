"""Busqueda de la mejor ruta usando una cola de prioridad."""

import heapq
from dataclasses import dataclass

from knowledge import STATIONS, build_graph


TRANSFER_PENALTY = 8


@dataclass
class RouteResult:
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
    if origin not in STATIONS or destination not in STATIONS:
        raise ValueError("La estacion de origen o destino no existe.")

    if origin == destination:
        return RouteResult(origin, destination, [origin], [], 0, 0, 0)

    graph = build_graph()
    queue = [(0, 0, origin, None, [origin], [])]
    visited = {}

    while queue:
        score, minutes, station, last_line, path, lines = heapq.heappop(queue)
        state = (station, last_line)

        if state in visited and visited[state] <= score:
            continue
        visited[state] = score

        if station == destination:
            transfers = sum(
                1 for previous, current in zip(lines, lines[1:])
                if previous != current
            )
            return RouteResult(
                origin, destination, path, lines, minutes, transfers, score
            )

        for edge in graph[station]:
            transfer = last_line is not None and edge.line != last_line
            new_score = score + edge.minutes
            if transfer:
                new_score += TRANSFER_PENALTY

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

    raise ValueError("No existe una ruta entre las estaciones indicadas.")


def format_route(result: RouteResult) -> str:
    """Prepara el resultado para mostrarlo en consola."""
    station_names = " -> ".join(STATIONS[key] for key in result.stations)
    lines = ", ".join(result.lines) if result.lines else "Ninguna"
    return (
        f"Ruta: {station_names}\n"
        f"Lineas: {lines}\n"
        f"Tiempo estimado: {result.minutes} minutos\n"
        f"Transbordos: {result.transfers}\n"
        f"Puntaje: {result.score}"
    )
