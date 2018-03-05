# INSTITUTO TECNOLOGICO DE AERONAUTICA
# CES-22: Programação Orientada a Objetos
# Prof. Dr. Edgar Yano
# Aluno: Bruno Doria
# 1 semestre 2018

# Exercicio 3.8.6

import turtle

window = turtle.Screen()
window.bgcolor("lightblue")
window.title("Exercicio 3.8.6")

bruno = turtle.Turtle()
bruno.color("green")
bruno.pensize(2)
bruno.speed(2)

#draw triangle
for i in range(3):
    bruno.forward(80)
    bruno.left(120)

#reposition
bruno.penup()
bruno.forward(100)
bruno.pendown()

#draw square
for i in range(4):
    bruno.forward(80)
    bruno.left(90)

#reposition
bruno.penup()
bruno.right(90)
bruno.forward(60)
bruno.pendown()

#draw hexagon
for i in range(6):
    bruno.forward(80)
    bruno.left(60)

#reposition
bruno.penup()
bruno.right(90)
bruno.forward(40)
bruno.pendown()

#draw octogon
for i in range(8):
    bruno.forward(30)
    bruno.left(45)

bruno.hideturtle()
window.mainloop()
