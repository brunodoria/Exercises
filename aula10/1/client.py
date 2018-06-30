# INSTITUTO TECNOLOGICO DE AERONAUTICA
# CES-22: Programação Orientada a Objetos
# Prof. Dr. Edgar Yano
# Aluno: Bruno Doria
# 1 semestre 2018

# Exercicio 1
# Desenvolver um servidor de chat para múltiplos usuários

# arquivo user: execute para adicionar usuarios ao servidor ja criado
import socket
import threading
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 1234

uname = input("Digite seu nome::")

ip = input('Endereco de IP::')

s.connect((ip, port))
s.send(uname.encode('ascii'))

clientRunning = True

def receiveMsg(sock):
    serverDown = False
    while clientRunning and (not serverDown):
        try:
            msg = sock.recv(1024).decode('ascii')
            print(msg)
        except:
            print('O servidor caiu. Voce foi desconectado...')
            serverDown = True

threading.Thread(target = receiveMsg, args = (s,)).start()

while clientRunning:
    tempMsg = input()
    msg = uname + '>>' + tempMsg
    if '**quit' in msg:
        clientRunning = False
        s.send('**quit'.encode('ascii'))
    else:
        s.send(msg.encode('ascii'))
