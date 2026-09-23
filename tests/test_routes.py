# Pruebas automaticas del sistema de busqueda de rutas.

import sys
import unittest
from pathlib import Path

# Se agrega la carpeta src para poder importar los modulos del proyecto.
sys.path.insert(0, str(Path(__file__).parents[1] / "src"))

from route_search import best_route


class RouteSearchTests(unittest.TestCase):
    # Verifica rutas validas y el manejo de errores.

    def test_americas_to_museo_del_oro(self):
        # Comprueba una ruta con cambio de linea.
        result = best_route("portal_americas", "museo_oro")
        self.assertEqual(result.stations[0], "portal_americas")
        self.assertEqual(result.stations[-1], "museo_oro")
        self.assertGreater(result.minutes, 0)
        self.assertEqual(result.transfers, 1)

    def test_north_to_calle_76(self):
        # Comprueba una ruta directa sin transbordos.
        result = best_route("portal_norte", "calle_76")
        self.assertEqual(result.stations[0], "portal_norte")
        self.assertEqual(result.stations[-1], "calle_76")
        self.assertEqual(result.minutes, 19)
        self.assertEqual(result.transfers, 0)

    def test_unknown_station(self):
        # Comprueba que una estacion inexistente produzca un error.
        with self.assertRaises(ValueError):
            best_route("no_existe", "museo_oro")


if __name__ == "__main__":
    # Permite ejecutar este archivo directamente con Python.
    unittest.main()
