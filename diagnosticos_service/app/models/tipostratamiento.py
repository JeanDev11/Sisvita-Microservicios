from app.extensions import db
from dataclasses import dataclass

@dataclass
class TiposTratamiento(db.Model):
    __tablename__ = 'tipostratamiento'
    id_tipo_tratamiento = db.Column(db.Integer, primary_key=True)
    nombre_tratamiento = db.Column(db.String(100), nullable=False)

    def __init__(self, nombre_tratamiento):
        self.nombre_tratamiento = nombre_tratamiento