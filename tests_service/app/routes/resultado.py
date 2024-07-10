from app.models.test_resultado import TestResultado

@tests_bp.route('/resultados/<int:resultado_id>', methods=['GET'])
def get_resultado(resultado_id):
    result = {}
    try:
        resultado = TestResultado.query.get(resultado_id)
        if not resultado:
            result["status_code"] = 404
            result["msg"] = "Resultado de test no encontrado"
            return jsonify(result), 404

        result["status_code"] = 200
        result["data"] = {
            "resultado_id": resultado.resultado_id,
            "test_id": resultado.test_id,
            "usuario_id": resultado.usuario_id,
            "puntaje_obtenido": resultado.puntaje_obtenido,
            "fecha_creacion": resultado.fecha_creacion.strftime('%Y-%m-%d %H:%M:%S'),
            "id_nivel": resultado.id_nivel
        }
        return jsonify(result), 200

    except Exception as e:
        result["status_code"] = 500
        result["msg"] = f"Error al obtener el resultado de test: {str(e)}"
        return jsonify(result), 500
