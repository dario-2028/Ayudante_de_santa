import mysql.connector


def get_database_connection():
    try:
        # Configuración de la base de datos
        db_config = {
            "host": "localhost",
            "user": "root",
            "password": "",
            "database": "formularios",
            "port": 3306,  # Este es el puerto por defecto para MySQL, ajusta según sea necesario
        }

        # Crear la conexión a la base de datos
        connection = mysql.connector.connect(**db_config)

        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
