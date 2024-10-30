from jwt import encode, decode, exceptions
from os import getenv
from datetime import datetime, timedelta
from flask import jsonify


def expire_date(days: int):
    """
    datetime.now()  # obtiene la fecha y hora actual
    timedelta(days)  # da los días de diferencia y los sumamos
    """
    now = datetime.now()
    new_date = now + timedelta(days)
    return new_date


def write_token(data: dict):
    """
    encode codifica lo que se le pase según el algoritmo de encriptación, en este caso HS256
    se coloca la clave secreta
    y la carga útil (payload) que es la data y otros parámetros como cuando expira el token
    **data desempaqueta el diccionario (objeto) y le añade los pares clave valor a los que parámetros que colocamos nosotros
    """
    token = encode(
        payload={**data, "exp": expire_date(2)}, key=getenv("SECRET"), algorithm="HS256"
    )
    return token.encode("UTF-8")


def valida_token(token, output=False):
    try:
        if output:
            return decode(token, key=getenv("SECRET"), algorithms=["HS256"])
        # en caso de que el output sea true se retorna el payload al usuario, sino solo se ejecuta
        decode(token, key=getenv("SECRET"), algorithms=["HS256"])

    except exceptions.DecodeError:
        response = jsonify({"message": "Invalid Token"})
        response.status_code = 401
        return response

    except exceptions.ExpiredSignatureError:
        response = jsonify({"message": "Token Expired"})
        response.status_code = 401
        return response
