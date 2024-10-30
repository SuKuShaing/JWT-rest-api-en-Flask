from flask import Blueprint, request
from requests import get

users_github = Blueprint("users_github", __name__)


@users_github.route("/github/users", methods=["POST"])
def github():
    """
    Se obtiene la data de los usuarios del país enviado
    """
    data = request.get_json()
    country = data["country"]
    return get(f'https://api.github.com/search/users?q=location:"{country}"&page=1').json()
