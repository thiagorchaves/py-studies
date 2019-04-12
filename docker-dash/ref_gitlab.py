#!usr/bin/env python3
import requests
import json
token = "7UnkBFxhU-KW1CrxMQNR"

# Pegando dados da API
# projetos = requests.get("https://gitlab.com/api/v4/projects?private_token=%s"%(token))
# print(
#     json.dumps(
#         projetos.json(),
#         indent=4, sort_keys=True
#         )
# )

# Adicionando projeto
# data = {
#     "name": "flask-app"
# }

# projetos = requests.post("https://gitlab.com/api/v4/projects?private_token=%s"%(token), post")
# print(projetos.json())

# Listando usuários
# usuarios = requests.get("https://gitlab.com/api/v4/users?private_token=%s"%(token), post")
#  print(
#      json.dumps(
#          usuarios.json(),
#          indent=4, sort_keys=True
#          )
# )

# Adicionando Usuário
# post = {
#     "email": "thiago@qcx.com.br",
#     "username": "thiagorchaves",
#     "name": "Thiago Chaves",
#     "password": "tT261009"
# }

# usuario = requests.post("https://gitlab.com/api/v4/users?private_token=%s"%(token), post")
# print(usuario.json())

# Adicionando membro ao projeto
# project_id = 2
# post = {
#     "user_id": 2,
#     "access_level": 40
# }

# projeto = requests.post("https://gitlab.com/api/v4/projects/%s/members?private_token=%s"%(project_id, token), post)
# print(usuario.json())
