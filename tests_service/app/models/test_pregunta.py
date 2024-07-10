from app.extensions import db
from dataclasses import dataclass

@dataclass
class TestPregunta(db.Model):
    __tablename__ = 'test_pregunta'
    pregunta_id: int
    test_id: int
    texto_pregunta: str
    orden: int

    pregunta_id = db.Column(db.Integer, primary_key=True)
    test_id = db.Column(db.Integer, db.ForeignKey('test.test_id'), nullable=False)
    texto_pregunta = db.Column(db.String(255), nullable=False)
    orden = db.Column(db.Integer)

    def __init__(self, test_id, texto_pregunta, orden):
        self.test_id = test_id
        self.texto_pregunta = texto_pregunta
        self.orden = orden
