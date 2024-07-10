import os
from flask import Flask
from app.extensions import db, ma
from app.routes.test_routes import tests_bp
from app.routes.resultado_routes import resultados_bp
from app.routes.nivel_routes import niveles_bp

# Inicializar la aplicación Flask
app = Flask(__name__)

# Configurar la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar SQLAlchemy y Marshmallow con la aplicación Flask
db.init_app(app)
ma.init_app(app)

# Registrar blueprints
app.register_blueprint(tests_bp, url_prefix='/api/tests')
app.register_blueprint(resultados_bp, url_prefix='/api/resultados')
app.register_blueprint(niveles_bp, url_prefix='/api/niveles')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5003)

