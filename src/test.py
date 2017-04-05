from hash_table import *
from dictionary_class import *
from sys import getsizeof

dict = Dictionary("../project-exercises/", "dictionary.csv")
print 'Loading dictionary'
dict.read_words_from_CSV("../project-exercises/", "dictionary.csv",20)

while True:

    print '\n\nChoose and operation:'

    print '1. Search for a word definition'
    print '2. Add definition'
    print '3. Modifiy definition'
    print '4. Delete word'
    print '5. Exit'

    user_choice = raw_input('\n')
    if user_choice == str(1):
        print 'Enter a word: ',
        word = raw_input()
        dict.print_definitions(word)

    elif user_choice == str(2):
        print 'Enter a word',
        word = raw_input()
        print 'Enter definition',
        definition = raw_input()
        dict.add_definition(word,definition)

    elif user_choice == str(3):
        print 'Enter a word',
        word = raw_input()
        #dict.print_definitions(word)
        word_def =  dict.get_word_and_definitions(word)
        if word_def[0] == True:
            i = 0
            for w in word_def[1]:
                print str(i), w
                i += 1
            print 'Choose which definition to modify [numbers]'
            def_num = raw_input()
            print 'Enter new definition'
            new_definition = raw_input()
            dict.edit_definition(word,def_num,new_definition)
            dict.print_definitions(word)
        else:
            print "Error: word doesn't exist"
    elif user_choice == str(4):
        print 'Enter a word'
        word = raw_input()
        dict.delete_word(word)

    elif user_choice == str(5):
        break
    else:
        print 'Wrong input. Input range (1 - 5)'
