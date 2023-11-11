#!C:\Users\deras\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\python.exe

from urllib.parse import parse_qs
import os
import htmlCode
import modules.database

# Obtener los parametros que envía el formulario
parameter = parse_qs(os.environ.get('QUERY_STRING'))
values = []

def parameter_validation(): # Crea el filtro de la consulta SQL
    query = ""
    missing = 0 # Mantiene un conteo de los parametros no enviados
    if "company" in parameter and parameter["company"][0]!="": # Si el parametro company está presente
        query += " company=%s" # Se añade company a la consulta
        values.append(parameter["company"][0]) # Se añade el valor del parametro al array de valores
    else:
        missing += 1 # Aumenta el contador de parámetros no enviados
    if "theme" in parameter and parameter["theme"][0]!="": # Si el parametro theme está presente
        if query != "": # Si no es el primer parámetro en añadirse
            query += " AND" # Se añade AND a la consulta
        query += " theme=%s" # Se añade company a la consulta
        values.append(parameter["theme"][0]) # Se añade el valor del parametro al array de valores
    else:
        missing += 1 # Aumenta el contador de parámetros no enviados
    if "player-count" in parameter and parameter["player-count"][0]!="": # Si el parametro player-count está presente
        if query != "": # Si no es el primer parámetro en añadirse
            query += " AND" # Se añade AND a la consulta
        query += " player_count=%s" # Se añade company a la consulta
        values.append(parameter["player-count"][0]) # Se añade el valor del parametro al array de valores
    else:
        missing += 1 # Aumenta el contador de parámetros no enviados
    if "from-year" in parameter and parameter["from-year"][0]!="": # Si el parametro from-year está presente
        if query != "": # Si no es el primer parámetro en añadirse
            query += " AND" # Se añade AND a la consulta
        query += " release_date>=%s" # Se añade company a la consulta
        values.append(parameter["from-year"][0]) # Se añade el valor del parametro al array de valores
    else:
        missing += 1 # Aumenta el contador de parámetros no enviados
    if "until" in parameter and parameter["until"][0]!="": # Si el parametro until está presente
        if query != "": # Si no es el primer parámetro en añadirse
            query += " AND" # Se añade AND a la consulta
        query += " release_date<=%s" # Se añade company a la consulta
        values.append(parameter["until"][0]) # Se añade el valor del parametro al array de valores
    else:
        missing += 1 # Aumenta el contador de parámetros no enviados

    if missing == 5: # Si no se han envíado ninguno de los valores del filtro
        htmlCode.message_page("success","Filter applied","crud.py") # Da un mensaje de éxito y te muestra la tabla sin filtros
        exit() # Se sale del python
    return query # Devuelve la consulta

database = modules.database.Database_Manager("localhost","videojuegos","videojuegos","videojuegos") # Hace una conexion con la base de datos

htmlCode.crud(database.custom_query_fetch("videojuegosantiguos",parameter_validation(), values)) # Crea la tabla con los datos que devuelve custom_query_fetch

database = database.close_database() # Cierra la BDD