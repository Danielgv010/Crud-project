import mysql.connector, sys

# Donde se pidan valores (filter_values, values, id) hay que pasarlos como lista

class Database_Manager:
    def __init__(self, db_host, db_user, db_password, db_database): # Crea la conexión con la BDD basandose en los parametros que se pasan al constructor
        self.database_connection = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_database)
    
    def fetch_all(self, table, order): # Devuelve todos los registros de una tabla con el orden que se le indique
        db_cursor = self.database_connection.cursor() # Crea un cursor
        query = f"SELECT * FROM {table} " # Crea la consulta SQL
        if order != 0: # Si el usuario pasó algo distinto a 0 en el parámetro order
            query += f"ORDER BY {order}" # Se añade un orden a la consulta SQL con lo que pasó en el parámetro
        sys.stderr.write(str(query)+"\n") # Escribe la consulta completa en el log de errores de apache
        db_cursor.execute(query) # Ejecuta la consulta SQL
        result = db_cursor.fetchall() # Guarda los resultados de la consulta SQL en una variable
        db_cursor.close() # Cierra el cursor
        return result # Devuelve los resultados de la consulta
    
    # !!! No poner unique = True si el resultado trae multiples lineas !!!
    # Solo sirve para filtrar con este formato ==> columna = valor
    def fetch_filtered(self, table, order, filter_columns, filter_values, unique): # Devuelve todos los registros de una tabla que coincidan con una serie de filtros
        iterator = 0 # Iterador para saber cuantos filtros hay
        db_cursor = self.database_connection.cursor() # Crea un cursor
        query = f"SELECT * FROM {table} WHERE " # Crea la consulta SQL
        for column in filter_columns: # Por cada columna que se quiera filtrar
            iterator += 1 # Se añade 1 al numero de iteraciones
            query += column + " = %s " # Se añade la columna = %s a la consulta
            if iterator<len(filter_columns): # Si hay más filtros que añadir
                query += "AND " # Se añade AND a la consulta SQL y el for vuelve a ejecutarse
        if order != 0: # Si el usuario pasó algo distinto a 0 en el parámetro order
            query += f"ORDER BY {order}" # Se añade un orden a la consulta SQL con lo que pasó en el parámetro
        sys.stderr.write(str(query)+"\n") # Escribe la consulta completa en el log de errores de apache
        db_cursor.execute(query,filter_values) # Ejecuta la consulta SQL rellenando los %s con las posiciones del array filter_values
        if unique: # Si se indica al metodo que el resultado es unico (Un id por ejemplo)
            result = db_cursor.fetchone() # Guarda solo un registro de la consulta en la variable
        else: # Si se indica al metod que el resultado no es unico
            result = db_cursor.fetchall() # Guarda todos los registros de la consulta en la variable
        db_cursor.close() # Cierra el cursor
        return result # Devuelve los resultados de la consulta

    def custom_query_fetch(self, table, custom_query, values): # Permite crear una consulta a la bdd
        db_cursor = self.database_connection.cursor() # Crea un cursor
        query = f"SELECT * FROM {table} WHERE {custom_query}" # Crea la consulta SQL
        db_cursor.execute(query, values) # Ejecuta la consulta SQL rellenando los %s con las posiciones del array values
        result = db_cursor.fetchall() # Guarda todos los registros de la consulta en la variable
        sys.stderr.write(str(query)+"\n") # Escribe la consulta completa en el log de errores de apache
        db_cursor.close() # Cierra el cursor
        return result # Devuelve los resultados de la consulta

    def insert(self, table, column_name, values): # Inserta un nuevo registro en la BDD
        iterator = 0 # Iterador para saber cuantas columnas hay
        db_cursor = self.database_connection.cursor() # Crea un cursor
        query = f"INSERT INTO {table} (" # Crea la primera parte de la consulta SQL
        query_values = "" # Crea una variable donde meter la parte de VALUES() de la consulta SQL
        for name in column_name: # Por cada columna que se le haya pasado al metodo
            iterator += 1 # Se añade 1 al numero de iteraciones 
            query+=name # Se añade el nombre de la columna a la consulta
            query_values += "%s" # Se añade %s a la parte de VALUES()
            if iterator<len(column_name): # Si hay más columnas que añadir
                query += ", " # Se añade , a la consulta
                query_values += ", " # Se añade , a la parte de VALUES() y el for vuelve a ejecutarse
        query += f") VALUES ({query_values})" # Se añade la parte de VALUES() completada a la consulta SQL
        sys.stderr.write(str(query)+"\n") # Escribe la consulta completa en el log de errores de apache
        db_cursor.execute(query,values) # Ejecuta la consulta SQL rellenando los %s con las posiciones del array values
        self.database_connection.commit() # Se aplican los cambios en la BDD
        db_cursor.close() # Cierra el cursor

    def delete_with_id(self, table, id): # Borra un registro a partir de un id
        db_cursor = self.database_connection.cursor() # Crea un cursor
        query = f"DELETE FROM {table} " + "WHERE id = %s" # Crea la consulta SQL
        sys.stderr.write(str(query)+"\n") # Escribe la consulta completa en el log de errores de apache
        db_cursor.execute(query, id) # Ejecuta la consulta SQL rellenando los %s con las posiciones del array id
        self.database_connection.commit() # Se aplican los cambios en la BDD
        db_cursor.close() # Cierra el cursor


    def modify(self, table, column_name, values, filter_columns, filter_values): # Modifica un registro de la BDD
        iterator = 0 # Iterador para saber cuantas columnas hay
        iterator2 = 0 # Iterador para saber cuantos filtros hay
        db_cursor = self.database_connection.cursor() # Crea un cursor
        query = f"UPDATE {table} SET " # Crea la consulta SQL
        for name in column_name: # Por cada columna que se quiera modificar
            iterator += 1 # Se añade 1 al numero de iteraciones
            query += name + " = %s" # Se añade la columna = %s a la consulta SQL
            if iterator<len(column_name): # Si hay más columnas que modificar
                query += ", " # Se añade , a la consulta SQL y el for vuelve a ejecutarse
        if filter_columns != 0: # Si se quiere hacer la modificación a unas columnas en específico
            query += " WHERE " # Se añade WHERE a la consulta SQL
            for column in filter_columns: # Por cada columna que se quiera filtrar
                iterator2 += 1 # Se añade 1 al numero de iteraciones
                query += column + " = %s " # Se añade la columna = %s a la consulta SQL
                if iterator2<len(filter_columns): # Si hay más filtros que añadir
                    query += "AND " # Se añade AND a la consulta SQL y el for vuelve a ejecutarse
        sys.stderr.write(str(query)+"\n") # Escribe la consulta completa en el log de errores de apache
        db_cursor.execute(query,values+filter_values) # Ejecuta la consulta SQL rellenando los %s con las posiciones del array values y el array filter_values
        self.database_connection.commit() # Se aplican los cambios en la BDD
        db_cursor.close() # Cierra el cursor

    def close_database(self): # Cierra la BDD
        self.database_connection.close()