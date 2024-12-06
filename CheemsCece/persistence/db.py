import mysql.connector
from mysql.connector import Error

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='carlos04',  # Cambia esta contraseña si es necesario
            database='localhost'  # Asegúrate de que el nombre de la base de datos sea correcto
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print("Error while connecting to MySQL", e)
        return None