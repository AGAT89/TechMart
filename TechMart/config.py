import pyodbc

class Config:
    """
    Configuración para la conexión a la base de datos SQL Server.
    """
    SERVER = 'DbTechMart.mssql.somee.com'
    DATABASE = 'DbTechMart'
    USERNAME = 'agat_SQLLogin_1'
    PASSWORD = 'uud5pzxn2s'
    
    # Cadena de conexión a la base de datos SQL Server
    CONNECTION_STRING = (
        "DRIVER={SQL Server};"
        f"SERVER={SERVER};"
        f"DATABASE={DATABASE};"
        f"UID={USERNAME};"
        f"PWD={PASSWORD};"
        "TrustServerCertificate=YES;"
    )

class DatabaseConnection:
    """
    Clase para gestionar la conexión a la base de datos utilizando pyodbc.
    """
    def __init__(self):
        self.connection = None
        self.cursor = None

    def connect(self):
        """
        Establece la conexión a la base de datos.
        """
        try:
            self.connection = pyodbc.connect(Config.CONNECTION_STRING)
            self.cursor = self.connection.cursor()
            print("Conexión a la base de datos exitosa.")
        except Exception as e:
            print(f"Error al conectar a la base de datos: {e}")

    def disconnect(self):
        """
        Cierra la conexión a la base de datos.
        """
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
            print("Conexión cerrada.")

    def execute_query(self, query, params=None):
        """
        Ejecuta una consulta SQL y retorna los resultados.
        
        :param query: Consulta SQL a ejecutar.
        :param params: Parámetros opcionales para la consulta.
        :return: Lista con los resultados o None en caso de error.
        """
        try:
            if not self.connection:
                self.connect()
            if params is None:
                params = []
            self.cursor.execute(query, params)
            result = self.cursor.fetchall()
            return result
        except Exception as e:
            print(f"Error al ejecutar la consulta: {e}")
            return None

def get_db_connection():
    """
    Crea y retorna una nueva conexión directa a la base de datos utilizando pyodbc.
    Se usa en las rutas para obtener una conexión que permite invocar cursor() y close().
    """
    try:
        connection = pyodbc.connect(Config.CONNECTION_STRING)
        print("Conexión directa a la base de datos exitosa.")
        return connection
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None
