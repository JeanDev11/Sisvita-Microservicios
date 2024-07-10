from flask import Blueprint, jsonify, request
from app.extensions import db
from app.models.tiposdiagnostico import TiposDiagnostico

tiposdiagnostico_bp = Blueprint('tiposdiagnostico', __name__)

@tiposdiagnostico_bp.route('/tiposdiagnostico/getall', methods=['GET'])
def get_tipos_diagnostico_all():
    result = {}
    try:
        tipos_diagnosticos = TiposDiagnostico.query.all()
        result = [
            {
                "id_tipo_diagnostico": td.id_tipo_diagnostico,
                "nombre_diagnostico": td.nombre_diagnostico,
            } for td in tipos_diagnosticos
        ]
        return jsonify(result), 200
    except Exception as e:
        result["status_code"] = 500
        result["msg"] = f"Error al obtener diagnósticos: {str(e)}"
        return jsonify(result), 500


@tiposdiagnostico_bp.route('/tiposdiagnostico/insert', methods=['POST'])
def create_tipos_diagnostico():
    result = {}
    try:
        data = request.get_json()
        nombre_diagnostico = data.get('nombre_diagnostico')
        
        if not nombre_diagnostico:
            result["status_code"] = 400
            result["msg"] = "Nombre de diagnóstico es requerido."
            return jsonify(result), 400
        
        new_diagnostico = TiposDiagnostico(nombre_diagnostico=nombre_diagnostico)
        db.session.add(new_diagnostico)
        db.session.commit()
        
        result["status_code"] = 201
        result["msg"] = "Tipo de diagnóstico creado exitosamente."
        return jsonify(result), 201
    except Exception as e:
        result["status_code"] = 500
        result["msg"] = f"Error al crear diagnóstico: {str(e)}"
        return jsonify(result), 500

@tiposdiagnostico_bp.route('/tiposdiagnostico/<int:id>', methods=['GET'])
def get_tipos_diagnostico_by_id(id):
    result = {}
    try:
        diagnostico = TiposDiagnostico.query.get(id)
        if diagnostico is None:
            result["status_code"] = 404
            result["msg"] = "Tipo de diagnóstico no encontrado."
            return jsonify(result), 404
        
        result = {
            "id_tipo_diagnostico": diagnostico.id_tipo_diagnostico,
            "nombre_diagnostico": diagnostico.nombre_diagnostico,
        }
        return jsonify(result), 200
    except Exception as e:
        result["status_code"] = 500
        result["msg"] = f"Error al obtener diagnóstico: {str(e)}"
        return jsonify(result), 500
