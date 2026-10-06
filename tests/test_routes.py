# Pruebas automaticas del sistema de busqueda de rutas.

# Permite modificar temporalmente la ruta de importacion de Python.
import sys

# Proporciona las herramientas para crear y ejecutar pruebas automaticas.
import unittest

# Permite construir la ruta hacia la carpeta src.
from pathlib import Path

# Se agrega la carpeta src para poder importar los modulos del proyecto.
sys.path.insert(0, str(Path(__file__).parents[1] / "src"))

# Importa la funcion que sera evaluada en las pruebas.
from route_search import best_route


# Agrupa las pruebas relacionadas con la busqueda de rutas.
# Cada metodo comprueba un comportamiento esperado del sistema.
class RouteSearchTests(unittest.TestCase):
    # Comprueba que el sistema encuentre el trayecto correcto entre Portal
    # Americas y Museo del Oro, incluyendo el cambio de la linea F a la J.
    def test_americas_to_museo_del_oro(self):
        """Comprueba una ruta valida con un transbordo de linea."""
        # Solicita al algoritmo la mejor ruta para las estaciones indicadas.
        result = best_route("portal_americas", "museo_oro")

        # Verifica que la ruta comience en el origen solicitado.
        self.assertEqual(result.stations[0], "portal_americas")

        # Verifica que la ruta termine en el destino solicitado.
        self.assertEqual(result.stations[-1], "museo_oro")

        # Confirma que el trayecto tenga un tiempo mayor que cero.
        self.assertGreater(result.minutes, 0)

        # Confirma que el algoritmo haya contado un transbordo.
        self.assertEqual(result.transfers, 1)

    # Comprueba una ruta entre Portal Norte y Calle 76 sin cambio de linea.
    def test_north_to_calle_76(self):
        """Comprueba una ruta valida sin transbordos."""
        # Ejecuta la busqueda con el origen y destino de la prueba.
        result = best_route("portal_norte", "calle_76")

        # Verifica los extremos de la ruta encontrada.
        self.assertEqual(result.stations[0], "portal_norte")
        self.assertEqual(result.stations[-1], "calle_76")

        # Comprueba que el tiempo calculado coincida con los datos definidos.
        self.assertEqual(result.minutes, 19)

        # Comprueba que el recorrido no tenga transbordos.
        self.assertEqual(result.transfers, 0)

    # Comprueba que el sistema controle correctamente una estacion desconocida.
    def test_unknown_station(self):
        """Comprueba que una estacion inexistente genere un error controlado."""
        # Se espera un ValueError cuando la estacion no existe en la base.
        with self.assertRaises(ValueError):
            best_route("no_existe", "museo_oro")


if __name__ == "__main__":
    # Permite ejecutar este archivo directamente con Python.
    unittest.main()
