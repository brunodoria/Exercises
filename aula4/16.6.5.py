# INSTITUTO TECNOLOGICO DE AERONAUTICA
# CES-22: Programação Orientada a Objetos
# Prof. Dr. Edgar Yano
# Aluno: Bruno Doria
# 1 semestre 2018

# Exercicio 16.6.5

# classe para um ponto no plano xy
class Point:
    """ Create a new Point, at coordinates x, y """

    def __init__(self, x=0, y=0):
        """ Create a new point at x, y """
        self.x = x
        self.y = y

# classe para o retangulo
class Rectangle:
    """ A class to manufacture rectangle objects """

    def __init__(self, posn, w, h):
        """ Initialize rectangle at posn, with width w, height h """
        self.corner = posn
        self.width = w
        self.height = h

    def there_is_collision(rec1, rec2):
        """ Functions that verifies the superposition between two rectangles"""
        # verificar cada vertice tomando como referência o primeiro retangulo e depois o segundo retangulo
        # assim, cobrem-se os possiveis casos de interseccao
        
        # verificar vertice superior esquerdo
        if ((rec1.corner.x <= rec2.corner.x) and  ((rec1.corner.x + rec1.width) >= rec2.corner.x) and
            (rec1.corner.y <= rec2.corner.y) and ((rec1.corner.y + rec1.width) >= rec2.corner.y)):
            return True
        elif ((rec2.corner.x <= rec1.corner.x) and ((rec2.corner.x + rec2.width) >= rec1.corner.x) and
            (rec2.corner.y <= rec1.corner.y) and ((rec2.corner.y + rec2.width) >= rec1.corner.y)):
            return True
        # verificar vertcie superior direito
        elif ((rec1.corner.x <= (rec2.corner.x + rec2.width)) and ((rec1.corner.x + rec1.width) >= (rec2.corner.x + rec2.width)) and
            (rec1.corner.y <= rec2.corner.y) and ((rec1.corner.y + rec1.width) >= rec2.corner.y)):
            return True
        elif ((rec2.corner.x <= (rec1.corner.x + rec1.width)) and ((rec2.corner.x + rec2.width) >= (rec1.corner.x + rec1.width)) and
            (rec2.corner.y <= rec1.corner.y) and ((rec2.corner.y + rec2.width) >= rec1.corner.y)):
            return True
        # verificar vertice inferior esquerdo
        elif ((rec1.corner.x <= rec2.corner.x) and ((rec1.corner.x + rec1.width) >= rec2.corner.x) and
            (rec1.corner.y <= (rec2.corner.y + rec2.height)) and ((rec1.corner.y + rec1.width) >= (rec2.corner.y + rec2.height))):
            return True
        elif ((rec2.corner.x <= rec1.corner.x) and ((rec2.corner.x + rec2.width) >= rec1.corner.x) and
            (rec2.corner.y <= (rec1.corner.y + rec1.height)) and ((rec2.corner.y + rec2.width) >= (rec1.corner.y + rec1.height))):
            return True
        # verificar vertice superior direito
        elif ((rec1.corner.x <= (rec2.corner.x + rec2.width)) and ((rec1.corner.x + rec1.width) >= (rec2.corner.x + rec2.width)) and
        (rec1.corner.y <= (rec2.corner.y + rec2.height)) and ((rec1.corner.y + rec1.width) >= (rec2.corner.y + rec2.height))):
            return True
        elif ((rec2.corner.x <= (rec1.corner.x + rec1.width)) and ((rec2.corner.x + rec2.width) >= (rec1.corner.x + rec1.width)) and
        (rec2.corner.y <= (rec1.corner.y + rec1.height)) and ((rec2.corner.y + rec2.width) >= (rec1.corner.y + rec1.height))):
            return True
        # caso contrario, nao ha colisao
        else: return False
