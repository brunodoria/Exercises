# INSTITUTO TECNOLOGICO DE AERONAUTICA
# CES-22: Programação Orientada a Objetos
# Prof. Dr. Edgar Yano
# Aluno: Bruno Doria
# 1 semestre 2018

# Exercicio 8.19.10

import sys
import string

def test(did_pass):
    """ Print the result of a test. """
    linenum = sys._getframe(1).f_lineno # Get the caller’s line number.
    if did_pass:
        msg = "     Test at line {0} ok.".format(linenum)
    else:
        msg = "     Test at line {0} FAILED.".format(linenum)
    print(msg)

def reverse(word):
    """Inverte os caracteres de um palavra"""
    rev_word = ""
    for i in range(1, len(word)+1):
        rev_word = rev_word + word[len(word) - i]
    return rev_word

def is_palindrome(word):
    """Verifica se uma palavra é um palindromo"""
    if word == reverse(word):
        return True
    else:
        return False

#casos de teste fornecidos
test(is_palindrome("abba"))
test(not is_palindrome("abab"))
test(is_palindrome("tenet"))
test(not is_palindrome("banana"))
test(is_palindrome("straw warts"))
test(is_palindrome("a"))
test(is_palindrome(""))
