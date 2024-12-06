from persistence.db import get_db_connection
from mysql.connector import Error

class Paquete: 
    def __init__(self, id=None, id_cliente=None, fecha_envio=None, fecha_llegada=None, tamano=None, codigo_paquete=None, estado=None):
        self.id = id  # El id del paquete
        self.id_cliente = id_cliente
        self.fecha_envio = fecha_envio
        self.fecha_llegada = fecha_llegada
        self.tamano = tamano
        self.codigo_paquete = codigo_paquete
        self.estado = estado

    @classmethod
    def get_all(cls):
        try:
            connection = get_db_connection()
            cursor = connection.cursor(dictionary=True)
            cursor.execute('SELECT * FROM paquetes')
            return cursor.fetchall()
        except Error as e:
            print(f"Error al obtener todos los paquetes: {e}")
            return []
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    @classmethod
    def get_by_codigo(cls, codigo_paquete):
        try:
            connection = get_db_connection()
            cursor = connection.cursor(dictionary=True)
            cursor.execute('SELECT * FROM paquetes WHERE codigo_paquete = %s', (codigo_paquete,))
            return cursor.fetchone()  # Devuelve el primer paquete que coincida con el código
        except Error as e:
            print(f"Error al obtener paquete por código: {e}")
            return None
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    @classmethod
    def save(cls, paquete):
        try:
            connection = get_db_connection()
            cursor = connection.cursor()
            query = '''
                INSERT INTO paquetes (id_cliente, fecha_envio, fecha_llegada, tamano, codigo_paquete, estado) 
                VALUES (%s, %s, %s, %s, %s, %s)
            '''
            cursor.execute(query, (paquete.id_cliente, paquete.fecha_envio, paquete.fecha_llegada,
                                   paquete.tamano, paquete.codigo_paquete, paquete.estado))
            connection.commit()
            return cursor.lastrowid  # Retorna el id del registro recién insertado
        except Error as e:
            print(f"Error al guardar paquete: {e}")  # Mensaje de error para debugging
            raise Exception("Error al guardar el paquete en la base de datos")
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    @classmethod
    def update(cls, id, paquete):
        try:
            connection = get_db_connection()
            cursor = connection.cursor()
            query = '''
                UPDATE paquetes 
                SET id_cliente = %s, fecha_envio = %s, fecha_llegada = %s, tamano = %s, 
                    codigo_paquete = %s, estado = %s 
                WHERE id = %s
            '''
            cursor.execute(query, (paquete.id_cliente, paquete.fecha_envio, paquete.fecha_llegada,
                                   paquete.tamano, paquete.codigo_paquete, paquete.estado, id))
            connection.commit()
            return cursor.rowcount  # Devuelve la cantidad de filas afectadas
        except Error as e:
            print(f"Error al actualizar paquete: {e}")
            raise Exception("Error al actualizar el paquete en la base de datos")
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    @classmethod
    def get_by_id(cls, id):
        try:
            connection = get_db_connection()
            cursor = connection.cursor(dictionary=True)
            cursor.execute('SELECT * FROM paquetes WHERE id = %s', (id,))
            return cursor.fetchone()  # Devuelve el paquete por su id
        except Error as e:
            print(f"Error al obtener paquete por ID: {e}")
            return None
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()
