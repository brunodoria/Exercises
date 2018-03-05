# INSTITUTO TECNOLOGICO DE AERONAUTICA
# CES-22: Programação Orientada a Objetos
# Prof. Dr. Edgar Yano
# Aluno: Bruno Doria
# 1 semestre 2018

# Exercicio 3.8.11

import turtle

window = turtle.Screen()
window.bgcolor("white")
window.title("Exercicio 3.8.11")

bruno = turtle.Turtle()
bruno.hideturtle()
bruno.penup()
bruno.color("yellow")
bruno.pensize(2)
bruno.speed(2)
bruno.setpos(-80.0, 0.00)
bruno.showturtle()
bruno.pendown()

#draw star
for i in range(5):
    bruno.forward(160)
    bruno.right(144)

bruno.hideturtle()
window.mainloop()
