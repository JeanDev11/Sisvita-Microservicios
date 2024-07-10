from app.extensions import db
from dataclasses import dataclass

@dataclass
class EvaluacionPaciente(db.Model):
    __tablename__ = 'evaluacionpaciente'
    id_evaluacion = db.Column(db.Integer, primary_key=True)
    id_diagnostico = db.Column(db.Integer, db.ForeignKey('diagnostico.id_diagnostico', onupdate='RESTRICT', ondelete='RESTRICT'))
    especialista_id = db.Column(db.Integer, nullable=False)
    resultado_id = db.Column(db.Integer, nullable=False)
    fecha_evaluacion = db.Column(db.DateTime, nullable=False)

    diagnostico = db.relationship('Diagnostico', backref=db.backref('evaluaciones', uselist=True))

    def __init__(self, id_diagnostico, especialista_id, resultado_id, fecha_evaluacion):
        self.id_diagnostico = id_diagnostico
        self.especialista_id = especialista_id
        self.resultado_id = resultado_id
        self.fecha_evaluacion = fecha_evaluacion