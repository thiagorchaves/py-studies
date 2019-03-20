from flask import Blueprint
import json

usuarios_routes = Blueprint("usuarios", __name__, url_prefix="/usuarios")

@usuarios_routes.route("")
def getUsuarios():
    return "Lista de usuarios"