from marshmallow import fields
from app.extensions import ma
from app.models.evaluacionpaciente import EvaluacionPaciente

class EvaluacionPacienteSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = EvaluacionPaciente
        include_fk = True
        load_instance = True

    id_evaluacion = fields.Integer()
    id_diagnostico = fields.Integer()
    especialista_id = fields.Integer()
    resultado_id = fields.Integer()
    fecha_evaluacion = fields.DateTime()
