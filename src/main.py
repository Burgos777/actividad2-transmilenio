# Interfaz de consola del sistema inteligente.
# Coordina la entrada del usuario, la busqueda y la presentacion del resultado.

# Importa las reglas y las estaciones que se muestran al usuario.
from knowledge import RULES, STATIONS

# Importa las funciones que buscan y formatean la ruta.
from route_search import best_route, format_route


# Muestra las claves de las estaciones que se pueden consultar.
def show_stations():
    print("\nEstaciones disponibles:")
    for key, name in STATIONS.items():
        print(f"  {key:<18} - {name}")


# Muestra las reglas logicas que utiliza el sistema.
def show_rules():
    print("\nReglas del sistema:")
    for number, rule in enumerate(RULES, start=1):
        print(f"  {number}. {rule}")


# Ejecuta el flujo principal de la aplicacion.
def main():
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
