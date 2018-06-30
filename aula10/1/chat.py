# INSTITUTO TECNOLOGICO DE AERONAUTICA
# CES-22: Programação Orientada a Objetos
# Prof. Dr. Edgar Yano
# Aluno: Bruno Doria
# 1 semestre 2018

# Exercicio 1
# Desenvolver um servidor de chat para múltiplos usuários

# arquivo server: execute para iniciar um servidor
import socket
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverRunning = True
ip = str(socket.gethostbyname(socket.gethostname()))
port = 1234

clients = {}

s.bind((ip, port))
s.listen()
print('Servidor pronto...')
print('IP do servidor::%s' %ip)

def handleClient(client, uname):
    clientConnected = True
    keys = clients.keys()
    help = '''Os comandos do chat sao\n1::**list=>lista os usuarios online\n
              2::**quit=>encerra sessao \n
              3::Para enviar uma mensagem adicione o nome do usuario ao final do texto com o prefixo **'''

    while clientConnected:
        try:
            msg = client.recv(1024).decode('ascii')
            response = 'Numero de usuarios online:\n'
            found = False
            if '**list' in msg:
                clientNo = 0
                for name in keys:
                    clientNo += 1
                    response = response + str(clientNo) + '::' + name+'\n'
                client.send(response.encode('ascii'))
            elif '**help' in msg:
                client.send(help.encode('ascii'))
            elif '**quit' in msg:
                response = 'Encerrando sessao...'
                client.send(response.encode('ascii'))
                clients.pop(uname)
                print(uname + ' foi desconectado')
                clientConnected = False
            else:
                for name in keys:
                    if('**'+name) in msg:
                        msg = msg.replace('**'+name, '')
                        clients.get(name).send(msg.encode('ascii'))
                        found = True
                if(not found):
                    client.send('Destinatario invalido.'.encode('ascii'))
        except:
            clients.pop(uname)
            print(uname + ' foi desconectado')
            clientConnected = False


while serverRunning:
    client, address = s.accept()
    uname = client.recv(1024).decode('ascii')
    print('%s conectado ao servidor'%str(uname))
    client.send('Bem vindo ao chat. Digite **help para ver os comandos'.encode('ascii'))

    if(client not in clients):
        clients[uname] = client
        threading.Thread(target = handleClient, args = (client, uname, )).start()
