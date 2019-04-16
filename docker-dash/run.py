#!/usr/bin/env python3

from flask import Flask, render_template

from R_jenkins.blueprint import jenkins_routes
from R_docker.blueprint import docker_routes
from R_gitlab.blueprint import gitlab_routes
from R_ldap.blueprint import ldap_routes

app = Flask(__name__)

app.register_blueprint(jenkins_routes)
app.register_blueprint(docker_routes)
app.register_blueprint(gitlab_routes)
app.register_blueprint(ldap_routes)
app.secret_key = "mySecretKey"

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)