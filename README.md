# Actividad 2 - Busqueda y sistemas basados en reglas

## Sistema inteligente de rutas para TransMilenio

Proyecto de Inteligencia Artificial.

### Integrantes

- Carlos Enrique Burgos Castillo - I.D. 100173307
- Jorge Andres Fernandez Maldonado - I.D. 100142226
- Alexander Patino Londono - I.D. 100150470

Docente: Ing. Sandra Isabel Rodriguez  
Fecha: 27 de septiembre de 2026

## Ejecucion

Requiere Python 3.10 o superior.

```bash
python src/main.py
```

Para ejecutar las pruebas:

```bash
python -m unittest discover -s tests -v
```

## Estructura

- `src/knowledge.py`: hechos, conexiones y reglas.
- `src/route_search.py`: algoritmo de busqueda.
- `src/main.py`: programa principal.
- `tests/test_routes.py`: pruebas automaticas.
