from flask import Flask
from flask.helpers import url_for
from flask import url_for
from flask import redirect
from flask import render_template
from flask import request
from flask import flash
from datetime import datetime
from flask.scaffold import _matching_loader_thinks_module_is_package
from flaskext.mysql import MySQL
import pymysql


#  Creación de nuestra primera aplicación en Flask
app = Flask(__name__)  #  Instanciar el nombre de nuestra aplicación
api = MySQL(app)

app.secret_key = 'clave_secreta_flask'

# Conexión de la Base de Datos
db = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = 'Tov@rLd5',
    db = 'proyectoflask'
)

#  Context processor
@app.context_processor
def date_now():
    return {
        'now': datetime.utcnow()
    }

#  Endpoint

@app.route('/')
def index():
    edad = 123

    personas=['Juan','Ricardo','Elmer','Jaime','Eric']

    return render_template('index.html',
                            edad=edad,
                            dato1='Dato1',
                            dato2='Dato2',
                            lista=["uno","dos","tres"],
                            personas=personas
                        )


@app.route('/informacion')  #  Para trabajar con parámetros opcionales
@app.route('/informacion/<string:nombre>')
@app.route('/informacion/<string:nombre>/<string:apellidos>')
def informacion(nombre = None, apellidos = None):
    
    texto = ""
    if nombre != None and apellidos != None:
        texto = f"Bienvenido {nombre} {apellidos}"
    
    return render_template('informacion.html', 
                            texto = texto
                            )

@app.route('/contacto')
@app.route('/contacto/<redireccion>')
def contacto(redireccion = None):
    if redireccion is not None:
        return redirect(url_for('lenguajes')) 

    return render_template('contacto.html')

@app.route('/lenguajes-de-programación')
def lenguajes():
    #return "<h1>Página de lenguajes</h1>"
    return render_template('lenguajes.html')

@app.route('/crear-coche', methods=['GET','POST'])
def crear_coche():
    if request.method == 'POST':
        
        marca = request.form['marca']
        modelo = request.form['modelo']
        precio = request.form['precio']
        ciudad = request.form['ciudad']

        #return f"{marca} {modelo} {precio} {ciudad}" # Solo visualizo la información en pantalla

        cursor = db.cursor()
        cursor.execute("INSERT INTO coches VALUES (NULL,%s, %s, %s, %s)", (marca, modelo, precio, ciudad))
        cursor.connection.commit()
        flash("Has registrado el coche correctamente")
        return redirect(url_for('index'))
    
    return render_template('crear_coche.html')

@app.route('/coches')
def coches():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM coches ORDER BY id DESC")
    coches = cursor.fetchall()
    cursor.close()

    return render_template('coches.html', coches=coches)

@app.route('/coche/<coche_id>')
def coche(coche_id):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM coches WHERE id = %s", (coche_id))
    coches = cursor.fetchall()
    cursor.close()

    return render_template('coche.html', coche=coches[0])

@app.route('/borrar-coche/<coche_id>')
def borrar_coche(coche_id):
    cursor = db.cursor()
    #cursor.execute("DELETE FROM coches WHERE id = %s" (coche_id))
    cursor.execute(f"DELETE FROM coches WHERE id = {coche_id}")
    cursor.connection.commit()

    flash("El coche ha sido eliminado !!")

    return redirect(url_for('coches'))

@app.route('/editar-coche/<coche_id>', methods=['GET', 'POST'])
def editar_coche(coche_id):
    if request.method == 'POST':
            
            marca = request.form['marca']
            modelo = request.form['modelo']
            precio = request.form['precio']
            ciudad = request.form['ciudad']

            #return f"{marca} {modelo} {precio} {ciudad}" # Solo visualizo la información en pantalla

            cursor = db.cursor()
            cursor.execute("""
                UPDATE coches 
                SET marca = %s,
                    modelo = %s,
                    precio = %s,
                    ciudad = %s
                WHERE id = %s
            """, (marca, modelo, precio, ciudad, coche_id))
            cursor.connection.commit()
            
            flash("Has editado el coche correctamente")

            return redirect(url_for('coches'))

    cursor = db.cursor()
    cursor.execute("SELECT * FROM coches WHERE id = %s", (coche_id))
    coches = cursor.fetchall()
    cursor.close()

#  Reutilizmos la vista de crear coche solamente le pasamos los parámetros correctos
    return render_template('crear_coche.html', coche=coches[0])


if __name__ == '__main__':
    app.run(debug=True)