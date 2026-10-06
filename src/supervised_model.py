# Modelo de aprendizaje supervisado para clasificar la demanda de una ruta.
# El programa aprende con ejemplos del dataset y luego predice si la demanda
# de una nueva situacion es baja, media o alta.

# Permite construir rutas de archivos independientes del sistema operativo.
# De esta forma el programa encuentra los archivos aunque se ejecute desde
# diferentes carpetas o sistemas operativos.
from pathlib import Path

# Permite cargar y organizar el dataset en una tabla.
# pandas facilita leer el archivo CSV y convertir cada fila en un registro.
import pandas as pd

# Permite crear la grafica de probabilidades de la prediccion.
# matplotlib dibuja y guarda la imagen que se muestra durante la demostracion.
import matplotlib.pyplot as plt

# Permite separar los datos para entrenamiento y evaluacion.
# Una parte de los registros ensena al modelo y otra parte permite comprobarlo.
from sklearn.model_selection import train_test_split

# Permite convertir variables categoricas en columnas numericas.
# El modelo necesita valores numericos para procesar textos como "laboral".
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

# Implementa el clasificador basado en arboles de decision.
# Pipeline conecta el preprocesamiento con el arbol en un solo flujo.
from sklearn.pipeline import Pipeline
from sklearn.tree import DecisionTreeClassifier


# Ubicacion del dataset academico usado por el modelo.
# El dataset contiene los ejemplos con los que se entrenara el modelo.
DATASET_PATH = Path(__file__).parents[1] / "data" / "transit_supervised.csv"

# Ubicacion donde se guardara la grafica de probabilidades.
CHART_PATH = Path(__file__).parents[1] / "output" / "prediccion_demanda.png"

# Condiciones de ruta definidas internamente para realizar la consulta.
# El usuario solo escribe la pregunta; estas condiciones ya estan cargadas.
ROUTE_CONDITIONS = {
    "linea": "F",
    "hora": 18,
    "dia": "laboral",
    "clima": "lluvia",
    "estaciones_recorridas": 9,
    "pasajeros_hora": 850,
}


# Carga el archivo CSV y convierte sus datos en una lista de diccionarios.
# Cada diccionario representa una fila y contiene las variables de una ruta.
def load_dataset(path: Path = DATASET_PATH) -> list[dict]:
    # Lee el archivo CSV y lo convierte en una tabla de pandas.
    dataframe = pd.read_csv(path)

    # Convierte la tabla en registros para que el modelo pueda procesarlos.
    return dataframe.to_dict(orient="records")


# Entrena un arbol de decision usando las caracteristicas del dataset.
# Tambien devuelve la precision obtenida al evaluar los datos de prueba.
def train_model(rows: list[dict]) -> tuple[Pipeline, float]:
    # Define las columnas que el modelo utilizara como datos de entrada.
    feature_names = [
        "linea",
        "hora",
        "dia",
        "clima",
        "estaciones_recorridas",
        "pasajeros_hora",
    ]
    # Estas variables contienen categorias escritas como texto.
    categorical_features = ["linea", "dia", "clima"]

    # Estas variables contienen cantidades numericas.
    numeric_features = [
        "hora",
        "estaciones_recorridas",
        "pasajeros_hora",
    ]

    # Busca la posicion de cada variable para configurar el preprocesamiento.
    categorical_indexes = [feature_names.index(name) for name in categorical_features]
    numeric_indexes = [feature_names.index(name) for name in numeric_features]

    # Construye la matriz de entradas y la lista de respuestas esperadas.
    features = [[row[name] for name in feature_names] for row in rows]
    target = [row["nivel_demanda"] for row in rows]

    # Divide los registros: 75 por ciento para aprender y 25 por ciento para evaluar.
    x_train, x_test, y_train, y_test = train_test_split(
        features,
        target,
        test_size=0.25,
        random_state=42,
        stratify=target,
    )

    # Codifica las categorias y conserva las variables numericas sin modificarlas.
    transformer = ColumnTransformer(
        [
            (
                "categoricas",
                OneHotEncoder(handle_unknown="ignore"),
                categorical_indexes,
            ),
            ("numericas", "passthrough", numeric_indexes),
        ]
    )

    # Une el preprocesamiento con el arbol de decision.
    model = Pipeline(
        [
            ("preprocesamiento", transformer),
            ("arbol", DecisionTreeClassifier(max_depth=4, random_state=42)),
        ]
    )
    # Entrena el modelo con los ejemplos y sus respuestas conocidas.
    model.fit(x_train, y_train)

    # Calcula que porcentaje de predicciones coincide con las respuestas reales.
    return model, model.score(x_test, y_test)


# Predice el nivel de demanda para una nueva situacion de viaje.
# Utiliza exactamente el mismo orden de variables empleado durante el entrenamiento.
def predict_demand(model: Pipeline, sample: dict) -> str:
    # Organiza los datos de la nueva ruta en una sola fila.
    values = [[
        sample["linea"],
        sample["hora"],
        sample["dia"],
        sample["clima"],
        sample["estaciones_recorridas"],
        sample["pasajeros_hora"],
    ]]
    # Obtiene la categoria predicha por el arbol de decision.
    return str(model.predict(values)[0])


# Crea una grafica con la probabilidad estimada para cada nivel de demanda.
# La imagen sirve como evidencia visual del resultado obtenido.
def create_prediction_chart(model: Pipeline, sample: dict, path: Path = CHART_PATH) -> None:
    # Organiza la nueva ruta con el mismo orden utilizado para entrenar el modelo.
    values = [[
        sample["linea"],
        sample["hora"],
        sample["dia"],
        sample["clima"],
        sample["estaciones_recorridas"],
        sample["pasajeros_hora"],
    ]]
    # Calcula la probabilidad de pertenecer a cada categoria.
    probabilities = model.predict_proba(values)[0]

    # Obtiene los nombres de las categorias que aparecen en el eje horizontal.
    classes = model.named_steps["arbol"].classes_

    # Crea la carpeta de salida si todavia no existe.
    path.parent.mkdir(parents=True, exist_ok=True)

    # Configura el tamano y las barras de la grafica.
    plt.figure(figsize=(7, 4))
    bars = plt.bar(classes, probabilities, color=["#63b3ed", "#f6ad55", "#fc8181"])
    plt.ylim(0, 1)
    plt.ylabel("Probabilidad")
    plt.xlabel("Nivel de demanda")
    plt.title("Prediccion del modelo supervisado")
    # Escribe el porcentaje encima de cada barra.
    for bar, probability in zip(bars, probabilities):
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            probability + 0.03,
            f"{probability:.0%}",
            ha="center",
        )
    # Ajusta los elementos, guarda la imagen y la muestra en pantalla.
    plt.tight_layout()
    plt.savefig(path, dpi=150)
    # Muestra la grafica en una ventana para facilitar la demostracion.
    plt.show()
    plt.close()


# Ejecuta el entrenamiento y muestra una prediccion de ejemplo.
# Esta es la funcion principal que coordina todo el flujo del programa.
def main() -> None:
    # Carga los datos y entrena el arbol de decision.
    rows = load_dataset()
    model, accuracy = train_model(rows)

    # Muestra las condiciones que seran evaluadas.
    print("=== CONSULTA DE DEMANDA ===")
    print("Condiciones de la ruta cargadas por el sistema:")
    print(ROUTE_CONDITIONS)

    # Permite que el usuario formule la pregunta antes de mostrar la respuesta.
    input("\nSegun estas condiciones, la demanda sera baja, media o alta? ")

    # Realiza la prediccion y genera la grafica correspondiente.
    prediction = predict_demand(model, ROUTE_CONDITIONS)
    create_prediction_chart(model, ROUTE_CONDITIONS)
    print("=== MODELO SUPERVISADO DE DEMANDA ===")
    print(f"Registros usados: {len(rows)}")
    print(f"Precision sobre datos de prueba: {accuracy:.2%}")
    print(f"Prediccion: segun estas condiciones, la demanda sera {prediction}")
    print(f"Grafica guardada en: {CHART_PATH}")


if __name__ == "__main__":
    main()
