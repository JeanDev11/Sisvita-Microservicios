from flask import Blueprint, request, jsonify
from app.extensions import db
from app.schemas.evaluacionpaciente_schema import EvaluacionPacienteSchema
from app.models.evaluacionpaciente import EvaluacionPaciente
from app.models.diagnostico import Diagnostico
from datetime import datetime

evaluacion_bp = Blueprint('evaluacion', __name__)

@evaluacion_bp.route('/evaluaciones/insert', methods=['POST'])
def create_evaluacion():
    result = {}
    try:
        data = request.get_json()
        evaluacion_schema = EvaluacionPacienteSchema()
        evaluacion_data = evaluacion_schema.load(data)
        
        id_diagnostico = evaluacion_data['id_diagnostico']
        especialista_id = evaluacion_data['especialista_id']
        resultado_id = evaluacion_data['resultado_id']
        fecha_evaluacion = evaluacion_data['fecha_evaluacion']

        if not (id_diagnostico and especialista_id and resultado_id and fecha_evaluacion):
            result["status_code"] = 400
            result["msg"] = "Todos los campos son requeridos."
            return jsonify(result), 400
        
        diagnostico = Diagnostico.query.get(id_diagnostico)
        if not diagnostico:
            result["status_code"] = 404
            result["msg"] = "Diagnóstico no encontrado."
            return jsonify(result), 404
        
        new_evaluacion = EvaluacionPaciente(
            id_diagnostico=id_diagnostico,
            especialista_id=especialista_id,
            resultado_id=resultado_id,
            fecha_evaluacion=fecha_evaluacion
        )
        db.session.add(new_evaluacion)
        db.session.commit()
        
        result["status_code"] = 201
        result["msg"] = "Evaluación creada exitosamente."
        return jsonify(result), 201
    except Exception as e:
        result["status_code"] = 500
        result["msg"] = f"Error al crear evaluación: {str(e)}"
        return jsonify(result), 500

@evaluacion_bp.route('/evaluaciones/<int:id>', methods=['GET'])
def get_evaluacion_by_id(id):
    result = {}
    try:
        evaluacion = EvaluacionPaciente.query.get(id)
        if evaluacion is None:
            result["status_code"] = 404
            result["msg"] = "Evaluación no encontrada."
            return jsonify(result), 404
        
        evaluacion_schema = EvaluacionPacienteSchema()
        result = evaluacion_schema.dump(evaluacion)
        return jsonify(result), 200
    except Exception as e:
        result["status_code"] = 500
        result["msg"] = f"Error al obtener evaluación: {str(e)}"
        return jsonify(result), 500 
