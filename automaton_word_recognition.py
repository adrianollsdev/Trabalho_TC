import re

class Automaton:

    def make(key_word):
        q = []
        for letter in key_word:
            q = q + [letter]
        return q

    def verify_acceptance(word, automato):
        i = 0
        word = Automaton.clean_word(word)
        for letter in word:
            if i < len(word):
                if letter == automato[i]:
                    i = i + 1
                    if i == len(word) and i == len(automato):
                        i = 0
                        return 1
                else:
                    i = 0
                    return 0
            else:
                if i == len(word) and i == len(automato):
                   i = 0
                   return 1
                else:
                   i = 0
                   return 0

    def run(key_word, words_texto, automato, out_info):
        count_i     = 0
        count_text  = 1
        count_print = 0
        out_info.write('\nAutomato para validar a string: %s \n\n' % key_word)
        for word in words_texto:
            word_print = Automaton.clean_word(word)
            flag_accept = Automaton.verify_acceptance(word, automato)
            if(flag_accept == 1):
                line = 'Palavra -> ' + str(word_print) + ' = Aceita......Começa na Posição: ' + str(count_text)
                out_info.write(line +'\n')
                count_text = count_text + len(word) + 1
                count_print += 1
            else :
                count_text = count_text + len(word) + 1
            count_i = count_i + 1
        if count_print == 0:
            out_info.write('Não há esta palavra no texto.\n')
        return 0
    
    def clean_word(word):
        return re.sub(r'[^\w\s]', '', word)


in_text = open('..\\Trabalho_TC\\Input\\input_text.txt', encoding='UTF-8')
in_key_words = open('..\\Trabalho_TC\\Input\\input_key_word.txt', encoding='UTF-8')
out_info = open('..\\Trabalho_TC\\Output\\output_information.txt', 'a', encoding='UTF-8')


text = in_text.readlines()
key_words = in_key_words.read().splitlines()
count = 0
words_texto = []

for line in text:
    words_texto = words_texto + line.replace('\n', '').split(' ')

for key_word in key_words:
    automato = Automaton.make(key_word)
    count = count + 1
    automato = Automaton.run(key_word, words_texto, automato, out_info)

out_info.close()