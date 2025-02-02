from flask import Flask, render_template
from config import DatabaseConnection, Config
from routes import routes
from flask_cors import CORS

app = Flask(__name__, template_folder="templates")
app.config.from_object(Config)
CORS(app)

# Inicializar la conexión a la base de datos (opcional, para otros usos)
db = DatabaseConnection()
db.connect()

# Registrar las rutas
app.register_blueprint(routes)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
