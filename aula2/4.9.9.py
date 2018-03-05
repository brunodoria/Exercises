# INSTITUTO TECNOLOGICO DE AERONAUTICA
# CES-22: Programação Orientada a Objetos
# Prof. Dr. Edgar Yano
# Aluno: Bruno Doria
# 1 semestre 2018

# Exercicio 4.9.9

import turtle

def draw_star():
    '''Function that draws a star using turtle module'''
    window = turtle.Screen()
    window.bgcolor("white")
    window.title("Exercicio 4.9.9")

    tess = turtle.Turtle()
    tess.color("black")
    tess.pensize(2)
    tess.speed(2)

    for i in range(5):
        tess.forward(100)
        tess.right(144)

    tess.hideturtle()
    window.mainloop()

#function call
draw_star()
