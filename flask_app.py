from cambio import *
from flask import Flask, render_template,redirect,request

app = Flask(__name__)

@app.route('/', methods = ['GET','POST'])
def index():
    cb = Cambio()
    moedas = cb.moedasDisponiveis()
    if request.method == 'POST':
        cotacao = cb.trataCotacao(request.form['tipoMoeda1'],request.form['tipoMoeda2'],int(request.form['moeda1']))
        return render_template('index.html',moedas = moedas, cotacao = cotacao)
    return render_template('index.html',moedas = moedas)


if __name__ == '__main__':
    app.run(debug=True)