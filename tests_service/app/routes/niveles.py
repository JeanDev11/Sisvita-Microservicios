from app.models.nivel_test import NivelTest

@tests_bp.route('/niveles/<int:nivel_id>', methods=['GET'])
def get_nivel(nivel_id):
    result = {}
    try:
        nivel = NivelTest.query.get(nivel_id)
        if not nivel:
            result["status_code"] = 404
            result["msg"] = "Nivel de test no encontrado"
            return jsonify(result), 404

        result["status_code"] = 200
        result["data"] = {
            "id_nivel": nivel.id_nivel,
            "min_puntos": nivel.min_puntos,
            "max_puntos": nivel.max_puntos,
            "descripcion": nivel.descripcion,
            "test_id": nivel.test_id,
            "semaforo": nivel.semaforo
        }
        return jsonify(result), 200

    except Exception as e:
        result["status_code"] = 500
        result["msg"] = f"Error al obtener el nivel de test: {str(e)}"
        return jsonify(result), 500
