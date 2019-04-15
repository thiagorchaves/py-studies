from flask import Blueprint, render_template
import requests

gitlab_routes = Blueprint("gitlab", __name__, url_prefix="/gitlab")
token = "7UnkBFxhU-KW1CrxMQNR"

@gitlab_routes.route("")
def index():
    try:
        usuarios = requests.get("https://gitlab.com/api/v4/users?private_token=%s"%(token))
        usuarios = usuarios.json()
        projetos = requests.get("https://gitlab.com/api/v4/projects?private_token=%s"%(token))
        projetos = projetos.json()
    except Exception as error:
        return "%s"%(error)
    return render_template("gitlab.html", users=usuarios, projects=projetos)

# @gitlab_routes.route("")
# def projetos():
#     try:
#         projects = requests.get("")    
#     except Exception as error:
#         return "%s"%(error)
#     return render_template