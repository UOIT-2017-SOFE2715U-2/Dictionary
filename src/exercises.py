from dictionary_class import *

filePath = "../project-exercises/"
fileName_definitions = "definitions.csv"
fileName_dictionary = "dictionary.csv"
fileName_words = "words.txt"

dict = dictionary()
dict.read(filePath, fileName_dictionary,100)

