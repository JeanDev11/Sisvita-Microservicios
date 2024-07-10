from app.extensions import db
from dataclasses import dataclass

@dataclass
class Test(db.Model):
    __tablename__ = 'test'
    test_id: int
    descripcion: str
    rango_puntuacion: int
    titulo: str

    test_id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(255))
    rango_puntuacion = db.Column(db.Integer)
    titulo = db.Column(db.String(100))

    preguntas = db.relationship('TestPregunta', backref='test', lazy=True)
    resultados = db.relationship('TestResultado', backref='test', lazy=True)
    niveles = db.relationship('NivelTest', backref='test', lazy=True)

    def __init__(self, descripcion, rango_puntuacion, titulo):
        self.descripcion = descripcion
        self.rango_puntuacion = rango_puntuacion
        self.titulo = titulo
