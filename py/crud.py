#!C:\Users\deras\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\python.exe

import modules.cookies
import modules.database
import htmlCode

if modules.cookies.get_cookies() == None or not modules.cookies.check_cookie_existence("LOGIN"): # Si no hay cookies o la cookie de LOGIN no está
    htmlCode.message_page("error","You are not logged in","main.py") # Muestra mensaje de error
    exit() # Se sale del python

database = modules.database.Database_Manager("localhost","videojuegos","videojuegos","videojuegos") # Hace una conexion con la base de datos

htmlCode.crud(database.fetch_all("videojuegosantiguos","name")) # Devuelve todos los registros de la tabla videojuegosantiguos ordenados por la columna name

database.close_database() # Cierra la BDD
