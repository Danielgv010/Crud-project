#!C:\Users\deras\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\python.exe

import uuid
import modules.cookies
import htmlCode
import os, json, hashlib
from urllib.parse import parse_qs

# Obtener los parametros que envía el formulario
parameter = parse_qs(os.environ.get('QUERY_STRING'))

data_directory = '../data/';data_file = 'accounts.json' # Ruta del archivo .json

def parameter_validation():
    expected_parameters = ["email","password"] # Parámetros a comprobar que están

    for expected in expected_parameters: # Por cada parámetro esperado
        if expected not in parameter: # Si falta en la url
            htmlCode.message_page("error", f"{expected} parameter cant be missing", "main.py") # Muestra mensaje de error
            exit() # Se sale del python
        if parameter[expected][0] == "": # Si el parámetro está vacío
            htmlCode.message_page("error", f"{expected} cant be empty", "main.py") # Muestra un mensaje de error
            exit() # Se sale del python

    #Recupera los parámetros de la URL
    email = parameter["email"][0]
    password = parameter["password"][0]
    
    password_encode = hashlib.sha512(str.encode(password)).hexdigest() # Encripta la contraseña

    return email,password_encode # Devuelve el email y la contraseña encriptada

credentials = parameter_validation() # Guarda las credenciales

with open(data_directory+data_file) as file: # Abre el fichero en modo lectura
    try: # Intenta cargar el json en la variable
        account_list = json.load(file)
    except: # Si el json está vacío crea un array
        account_list = []

    for account_iterator in account_list: # Por cada cuenta en la lista de cuentas
        if account_iterator[1] == credentials[0] and account_iterator[2]==credentials[1]: # Si coincide el email y la contraseña
            modules.cookies.create_cookie("LOGIN",uuid.uuid1(),"Mon, 13 Nov 2023 07:30:00 GMT;") # Se crea una cookie con el nombre LOGIN, un valor aleatorio y que expira el lunes 13
            htmlCode.message_page("success", f"Youve logged in as {account_iterator[0]}", "crud.py") # Muestra un mensaje de éxito
            exit() # Se sale del python

htmlCode.message_page("error", "Invalid login", "main.py") # Si no ha iniciado sesión muestra mensaje de error