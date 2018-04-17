# INSTITUTO TECNOLOGICO DE AERONAUTICA
# CES-22: Programação Orientada a Objetos
# Prof. Dr. Edgar Yano
# Aluno: Bruno Doria
# 1 semestre 2018

# Exercicio 1
# Faca um programa para comparar o desempenho de
# threads e processos. Crie uma situacao onde usar thread
# e mais vantajoso que processos e vice-versa.

# threads utilizam o mesmo espaco de memoria nas execucoes
# e assim demandam certo controle com a manipulacao dos dados
# assim, justifica-se o uso do lock
# um caso interessante de uso de threads seria quando se deseja
# monitorar as execucoes em si

# import logging
# import random
# import threading
# import time
#
# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s (%(threadName)-2s) %(message)s')
#
# class BeginClass(object):
#     def __init__(self):
#         super(BeginClass, self).__init__()
#         self.active = []
#         self.lock = threading.Lock()
#     def Return(self, name):
#         with self.lock:
#             self.active.append(name)
#             logging.debug('Teaching: %s', self.active)
#     def Interval(self, name):
#         with self.lock:
#             self.active.remove(name)
#             logging.debug('Teaching: %s', self.active)
#
# def worker(s, pool):
#     logging.debug('Waiting to join the class and learn more')
#     with s:
#         name = threading.currentThread().getName()
#         pool.Return(name)
#         time.sleep(0.1)
#         pool.Interval(name)
#
# firstclass = BeginClass()
# s = threading.Semaphore(2)
# for i in range(4):
#     t = threading.Thread(target=worker, name=str(i), args=(s, firstclass))
#     t.start()

################################################################################

# processos possuem memoria separada, ou seja, as execucoes nao
# copartilham um mesmo espaco de memoria; apesar de nao possuirem
# o problema de overwrite indicado acima, o compartilhamento de
# objetos e dificultado
# um caso interessante do uso de processos seria quando se deseja
# monitorar o inicio e termino das execucoes

# import multiprocessing
# import time
#
# def worker():
#     name = multiprocessing.current_process().name
#     print (name, 'Preparing to solve')
#     time.sleep(2)
#     print (name, 'Finishing...well done')
#
# def my_service():
#     name = multiprocessing.current_process().name
#     print (name, 'Starting')
#     time.sleep(3)
#     print (name, 'Answering')
#
# if __name__ == '__main__':
#     service_1 = multiprocessing.Process(name='question 1', target=my_service)
#     service_2 = multiprocessing.Process(name='question 2', target=my_service)
#     worker_1 = multiprocessing.Process(name='student 1', target=worker)
#     worker_2 = multiprocessing.Process(name='student 2', target=worker)
#
#     service_2.start()
#     worker_1.start()
#     service_1.start()
#     worker_2.start()
