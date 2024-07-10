from flask import Blueprint, request, jsonify
from app.models.test import Test
from app.extensions import db

tests_bp = Blueprint('tests', __name__)

@tests_bp.route('/tests', methods=['POST'])
def create_test():
    result = {}
    try:
    
        data = request.get_json()
        descripcion = data.get('descripcion')
        rango_puntuacion = data.get('rango_puntuacion')
        titulo = data.get('titulo')

        nuevo_test = Test(descripcion=descripcion, rango_puntuacion=rango_puntuacion, titulo=titulo)

        db.session.add(nuevo_test)
        db.session.commit()

        result["status_code"] = 201
        result["msg"] = "Test creado correctamente"
        result["data"] = {
            "test_id": nuevo_test.test_id,
            "descripcion": nuevo_test.descripcion,
            "rango_puntuacion": nuevo_test.rango_puntuacion,
            "titulo": nuevo_test.titulo
        }
        return jsonify(result), 201

    except Exception as e:
        db.session.rollback()
        result["status_code"] = 500
        result["msg"] = f"Error al crear el test: {str(e)}"
        return jsonify(result), 500

@tests_bp.route('/tests/<int:test_id>', methods=['GET'])
def get_test(test_id):
    result = {}
    try:
        test = Test.query.get(test_id)
        if not test:
            result["status_code"] = 404
            result["msg"] = "Test no encontrado"
            return jsonify(result), 404

        result["status_code"] = 200
        result["data"] = {
            "test_id": test.test_id,
            "descripcion": test.descripcion,
            "rango_puntuacion": test.rango_puntuacion,
            "titulo": test.titulo
        }
        return jsonify(result), 200

    except Exception as e:
        result["status_code"] = 500
        result["msg"] = f"Error al obtener el test: {str(e)}"
        return jsonify(result), 500
