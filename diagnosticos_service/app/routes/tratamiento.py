from flask import Blueprint, jsonify
from app.models.tratamiento import Tratamiento

tratamiento_bp = Blueprint('tratamiento', __name__)

@tratamiento_bp.route('/tratamientos/getall', methods=['GET'])
def get_all_tratamientos():
    result = {}
    try:
        tratamientos = Tratamiento.query.all()
        result = [
            {
                "id_tratamiento": tratamiento.id_tratamiento,
                "id_tipo_tratamiento": tratamiento.id_tipo_tratamiento,
                "id_diagnostico": tratamiento.id_diagnostico,
                "tipo_tratamiento": {
                    "id_tipo_tratamiento": tratamiento.tipo_tratamiento.id_tipo_tratamiento,
                    "nombre_tratamiento": tratamiento.tipo_tratamiento.nombre_tratamiento
                },
                "diagnostico": {
                    "id_diagnostico": tratamiento.diagnostico.id_diagnostico,
                    "id_tipo_diagnostico": tratamiento.diagnostico.id_tipo_diagnostico,
                    "fundamentacion_cientifica": tratamiento.diagnostico.fundamentacion_cientifica
                }
            } for tratamiento in tratamientos
        ]
        return jsonify(result), 200
    except Exception as e:
        result["status_code"] = 500
        result["msg"] = f"Error al obtener tratamientos: {str(e)}"
        return jsonify(result), 500
