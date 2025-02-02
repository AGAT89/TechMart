from flask import Flask, render_template, jsonify
from config import mysql, Config
from routes import routes
from flask_cors import CORS

app = Flask(__name__, template_folder="templates")  # 👈 Asegura que Flask sabe dónde están los templates
app.config.from_object(Config)
mysql.init_app(app)
CORS(app)

# Registrar las rutas
app.register_blueprint(routes)

# Ruta para servir el frontend
@app.route('/')
def home():
    return render_template('index.html')  # Carga tu HTML en la web

if __name__ == '__main__':
    app.run(debug=True)
