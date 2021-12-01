import mysql.connector

#  conexión
database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "master_python"
)

#  ¿La conexión ha sido correcta?
#  print(database)  #  Verificar conexión

#  Cursor
cursor = database.cursor(buffered=True)

#  Crear Base de Datos
"""
cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")

#  Mostrar Bases de Datos
cursor.execute("SHOW DATABASES")

for bd in cursor:
    print(bd)
"""

#  Crear tablas
cursor.execute("""
CREATE TABLE IF NOT EXISTS vehiculos(
    id int(10) auto_increment not null,
    marca varchar(40) not null,
    modelo varchar(40) not null,
    precio float(10,2) not null,
    CONSTRAINT pk_vehiculo PRIMARY KEY(id)
)
""")

#  Mostrar las tablas que contiene nuestra base de datos
cursor.execute("SHOW TABLES")

for tables in cursor:
    print(tables)

#  Insertar registro
#cursor.execute("INSERT INTO vehiculos VALUES(null,'Seat','Ibiza', 8500)")
#cursor.execute("INSERT INTO vehiculos VALUES(null,'Renault','Clio', 15000)")

"""
#  Insertar Varios registros por medio de una lista con diferentes tuplas
coches = [
    ('VolksWagen','Caribe',10000),
    ('Chevrolet','Chevy',32000),
    ('Suzuki','SX4',85000),
    ('Audi','e-tron',150000)
]
"""
#cursor.executemany("INSERT INTO vehiculos VALUES(null, %s, %s, %s)", coches)

database.commit()

cursor.execute("SELECT * FROM vehiculos")

result = cursor.fetchall()

print("-----------Todos los coches--------------")

for coche in result:
    #print(coche)
    print(coche[1], coche[2], coche[3])

print("\n-----------El primero de mi tabla--------------")
cursor.execute("SELECT * FROM vehiculos")
coche = cursor.fetchone()
print(coche)

#  Borrar Registros
"""
cursor.execute("DELETE FROM vehiculos WHERE marca = 'Seat'")
database.commit()

print(cursor.rowcount, " borrados!!")

"""
#  Actualizar

cursor.execute("UPDATE vehiculos SET modelo = 'León' WHERE marca = 'Seat' ")
database.commit()
print(cursor.rowcount, " actualizados!!")
