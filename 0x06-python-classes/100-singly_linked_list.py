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
        
def insert_at_beginning(head, data):
    new_node = Node(data)
    new_node.next_node = head

    return new_node

def print_list(head):
    current = head
    while current is not None:
        print(current.data)
        current = current.next_node
head = None
head = insert_at_beginning(head, 5)
head = insert_at_beginning(head, 5)
head = insert_at_beginning(head, 7)

print_list(head)


    
        
        

