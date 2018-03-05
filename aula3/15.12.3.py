# INSTITUTO TECNOLOGICO DE AERONAUTICA
# CES-22: Programação Orientada a Objetos
# Prof. Dr. Edgar Yano
# Aluno: Bruno Doria
# 1 semestre 2018

# Exercicio 15.12.3

class Point:
    """ Create a new Point, at coordinates x, y """

    def __init__(self, x=0, y=0):
        """ Create a new point at x, y """
        self.x = x
        self.y = y

    def slope_from_origin(self):
        """ Slope of the line joining the origin to the point """
        if self.x == 0:
            print ("A tangente do angulo nãp possui valor definido")
            return ("Ponto pertencente ao eixo das ordenadas")
        else:
            return ((self.y)/(self.x))
