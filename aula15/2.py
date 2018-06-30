# INSTITUTO TECNOLOGICO DE AERONAUTICA
# CES-22: Programação Orientada a Objetos
# Prof. Dr. Edgar Yano
# Aluno: Bruno Doria
# 1 semestre 2018

# Exercicio 2
# Exemplo do padrao mediador

import sys

# classe abstrata
class Individual:
  def __init__(self, mediator, identity):
    self._mediator = mediator
    self._id = identity

  def getID(self):
    return self._id

  def send(self, message):
    pass

  def receive(self, message):
    pass

# fabrica concreta
class ConcreteIndividual(Individual):
  def __init__(self, mediator, identity):
    super().__init__(mediator, identity)

  def send(self, message):
    print("Mensagem '" + message + "' enviada por Individuo " + str(self._id))
    self._mediator.distribute(self, message)

  def receive(self, message):
    print("Mensagem '" + message + "' recebida por Individuo " + str(self._id))

# mediador: interface de comunicacao entre os objetos
class Mediator:
  def add(self, colleague):
    pass

  def distribute(self, sender, message):
    pass


# fabrica concreta do mediador
class ConcreteMediator(Mediator):
  def __init__(self):
    Mediator.__init__(self)
    self._colleagues = []

  # lista dos individuos
  def add(self, individual):
    self._colleagues.append(individual)

  # distribuir mensagem e fazer conexão
  def distribute(self, sender, message):
    for individual in self._colleagues:
      if individual.getID() != sender.getID():
        individual.receive(message)


if __name__ == "__main__":

  # instanciar mediador
  mediator = ConcreteMediator()

  # instanciar objetos
  c1 = ConcreteIndividual(mediator, 1)
  c2 = ConcreteIndividual(mediator, 2)
  c3 = ConcreteIndividual(mediator, 3)
  c4 = ConcreteIndividual(mediator, 4)
  c5 = ConcreteIndividual(mediator, 5)

  # adicionar objetos ao mediador
  mediator.add(c1)
  mediator.add(c2)
  # retirando a adicao de um objeto perde-se a comunicacao
  #mediator.add(c3)
  mediator.add(c4)
  mediator.add(c5)

  # exemplo de envio de mensagem, que sera detectada pelo restante dos objetos
  c1.send("Oi, tudo beleza?");
  c5.send("Hello World para voces!");
