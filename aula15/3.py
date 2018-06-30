# INSTITUTO TECNOLOGICO DE AERONAUTICA
# CES-22: Programação Orientada a Objetos
# Prof. Dr. Edgar Yano
# Aluno: Bruno Doria
# 1 semestre 2018

# Exercicio 3
# Exemplo do padrao state

import sys

# fabrica abstrata para o estado
class State:
  def handle(self):
    pass

# fabricas concretas, ilustrando possiveis estados
class ConcreteStateA(State):
  def __init__(self):
    State.__init__(self)

  def handle(self):
    print("Estado A -> Finished!")

class ConcreteStateB(State):
  def __init__(self):
    State.__init__(self)

  def handle(self):
    print("Estado B -> Finished!")

class ConcreteStateC(State):
  def __init__(self):
    State.__init__(self)

  def handle(self):
    print("Estado C -> Finished!")

class ConcreteStateD(State):
  def __init__(self):
    State.__init__(self)

  def handle(self):
    print("Estado D -> Finished!")

# interface para interacao com os estados
class Interface:
  def __init__(self):
    self._state = State()

  def setState(self, state):
    self._state = state

  def request(self):
    self._state.handle()


if __name__ == "__main__":

  # instanciar estados
  stateA = ConcreteStateA()
  stateB = ConcreteStateB()
  stateC = ConcreteStateC()
  stateD = ConcreteStateD()

  context = Interface()

  # simular um percurso dos estados ( A -> C -> B -> D )
  context.setState(stateA)
  context.request()

  context.setState(stateC)
  context.request()

  context.setState(stateB)
  context.request()

  context.setState(stateD)
  context.request()
