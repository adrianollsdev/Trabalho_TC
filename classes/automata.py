import re

class Automata:

    def make(search_key):
        q = []
        for letter in search_key:
            q = q + [letter]
        return q

    def verify_acceptance(word, automata):
        i = 0
        word = Automata.clean_word(word)

        for letter in word:
            
            if i < len(word) and i < len(automata):
                if letter == automata[i]:
                    i += 1
                    if i == len(word) and i == len(automata):
                        return 1
                else:
                    return 0
            else:
                if i == len(word) and i == len(automata):
                   return 1
                else:
                   return 0
        return 0

    def run(search_key, words_text, automata, out_info):
        count_pos   = 1
        count_print = 0
        separator   = ''

        text_automata = Automata.print_automata(automata)
        out_info.write('\n****Automato para reconhecer a string %s \n\n' % search_key)
        out_info.write(separator.join(text_automata))
        out_info.write('\n\n')
        
        for word in words_text:
            word_print = Automata.clean_word(word)
            flag_accept = Automata.verify_acceptance(word, automata)
            if(flag_accept == 1):
                line = 'Palavra -> ' + str(word_print) + ' = Encontrada na Posição: ' + str(count_pos)
                out_info.write(line +'\n')
                count_pos = count_pos + len(word) + 1
                count_print += 1
            else :
                count_pos = count_pos + len(word) + 1
        if count_print == 0:
            out_info.write('Não há esta palavra no texto.\n')
        return 0
    
    def clean_word(word):
        return re.sub(r'[^\w\s]', '', word)

    def print_automata(automata):
        text_automata = []
        for i in range(len(automata)):
            if i != 0:
                text_automata += 'Q%d' %i, ' === ', automata[i], ' ===> '
            else:
                text_automata += '|>Q%d' %i, ' === ', automata[i], ' ===> '
            if i == len(automata)-1:
                text_automata += '((Q%d' %(i+1), '))'
        return text_automata