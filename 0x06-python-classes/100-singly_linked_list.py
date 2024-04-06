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
        if value is not None and not isinstance(value, Node):
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
        if self.__head is None:
            # If the list is empty, insert the new node as the head
            new_node.next_node = None
            self.__head = new_node
        elif value <= self.__head.data:
            # If the value is less than or equal to the head,
            # insert at the beginning
            new_node.next_node, self.__head = self.__head, new_node
        else:
            # Traverse the list to find the correct position
            curr = self.__head
            while curr.next_node and value > curr.next_node.data:
                curr = curr.next_node
            # Insert the new node after the current node
            new_node.next_node = curr.next_node
            curr.next_node = new_node

    def __str__(self):
        """Define the print() representation of a SinglyLinkedList."""
        current = self.__head

        # values = []
        # while current:
        #     values.append(str(current.data))
        #     current = current.next_node
        # return '\n'.join(values)

        # another way
        string = ""
        while current:
            string += (str(current.data)) + '\n'
            current = current.next_node
        return string[:-1]
