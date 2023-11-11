#!C:\Users\deras\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\python.exe

from urllib.parse import parse_qs
import os
import htmlCode
import modules.database

# Obtener los parametros que envía el formulario
parameter = parse_qs(os.environ.get('QUERY_STRING'))

data_directory = '../data/';data_file = 'accounts.json' # Ruta del archivo .json

def parameter_validation(): # Comprueba que se envían todos los parametros
    expected_parameters = ["name","company","theme","player-count","release-date"] # Parámetros a comprobar que están

    for expected in expected_parameters: # Por cada parámetro esperado
        if expected not in parameter: # Si falta en la url
            htmlCode.message_page("error",f"{expected} parameter cant be missing", "main.py") # Muestra un mensaje de error
            exit() # Se sale del python
        if parameter[expected][0] == "": # Si el parámetro está vacío
            htmlCode.message_page("error",f"{expected} cant be empty", "main.py") # Muestra un mensaje de error
            exit() # Se sale del python

    #Recupera los parámetros de la URL
    name = parameter["name"][0]
    company = parameter["company"][0]
    theme = parameter["theme"][0]
    player_count = parameter["player-count"][0]
    release_date = parameter["release-date"][0]

    return name,company,theme,player_count,release_date # Devuelve los parámetros de la URL

column_name = ["name","company","theme","player_count","release_date"] # Nombres de las columnas de la BDD

database = modules.database.Database_Manager("localhost","videojuegos","videojuegos","videojuegos") # Hace una conexion con la base de datos

database.insert("videojuegosantiguos",column_name,parameter_validation()) # Inserta los parámetros en la BDD

database.close_database() # Cierra la BDD

htmlCode.message_page("success", "Row inserted", "crud.py") # Muestra mensaje de éxito