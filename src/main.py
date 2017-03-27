## this is the main entry for the program
# read dictionary.csv from project exercises
# operations: Search, add, delete, edit the definition

from dictionary_class import *

dict = dictionary()
dict.read("../project-exercises/", "dictionary.csv",0)
if dict.search("a"):
    dict.print_definition("a")
else:
    print "word not found"
