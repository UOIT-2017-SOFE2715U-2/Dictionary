import re
import os


class dictionary:

    __fileName = "dictionary.csv"
    __filePath = "../data/"
    __dictionary = {}

    def __init__(self,filePath = "../data/", fileName = "dictionary.csv" ):
        self.__fileName = fileName
        self.__filePath = filePath
        if not os.path.exists(filePath) or\
            not os.path.isfile(filePath + fileName):
            print "Error! file not found"
            exit()
    '''
        else:
            self.read(filePath,fileName,0)
            if new_file:
                self.write()
    '''

    # Reading dictionary.csv
    def read(self, filePath, fileName, number_of_lines):
        with open(str(filePath) + str(fileName)) as f:
            # skip header line
            f.readline()

            for line in f:
            #for i in xrange(0,number_of_lines):
             #   line = f.next()
                (key, val) = line.split(',', 1)
                key = re.sub(r'^"*|"*$', '', key)
                val = re.sub(r'^"*|"*\n', '', val)
                if self.__dictionary.has_key(key):
                    self.__dictionary[key] = self.__dictionary[key] + [val]
                else:
                    self.__dictionary[key] = [val]
        self.write()


    # writing to our dictionary
    def write(self, filePath = __filePath, fileName = __fileName):
        if not os.path.exists(filePath):
            os.makedirs(filePath)
        with open(str(filePath) + fileName, 'w+') as f:
            for word in self.__dictionary:
                for definition in self.__dictionary[word]:
                    f.writelines(word + ',' + definition + '\n')

    def search(self, word):
        if self.__dictionary.has_key(word):
            return self.__dictionary[word]
        else:
            return False


    def add(self, word, definition):
        if self.__dictionary.has_key(word):
            self.__dictionary[word] = self.__dictionary[word] + [definition]
        else:
            self.__dictionary[word] = [definition]
        self.write()



    def delete(self, word):
        if self.__dictionary.has_key(word):
            temp = self.__dictionary[word]
            del self.__dictionary[word]
            self.write()
            return temp
        else:
            return False


    def edit(self, word, definition_no, new_definition):
        if self.__dictionary.has_key(word) and\
                (len(self.__dictionary[word]) >= definition_no):
            self.__dictionary[word][definition_no-1]=new_definition
            self.write()
            return self.__dictionary[word]
        else:
            return False

    def print_definition(self,word):
        i = 0
        for definition in self.__dictionary[word]:
            i += 1
            print str(i) + "\t" + definition
