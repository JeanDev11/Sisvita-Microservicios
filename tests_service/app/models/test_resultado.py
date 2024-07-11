from app.extensions import db
from dataclasses import dataclass

@dataclass
class TestResultado(db.Model):
    __tablename__ = 'test_resultado'
    resultado_id = db.Column(db.Integer, primary_key=True)
    test_id = db.Column(db.Integer, db.ForeignKey('test.test_id'), nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.usuario_id'), nullable=False)
    puntaje_obtenido = db.Column(db.Integer, nullable=False)
    fecha_creacion = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    id_nivel = db.Column(db.Integer, db.ForeignKey('nivel_test.id_nivel'), nullable=False)

    test__rel = db.relationship('Test', backref='test_resultado')
    usuario__rel = db.relationship('Usuario', backref='test_resultado')
    nivel__rel = db.relationship('NivelTest', backref='test_resultado')

    def __init__(self, test_id, usuario_id, puntaje_obtenido, id_nivel):
        self.test_id = test_id
        self.usuario_id = usuario_id
        self.puntaje_obtenido = puntaje_obtenido
        self.id_nivel = id_nivel
