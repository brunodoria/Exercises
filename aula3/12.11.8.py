# INSTITUTO TECNOLOGICO DE AERONAUTICA
# CES-22: Programação Orientada a Objetos
# Prof. Dr. Edgar Yano
# Aluno: Bruno Doria
# 1 semestre 2018

# Exercicio 12.11.8

import sys
import string

def test(did_pass):
    """ Print the result of a test. """
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "     Test at line {0} ok.".format(linenum)
    else:
        msg = "     Test at line {0} FAILED.".format(linenum)
    print(msg)

def cleanword(word):
    """Removes any odd character from the input word"""

    odd_set = ["!", "@", "#", "$", "%", "¨", "&", "*", "(", ")", "-", "+",
    "_", "=", "?", "[", "{", "}", "]","/", ":", ";", ",", ".", "<", ">", "'", "’"]
    new_word = ""
    for i in word:
         if i not in odd_set:
             new_word = new_word + i
    return new_word

def cleanword_with_spaces(word):
    """Removes any odd character from the input word"""

    odd_set = ["!", "@", "#", "$", "%", "¨", "&", "*", "(", ")", "-", "+",
    "_", "=", "?", "[", "{", "}", "]","/", ":", ";", ",", ".", "<", ">", "'", "’"]
    new_word = ""
    for i in word:
         if i not in odd_set:
             new_word = new_word + i
         else:
             new_word = new_word + " "
    return new_word

def has_dashdash(word):
    """Verifies the presence of -- in the input"""
    if "--" in word:
        return True
    else:
        return False

def extract_words(line):
    """Separates the word in a certain sentence"""
    line = line.lower()
    line = cleanword_with_spaces(line)
    words = line.split()
    return words

def wordcount(word, word_list):
    """Counts the ocurrences of word in list"""
    count = 0
    for i in word_list:
        if (i == word):
            count = count + 1
    return count

def wordset(word_list):
    """Build an ordered set of words"""
    word_set = []
    if len(word_list) != 0:
        for i in word_list:
            if i not in word_set:
                word_set.append(i)
    return sorted(word_set)

def longestword(word_list):
    """Counts the lenght of the longest string"""
    max_lenght = 0
    for i in word_list:
        if (len(i) >= max_lenght):
            max_lenght = len(i)
    return max_lenght

test(cleanword("what?") == "what")
test(cleanword("’now!’") == "now")
test(cleanword("?+=’w-o-r-d!,@$()’") == "word")

test(has_dashdash("distance--but"))
test(not has_dashdash("several"))
test(has_dashdash("spoke--"))
test(has_dashdash("distance--but"))
test(not has_dashdash("-yo-yo-"))

test(extract_words("Now is the time! ’Now’, is the time? Yes, now.") == ["now", "is", "the", "time", "now", "is", "the", "time", "yes", "now"])
test(extract_words("she tried to curtsey as she spoke--fancy") == ["she", "tried", "to", "curtsey", "as", "she", "spoke", "fancy"])

test(wordcount("now", ["now","is","time","is","now","is","is"]) == 2)
test(wordcount("is", ["now","is","time","is","now","the","is"]) == 3)
test(wordcount("time", ["now","is","time","is","now","is","is"]) == 1)
test(wordcount("frog", ["now","is","time","is","now","is","is"]) == 0)

test(wordset(["now", "is", "time", "is", "now", "is", "is"]) ==
["is", "now", "time"])
test(wordset(["I", "a", "a", "is", "a", "is", "I", "am"]) ==
["I", "a", "am", "is"])
test(wordset(["or", "a", "am", "is", "are", "be", "but", "am"]) ==
["a", "am", "are", "be", "but", "is", "or"])

test(longestword(["a", "apple", "pear", "grape"]) == 5)
test(longestword(["a", "am", "I", "be"]) == 2)
test(longestword(["this","supercalifragilisticexpialidocious"]) == 34)
test(longestword([ ]) == 0)
