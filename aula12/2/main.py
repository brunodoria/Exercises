# INSTITUTO TECNOLOGICO DE AERONAUTICA
# CES-22: Programação Orientada a Objetos
# Prof. Dr. Edgar Yano
# Aluno: Bruno Doria
# 1 semestre 2018

# Exercicio 2
# Desenvolver uma aplicação Flask usando sessoes

# aplicacao direta de sessoes na interacao de usuarios
# como simulacao utilize qualquer nome de usuario com a senha "password"
# para acessar a area 'restrita'

from flask import Flask, session, render_template, request, redirect, g, url_for
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        session.pop('user', None)

        # apenas verificacao da senha
        if request.form['password'] == 'password':
            session['user'] = request.form['username']
            return redirect(url_for('protected'))

    return render_template('index.html')

@app.route('/protected')
def protected():
    if g.user:
        return render_template('protected.html')

    return redirect(url_for('index'))

@app.before_request
def before_request():
    g.user = None
    if 'user' in session:
        g.user = session['user']

@app.route('/getsession')
def getsession():
    if 'user' in session:
        return session['user']

    return 'Nao logado !'

@app.route('/dropsession')
def dropsession():
    session.pop('user', None)
    return 'Saida!'

if __name__ == '__main__':
    app.run()
