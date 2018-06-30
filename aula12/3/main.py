# INSTITUTO TECNOLOGICO DE AERONAUTICA
# CES-22: Programação Orientada a Objetos
# Prof. Dr. Edgar Yano
# Aluno: Bruno Doria
# 1 semestre 2018

# Exercicio 3
# Desenvolva uma aplicação que permita carregar arquivos em um servidor,
# listar e acessar arquivos no servidor.

# aplicação simples do armazenamento de imagens, nao existe restricao de
# usuario, o acesso a aplicacao permite direto o upload de qualquer imagem

import os
from flask import Flask, request, render_template, send_from_directory

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
    return render_template("upload.html")

@app.route("/upload", methods=["POST"])
def upload():
    target = os.path.join(APP_ROOT, 'images/')
    print(target)
    if not os.path.isdir(target):
            os.mkdir(target)
    else:
        print("Couldn't create upload directory: {}".format(target))
    print(request.files.getlist("file"))
    for upload in request.files.getlist("file"):
        print(upload)
        print("{} is the file name".format(upload.filename))
        filename = upload.filename
        destination = "/".join([target, filename])
        print ("Accept incoming file:", filename)
        print ("Save it to:", destination)
        upload.save(destination)

    return render_template("complete.html", image_name=filename)

#armazenar imagem no diretorio
@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory("images", filename)

#exibicao dos arquivos (imagens)
@app.route('/gallery')
def get_gallery():
    #passagem dos arquivos
    image_names = os.listdir('./images')
    print(image_names)
    #template da galeria de exibicao
    return render_template("gallery.html", image_names=image_names)

if __name__ == "__main__":
    app.run()
