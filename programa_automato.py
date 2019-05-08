
def monta_automato(key_word):
    q = []
    for letter in key_word:
        q = q + [letter]
    return q

def executa_automato(key_word, words_texto, automato, out_info):
    count_i = 0
    count_text = 0
    flag_aceitacao = 0
    out_info.write('\nAutomato para a string: %s \n\n' % key_word)
    for word in words_texto:
        print(word)
        flag_aceita = automato_aceita(word, automato, flag_aceitacao)
        print('flag_aceita: ', flag_aceita)
        if(flag_aceita == 1):
            line = 'Palavra -> ' + str(word) + ' = Aceita......Começa na Posição: ' + str(count_text)
            print(line)
            out_info.write(line +'\n')
        else :
            count_text = count_text + len(word)
        count_i = count_i + 1
    return 0
        

def automato_aceita(word, automato, flag_aceitacao):
    i = 0
    
    for letter in word:
        if i < len(word):
            print('letter: ', letter, 'automato[%d]: ' % i, automato[i])
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



ent_texto = open('D:\\Users\\adria\\Documentos\\GitHub\\Trabalho_TC\\Input\\entrada_texto.txt', encoding='UTF-8')
ent_key_words = open('D:\\Users\\adria\\Documentos\\GitHub\\Trabalho_TC\\Input\\entrada_key_word.txt', encoding='UTF-8')

out_info = open('D:\\Users\\adria\\Documentos\\GitHub\\Trabalho_TC\\Output\\saida_dados.txt', 'a', encoding='UTF-8')


var_texto = ent_texto.readlines()
var_key_word = ent_key_words.read().splitlines()
count = 0

for linha in var_texto:
    words_texto = linha.replace(',', '').split(' ')

for key_word in var_key_word:
    automato = monta_automato(key_word)
    count = count + 1
    executa_automato(key_word, words_texto, automato, out_info)

out_info.close()