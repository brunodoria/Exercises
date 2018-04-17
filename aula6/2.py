# INSTITUTO TECNOLOGICO DE AERONAUTICA
# CES-22: Programação Orientada a Objetos
# Prof. Dr. Edgar Yano
# Aluno: Bruno Doria
# 1 semestre 2018

# Exercicio 2
# Pesquise o assunto 'Decoradores'. Desenvolva um
# 'Decorador exemplo'.

def add_tomatoes(func):
   def func_wrapper(self):
       return "{} some tomatoes;".format(func(self))
   return func_wrapper

def add_lettuce(func):
   def func_wrapper(self):
       return "{} lettuce;".format(func(self))
   return func_wrapper

def add_carrots(func):
   def func_wrapper(self):
       return "{} some carrots;".format(func(self))
   return func_wrapper

def add_sesame(func):
   def func_wrapper(self):
       return "{} sesame seeds;".format(func(self))
   return func_wrapper

class Salad(object):
    def __init__(self):
        self.recipient = "bowl"
        self.sauce = "caeser"
        self.mix = True

    @add_lettuce
    @add_tomatoes
    @add_sesame
    @add_carrots
    def complete_salad(self):
        return "Put in a "+self.recipient+" with "+self.sauce+" sauce: "

    @add_lettuce
    @add_tomatoes
    def simple_salad(self):
        return "Put in a "+self.recipient+" with "+self.sauce+" sauce: "


instruction1 = Salad()
instruction2 = Salad()
print("Complete salad -> "+instruction1.complete_salad())
print("Simple salad -> "+instruction2.simple_salad())
