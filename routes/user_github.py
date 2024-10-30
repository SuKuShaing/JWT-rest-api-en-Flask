from flask import Blueprint, request
from requests import get
from funtion_jwt import valida_token

users_github = Blueprint("users_github", __name__)


# Middleware
@users_github.before_request
def verify_token_middleware():
    """
    Solo sí la solicitud tiene un token valido lo deja pasar
    """

    token = request.headers["Authorization"].split(" ")[1]
    valida_token(token, output=False)

    """
    No queremos que retorne nada si está todo bien, que siga su camino a la ruta de /github/users, 
    sí va mal nos retorna un error
    """


@users_github.route("/github/users", methods=["POST"])
def github():
    """
    Se obtiene la data de los usuarios del país enviado
    """
    data = request.get_json()
    country = data["country"]
    return get(
        f'https://api.github.com/search/users?q=location:"{country}"&page=1'
    ).json()
