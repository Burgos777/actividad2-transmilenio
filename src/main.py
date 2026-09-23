"""Interfaz de consola del sistema inteligente.

Este archivo coordina la entrada del usuario, la busqueda de la ruta y la
presentacion del resultado.
"""

from knowledge import RULES, STATIONS
from route_search import best_route, format_route


def show_stations():
    """Muestra las claves de las estaciones que se pueden consultar."""
    print("\nEstaciones disponibles:")
    for key, name in STATIONS.items():
        print(f"  {key:<18} - {name}")


def show_rules():
    """Muestra las reglas logicas que utiliza el sistema."""
    print("\nReglas del sistema:")
    for number, rule in enumerate(RULES, start=1):
        print(f"  {number}. {rule}")


def main():
    """Ejecuta el flujo principal de la aplicacion."""
    print("=== SISTEMA INTELIGENTE DE RUTAS TRANSMILENIO ===")

    # Se informa al usuario que estaciones y reglas estan disponibles.
    show_stations()
    show_rules()

    # Se leen y normalizan las claves escritas por el usuario.
    origin = input("\nClave de la estacion de origen: ").strip().lower()
    destination = input("Clave de la estacion de destino: ").strip().lower()

    try:
        # Se solicita al modulo de busqueda la mejor ruta.
        result = best_route(origin, destination)
    except ValueError as error:
        # Se muestra un mensaje claro cuando la entrada no es valida.
        print(f"\nError: {error}")
        return

    # Se imprime la solucion encontrada.
    print("\n=== RESULTADO ===")
    print(format_route(result))


if __name__ == "__main__":
    # Este bloque evita que main() se ejecute al importar el modulo en pruebas.
    main()
