from flask import Blueprint, request, redirect, url_for, session
from ldap3 import Server, Connection, MODIFY_REPLACE
from hashlib import md5
from binascii import b2a_base64

ldap_routes = Blueprint("ldap", __name__, url_prefix="/ldap")

@ldap_routes.route("/login", methods=["POST"])

def login():
    try:
        username="admin"
        password="4linux"
        
        server=Server("ldap://0.0.0.0:389")
        ldap_con=Connection(
            server,
            "cn=%s,dc=dexter,dc=comn,dc=br"%(username),
            password
        )
        ldap_con.bind()

        data = request.form 
        pass_md5=md5(data["password"].encode("utf-8")).digest()
        password="{MD5}" + b2a_base64(pass_md5).decode("utf-8")
        dn="uid=%s,dc=dexter,dc=com,dc=br"%(data["email"])
        ldap_con.search(dn,"(objectclass=person)", attributes=["mail", "userpassword"])

        if(password == ldap_con.entries[0].userPassword.value.decode("utf-8")):
            session["logged"] = True
            return redirect(url_for("docker.index"))
        else:
            return redirect(url_for("index"))
        
    except Exception as error:
        return "%s"%(error)

@ldap_routes.route("/logout", methods=["GET"])
def logout():
    
    return redirect(url_for('index'))