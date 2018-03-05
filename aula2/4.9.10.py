# INSTITUTO TECNOLOGICO DE AERONAUTICA
# CES-22: Programação Orientada a Objetos
# Prof. Dr. Edgar Yano
# Aluno: Bruno Doria
# 1 semestre 2018

# Exercicio 4.9.10

import turtle

def draw_five_star():
    '''Function that draws a five-star set using turtle module'''
    window = turtle.Screen()
    window.bgcolor("lightgreen")
    window.title("Exercicio 4.9.10")

    tess = turtle.Turtle()
    tess.hideturtle()
    tess.penup()
    tess.setpos(-200,0)
    tess.showturtle()
    tess.pendown()
    tess.color("pink")
    tess.pensize(2)
    tess.speed(5)

    for j in range(5):
        for i in range(5):
            tess.forward(100)
            tess.right(144)
        tess.penup()
        tess.forward(350)
        tess.right(144)
        tess.pendown()

    tess.hideturtle()
    window.mainloop()

#function call
draw_five_star()
