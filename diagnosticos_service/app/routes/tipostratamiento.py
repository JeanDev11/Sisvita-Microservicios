from flask import Blueprint, jsonify
from app.models.tipostratamiento import TiposTratamiento

tipostratamiento_bp = Blueprint('tipostratamiento', __name__)

@tipostratamiento_bp.route('/tipostratamiento/getall', methods=['GET'])
def get_tipos_tratamiento_all():
    result = {}
    try:
        tipos_tratamientos = TiposTratamiento.query.all()
        result = [
            {
                "id_tipo_tratamiento": tt.id_tipo_tratamiento,
                "nombre_tratamiento": tt.nombre_tratamiento,
            } for tt in tipos_tratamientos
        ]
        return jsonify(result), 200
    except Exception as e:
        result["status_code"] = 500
        result["msg"] = f"Error al obtener tratamientos: {str(e)}"
        return jsonify(result), 500