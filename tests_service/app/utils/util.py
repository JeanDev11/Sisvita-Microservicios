# tests_service/app/utils/util.py
import requests

def obtener_info_usuario(usuario_id):
    response = requests.get(f'http://usuarios_service:5000/usuarios/schema/{usuario_id}')
    if response.status_code == 200:
        return response.json()
    else:
        return None
