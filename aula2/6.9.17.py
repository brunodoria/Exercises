# INSTITUTO TECNOLOGICO DE AERONAUTICA
# CES-22: Programação Orientada a Objetos
# Prof. Dr. Edgar Yano
# Aluno: Bruno Doria
# 1 semestre 2018

# Exercicio 6.9.17

import sys

def test(did_pass):
    """ Print the result of a test. """
    linenum = sys._getframe(1).f_lineno # Get the caller’s line number.
    if did_pass:
        msg = "     Test at line {0} ok.".format(linenum)
    else:
        msg = "     Test at line {0} FAILED.".format(linenum)
    print(msg)

def is_multiple(f, n):
    """ Verifica se um numero é multiplo do outro """
    if (f % n == 0):
        return True
    else:
        return False

print("Sequencia de testes propostos:")
test(is_multiple(12, 3))
test(is_multiple(12, 4))
test(not is_multiple(12, 5))
test(is_multiple(12, 6))
test(not is_multiple(12, 7))
