from psycopg2 import connect
conexion = connect("dbname=empresa user=postgres password=root")
cursor = conexion.cursor()
cursor.execute("SELECT * FROM datos;")
respuesta = cursor.fetchall()
print(respuesta)