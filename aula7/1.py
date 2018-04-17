# INSTITUTO TECNOLOGICO DE AERONAUTICA
# CES-22: Programação Orientada a Objetos
# Prof. Dr. Edgar Yano
# Aluno: Bruno Doria
# 1 semestre 2018

# Exercicio 1
# Implemente o problema do produtor consumidor usando
# Rlock ao inves de uma fila.

import time
import threading

class Stock(object):
    lock = threading.RLock()

    def __init__(self):
        self.total_items = 0

    def execute(self, n):
        Stock.lock.acquire()
        self.total_items += n
        Stock.lock.release()

    def add(self):
        Stock.lock.acquire()
        self.execute(1)
        Stock.lock.release()

    def remove(self):
        Stock.lock.acquire()
        self.execute(-1)
        Stock.lock.release()

def adder(name, stock, items):
    while items > 0:
        print('Producer notify: item N %d added by %s'% (items, name))
        stock.add()
        time.sleep(3)
        items -= 1

def remover(name, stock, items):
    while items > 0:
        print('Consumer notify: item N %d popped by %s'% (items, name))
        stock.remove()
        time.sleep(3)
        items -= 1

if __name__ == '__main__':
    items = 5
    print ("Producer notify: Adding items")
    stock = Stock()
    t1 = threading.Thread(target=adder, args=('Thread-1', stock, items))
    t2 = threading.Thread(target=remover, args=('Thread-2', stock, items))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
