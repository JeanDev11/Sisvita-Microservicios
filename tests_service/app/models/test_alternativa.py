from app.extensions import db
from dataclasses import dataclass

@dataclass
class TestAlternativa(db.Model):
    __tablename__ = 'test_alternativa'
    alternativa_id: int
    pregunta_id: int
    alternativa: str
    puntaje: int

    alternativa_id = db.Column(db.Integer, primary_key=True)
    pregunta_id = db.Column(db.Integer, db.ForeignKey('test_pregunta.pregunta_id'), nullable=False)
    alternativa = db.Column(db.String(255), nullable=False)
    puntaje = db.Column(db.Integer, nullable=False)

    pregunta = db.relationship('TestPregunta', backref=db.backref('alternativas', lazy=True))

    def __init__(self, pregunta_id, alternativa, puntaje):
        self.pregunta_id = pregunta_id
        self.alternativa = alternativa
        self.puntaje = puntaje
