import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1] / "src"))

from route_search import best_route


class RouteSearchTests(unittest.TestCase):
    def test_americas_to_museo_del_oro(self):
        result = best_route("portal_americas", "museo_oro")
        self.assertEqual(result.stations[0], "portal_americas")
        self.assertEqual(result.stations[-1], "museo_oro")
        self.assertGreater(result.minutes, 0)
        self.assertEqual(result.transfers, 1)

    def test_north_to_calle_76(self):
        result = best_route("portal_norte", "calle_76")
        self.assertEqual(result.stations[0], "portal_norte")
        self.assertEqual(result.stations[-1], "calle_76")
        self.assertEqual(result.minutes, 19)
        self.assertEqual(result.transfers, 0)

    def test_unknown_station(self):
        with self.assertRaises(ValueError):
            best_route("no_existe", "museo_oro")


if __name__ == "__main__":
    unittest.main()
