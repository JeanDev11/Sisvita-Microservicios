from app.extensions import db
from dataclasses import dataclass

@dataclass
class Ubigeo(db.Model):
    __tablename__ = 'ubigeo'
    id_ubigeo = db.Column(db.Integer, primary_key=True)
    departamento = db.Column(db.String(255))
    provincia = db.Column(db.String(255))
    distrito = db.Column(db.String(255))
    latitud = db.Column(db.Float)
    longitud = db.Column(db.Float)

    def __init__(self, departamento, provincia, distrito, latitud, longitud):
        self.departamento = departamento
        self.provincia = provincia
        self.distrito = distrito
        self.latitud = latitud
        self.longitud = longitud
