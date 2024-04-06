#!/usr/bin/python3

'''square class'''

class Node:
    def __init__(self, data, next_node=None):

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value=None):
        if value != None and not isinstance(value, Node):
            raise TypeError('next_node must be a Node object')
        self.__next_node = value

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        self.__data = value
        
class SinglyLinkedList:
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        new_node = Node(value)
        if self.__head == None:
            new_node.data = value
            new_node.next_node = None
            self.__head = new_node
        else:
            new_node.data = value
            new_node.next_node = self.__head
            self.__head = new_node

    def __str__(self):
        """Define the print() representation of a SinglyLinkedList."""
        current = self.__head

        # values = []
        # while current:
        #     values.append(str(current.data))
        #     current = current.next_node
        # return '\n'.join(values)

        string = ""
        while current:
            string += (str(current.data)) + '\n'
            current = current.next_node
        str_2 = string[:-1]
        return str_2

    


    
        
        

