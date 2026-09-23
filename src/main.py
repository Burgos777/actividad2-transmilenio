"""Interfaz de consola del sistema inteligente."""

from knowledge import RULES, STATIONS
from route_search import best_route, format_route


def show_stations():
    print("\nEstaciones disponibles:")
    for key, name in STATIONS.items():
        print(f"  {key:<18} - {name}")


def show_rules():
    print("\nReglas del sistema:")
    for number, rule in enumerate(RULES, start=1):
        print(f"  {number}. {rule}")


def main():
    print("=== SISTEMA INTELIGENTE DE RUTAS TRANSMILENIO ===")
    show_stations()
    show_rules()

    origin = input("\nClave de la estacion de origen: ").strip().lower()
    destination = input("Clave de la estacion de destino: ").strip().lower()

    try:
        result = best_route(origin, destination)
    except ValueError as error:
        print(f"\nError: {error}")
        return

    print("\n=== RESULTADO ===")
    print(format_route(result))


if __name__ == "__main__":
    main()
