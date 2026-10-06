# Actividad 3 - Datos y modelo supervisado

**Fecha de entrega:** domingo, 11 de octubre de 2026.

## Problema

El sistema de la Actividad 2 encontraba una ruta entre estaciones, pero no clasificaba las condiciones de demanda. En esta actividad se utiliza aprendizaje supervisado para estimar si una ruta tiene demanda baja, media o alta.

## Fuente de datos

No se cuenta con una base completa y pública de viajes del grupo. Por eso se construyó un dataset académico de muestra en `data/transit_supervised.csv`, siguiendo la instrucción de la actividad. Cada fila representa una observación de una ruta o tramo de TransMilenio.

## Variables

- `linea`: línea utilizada, como F, B o J.
- `hora`: hora aproximada del viaje.
- `dia`: tipo de día: laboral o sábado.
- `clima`: condición climática simplificada.
- `estaciones_recorridas`: cantidad de estaciones del trayecto.
- `pasajeros_hora`: cantidad estimada de pasajeros por hora.
- `nivel_demanda`: resultado que el modelo debe aprender: baja, media o alta.

## Método supervisado

Se utiliza un árbol de decisión (`DecisionTreeClassifier`). El dataset se carga con `pandas`, se divide en 75 % para entrenamiento y 25 % para prueba. Las variables de texto se convierten mediante codificación One-Hot y las variables numéricas se conservan como números. La precisión se calcula sobre los datos de prueba. Además, el programa genera `output/prediccion_demanda.png`, una gráfica con la probabilidad estimada para cada nivel de demanda.

## Ejecución

Desde la carpeta del proyecto:

```bash
python src/supervised_model.py
python tests/run_tests.py
```

Al ejecutar el programa, las condiciones de la ruta ya están cargadas en el sistema. El usuario solamente escribe la pregunta sobre el nivel de demanda y el modelo responde si la demanda estimada es baja, media o alta.

El modelo es académico y sirve para demostrar el proceso de aprendizaje supervisado. No representa mediciones oficiales ni predicciones operativas reales.
