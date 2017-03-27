

# assumptions: Keys are case insinsitive letters only. numbers are not allowed as keys
# h(key) = key mod m, m is prime number
# some prime numbers: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199
# hash function: parameters can be: word length, sum of ascii codes,
# hash table of hash tables:
# hash table of first letter (26), key = letter order
# hash table of word size (29), key mod 29
# doubly linked list, value: word, definitions

class AlphabetHashTable():
    __values = [] * 26

    def store(self,letter, value):
        # order of litter in alphabets
        self.__values[ord(letter.lower())-97] = value
        return

    def value(self, letter):
        return self.__values[ord(letter.lower())-97]

class HashTable():
    __values = []
    __index = None
    __divisor = None

    def __init__(self, divisor):
        self.__divisor = divisor
        self.__values = [] * divisor

    def pre_hash(self, key):
        return key % self.__divisor

    def store(self,key, value):
        # write it in a way to append an object
        self.__values[self.pre_hash(key)] = value
        return

    def value(self, key):
        return

