# INSTITUTO TECNOLOGICO DE AERONAUTICA
# CES-22: Programação Orientada a Objetos
# Prof. Dr. Edgar Yano
# Aluno: Bruno Doria
# 1 semestre 2018

# Exercicio 1
# Exemplo do padrao ponte

from abc import ABC, abstractmethod

# interface abstrata utilizada pelo cliente
class Web(ABC):

    def __init__(self, implementation):
        self._implementation = implementation

    def __str__(self):
        return 'Interface: {}; Implementation: {}'.format(
            self.__class__.__name__, self._implementation.__class__.__name__)

    @abstractmethod
    def show_page(self):
        pass

# interface 1
class Web1(Web):

    def show_page(self):
        ads = self._implementation.get_ads()
        call_to_action = self._implementation.action()
        print(ads)
        print(call_to_action)
        print('')

# interface 2
class Web2(Web):

    def show_page(self):
        text = self._implementation.get_article()
        print(text)
        print('')

# cliente que interage com o servico
def main():
    a_free = Web1(ImplementationA())
    print(a_free)
    a_free.show_page()

    b_free = Web1(ImplementationB())
    print(b_free)
    b_free.show_page()

    a_paid = Web2(ImplementationA())
    print(a_paid)
    a_paid.show_page()

    b_paid = Web2(ImplementationB())
    print(b_paid)
    b_paid.show_page()

# implementacao desconectada do cliente
class Implementation(ABC):

    def get_article(self):
        return 'normal writing'

    def get_ads(self):
        return 'additionalllllll'

    @abstractmethod
    def action(self):
        pass

# primeira implementacao
class ImplementationA(Implementation):

    def action(self):
        return 'writting ... 1'

# segunda implementacao
class ImplementationB(Implementation):

    def action(self):
        return 'writting ... 2'


if __name__ == '__main__':
    main()
