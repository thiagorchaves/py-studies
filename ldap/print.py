#!/usr/bin/env python3

from ldap3 import Server, Connection, MODIFY_REPLACE
from hashlib import md5
from binascii import b2a_base64

username="admin"
password="4linux"

server=Server("ldap://localhost:389")
ldap_con=Connection(
    server,
    "cn=%s,dc=dexter,dc=com,dc=br"%(username),
    password
)
ldap_con.bind()




# Adicionando usuário ldap
# md5json = md5("senhapadrao".encode("utf-8")).digest()
# user = {
#     "cn": "Thiago",
#     "sn": "Chaves",
#     "mail": "thiago@qcx.com.br",
#     "uidNumber": "123",
#     "gidNumber": "123",
#     "uid": "thiago@qcx.com.br",
#     "homeDirectory": "/home/thiago",
#     "userPassword": "{MD5}" + b2a_base64(md5json).decode("utf-8")
# }

# objectClass = ["top", "person", "inetOrgPerson", "posixAccount", "organizationalPerson"]
# dn = "uid=%s,dc=dexter,dc=com,dc=br"%(user["mail"])
# user_added = ldap_con.add(dn, objectClass, user)
# print(user_added)

# Buscando Usuários
# email = "thiago@qcx.com.br"
# dn = dn = "uid=%s,dc=dexter,dc=com,dc=br"%(email)
# ldap_con.search(
#     dn,
#     "(objectclass=person)",
#     attributes=["sn", "userPassword"]

# )
# print (ldap_con.entries)

# Alterando Objeto

# email = "thiago@qcx.com.br"
# dn = "uid=%s,dc=dexter,dc=com,dc=br"%(email)
# changes = {
#      "cn": [(MODIFY_REPLACE, ["Thiago"])],
#      "sn": [(MODIFY_REPLACE, ["Romualdo Chaves"])],
# }
# ldap_con.modify(
#     dn,
#     changes
# )

# print(ldap_con.result)

# Deletando um objeto

# email = "thiago@qcx.com.br"
# dn = "uid=%s,dc=dexter,dc=com,dc=br"%(email)

# print(ldap_con.delete(dn))