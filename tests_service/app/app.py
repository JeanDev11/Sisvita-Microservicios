import os
from flask import Flask
from flask_cors import CORS
from app.extensions import db, ma
from app.routes.nivel_test import nivel_test
from app.routes.test_resultado import test_resultado
from app.routes.test import test_bp

# Inicializar la aplicación Flask
app = Flask(__name__)
CORS(app)

# Configurar la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar SQLAlchemy y Marshmallow con la aplicación Flask
db.init_app(app)
ma.init_app(app)

# Registrar blueprints
app.register_blueprint(nivel_test)
app.register_blueprint(test_resultado)
app.register_blueprint(test_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)

