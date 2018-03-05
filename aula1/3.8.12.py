# INSTITUTO TECNOLOGICO DE AERONAUTICA
# CES-22: Programação Orientada a Objetos
# Prof. Dr. Edgar Yano
# Aluno: Bruno Doria
# 1 semestre 2018

# Exercicio 3.8.12

import turtle

window = turtle.Screen()
window.bgcolor("lightgreen")
window.title("Exercicio 3.8.12")

bruno = turtle.Turtle()
bruno.color("blue")
bruno.pensize(2)
bruno.speed(2)
bruno.shape("turtle")
bruno.penup()

#draw pattern
for i in range(12):
    bruno.forward(100)
    bruno.pendown()
    bruno.forward(5)
    bruno.penup()
    bruno.forward(10)
    bruno.stamp()
    bruno.backward(115)
    bruno.right(30)

window.mainloop()
