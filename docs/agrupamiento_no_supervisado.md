# Actividad 4 - Agrupamiento no supervisado

**Fecha de entrega:** domingo, 11 de octubre de 2026.

## Problema

En la Actividad 3 el modelo recibia una etiqueta conocida y clasificaba la demanda como baja, media o alta. En esta actividad se utiliza aprendizaje no supervisado para descubrir grupos de situaciones de transporte parecidas sin usar esa etiqueta.

## Fuente de datos

Se reutiliza el dataset academico `data/transit_supervised.csv`, construido para el proyecto de TransMilenio. Para esta actividad se ignora la columna `nivel_demanda`, porque el algoritmo debe encontrar los grupos sin recibir una respuesta correcta previamente asignada.

## Variables utilizadas

- `hora`: hora aproximada del viaje.
- `estaciones_recorridas`: cantidad de estaciones del trayecto.
- `pasajeros_hora`: pasajeros estimados por hora.

## Metodo no supervisado

Se utiliza K-Means con tres grupos. Primero se estandarizan las variables con `StandardScaler`, porque sus escalas son diferentes. Luego K-Means calcula tres centros y asigna cada registro al centro mas cercano.

La calidad del agrupamiento se revisa con el indice de silueta. Un valor mas cercano a 1 indica grupos mas compactos y separados. Los grupos no tienen nombres asignados por el algoritmo; se interpretan observando sus promedios.

## Ejecucion

```bash
python src/unsupervised_model.py
python tests/run_tests.py
```

El programa muestra la cantidad de grupos, el indice de silueta, los promedios de cada grupo y genera `output/agrupamiento_rutas.png`.

El dataset es una muestra academica y no representa mediciones oficiales de TransMilenio.
