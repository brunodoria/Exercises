# INSTITUTO TECNOLOGICO DE AERONAUTICA
# CES-22: Programação Orientada a Objetos
# Prof. Dr. Edgar Yano
# Aluno: Bruno Doria
# 1 semestre 2018

# Exercicio 6.9.16

import sys

def test(did_pass):
    """ Print the result of a test. """
    linenum = sys._getframe(1).f_lineno # Get the caller’s line number.
    if did_pass:
        msg = "     Test at line {0} ok.".format(linenum)
    else:
        msg = "     Test at line {0} FAILED.".format(linenum)
    print(msg)

def is_factor(f, n):
    """ Verifica se um numero é divisor do outro """
    if (n % f == 0):
        return True
    else:
        return False

print("Sequencia de testes propostos:")
test(is_factor(3, 12))
test(not is_factor(5, 12))
test(is_factor(7, 14))
test(not is_factor(7, 15))
test(is_factor(1, 15))
test(is_factor(15, 15))
test(not is_factor(25, 15))
