# INSTITUTO TECNOLOGICO DE AERONAUTICA
# CES-22: Programação Orientada a Objetos
# Prof. Dr. Edgar Yano
# Aluno: Bruno Doria
# 1 semestre 2018

# Exercicio 20.8.3

def extract_words(line):
    """Separates the word in a certain sentence"""
    line = line.lower()
    line = cleanword_with_spaces(line)
    words = line.split()
    return words

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

#inicializar os arquivos
input_file = open("alice_example_input.txt", "r")
info_file = open("alice_info.txt", "w")
#escrever o inicio do arquivo de saida
info_file.write("Word               Count\n")
info_file.write("========================\n")
#ler o arquivo texto
words_in_file = input_file.read()
#extrair as palavras de modo util e colocar em ordem alfabetica
words = sorted(extract_words(words_in_file))
#criar um conjunto auxiliar(sem repeticoes)
set_of_words = wordset(words)

#para cada palavra
for word in set_of_words:
    #contar as ocorrencias
    freq = wordcount(word, words)
    #imprimir palavra
    info_file.write('{}'.format(word))
    #alinhar a impressao da tabela
    num = 25 - len(word) - len(str(freq)) - 1
    for i in range(num):
        info_file.write(' ')
    #imprimir ocorrencias
    info_file.write('{}\n'.format(freq))

#encerrar a utilizacao dos arquivos
input_file.close()
info_file.close()
