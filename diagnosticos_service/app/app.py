import os
from flask import Flask
from flask_cors import CORS
from app.extensions import db, ma
from app.routes.diagnostico import diagnostico_bp
from app.routes.evaluacionpaciente import evaluacion_bp
from app.routes.tiposdiagnostico import tiposdiagnostico_bp
from app.routes.tipostratamiento import tipostratamiento_bp
from app.routes.tratamiento import tratamiento_bp

# Inicializar la aplicación Flask
app = Flask(__name__)
CORS(app)

# Configurar la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar SQLAlchemy y Marshmallow con la aplicación Flask
db.init_app(app)
ma.init_app(app)

# Cargar todos los blueprints
app.register_blueprint(diagnostico_bp)
app.register_blueprint(evaluacion_bp)
app.register_blueprint(tiposdiagnostico_bp)
app.register_blueprint(tipostratamiento_bp)
app.register_blueprint(tratamiento_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5002)
