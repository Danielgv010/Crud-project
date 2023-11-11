import http.cookies
import os


def get_cookies(): # Devuelve una lista con las cookies activas
    return os.environ.get("HTTP_COOKIE")

def check_cookie_existence(cookie_name): # Comprueba que la cookie con el nombre que se le pasa a la funcion exista en la lista de cookies activas
    cookie = http.cookies.SimpleCookie() # Crea un objeto cookie vacio
    cookie.load(get_cookies()) # Carga las cookies activas en el objeto cookie
    return cookie_name in cookie # Devuelve true si la cookie con el nombre que se pasó existe o false si no existe

def print_cookie(cookie): # Imprime la cookie
    print("Content-type: text/html") # Imprime la cabecera html necesaria para la cookie
    print(cookie) # Imprime la cookie
    print() # Imprime una linea en blanco

def create_cookie(cookie_name, cookie_value, cookie_expiration): # Crea una cookie con los valores que se le pasan
    cookie = http.cookies.SimpleCookie() # Crea un objeto cookie vacio
    cookie[cookie_name] = cookie_value # Le asigna un nombre y un valor a la cookie
    if cookie_expiration != 0: # Si se añade una fecha de expiración a los parámetros de la funcion
        cookie[cookie_name]["expires"] = cookie_expiration # Añade la fecha de expiración a la cookie
    print_cookie(cookie) # Imprime la cookie

def delete_cookie(cookie_name): # Borra la cookie que se le indique a la funcion
    cookie = http.cookies.SimpleCookie() # Crea un objeto cookie vacio
    cookie[cookie_name] = 1 # Le asigna un valor a la cookie
    cookie[cookie_name]["expires"] = "Fri, 10 Oct 2023 07:30:00 GMT;" # Añade una fecha de expiración anterior a la fecha actual para que se borre la cookie
    print_cookie(cookie) # Imprime la cookie

def update_cookie(cookie_name, cookie_value, cookie_expiration): # Modifica el valor y la expiración de la cookie
    cookie = http.cookies.SimpleCookie() # Crea un objeto cookie vacio
    cookie[cookie_name] = cookie_value # Asigna el nuevo valor a la cookie
    cookie[cookie_name]["expires"] = cookie_expiration # Asigna la nueva fecha de expiracion a la cookie
    print_cookie(cookie) # Imprime la cookie

def update_cookie_value(cookie_name, cookie_value): # Modifica el valor de la cookie
    cookie = http.cookies.SimpleCookie() # Crea un objeto cookie vacio
    cookie[cookie_name] = cookie_value # Asigna el nuevo valor a la cookie
    print_cookie(cookie) # Imprime la cookie

def update_cookie_expiration(cookie_name, cookie_expiration): # Modifica el valor de la cookie
    cookie = http.cookies.SimpleCookie() # Crea un objeto cookie vacio
    cookie.load(get_cookies()) # Carga las cookies activas en el objeto cookie
    cookie[cookie_name] = cookie[cookie_name].value # Asigna el mismo valor a la cookie
    cookie[cookie_name]["expires"] = cookie_expiration # Asigna la nueva fecha de expiracion a la cookie
    print_cookie(cookie) # Imprime la cookie

def get_cookie_value(cookie_name): # Devuelve el valor de la cookie con el nombre que se le pasa a la funcion
    cookie = http.cookies.SimpleCookie() # Crea un objeto cookie vacio
    cookie.load(get_cookies()) # Carga las cookies activas en el objeto cookie
    return cookie[cookie_name].value

def counter_cookie(cookie_name, operator):
    cookie = http.cookies.SimpleCookie() # Crea un objeto cookie vacio
    cookie.load(get_cookies()) # Carga las cookies activas en el objeto cookie
    if operator == "+": # Si se quiere incrementar el valor de la cookie
            cookie[cookie_name] = int(cookie[cookie_name].value) + 1
    elif operator == "-": # Si se quiere decrementar el valor de la cookie
            cookie[cookie_name] = int(cookie[cookie_name].value) - 1
    print_cookie(cookie) # Imprime la cookie

