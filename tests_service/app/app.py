import os
from flask import Flask
from app.extensions import db, ma
from app.routes import nivel_test
from app.routes import test_resultado
from app.routes import test_bp

# Inicializar la aplicación Flask
app = Flask(__name__)

# Configurar la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar SQLAlchemy y Marshmallow con la aplicación Flask
db.init_app(app)
ma.init_app(app)

# Registrar blueprints
app.register_blueprint(test)
app.register_blueprint(test_resultado)
app.register_blueprint(nivel_test)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5003)

