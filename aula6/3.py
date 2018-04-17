# INSTITUTO TECNOLOGICO DE AERONAUTICA
# CES-22: Programação Orientada a Objetos
# Prof. Dr. Edgar Yano
# Aluno: Bruno Doria
# 1 semestre 2018

# Exercicio 3
# Crie um exemplo de funcao com lista de argumentos e
# dicionario de argumentos.

# *args e **kwargs sao utilizados na definicao de funcoes e
# permitem que um numero variavel de parametros sejam passados
# para a funcao em questao; a diferenca esta no fato de que kwargs
# trata de argumentos nomeados (keyworded)

def list_all_guests(*args):
    if args is not None:
        for name in sorted(args):
            print(name)
    else: print("Nao ha convidados")

def list_names(**kwargs):
    if kwargs is not None:
        for name, surname in kwargs.items():
            print(name+" "+surname+" is one of the guests")
    else: print("Think about some guests ;)")

print("\nHere is a party prototype")
print("I want to invite:")
list_names(Lee = "Miller", Anna = "Bolena", Audrey = "Hepburn", Miss = "Moneypenny")
print("\nThat means:")
list_all_guests("Miller", "Bolena", "Hepburn", "Moneypenny")
