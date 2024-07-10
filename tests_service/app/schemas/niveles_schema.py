from app.extensions import ma
from app.models.nivel_test import NivelTest

class NivelTestSchema(ma.Schema):
    class Meta:
        model = NivelTest
        fields = ('id_nivel', 'descripcion', 'semaforo')
