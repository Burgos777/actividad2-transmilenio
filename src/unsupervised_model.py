# Modelo de aprendizaje no supervisado para agrupar situaciones de transporte.
# El algoritmo encuentra grupos de rutas parecidas sin recibir una respuesta
# previamente asignada como baja, media o alta.

# Permite construir rutas de archivos independientes del sistema operativo.
from pathlib import Path

# Permite cargar y analizar el dataset como una tabla.
import pandas as pd

# Permite crear la grafica de los grupos encontrados.
import matplotlib.pyplot as plt

# Permite estandarizar las variables antes del agrupamiento.
from sklearn.preprocessing import StandardScaler

# Implementa el algoritmo de agrupamiento K-Means.
from sklearn.cluster import KMeans

# Mide que tan separados y compactos son los grupos encontrados.
from sklearn.metrics import silhouette_score


# Ubicacion del dataset academico utilizado en el proyecto de transporte.
DATASET_PATH = Path(__file__).parents[1] / "data" / "transit_supervised.csv"

# Ubicacion donde se guardara la grafica de los grupos.
CHART_PATH = Path(__file__).parents[1] / "output" / "agrupamiento_rutas.png"

# Variables numericas utilizadas para comparar situaciones de transporte.
FEATURES = ["hora", "estaciones_recorridas", "pasajeros_hora"]


# Carga unicamente las variables de entrada y descarta la etiqueta supervisada.
def load_features(path: Path = DATASET_PATH) -> pd.DataFrame:
    dataframe = pd.read_csv(path)
    return dataframe[FEATURES].copy()


# Entrena K-Means y devuelve los grupos asignados y el indice de silueta.
def train_clusters(dataframe: pd.DataFrame, number_of_clusters: int = 3):
    # Convierte las variables a una escala comparable para evitar que
    # pasajeros_hora domine el agrupamiento por tener valores mas grandes.
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(dataframe[FEATURES])

    # K-Means busca centros y asigna cada registro al centro mas cercano.
    model = KMeans(n_clusters=number_of_clusters, random_state=42, n_init=10)
    labels = model.fit_predict(scaled_data)

    # La silueta cercana a 1 indica grupos compactos y bien separados.
    score = silhouette_score(scaled_data, labels)
    return model, scaler, labels, score


# Resume cada grupo usando los promedios originales de sus variables.
def summarize_clusters(dataframe: pd.DataFrame, labels) -> pd.DataFrame:
    result = dataframe.copy()
    result["grupo"] = labels
    return result.groupby("grupo")[FEATURES].mean().round(2)


# Genera una grafica donde cada color representa un grupo de rutas.
def create_cluster_chart(dataframe: pd.DataFrame, labels, path: Path = CHART_PATH) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    plt.figure(figsize=(8, 5))
    scatter = plt.scatter(
        dataframe["hora"],
        dataframe["pasajeros_hora"],
        c=labels,
        cmap="viridis",
        s=80,
        edgecolors="black",
    )
    plt.xlabel("Hora del viaje")
    plt.ylabel("Pasajeros estimados por hora")
    plt.title("Agrupamiento no supervisado de situaciones de transporte")
    plt.colorbar(scatter, label="Grupo encontrado")
    plt.tight_layout()
    plt.savefig(path, dpi=150)
    # Muestra la grafica para facilitar la explicacion en el video.
    plt.show()
    plt.close()


# Ejecuta el agrupamiento y muestra los resultados en la consola.
def main() -> None:
    dataframe = load_features()
    model, scaler, labels, score = train_clusters(dataframe)
    summary = summarize_clusters(dataframe, labels)
    create_cluster_chart(dataframe, labels)

    print("=== AGRUPAMIENTO NO SUPERVISADO DE RUTAS ===")
    print(f"Registros analizados: {len(dataframe)}")
    print(f"Cantidad de grupos encontrados: {model.n_clusters}")
    print(f"Indice de silueta: {score:.3f}")
    print("\nPromedios de cada grupo:")
    print(summary)
    print(f"\nGrafica guardada en: {CHART_PATH}")


if __name__ == "__main__":
    main()
