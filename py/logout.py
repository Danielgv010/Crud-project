#!C:\Users\deras\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\python.exe

import modules.cookies
import htmlCode

modules.cookies.delete_cookie("LOGIN") # Borra la cookie LOGIN
htmlCode.message_page("info","You logged out and you are being redirected to the home page","main.py") # Muestra un mensaje de info que indica que se ha cerrado la sesión y redirige a la pagina principal