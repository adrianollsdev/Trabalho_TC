from classes.automata import Automata

# Importing files of the directory
in_text = open('..\\Trabalho_TC\\Input\\input_text.txt', encoding='UTF-8')
in_search_words = open('..\\Trabalho_TC\\Input\\input_search_word.txt', encoding='UTF-8')
out_info = open('..\\Trabalho_TC\\Output\\output_information.txt', 'a', encoding='UTF-8')

# Reading content of the file
text = in_text.readlines()
search_words = in_search_words.read().splitlines()

# Initializing how list a variable
words_texto = []

# Walking in the lines and extracting words of the text and storaging in the list
for line in text:
    words_texto = words_texto + line.replace('\n', '').split(' ')

# Making the Automata for each word of search, and run Automata for each word of the text
for search_word in search_words:
    automato = Automata.make(search_word)
    automato = Automata.run(search_word, words_texto, automato, out_info)

out_info.close()