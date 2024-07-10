from app.extensions import db
from dataclasses import dataclass

@dataclass
class Diagnostico(db.Model):
    __tablename__ = 'diagnostico'
    id_diagnostico = db.Column(db.Integer, primary_key=True)
    id_tipo_diagnostico = db.Column(db.Integer, db.ForeignKey('tiposdiagnostico.id_tipo_diagnostico', onupdate='RESTRICT', ondelete='RESTRICT'))
    fundamentacion_cientifica = db.Column(db.String, nullable=True)

    tipo_diagnostico = db.relationship('TiposDiagnostico', backref=db.backref('diagnosticos', uselist=True))

    def __init__(self, id_tipo_diagnostico, fundamentacion_cientifica):
        self.id_tipo_diagnostico = id_tipo_diagnostico
        self.fundamentacion_cientifica = fundamentacion_cientifica