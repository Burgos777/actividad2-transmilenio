# Pruebas automaticas del modelo de aprendizaje supervisado.

# Permite ejecutar pruebas con el modulo incluido en Python.
import unittest

# Importa las funciones que se van a comprobar.
from supervised_model import load_dataset, predict_demand, train_model


# Agrupa las pruebas del modelo supervisado.
# Estas pruebas comprueban el flujo desde la carga del dataset hasta la prediccion.
class SupervisedModelTests(unittest.TestCase):
    # Verifica que el dataset pueda cargarse y tenga la cantidad esperada de filas.
    def test_dataset_has_expected_records(self):
        """Comprueba que el dataset tenga 42 registros y la variable objetivo."""
        # Carga los registros desde el archivo CSV mediante pandas.
        rows = load_dataset()

        # Confirma que la muestra academica contiene 42 observaciones.
        self.assertEqual(len(rows), 42)

        # Confirma que cada registro incluya la respuesta que debe aprender el modelo.
        self.assertIn("nivel_demanda", rows[0])

    # Verifica que el modelo se entrene y produzca una prediccion valida.
    def test_model_trains_with_valid_accuracy(self):
        """Comprueba el entrenamiento y una prediccion de demanda valida."""
        # Entrena el arbol y obtiene su precision sobre los datos de prueba.
        model, accuracy = train_model(load_dataset())

        # Exige una precision minima para considerar valido el entrenamiento.
        self.assertGreaterEqual(accuracy, 0.5)

        # Construye un caso de prueba con condiciones de una ruta.
        prediction = predict_demand(
            model,
            {
                "linea": "F",
                "hora": 18,
                "dia": "laboral",
                "clima": "lluvia",
                "estaciones_recorridas": 9,
                "pasajeros_hora": 850,
            },
        )

        # Confirma que la respuesta pertenezca a las tres categorias permitidas.
        self.assertIn(prediction, {"baja", "media", "alta"})


if __name__ == "__main__":
    unittest.main()
