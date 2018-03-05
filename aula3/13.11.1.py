# INSTITUTO TECNOLOGICO DE AERONAUTICA
# CES-22: Programação Orientada a Objetos
# Prof. Dr. Edgar Yano
# Aluno: Bruno Doria
# 1 semestre 2018

# Exercicio 13.11.1

reading_file = open("input_test-13.11.1.txt", "r")
writing_file = open("output_test-13.11.1.txt", "w")
lines_list = []

while True:
    line = reading_file.readline()
    lines_list.append(line)
    if len(line) == 0:
        break

for i in reversed(lines_list):
    writing_file.write(i)

reading_file.close()
writing_file.close()
