from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models.diagnostico import Diagnostico
from app.models.tiposdiagnostico import TiposDiagnostico

diagnostico_bp = Blueprint('diagnostico', __name__)

@diagnostico_bp.route('/diagnosticos/insert', methods=['POST'])
def create_diagnostico():
    result = {}
    try:
        data = request.get_json()
        id_tipo_diagnostico = data.get('id_tipo_diagnostico')
        fundamentacion_cientifica = data.get('fundamentacion_cientifica')

        if not id_tipo_diagnostico:
            result["status_code"] = 400
            result["msg"] = "ID del tipo de diagnóstico es requerido."
            return jsonify(result), 400
        
        tipo_diagnostico = TiposDiagnostico.query.get(id_tipo_diagnostico)
        if not tipo_diagnostico:
            result["status_code"] = 404
            result["msg"] = "Tipo de diagnóstico no encontrado."
            return jsonify(result), 404
        
        new_diagnostico = Diagnostico(id_tipo_diagnostico=id_tipo_diagnostico, fundamentacion_cientifica=fundamentacion_cientifica)
        db.session.add(new_diagnostico)
        db.session.commit()
        
        result["status_code"] = 201
        result["msg"] = "Diagnóstico creado exitosamente."
        return jsonify(result), 201
    except Exception as e:
        result["status_code"] = 500
        result["msg"] = f"Error al crear diagnóstico: {str(e)}"
        return jsonify(result), 500

@diagnostico_bp.route('/diagnosticos/<int:id>', methods=['GET'])
def get_diagnostico_by_id(id):
    result = {}
    try:
        diagnostico = Diagnostico.query.get(id)
        if diagnostico is None:
            result["status_code"] = 404
            result["msg"] = "Diagnóstico no encontrado."
            return jsonify(result), 404
        
        result = {
            "id_diagnostico": diagnostico.id_diagnostico,
            "id_tipo_diagnostico": diagnostico.id_tipo_diagnostico,
            "fundamentacion_cientifica": diagnostico.fundamentacion_cientifica,
            "tipo_diagnostico": {
                "id_tipo_diagnostico": diagnostico.tipo_diagnostico.id_tipo_diagnostico,
                "nombre_diagnostico": diagnostico.tipo_diagnostico.nombre_diagnostico,
            }
        }
        return jsonify(result), 200
    except Exception as e:
        result["status_code"] = 500
        result["msg"] = f"Error al obtener diagnóstico: {str(e)}"
        return jsonify(result), 500