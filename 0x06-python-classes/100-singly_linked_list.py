#!/usr/bin/python3
"""
This module defines the `Node` and `SinglyLinkedList` classes.
It creates a singly linked list that supports insertion in a sorted order.
"""


class Node:
    """Class that defines a node of a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initializes the node with data and next_node."""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter method to retrieve the data."""
        return self.__data

    @data.setter
    def data(self, value):
        """Setter method to set the data, ensuring it's an integer."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Getter method to retrieve the next node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setter method to set the next node, ensuring it's a Node or None."""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Class that defines a singly linked list."""

    def __init__(self):
        """Initializes an empty singly linked list."""
        self.__head = None

    def __str__(self):
        """Returns a string representation of the list."""
        node = self.__head
        values = []
        while node is not None:
            values.append(str(node.data))
            node = node.next_node
        return "\n".join(values)

    def sorted_insert(self, value):
        """Inserts a new Node into the correct sorted position in the list."""
        new_node = Node(value)  # Create the new node

        """Case 1: The list is empty or the new node should be the new head"""
        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            """Case 2: Insert node in the correct sorted position"""
            current = self.__head
            while (current.next_node is not None and
                   current.next_node.data < value):
                current = current.next_node

            """Insert the new node"""
            new_node.next_node = current.next_node
            current.next_node = new_node
