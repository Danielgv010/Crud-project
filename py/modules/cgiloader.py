import cgi ,os
import cgitb; cgitb.enable()

# Si se va a usar este .py el form necesita tener enctype="multipart/form-data" y method="post" como atributos

def directory_exists(directory): # Comprueba que el directorio donde se guardará el archivo existe
    if not os.path.isdir(directory): # Si no existe la carpeta
        os.mkdir(directory) # Crea la carpeta

def save_file(file_selector_name, file_directory): # Hace una copia del archivo subido por el usuario en el directorio que se le indica a la funcion
    directory_exists(file_directory)  # Comprueba que el directorio donde se guardará el archivo existe
    form = cgi.FieldStorage() # Crea un objeto cgi
    file_item = form[file_selector_name] # Pilla el archivo subido en el formulario
    if file_item.filename: # Comprueba que se haya seleccionado un fichero
        file_name = os.path.basename(file_item.filename) # Extrae el nombre del fichero de la ruta
        open(f"{file_directory}{file_name}","wb").write(file_item.file.read()) # Copia el fichero subido por el usuario en un directorio local con el mismo nombre
    return file_name


def create_table(file_directory, file_name, separator): # Devuelve una tabla con los datos del fichero
    table = "<table border='1px solid'>" # Variable donde se guardará la tabla html
    with open(file_directory+file_name) as file: # Abre el fichero en modo lectura
        header = file.readline().split(separator) # Hace un array separando la primera linea del fichero por el separador que se le pasa a la funcion
        header = [element.strip() for element in header] # Elimina los espacios vacíos de los valores del array
        table += "<tr>" # Se añade el principio del primer tr a la tabla
        for value in header: # Por cada valor del array header
            table += f"<th>{value}</th>" # Se añaden los valores de la cabecera dentro de un <th/> y luego el <th/> a la tabla
        table += "</tr>" # Se añade el final del primer tr a la tabla
        for line in file: # Por cada linea restante en el fichero
            table += "<tr>" # Se añade una etiqueta <tr> a la tabla
            for data in line.split(separator): # Hace un array separando la primera linea del fichero por el separador que se le pasa a la funcion
                table += f"<td>{data.strip()}</td>" # Se añade cada valor dentro de un <td/> y luego el <td/> a la tabla
            table += "<tr>" # Se añade una etiqueta </tr> a la tabla
        table += "</table>" # Se añade la etiqueta de cierre a la tabla
        return table # Devuleve la tabla

def create_list(file_directory, file_name, separator): # Crea la lista
    list = "<ol>" # Inicio de la lista
    with open(file_directory+file_name) as file: # Abre el fichero en modo lectura
        for i, value in enumerate(file.read().split(separator)): # Lee el fichero, lo mete en un array separandolo por el separator pasado a la funcion y recorre el array almacenando el número de iteración en i
            if i == 0: # Si es la primera iteracion del for
                list += f"<h1>{value}</h1>" # Crea un h1
            else: # Si no es la primera iteracion
                list += f"<li>{value}</li>" # Crea un li
    list += "</ol>" # Fin de la lista
    return list # Devuelve la lista
