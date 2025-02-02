from flask import Blueprint, request, jsonify
from config import get_db_connection

routes = Blueprint('routes', __name__)

# Obtener todos los productos
@routes.route('/productos', methods=['GET'])
def obtener_productos():
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, nombre, descripcion, precio, stock FROM productos")
        productos = [
            {"id": row[0], "nombre": row[1], "descripcion": row[2], "precio": row[3], "stock": row[4]}
            for row in cursor.fetchall()
        ]
        cursor.close()
        conn.close()
        return jsonify(productos)
    else:
        return jsonify({"error": "No se pudo conectar a la base de datos"}), 500

# Agregar un nuevo producto
@routes.route('/productos', methods=['POST'])
def agregar_producto():
    data = request.json
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO productos (nombre, descripcion, precio, stock) VALUES (?, ?, ?, ?)",
            (data['nombre'], data['descripcion'], data['precio'], data['stock'])
        )
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"mensaje": "Producto agregado correctamente"}), 201
    else:
        return jsonify({"error": "No se pudo conectar a la base de datos"}), 500

# Actualizar un producto
@routes.route('/productos/<int:id>', methods=['PUT'])
def actualizar_producto(id):
    data = request.json
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE productos SET nombre=?, descripcion=?, precio=?, stock=? WHERE id=?",
            (data['nombre'], data['descripcion'], data['precio'], data['stock'], id)
        )
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"mensaje": "Producto actualizado correctamente"})
    else:
        return jsonify({"error": "No se pudo conectar a la base de datos"}), 500

# Eliminar un producto
@routes.route('/productos/<int:id>', methods=['DELETE'])
def eliminar_producto(id):
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM productos WHERE id=?", (id,))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"mensaje": "Producto eliminado correctamente"})
    else:
        return jsonify({"error": "No se pudo conectar a la base de datos"}), 500
