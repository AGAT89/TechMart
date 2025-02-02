from flask import Blueprint, request, jsonify
from config import mysql

routes = Blueprint('routes', __name__)

# Obtener todos los productos
@routes.route('/productos', methods=['GET'])
def obtener_productos():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    cursor.close()
    return jsonify(productos)

# Agregar un nuevo producto
@routes.route('/productos', methods=['POST'])
def agregar_producto():
    data = request.json
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO productos (nombre, descripcion, precio, stock) VALUES (%s, %s, %s, %s)", 
                   (data['nombre'], data['descripcion'], data['precio'], data['stock']))
    mysql.connection.commit()
    cursor.close()
    return jsonify({"mensaje": "Producto agregado correctamente"}), 201

# Actualizar un producto
@routes.route('/productos/<int:id>', methods=['PUT'])
def actualizar_producto(id):
    data = request.json
    cursor = mysql.connection.cursor()
    cursor.execute("UPDATE productos SET nombre=%s, descripcion=%s, precio=%s, stock=%s WHERE id=%s",
                   (data['nombre'], data['descripcion'], data['precio'], data['stock'], id))
    mysql.connection.commit()
    cursor.close()
    return jsonify({"mensaje": "Producto actualizado correctamente"})

# Eliminar un producto
@routes.route('/productos/<int:id>', methods=['DELETE'])
def eliminar_producto(id):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM productos WHERE id=%s", (id,))
    mysql.connection.commit()
    cursor.close()
    return jsonify({"mensaje": "Producto eliminado correctamente"})
