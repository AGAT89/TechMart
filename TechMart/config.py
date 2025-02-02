import pyodbc

# Configuración de conexión
server = 'DbTechMart.mssql.somee.com'
database = 'DbTechMart'
username = 'agat_SQLLogin_1'
password = 'uud5pzxn2s'

# Cadena de conexión
conn_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password};TrustServerCertificate=YES'

try:
    # Intentar la conexión
    conn = pyodbc.connect(conn_string)
    cursor = conn.cursor()
    
    # Probar la conexión con una consulta simple
    cursor.execute("SELECT 1 AS Test")
    result = cursor.fetchone()
    print(f"Conexión exitosa: {result[0]}")
    
    # Cierra la conexión
    cursor.close()
    conn.close()
    
except Exception as e:
    print(f"Error al conectar: {e}")
