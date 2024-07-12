from flask import Blueprint, request, jsonify
from app.models.test_resultado import TestResultado
from app.extensions import db
from app.schemas.test_resultado_schema import testResultados_schema

test_resultado = Blueprint('test_resultado', __name__)

@test_resultado.route('/test_resultado/insert', methods=['POST'])
def insert_test_resultado():
    result = {}
    body = request.get_json()
    test_id = body.get('test_id')
    usuario_id = body.get('usuario_id')
    puntaje_obtenido = body.get('puntaje_obtenido')
    id_nivel = body.get('id_nivel')

    if not test_id or not usuario_id or not puntaje_obtenido:
        result["status_code"] = 400
        result["msg"] = "Faltan datos obligatorios"
        return jsonify(result), 400
    
    nuevo_resultado = TestResultado(
        test_id=test_id,
        usuario_id=usuario_id,
        puntaje_obtenido=puntaje_obtenido,
        id_nivel=id_nivel
    )
    
    db.session.add(nuevo_resultado)
    db.session.commit()
    
    result["data"] = {
        "resultado_id": nuevo_resultado.resultado_id,
        "test_id": nuevo_resultado.test_id,
        "usuario_id": nuevo_resultado.usuario_id,
        "puntaje_obtenido": nuevo_resultado.puntaje_obtenido,
        "id_nivel": nuevo_resultado.id_nivel,
        "fecha_creacion": nuevo_resultado.fecha_creacion
    }
    result["status_code"] = 201
    result["msg"] = "Resultado de test agregado correctamente"
    return jsonify(result), 201



@test_resultado.route('/test_resultado/get', methods=['GET'])
def get_test_resultados():
    result = {}
    try:
        resultados = TestResultado.query.all()
        data = testResultados_schema.dump(resultados)
        return jsonify(data), 200
    except Exception as e:
        result["status_code"] = 500
        result["msg"] = f"Error al obtener resultados: {str(e)}"
        return jsonify(result), 500
    
