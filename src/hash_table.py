from linked_list import *

# assumptions: Keys are case insinsitive letters only. numbers are not allowed as keys
# h(key) = key mod m, m is prime number
# some prime numbers: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199
# hash function: parameters can be: word length, sum of ascii codes,
# hash table of hash tables:
# hash table of first letter (26), key = letter order
# hash table of word size (29), key mod 29
# doubly linked list, value: word, definitions

class AlphabetHashTable():
    __word_tables = [None] * 27

    def __init__(self):
        for i in xrange(0, 27):
            self.__word_tables[i] = WordsHashTable(29)

    def __iter__(self):
        for i in xrange(0, 27):
            yield self.__word_tables[i]

    def pre_hash(self,letter):
        ascii = ord(letter.lower())
        if ascii >= 97 and ascii <= 122:
            return ascii - 97
        else:
            return 26

    def store(self,letter, value):
        key = self.pre_hash(letter)
        # order of litter in alphabets
        self.__word_tables[key] = value

    def get_word_table(self, letter):
        key = self.pre_hash(letter)
        return self.__word_tables[key]

    def add_word(self, word):
        key = self.pre_hash(word[0])
        self.__word_tables[key].add_word(word)

    def delete_word(self, word):
        key = self.pre_hash(word[0])
        self.__word_tables[key].delete_word(word)

    def add_definition(self, word, definition):
        key = self.pre_hash(word[0])
        self.__word_tables[key].add_definition(word, definition)

    def delete_definition(self, word, number):
        key = self.pre_hash(word[0])
        self.__word_tables[key].delete_definition(word, number)

    def edit_definition(self, word, definition_number, new_definition):
        key = self.pre_hash(word[0])
        self.__word_tables[key].edit_definition(word, definition_number)

    def get_word_with_definition(self, word):
        key = self.pre_hash(word[0])
        return self.__word_tables[key].get_word_with_definition(self,word)

    def print_definitions(self, word):
        key = self.pre_hash(word[0])
        self.__word_tables[key].print_definitions(word)


class WordsHashTable():
    # every cell store either None or Doubly Linked list
    __cell = []
    __index = None
    __divisor = None

    # divisor was choosen to 29 based on the length of longest uncoined word in dictionaries
    def __init__(self, divisor=29):
        self.__divisor = divisor
        self.__cell = [None] * divisor

        #for i in xrange(0, divisor):
         #   self.__cell[i] = DoublyLinkedList()

    def __iter__(self):
        for i in xrange(0, self.__divisor):
            yield self.__cell[i]

    def pre_hash(self, word):
        return len(word) % self.__divisor

    def add_word(self,word):
        # if it is first word in this cell
        key = self.pre_hash(word)
        if self.__cell[key] is None:
            new_linked_list = DoublyLinkedList(word)
            self.__cell[key] = new_linked_list
        else:
            #if it is not None, it should be DoublyLinknedList
            self.__cell[key].append_word(word)

    def delete_word(self,word):
        key = self.pre_hash(word)
        if self.__cell[key] is None:
            print "Error: word doesn't exist"
            return False
        else:
            self.__cell[key].delete_word(word)

    def add_definition(self,word, definition):
        key = self.pre_hash(word)
        if self.__cell[key] is None:
            self.add_word(word)

        self.__cell[key].add_definition(word, definition)

    def delete_definition(self, word, number):
        key = self.pre_hash(word)
        if self.__cell[key] is None:
            print "Error: word doesn't exist"
        else:
            self.__cell[key].delete_definition(word, number)

    def edit_definition(self, word, number, new_definition):
        key = self.pre_hash(word)
        if self.__cell[key] is None:
            print "Error: word doesn't exist"
        else:
            self.__cell[key].edit_definition(word, number, new_definition)

    def get_word_with_definition(self,word):
        key = self.pre_hash(word)
        if self.__cell[key] is None:
            print "Error: word doesn't exist"
            return False
        else:
            return self.__cell[key].get_word_with_definitions(word)

    def print_definitions(self,word):
        key = self.pre_hash(word)
        if self.__cell[key] is None:
            print "Error: word doesn't exist"
            return False
        else:
            self.__cell[key].print_definitions(word)


    def value(self, key):
        return self.__cell[self.pre_hash(key)]

