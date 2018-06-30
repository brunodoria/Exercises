# INSTITUTO TECNOLOGICO DE AERONAUTICA
# CES-22: Programação Orientada a Objetos
# Prof. Dr. Edgar Yano
# Aluno: Bruno Doria
# 1 semestre 2018

# Exercicio 2
# Exemplo do padrao decorador

import time

# contagem do tempo de execução
def timing_function(some_function):
    def wrapper():
        t1 = time.time()
        some_function()
        t2 = time.time()
        return "Tempo de execução da função: " + str((t2 - t1)) + "\n"
    return wrapper

# decorador para contar o tempo de execução de determinada função
@timing_function
def my_function1():
    num_list = []
    for num in (range(0, 1000000)):
        num_list.append(num)
    print("\nSoma de 1 a 1000000: " + str((sum(num_list))))

# decorador para contar o tempo de execução de determinada função
@timing_function
def my_function2():
    num_list = []
    for num in (range(0, 20)):
        print('.')

print(my_function1())
print(my_function2())
