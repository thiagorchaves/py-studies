from flask import Blueprint, render_template, request, redirect, url_for, session
import jenkins

jenkins_routes = Blueprint("jenkins",__name__, url_prefix="/jenkins")

@jenkins_routes.route("")
def index():
    if not "logged" in session or not session["logged"]:
        return redirect(url_for('index'))
    try:
        jenkins_con = jenkins.Jenkins(
            "http://127.0.0.1:8080",
            username="4linux", password="4linux123"
        )
        jobs_list = jenkins_con.get_jobs()
        jobs=[]
        for job in jobs_list:
            jobs.append(jenkins_con.get_job_info(job["fullname"]))
    except Exception as error:
        return "%s"%(error)
    return render_template("jenkins.html", jobs=jobs)

@jenkins_routes.route("/update/<string:job_name>")
def update(job_name):
    if not "logged" in session or not session["logged"]:
        return redirect(url_for('index'))
    try:
       jenkins_con = jenkins.Jenkins("http://127.0.0.1:8080",username="4linux", password="4linux123")
       job = {
           "name": job_name,
           "xml": jenkins_con.get_job_config(job_name)
       }
    except Exception as error:
        return "%s"%(error)
    return render_template("jenkins_update.html", job=job)

@jenkins_routes.route("/reconfig", methods=["POST"])
def reconfig():
    if not "logged" in session or not session["logged"]:
        return redirect(url_for('index'))
    data = request.form
    try:
       jenkins_con = jenkins.Jenkins("http://127.0.0.1:8080",username="4linux", password="4linux123")
       jenkins_con.reconfig_job(data["name"], data["xml"])
       return redirect(url_for("jenkins.index"))
    except Exception as error:
        return redirect(url_for("jenkins.update", job_name=data["name"]))

@jenkins_routes.route("/build/<string:job_name>")
def build(job_name):
    if not "logged" in session or not session["logged"]:
        return redirect(url_for('index'))
    try:
       jenkins_con = jenkins.Jenkins("http://127.0.0.1:8080",username="4linux", password="4linux123")
       jenkins_con.build_job(job_name)
    except Exception as error:
        pass
    return redirect(url_for("jenkins.index"))
