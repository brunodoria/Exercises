# INSTITUTO TECNOLOGICO DE AERONAUTICA
# CES-22: Programação Orientada a Objetos
# Prof. Dr. Edgar Yano
# Aluno: Bruno Doria
# 1 semestre 2018

# Exercicio 11.22.5

import sys

def test(did_pass):
    """ Print the result of a test. """
    linenum = sys._getframe(1).f_lineno # Get the caller’s line number.
    if did_pass:
        msg = "     Test at line {0} ok.".format(linenum)
    else:
        msg = "     Test at line {0} FAILED.".format(linenum)
    print(msg)

def add_vectors(a, b):
    """Funcao para adicao de vetores"""
    addition = []
    for i in range(len(a)):
        addition.append(a[i] + b[i])
    return addition

test(add_vectors([1, 1], [1, 1]) == [2, 2])
test(add_vectors([1, 2], [1, 4]) == [2, 6])
test(add_vectors([1, 2, 1], [1, 4, 3]) == [2, 6, 4])
