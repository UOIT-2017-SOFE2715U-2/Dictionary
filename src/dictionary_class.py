import re
import os
from hash_table import *
import pickle


class Dictionary:

    __fileName = "dictionary.csv"
    __filePath = "../data/"
    #__alphabet_table = AlphabetHashTable

    def __init__(self, filePath="../data/", fileName="dictionary.csv"):
        self.__alphabet_table = AlphabetHashTable()
        self.__fileName = fileName
        self.__filePath = filePath
        if not os.path.exists(filePath) or \
                not os.path.isfile(filePath + fileName):
            print "Error! file not found"
            exit()

    def add_definition(self,word, definition):
        self.__alphabet_table.add_definition(word, definition)

    def delete_word(self,word):
        return self.__alphabet_table.delete_word(word)

    def delete_definition(self, word, number):
        return self.__alphabet_table.delete_definition(word, number)

    def edit_definition(self, word, definition_number, new_definition):
        return self.__alphabet_table.edit_definition(word, definition_number, new_definition)

    def get_word_and_definitions(self, word):
        return self.__alphabet_table.get_word_with_definition(word)

    def print_definitions(self, word):
        self.__alphabet_table.print_definitions(word)


    # Reading dictionary.csv
    def load_dictionary_from_CSV(self, file_path, file_name):
        with open(str(file_path) + str(file_name)) as f:
            # skip header line
            f.readline()
            for line in f:
                (word, definition) = line.split(',', 1)
                word = re.sub(r'^"*|"*$', '', word)
                definition = re.sub(r'^"*|"*\n', '', definition)
                self.add_definition(word, definition)

    def save_dictionary_as_CSV(self, filePath = __filePath, fileName = __fileName):
        if not os.path.exists(filePath):
            os.makedirs(filePath)
        with open(str(filePath) + fileName, 'w+') as f:
            for word_table in self.__alphabet_table:
                for word_list in word_table:
                    if word_list is not None:
                        for word_node in word_list:
                            definitions_list = word_node.get_word_with_definitions()
                            word = definitions_list[0]
                            for d in xrange(1, len(definitions_list)):
                                f.writelines(word + ',' + definitions_list[d] + '\n')

    def read_words_from_CSV(self, file_path, file_name, number_of_words ):
        with open(str(file_path) + str(file_name)) as f:
            # skip header line
            f.readline()
            for n in xrange(0, number_of_words):
                line = f.readline()

                (word, definition) = line.split(',', 1)
                word = re.sub(r'^"*|"*$', '', word)
                definition = re.sub(r'^"*|"*\n', '', definition)
                self.add_definition(word, definition)

    def save_dictionary(self, filePath = __filePath, fileName = __fileName):
        with open(str(filePath) + str(fileName),'wb') as f:
            pickle.dump(self.__alphabet_table,f,pickle.HIGHEST_PROTOCOL)
            for word_table in self.__alphabet_table:
                pickle.dump(word_table, f, pickle.HIGHEST_PROTOCOL)


    def load_dictionary(self, filePath = __filePath, fileName = __fileName):
        with open(str(filePath) + str(fileName),'rb') as f:
            self.__alphabet_table = pickle.load(f)
