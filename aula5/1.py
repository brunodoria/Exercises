# INSTITUTO TECNOLOGICO DE AERONAUTICA
# CES-22: Programação Orientada a Objetos
# Prof. Dr. Edgar Yano
# Aluno: Bruno Doria
# 1 semestre 2018

# Exercicio 1
# Crie um exemplo usando metodos abstratos, metodos
# estaticos e metodos de classe. O exemplo deve ilustrar
# as vantagens de cada tipo de metodo.

# metodo estatico: nao tem nenhum conhecimneto da classe ou instancia
# pela qual foi chamado, possui o argumento que lhe foi passado, sem argumentos
# implicitos relacionados a classe

# metodo de classe: util para elaborar factories; estao associados a classe
# em si, seu primeiro argumento sera a propria classe

# metodo abstrato: e um metodo declarado na classe, mas que nao possui uma
# implementacao; nao sao instanciadas de modo que as subclasses eventualmente
# realizam a implementacao

import abc

class Sandwich(object):
    def __init__(self, bread, sauce):
        self.bread = bread
        self.sauce = sauce

    def get_bread(self):
        return "The bread is {}".format(self.bread)

    @staticmethod
    def get_sauce(sauce):
        return "The sauce is {}".format(str(sauce))

    @classmethod
    def double_sauce(cls):
        return "Double of {}".format(cls.sauce)

    @abc.abstractmethod
    def grilled_sandwich():
        pass

class GrillSandwich(Sandwich):
    def __init__(self, time):
        self.time = time

    def grilled_sandwich(self):
        return "In the oven for {} min".format(self.time)
