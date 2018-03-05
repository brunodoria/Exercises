# INSTITUTO TECNOLOGICO DE AERONAUTICA
# CES-22: Programação Orientada a Objetos
# Prof. Dr. Edgar Yano
# Aluno: Bruno Doria
# 1 semestre 2018

# Exercicio 7.26.12

import turtle
import math

def turtle_moves(t, list):
    """ Move a 'tartaruga' de acordo com os movimentos indicados """
    for (a,b) in list:
        t.forward(a)
        t.right(b)

window = turtle.Screen()
window.bgcolor("white")
window.title("Exercicio 7.26.12")

bruno = turtle.Turtle()
bruno.color("black")
bruno.pensize(4)
bruno.speed(2)
bruno.left(90)

turtle_moves(bruno, [(50, 30), (50, 120), (50, 75), (50*math.sqrt(2), 225), (50, 270), (50, 270), (50, 225), (50*math.sqrt(2), 0)])

window.mainloop()
