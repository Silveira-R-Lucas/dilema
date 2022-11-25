from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/form_dilema')
def form_dilema():
    return render_template("dilema.html")

@app.route("/sorteio", methods=['POST'])
def sorteio():
    argumentos = request.form.to_dict()
    resultado = []
    for values in argumentos.values():
        resultado.append(values)
    resultado = random.choice (resultado)
    return render_template("resultado.html", resultado = resultado)
