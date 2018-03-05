# INSTITUTO TECNOLOGICO DE AERONAUTICA
# CES-22: Programação Orientada a Objetos
# Prof. Dr. Edgar Yano
# Aluno: Bruno Doria
# 1 semestre 2018

# Exercicio 7.26.13

#Observando a teoria sobre caminhos eulerianos temos que
#o caminho poderá ser percorrido se tiver zero ou dois vértices com
#um número ímpar de conexões. Analisando os grafos apresentados segue
#que o primeiro, o segundo, o quinto e o sexto podem ser desenhados.

import turtle
import math

def turtle_moves(t, list):
    """ Move a 'tartaruga' de acordo com os movimentos indicados """
    for (a,b) in list:
        t.forward(a)
        t.right(b)

window = turtle.Screen()
window.bgcolor("white")
window.title("Exercicio 7.26.13")

bruno = turtle.Turtle()
bruno.color("black")
bruno.pensize(4)
bruno.speed(2)

#primeiro caminho
bruno.right(90)
turtle_moves(bruno, [(50,270), (50,270), (50,330), (50,240), (50,240), (50,0)])

#segundo caminho
bruno.penup()
bruno.hideturtle()
bruno.setpos(130, 0)
bruno.pendown()
bruno.showturtle()
bruno.left(120)
turtle_moves(bruno, [(50, 240), (50, 240), (50, 90), (50, 90), (50, 90), (50, 135), (50*math.sqrt(2), 0)])

#quinto caminho
bruno.penup()
bruno.hideturtle()
bruno.setpos(0, 100)
bruno.left(180)
bruno.pendown()
bruno.showturtle()
turtle_moves(bruno, [(50, 90), (100, 90), (50, 135), (50*math.sqrt(2), 270),
(50*math.sqrt(2), 270), (50*math.sqrt(2), 270), (50*math.sqrt(2), 135), (50, 90), (50, 0)])

#sexto caminho
bruno.penup()
bruno.hideturtle()
bruno.setpos(180, 100+50*math.sqrt(2))
bruno.pendown()
bruno.showturtle()
turtle_moves(bruno, [(50, 270), (50, 315), (50*math.sqrt(2), 225), (100, 135),
(50*math.sqrt(2), 135), (100, 135), (50*math.sqrt(2), 45), (50, 90),
(100, 90), (50, 135), (50*math.sqrt(2), 0)])

window.mainloop()
