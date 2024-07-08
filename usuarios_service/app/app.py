import os
from flask import Flask
from app.extensions import db, ma
from app.routes.usuario import usuarios_bp
from app.routes.especialista import especialista_bp
from app.routes.ubigeo import ubigeo_bp

# Inicializar la aplicación Flask
app = Flask(__name__)

# Configurar la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar SQLAlchemy y Marshmallow con la aplicación Flask
db.init_app(app)
ma.init_app(app)

# Cargar todos los blueprints
app.register_blueprint(usuarios_bp)
app.register_blueprint(especialista_bp)
app.register_blueprint(ubigeo_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)