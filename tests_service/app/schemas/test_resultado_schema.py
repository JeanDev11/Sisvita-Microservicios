from app.extensions import ma
from app.models.test_resultado import TestResultado
from app.schemas.usuario_schema import UsuarioSchema
from app.schemas.test_schema import TestSchema
from app.schemas.nivel_test_schema import NivelTestSchema
from marshmallow import fields, pre_dump
import pytz

class TestResultadoSchema(ma.Schema):
    usuario__rel = ma.Nested(UsuarioSchema)
    # usuario = ma.Nested(UsuarioSchema(only=("usuario_id", "nombres","apellidos")))
    test__rel = ma.Nested(TestSchema)
    nivel__rel = ma.Nested(NivelTestSchema)
    fecha_creacion = fields.DateTime('%d-%m-%Y %H:%M:%S')

    @pre_dump
    def convert_to_local_time(self, data, **kwargs):
        # Convertir fecha_creacion a la zona horaria de Lima
        if data.fecha_creacion:
            utc_zone = pytz.utc
            lima_zone = pytz.timezone('America/Lima')
            utc_time = data.fecha_creacion.replace(tzinfo=utc_zone)
            data.fecha_creacion = utc_time.astimezone(lima_zone).replace(tzinfo=None)
        return data

    class Meta:
        model = TestResultado
        fields = ('resultado_id', 
                  'puntaje_obtenido', 
                  'descripcion', 
                  'fecha_creacion', 
                  'usuario__rel', 
                  'test__rel',
                  'nivel__rel')
        

testResultado_schema = TestResultadoSchema()
testResultados_schema = TestResultadoSchema(many=True)