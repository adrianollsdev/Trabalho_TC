import re

class Automaton:

    def make(key_word):
        q = []
        for letter in key_word:
            q = q + [letter]
        return q

    def verify_acceptance(word, automato):
        i = 0
        for letter in word:
            if i < len(word):
                # print('letter: ', letter, 'automato[%d]: ' % i, automato[i])
                if letter == automato[i]:
                    i = i + 1
                    if i == len(word)-1 and i == len(automato)-1:
                        return 1
                else:
                    return 0
            else:
                if i == len(word) and i == len(automato):
                   return 1
                else:
                   return 0

    def run(key_word, words_texto, automato, out_info):
        count_i = 0
        count_text = 1
        out_info.write('\nAutomato para a string: %s \n\n' % key_word)
        for word in words_texto:
            flag_accept = Automaton.verify_acceptance(word, automato)
            # print('flag_aceita: ', flag_accept)
            if(flag_accept == 1):
                line = 'Palavra -> ' + str(word) + ' = Aceita......Começa na Posição: ' + str(count_text)
                out_info.write(line +'\n')
            else :
                count_text = count_text + len(word) + 1
            count_i = count_i + 1
        out_info.write('\nCaso não exista valor no intervalo acima é porque não existe a palavra chave no texto\n')
        return 0
        


in_text = open('..\\Trabalho_TC\\Input\\entrada_texto.txt', 'r+', encoding='UTF-8')
in_key_words = open('..\\Trabalho_TC\\Input\\entrada_key_word.txt', encoding='UTF-8')
out_info = open('..\\Trabalho_TC\\Output\\saida_dados.txt', 'a', encoding='UTF-8')


text = in_text.readlines()
in_text.write(' ')
key_words = in_key_words.read().splitlines()
count = 0

for line in text:
    line = re.sub(r'[^\w\s]', '', line)
    words_texto = line.split(' ')

for key_word in key_words:
    automato = Automaton.make(key_word)
    count = count + 1
    automato = Automaton.run(key_word, words_texto, automato, out_info)

out_info.close()