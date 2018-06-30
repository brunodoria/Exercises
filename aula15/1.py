# INSTITUTO TECNOLOGICO DE AERONAUTICA
# CES-22: Programação Orientada a Objetos
# Prof. Dr. Edgar Yano
# Aluno: Bruno Doria
# 1 semestre 2018

# Exercicio 1
# Exemplo de fabrica abstrata

# fabrica abstrata
class AbstractFactory(object):

  def create_product(self):
    pass

# classe de produto a ser solicitada pelo cliente
class Product(object):

  def do_something(self):
    print ("\nProduto disponível ... pronto para ser utilizado.\n")

# fabrica concreta para instanciar o produto
class ConcreteFactory(AbstractFactory):

  def create_product(self):
    return Product()

# cliente
class Client(object):

    def __init__(self, factory):
      self.factory = factory

    # solicita o uso de um produto
    def use_a_product(self):
      product = self.factory.create_product()
      product.do_something()


def main():
  # instanciar objetos
  product = ConcreteFactory()
  client = Client(product)
  # utilizar o produto
  client.use_a_product()

if __name__ == "__main__":
  main()
