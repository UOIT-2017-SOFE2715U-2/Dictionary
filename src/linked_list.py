

class Node():
    __next = None
    __prev = None
    __value_list = [None]

    def __init__(self, new_word, prev, next):
        self.__value_list = [None]
        self.__value_list[0] = new_word
        self.__prev = prev
        self.__next = next

    def __len__(self):
        return len(self.__value_list)

    def get_word(self):
        return self.__value_list[0]

    def add_definition(self,definition):
        self.__value_list.append(definition)

    def get_word_with_definitions(self):
        return True, self.__value_list

    def print_definitions(self):
        for i in xrange(1, len(self.__value_list)):
            print str(i) + ": " + self.__value_list[i]

    def remove_definition(self, number):
        if number == 0:
            return False
        else:
            del self.__value_list[number]
            return True

    def edit_definition(self,number, definition):
        number = int(number)
        if number == 0:
            return False, "Number of definition must be larger that 0"
        elif number >= len(self):
            return False, "Error: wrong definition number"
        else:
            self.__value_list[number] = definition
            return True, "Definition changed"

    def set_next(self,next):
        self.__next = next

    def set_prev(self,prev):
        self.__prev = prev

    def get_next(self):
        return  self.__next

    def get_prev(self):
        return  self.__prev

# for dictionary, every node will be a word with its definitions
class DoublyLinkedList():
    __head = None
    __tail = None
    #__index = None
    __len = None
    __current_node = None

    def __init__(self,new_word):
        self.__current_node = None
        self.__current_node = Node(new_word,None, None)
        self.__head = self.__current_node
        self.__tail = self.__current_node
        #self.__index = 0
        self.__len = 1

    def __len__(self):
        return self.__len

    def __iter__(self):
        node = self.__head
        for i in range(0, self.__len):
            yield node
            node = node.get_next()

    def append_word(self,new_word):
        last_node = self.__tail
        new_node = Node(new_word.lower(), last_node, None)
        last_node.set_next(new_node)
        self.__tail = new_node
        self.__current_node = new_node
        self.__len += 1


    def delete_word(self,word):
        # delete the node
        for w in self:
            # words are stored in lower case
            if w.get_word() == word.lower():
                prev_node = w.get_prev()
                next_node = w.get_next()
                #del w
                # check if only one node existed
                if self.__head == self.__tail:
                    self.__head = None
                    self.__tail = None
                elif w == self.__tail:
                    prev_node.set_next(None)
                    self.__tail = prev_node
                elif w == self.__head:
                    next_node.set_prev(None)
                    self.__head = next_node
                else:
                    prev_node.set_next(next_node)
                    next_node.set_prev(prev_node)

                self.__len -= 1
                return True, "Word: " + word + " was deleted from dictionary"
        return False, "Error: word doesn't exist," + word

    def add_definition(self,word, definition):
        for w in self:
            if w.get_word() == word.lower():
                w.add_definition(definition)
                return True
        #if the word doesn't exist
        self.append_word(word)
        self.add_definition(word, definition)

    def remove_definition(self, word, number):
        for w in self:
            if w.get_word() == word.lower():
                w.remove_definition(number)
                if len(w) == 1:
                    return self.delete_word(word)

    def edit_definition(self, word, number, definition):
        for w in self:
            if w.get_word() == word.lower():
                return w.edit_definition(number, definition)
        return False, "Error: word doesn't exist," + word

    def get_word_with_definitions(self, word):
        for w in self:
            if w.get_word() == word.lower():
                return w.get_word_with_definitions()
        return False, "Error: word doesn't exist," + word
    '''
    def remove_last_node(self):
        new_last_node = self.__tail.get_prev()
        if (self.__head == new_last_node):
            self.__head = None
            self.__tail = None
        else:
            new_last_node.set_next(None)
            self.__tail = new_last_node
        self.__len -= 1
    '''

    def print_definitions(self, word):
        for w in self:
            if w.get_word() == word.lower():
                w.print_definitions()
                return
        print "Error: word doesn't exist,", word

    def next(self):
        self.__current_node = self.__current_node.get_next()
        return self.__current_node

    def prev(self):
        self.__current_node = self.__current_node.get_prev()
        return self.__current_node
