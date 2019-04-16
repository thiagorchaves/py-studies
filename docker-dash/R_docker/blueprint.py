from flask import Blueprint, render_template, redirect, url_for, session
import docker
docker_routes = Blueprint("docker", __name__, url_prefix="/docker")

@docker_routes.route("")
def index():
    if not "logged" in session or not session["logged"]:
        return redirect(url_for('index'))
    try:
        docker_con = docker.DockerClient("0.0.0.0:2376")
        container = docker_con.containers.get("flask_app")
        flask_app = {
            "id": container.short.id,
            "imagem": container.image.tags[0],
            "nome": container.nome,
            "status": container.status
        }    
    except Exception as e:
        flask_app = None
    return render_template("docker.html", container=flask_app)

@docker_routes.route("/start")
def start():
    if not "logged" in session or not session["logged"]:
        return redirect(url_for('index'))
    try:
        docker_con = docker.DockerClient("0.0.0.0:2376")
        container = docker_con.containers.get("flask_app")
        container.start()
    except Exception as e:
        pass
    return redirect(url_for('docker.index'))

@docker_routes.route("/stopt")
def stop():
    if not "logged" in session or not session["logged"]:
        return redirect(url_for('index'))
    try:
        docker_con = docker.DockerClient("0.0.0.0:2376")
        container = docker_con.containers.get("flask_app")
        container.stop()
    except Exception as e:
        pass
    return redirect(url_for('docker.index'))