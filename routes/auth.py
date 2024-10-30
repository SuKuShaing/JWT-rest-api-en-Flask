from flask import Blueprint, request, jsonify
from funtion_jwt import write_token, valida_token

routes_auth = Blueprint("routes_auth", __name__)


@routes_auth.route("/login", methods=["POST"])
def login():
    data = request.get_json() # convierte un json en un dict (diccionario) 

    if data["username"] == "Sebastián Sanhueza": # verifica el usuario enviado, esto puede ser variable para un futuro
        return write_token(data=data) # write_token espera un argumento llamado data y que sea un dict

    else:
        response = jsonify({"message": "User not found"})
        response.status_code = 404
        return response

@routes_auth.route("/verify/token")
def verify():
    auth = request.headers['Authorization'] # devuelve en un string el esquema de autorización más el token 
    token = auth.split(" ")[1] #cortamos el string y devolvemos solo el token
    return valida_token(token, output=True) # Validamos el token