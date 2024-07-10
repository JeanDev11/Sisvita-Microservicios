from app.extensions import ma
from app.models.test import Test

class TestSchema(ma.Schema):
    class Meta:
        model = Test
        fields = ('test_id', 'titulo')
