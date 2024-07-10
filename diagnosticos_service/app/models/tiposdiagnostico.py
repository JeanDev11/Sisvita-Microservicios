from app.extensions import db
from dataclasses import dataclass

@dataclass
class TiposDiagnostico(db.Model):
    __tablename__ = 'tiposdiagnostico'
    id_tipo_diagnostico = db.Column(db.Integer, primary_key=True)
    nombre_diagnostico = db.Column(db.String(100), nullable=False)

    def __init__(self, nombre_diagnostico):
        self.nombre_diagnostico = nombre_diagnostico