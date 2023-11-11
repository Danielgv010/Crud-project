#!C:\Users\deras\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\python.exe

from urllib.parse import parse_qs
import os
import htmlCode
import modules.database
import sys

# Obtener los parametros que envía el formulario
parameter = parse_qs(os.environ.get('QUERY_STRING'))

database = modules.database.Database_Manager("localhost","videojuegos","videojuegos","videojuegos") # Hace una conexion con la base de datos

htmlCode.modify_window_crud(database.fetch_filtered("videojuegosantiguos","name",["id"],parameter["id"],1)) # Crea una pagina la cual tiene los inputs del registro rellenados con los datos del mismo

database.close_database()  # Cierra la BDD