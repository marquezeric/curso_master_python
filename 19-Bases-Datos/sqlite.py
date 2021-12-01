#  Importando módulo
import sqlite3

#  Conexión
conexion = sqlite3.connect('./19-Bases-Datos/pruebas.db')

#  Crear un cursor
cursor = conexion.cursor()

#  Crear una tabla
cursor.execute("""
CREATE TABLE IF NOT EXISTS productos("
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo varchar(255),
    descripcion text,
    precio int(255)"
);
""")

#  Guardar cambios
conexion.commit()

#  Insertar datos
"""
cursor.execute("INSERT INTO productos VALUES(NULL, 'Segundo producto', 'Descripción de mi producto', 550)")
conexion.commit()
"""

#  Borrar registros
#cursor.execute("DELETE FROM productos;")
#conexion.commit()


# Insertar muchos registro de golpe
productos = [
    ("Ordenador Portatil", "Buen equipo", 700),
    ("Teléfono Movil", "Buen teléfono", 140),
    ("Placa Base", "Buena placa", 80),
    ("Tablet", "Buena tablet", 300),
]
cursor.executemany("INSERT INTO productos VALUES(null,?,?,?)", productos)
conexion.commit()

# Actualizar datos UPDATE
cursor.execute("UPDATE productos SET precio = 678 WHERE precio = 80;")
conexion.commit()

#  Listar datos
#cursor.execute("SELECT * FROM productos;")
cursor.execute("SELECT * FROM productos WHERE precio >= 300;")
productos = cursor.fetchall()
#print(productos)


for producto in productos:
    print("ID: ", producto[0])
    print("Título: ", producto[1])
    print("Descripción: ", producto[2])
    print("Precio: ", producto[3])
    print("\n")


cursor.execute("SELECT titulo FROM productos;")
producto = cursor.fetchone()
print(producto)


#  Cerrar Conexión
conexion.close()