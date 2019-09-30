from pymongo import MongoClient
from pprint import pprint

try:
    con = MongoClient()
    db = con ['projetos']
except Exception as e:
    print('Erro {}'.format(e))
    exit()

# Inserindo usuários
# db.usuarios.insert({'_id':3, 'nome': 'Tati', 'idade': 36})
# print(db.usuarios.find_one())

# Removendo usuários
# db.usuarios.remove({'_id':3})

#Atualizando documentos

# db.usuarios.update({'_id':2}, {'$set': {'projetos': []}})
# db.usuarios.update({'_id':2}, {'$push':{'projetos':{'nome':'bevops2', 'desc':'api2'}}})
db.usuarios.update({'_id':2}, {'$pull':{'projetos':{'nome':'bevops2', 'desc':'api2'}}})

# Existem duas formas para printar o cursor
# primeira forma:
for x in db.usuarios.find():
    pprint(x)
#  Segunda forma:
# print([x for x in db.usuarios.find()])