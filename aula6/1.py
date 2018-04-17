# INSTITUTO TECNOLOGICO DE AERONAUTICA
# CES-22: Programação Orientada a Objetos
# Prof. Dr. Edgar Yano
# Aluno: Bruno Doria
# 1 semestre 2018

# Exercicio 1
# Crie extensoes no exemplo de classes de poligonos
# regulares de modo a avaliar os diferentes MROs possiveis.

# a ideia para o exericio e trabalhar com heranca multipla
# e aplicar MRO para verificar mais casos

class Shape:
    geometric_type = 'Generic Shape'

    def area(self):
        raise NotImplementedError

    def get_geometric_type(self):
        return self.get_geometric_type

class Plotter:
    def plot(self, ratio, topleft):
        print ('Plotting at {}, ratio {}.'.format(topleft, ratio))

class Polygon(Shape, Plotter):
    geometric_type = 'Polygon'

class RegularPolygon(Polygon):
    geometric_type = 'Regular Polygon'

    def __init__(self, side):
        self.side = side

class RegularPolygon2(Polygon):
    geometric_type = 'Not so regular'

    def __init__(self, side):
        self.side = side

class RegularPolygon3(Polygon):
    def __init__(self, side):
        self.side = side + 1
        self.add = side

class Hexagon1(RegularPolygon):
    pass

class Hexagon(RegularPolygon, RegularPolygon2):
    pass

class Square1(RegularPolygon):
    pass

class Square(RegularPolygon, RegularPolygon3):
    pass


square1 = Square1(1)
hexagon1 = Hexagon1(2)
square = Square(3)
hexagon = Hexagon(4)

print(square1.__class__.__mro__)
print(hexagon1.__class__.__mro__)
print(square.__class__.__mro__)
print(hexagon.__class__.__mro__)
