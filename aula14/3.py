# INSTITUTO TECNOLOGICO DE AERONAUTICA
# CES-22: Programação Orientada a Objetos
# Prof. Dr. Edgar Yano
# Aluno: Bruno Doria
# 1 semestre 2018

# Exercicio 3
# Exemplo do padrao composito

import sys

# comportamento dos objetos na composicao podendo ser, ou nao, implementados
class Component:
  def getChild(self, index):
    pass

  def add(self, component):
    pass

  def remove(self, index):
    pass

  def operation(self):
    pass

# subclasse: componentes que possuem filhos
# implementacao de todas as funcoes
class Composite(Component):
  def __init__(self):
    Component.__init__(self)
    self._children = []

  def getChild(self, index):
    return self._children[index]

  def add(self, component):
    self._children.append(component)

  def remove(self, index):
    self._children.remove(index)

  def operation(self):
    for i in range(len(self._children)):
      self._children[i].operation()


# subclasse: folha, nao possui filhos
# implementação diferente
class Folha(Component):
  def __init__(self, index):
    Component.__init__(self)
    self._idx = index

  def operation(self):
    print("Operação da folha " + str(self._idx) + ".")

if __name__ == "__main__":
  composite = Composite()
  # adicionar folhas para ilustrar
  for i in range(5):
    composite.add(Folha(i))

  composite.operation()
