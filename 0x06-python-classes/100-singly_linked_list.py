#!/usr/bin/python3
"""
module 100-singly_linked_list
Contains classes
- Node - creates a singly linked list Node
- SinglyLinkedList - creates the linked list
"""


class Node:
    """
    class Node - creates a Node oject with two private instance attributes
    """

    def __init__(self, data=0, next_node=None):
        """
        Node init - initializes node object
        data - private instance node int attribute
        next_node - private instance attribute next node 'pointer'
        """

        if type(data) is not int:
            raise TypeError("{}".format("data must be an integer"))
        if (next_node is not None):
            if isinstance(next_node, Node) is False:
                raise TypeError("{}".format("next_node must be a Node object"))

        self.__data = data
        self.__next_node = next_node

        @property
        def data(self):
            """
            property_data
            - initializes and gets the data value of the Node object
            """
            return (self.__data)

        @data.setter
        def data(self, value):
            """ setter_data - sets the data value of the Node """

            if isinstance(value, int) is False:
                raise TypeError("{}".format("data must be an integer"))
            self.__data = value

        @property
        def next_node(self):
            """
            property_next_node
            - initializes and gets the next_node value of the node object
            """

            return (self.__next_node)

        @next_node.setter
        def next_node(self, value):
            """ setter_next_node - sets the 'next_node value of the Node """

            if value is not None:
                if isinstance(value, Node) is False:
                    raise TypeError(
                            "{}".format("next_node must be a Node object"))
                self.__next_node = value


class SinglyLinkedList:
    """
    SinglyLinkedList - Pythonic Singly Linked list
    head - public instance attribute
    """

    def __init__(self):
        """ SinglyLinkedList_init - initializes the SLL class"""

        self.__head = None

    def sorted_insert(self, value):
        """ sorted_insert(public_method) - Incrementally inserts a new node"""

        prev = tmp = self.__head
        curr = Node()
        curr.data = value
        curr.next_node = None

        if self.__head is not None:
            while (tmp) is not None:
                if value > tmp.data:
                    prev = tmp
                    tmp = tmp.next_node
                else:
                    break
            if (prev != tmp):
                prev.next_node = curr
            else:
                self.__head = curr
            curr.next_node = tmp
        else:
            self.__head = curr

    def __str__(self):
        """ str return for the node objects"""

        linked_list = []

        tmp = self.__head

        while tmp is not None:
            linked_list.append(str(tmp.data))
            tmp = tmp.next_node
        linked_str = "\n".join(linked_list)
        return (linked_str)
