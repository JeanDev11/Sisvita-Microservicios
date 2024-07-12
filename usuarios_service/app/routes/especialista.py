from flask import Blueprint, request, jsonify
from app.models.especialista import Especialista

especialista_bp = Blueprint('especialista', __name__)

@especialista_bp.route('/especialista/<int:usuario_id>', methods=['GET'])
def get_especialista(usuario_id):
    result = {}
    try:
        especialista = Especialista.query.filter_by(usuario_id=usuario_id).first()
        if especialista:
            result = {
                'especialista_id': especialista.especialista_id,
                'usuario_id': especialista.usuario_id,
                'especialidad': especialista.especialidad,
                'nro_colegiado': especialista.nro_colegiado,
                'direccion_consultorio': especialista.direccion_consultorio
            }
            return jsonify(result), 200
        else:
            result["status_code"] = 404
            result["msg"] = "Especialista no encontrado"
            return jsonify(result), 404
    except Exception as e:
        result["status_code"] = 500
        result["msg"] = f"Error al obtener especialista: {str(e)}"
        return jsonify(result), 500