# INSTITUTO TECNOLOGICO DE AERONAUTICA
# CES-22: Programação Orientada a Objetos
# Prof. Dr. Edgar Yano
# Aluno: Bruno Doria
# 1 semestre 2018

# Exercicio 11.22.6

import sys

def test(did_pass):
    """ Print the result of a test. """
    linenum = sys._getframe(1).f_lineno # Get the caller’s line number.
    if did_pass:
        msg = "     Test at line {0} ok.".format(linenum)
    else:
        msg = "     Test at line {0} FAILED.".format(linenum)
    print(msg)

def scalar_mult(scl, vec):
    """Realiza a multiplicacao de um vetor por escalar"""
    result = []
    for i in vec:
        result.append(scl*i)
    return result

test(scalar_mult(5, [1, 2]) == [5, 10])
test(scalar_mult(3, [1, 0, -1]) == [3, 0, -3])
test(scalar_mult(7, [3, 0, 5, 11, 2]) == [21, 0, 35, 77, 14])
