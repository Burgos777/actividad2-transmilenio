# Pruebas automaticas del modelo de aprendizaje no supervisado.

# Permite ejecutar pruebas con el modulo incluido en Python.
import unittest

# Importa las funciones que se van a comprobar.
from unsupervised_model import load_features, summarize_clusters, train_clusters


# Agrupa las pruebas del algoritmo K-Means.
class UnsupervisedModelTests(unittest.TestCase):
    # Comprueba que se carguen las tres variables numericas del dataset.
    def test_features_have_expected_shape(self):
        """Comprueba que el dataset tenga 42 filas y tres variables numericas."""
        dataframe = load_features()
        self.assertEqual(dataframe.shape, (42, 3))
        self.assertEqual(
            list(dataframe.columns),
            ["hora", "estaciones_recorridas", "pasajeros_hora"],
        )

    # Comprueba que K-Means cree tres grupos y produzca una evaluacion valida.
    def test_clusters_are_created(self):
        """Comprueba la creacion de grupos y la calidad del agrupamiento."""
        dataframe = load_features()
        model, scaler, labels, score = train_clusters(dataframe)
        self.assertEqual(model.n_clusters, 3)
        self.assertEqual(len(labels), 42)
        self.assertGreater(score, 0)

        summary = summarize_clusters(dataframe, labels)
        self.assertEqual(len(summary), 3)


if __name__ == "__main__":
    unittest.main()
