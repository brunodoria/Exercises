# INSTITUTO TECNOLOGICO DE AERONAUTICA
# CES-22: Programação Orientada a Objetos
# Prof. Dr. Edgar Yano
# Aluno: Bruno Doria
# 1 semestre 2018

# Exercicio 1
# Desenvolver uma aplicação Flask usando cookies

# aplicação simples que guarda sua fonte preferida para exibição do texto

from flask import Flask, render_template, request, redirect, url_for, flash, make_response

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def article():
    if request.method == 'POST':
        print(request.form)

        # variavel para o set do cookie
        res = make_response("")
        res.set_cookie("font", request.form.get('font'), 60*60*24*15)
        res.headers['location'] = url_for('article')
        return res, 302

    return render_template('article.html')

if __name__ == "__main__":
    app.run()
