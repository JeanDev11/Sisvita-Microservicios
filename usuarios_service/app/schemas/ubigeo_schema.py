from app.extensions import ma
from app.models.ubigeo import Ubigeo

class UbigeoSchema(ma.Schema):
    class Meta:
        model = Ubigeo
        fields = ('id_ubigeo', 'departamento', 'latitud', 'longitud')
