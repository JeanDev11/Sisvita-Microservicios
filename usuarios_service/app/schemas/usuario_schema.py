from app.extensions import ma
from marshmallow import fields
from app.schemas.ubigeo_schema import UbigeoSchema

class UsuarioSchema(ma.Schema):
    usuario_id = fields.Integer()
    nombres = fields.String()
    apellidos = fields.String()
    dni = fields.String()
    correo_electronico = fields.String()
    ubigeo = ma.Nested(UbigeoSchema)

    # correo_electronico = fields.Email()
    # fecha_nac = fields.Date(format='%Y-%m-%d')