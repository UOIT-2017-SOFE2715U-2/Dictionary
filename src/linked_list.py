

class Node():
    __next = None
    __prev = None
    value = None

    def __init__(self, value, prev, next):
        self.value = value
        self.__prev = prev
        self.__next = next

    def set_next(self,next):
        self.__next = next

    def set_prev(self,prev):
        self.__prev = prev

    def get_next(self):
        return  self.__next

    def get_prev(self):
        return  self.__prev


    #def append_value(self,value):
    #    self.__value.append(value)

    #def remove_value(self, index):
    #    del self.__value[index]


# for dictionary, every node will be a word with its definitions
class DoublyLinkedList():
    __head = None
    __tail = None
    __index = None
    current_node = None

    def __init__(self, first_node_value):
        self.current_node = Node(first_node_value,None, None)
        self.__head = self.current_node
        self.__tail = self.current_node
        self.__index = 0

    def append_node(self,value):
        last_node = self.__tail
        new_node = Node(value, last_node, None)
        last_node.set_next(new_node)
        self.__tail = new_node
        self.current_node = new_node


    def remove_last_node(self):
        new_last_node = self.__tail.get_prev()
        if (self.__head == new_last_node):
            self.__head = None
            self.__tail = None
        else:
            new_last_node.set_next(None)
            self.__tail = new_last_node

    #def remove_node(self,index):

    def next(self):
        self.__current_node = self.__current_node.get_next()
        return self.__current_node

    def prev(self):
        self.__current_node = self.__current_node.get_prev()
        return self.__current_node


'''
    def set_value(self):

    def get_value(self):

    def get_index(self):


'''

