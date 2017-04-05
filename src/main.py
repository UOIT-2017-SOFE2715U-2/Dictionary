## this is the main entry for the program
# read dictionary.csv from project exercises
# operations: Search, add, delete, edit the definition

from dictionary_class import *
import datetime

start_time = datetime.datetime.now()
dict = Dictionary()
dict.load_dictionary_from_CSV("../project-exercises/", "dictionary.csv")
dict.save_dictionary_as_CSV("../data/", "dictionary.csv")
#dict.load_dictionary("../project-exercises/", "dictionary.p")
end_time = datetime.datetime.now()
print end_time - start_time

#dict.save_dictionary("../project-exercises/", "dictionary.p")

'''
while raw_input('\nDo you want to search for a word? Y/N').lower() == 'y':
    word = raw_input('Enter a word\n')
    dict.print_definitions(word)

'''