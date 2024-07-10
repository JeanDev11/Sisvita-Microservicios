from app.extensions import db
from dataclasses import dataclass

@dataclass
class Tratamiento(db.Model):
    __tablename__ = 'tratamiento'
    id_tratamiento = db.Column(db.Integer, primary_key=True)
    id_tipo_tratamiento = db.Column(db.Integer, db.ForeignKey('tipostratamiento.id_tipo_tratamiento', onupdate='RESTRICT', ondelete='RESTRICT'))
    id_diagnostico = db.Column(db.Integer, db.ForeignKey('diagnostico.id_diagnostico', onupdate='RESTRICT', ondelete='RESTRICT'))

    tipo_tratamiento = db.relationship('TiposTratamiento', backref=db.backref('tratamientos', uselist=True))
    diagnostico = db.relationship('Diagnostico', backref=db.backref('tratamientos', uselist=True))

    def __init__(self, id_tipo_tratamiento, id_diagnostico):
        self.id_tipo_tratamiento = id_tipo_tratamiento
        self.id_diagnostico = id_diagnostico