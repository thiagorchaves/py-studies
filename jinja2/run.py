#!/usr/bin/env python3

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", title="Lista de nomes", nomes=["João", "Gabriel", "Daniela", "Alice"])

if __name__ == "__main__":
    app.run(debug=True)