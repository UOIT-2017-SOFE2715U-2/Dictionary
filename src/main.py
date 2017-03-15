## this is the main entry for the program
# read dictionary.csv from project exercises
# operations: Search, add, delete, edit the definition

from dictionary_class import *

dict = dictionary(True, "../project-exercises/", "dictionary.csv")
defn = dict.search("aback")
dict.print_definition("aback")

