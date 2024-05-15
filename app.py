from conectar import *
from flask import *
from flask import request
from crud import insertar_libro, eliminar_libro, insertar_autor, eliminar_autor, insertar_cliente, eliminar_cliente


db = conexion()

app = Flask(__name__, static_folder="templates")
@app.route('/')
def home():
    coleccion_libros = db.libros.find()
    coleccion_autores = db.autores.find()
    coleccion_clientes = db.clientes.find()
    coleccion_pedidos = db.pedidos.find()
    return render_template('index.html',
                            libros=coleccion_libros,
                            autores=coleccion_autores,
                            clientes=coleccion_clientes,
                            pedidos=coleccion_pedidos)

@app.route('/libros', methods=['GET', 'POST'])
def libros():
    if request.method == 'POST':
        id_libro = request.form['id_libro']
        titulo = request.form['titulo']
        id_autor = request.form['id_autor']
        precio = request.form['precio']
        stock = request.form['stock']
    
        nuevo_libro = {
            "libros": {
                "id_libro": id_libro,
                "titulo": titulo,
                "autor_id": id_autor,
                "precio": precio,
                "stock": stock
            }
        }
        insertar_libro(nuevo_libro)
    libros_db = db.libros.find()    
    return render_template('libros.html', libros = libros_db)

@app.route('/autores', methods=['GET', 'POST'])
def autores():
    if request.method == 'POST':
        autor_id = request.form['autor_id']
        nombre_autor = request.form['nombre_autor']
        nacionalidad = request.form['nacionalidad']
    
        nuevo_autor = {
            "autores": {
                "autor_id": autor_id,
                "nombre_autor": nombre_autor,
                "nacionalidad": nacionalidad
            }
        }
        insertar_autor(nuevo_autor)
    autores_db = db.autores.find()    
    return render_template('autores.html', autores = autores_db)

@app.route('/clientes', methods=['GET','POST'])
def clientes():
    if request.method == 'POST':
        id_cliente = request.form['id_cliente']
        nombre = request.form['nombre']
        email = request.form['email']
    
        nuevo_cliente = {
            "clientes": {
                "id_cliente": id_cliente,
                "nombre": nombre,
                "email": email
            }
        }
        insertar_cliente(nuevo_cliente)
    clientes_db = db.clientes.find()    
    return render_template('clientes.html', clientes = clientes_db)

@app.route('/libros/eliminar', methods=['POST'])
def eliminar_elemento_libro():
    if request.method == 'POST':
        id_libro = request.form['id'] 
        eliminar_libro(id_libro)
    return redirect('/libros')

@app.route('/autores/eliminar', methods=['POST'])
def eliminar_elemento_autor():
    if request.method == 'POST':
        id_autor = request.form['id'] 
        eliminar_autor(id_autor)
    return redirect('/autores')

@app.route('/clientes/eliminar', methods=['POST'])
def eliminar_elemento_clientes():
    if request.method == 'POST':
        id_cliente = request.form['id'] 
        eliminar_cliente(id_cliente)
    return redirect('/clientes')

@app.route('/pedidos')
def pedidos():
    pedidos = db.pedidos.find()    
    return render_template('pedidos.html', pedidos = pedidos)

if __name__ == '__main__':
    app.run(debug=True)