#!C:\Users\deras\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\python.exe

import modules.cgiloader
import modules.database
import htmlCode

file_name = modules.cgiloader.save_file("file-item","../data/") # Guarda el nombre del fichero subido por el usuario aparte de hacer una copia del fichero en ../data/

database = modules.database.Database_Manager("localhost","videojuegos","videojuegos","videojuegos") # Hace una conexion con la base de datos
column_name = ["name","company","theme","player_count","release_date"] # Nombres de las columnas de la BDD
with open("../data/"+file_name,"r") as file: # Abre la copia del fichero en modo lectura
    for line in file: # Por cada linea en el fichero
        database.insert("videojuegosantiguos",column_name,line.split(";")) # Separa la linea por los ; y lo guarda en un array el cual pasa al metodo insert para insertar cada linea en la BDD

database.close_database() # Cierra la BDD
htmlCode.message_page("success","Rows inserted","crud.py") # Muestra un mensaje de éxito