# Ejecutor personalizado para mostrar las pruebas separadas en la consola.

# Permite cerrar el programa indicando si las pruebas fueron exitosas.
import sys

# Proporciona las clases para descubrir y ejecutar pruebas automaticas.
import unittest


# Agrega una linea en blanco despues de cada resultado de prueba.
class SpacedTestResult(unittest.TextTestResult):
    # Deja una separacion despues de una prueba exitosa.
    def addSuccess(self, test):
        super().addSuccess(test)
        self.stream.writeln()

    # Deja una separacion despues de una prueba fallida.
    def addFailure(self, test, err):
        super().addFailure(test, err)
        self.stream.writeln()

    # Deja una separacion despues de una prueba con error.
    def addError(self, test, err):
        super().addError(test, err)
        self.stream.writeln()


# Utiliza el resultado personalizado al ejecutar las pruebas del proyecto.
class SpacedTestRunner(unittest.TextTestRunner):
    resultclass = SpacedTestResult


# Descubre las pruebas y devuelve un codigo de salida para la consola.
def main() -> None:
    suite = unittest.defaultTestLoader.discover("tests")
    result = SpacedTestRunner(verbosity=2).run(suite)
    sys.exit(not result.wasSuccessful())


if __name__ == "__main__":
    main()
