import mysql.connector
from mysql.connector import Error

def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='Jesus_041104',
        database='cheems'
    )   
    