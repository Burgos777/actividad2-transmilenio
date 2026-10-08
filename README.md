# Actividades 2, 3 y 4 - Inteligencia artificial aplicada a TransMilenio

## Sistema inteligente de rutas y aprendizaje supervisado

Proyecto de Inteligencia Artificial.

### Integrantes

- Carlos Enrique Burgos Castillo - I.D. 100173307
- Jorge Andres Fernandez Maldonado - I.D. 100142226
- Alexander Patino Londono - I.D. 100150470

Docente: Ing. Sandra Isabel Rodriguez  
Fecha de la Actividad 2: 27 de septiembre de 2026  
Fecha de entrega de la Actividad 3: domingo, 11 de octubre de 2026  

## Ejecucion

Requiere Python 3.10 o superior, scikit-learn, pandas y matplotlib para la Actividad 3.

Para instalar la dependencia del modelo:

```bash
pip install -r requirements.txt
```

```bash
python src/main.py
```

Para ejecutar las pruebas con una separacion clara entre cada resultado:

```bash
python tests/run_tests.py
```

## Estructura

- `src/knowledge.py`: hechos, conexiones y reglas.
- `src/route_search.py`: algoritmo de busqueda.
- `src/main.py`: programa principal.
- `tests/test_routes.py`: pruebas automaticas.
- `data/transit_supervised.csv`: dataset academico para aprendizaje supervisado.
- `src/supervised_model.py`: arbol de decision para clasificar la demanda.
- `tests/test_supervised_model.py`: pruebas del modelo supervisado.
- `docs/datos_y_modelo.md`: descripcion de los datos y del metodo.
- `output/prediccion_demanda.png`: grafica generada por el modelo.
- `src/unsupervised_model.py`: agrupamiento no supervisado con K-Means.
- `tests/test_unsupervised_model.py`: pruebas del agrupamiento.
- `docs/agrupamiento_no_supervisado.md`: descripcion de la Actividad 4.

## Actividad 3: modelo supervisado

```bash
python src/supervised_model.py
```

El modelo clasifica la demanda estimada de una ruta como baja, media o alta utilizando un arbol de decision. Como no se dispone de una fuente completa de datos reales, se utiliza un dataset academico documentado.

## Actividad 4: agrupamiento no supervisado

```bash
python src/unsupervised_model.py
```

El programa utiliza K-Means para encontrar tres grupos de situaciones de transporte, sin utilizar la columna `nivel_demanda`. La grafica se guarda en `output/agrupamiento_rutas.png`.
