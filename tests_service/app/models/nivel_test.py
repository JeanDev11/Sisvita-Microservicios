from app.extensions import db
from dataclasses import dataclass

@dataclass
class NivelTest(db.Model):
    __tablename__ = 'nivel_test'
    id_nivel: int
    min_puntos: int
    max_puntos: int
    descripcion: str
    test_id: int
    semaforo: str

    id_nivel = db.Column(db.Integer, primary_key=True)
    min_puntos = db.Column(db.Integer, nullable=False)
    max_puntos = db.Column(db.Integer, nullable=False)
    descripcion = db.Column(db.String(255))
    test_id = db.Column(db.Integer, db.ForeignKey('test.test_id'), nullable=False)
    semaforo = db.Column(db.String)

    def __init__(self, min_puntos, max_puntos, descripcion, test_id, semaforo):
        self.min_puntos = min_puntos
        self.max_puntos = max_puntos
        self.descripcion = descripcion
        self.test_id = test_id
        self.semaforo = semaforo
