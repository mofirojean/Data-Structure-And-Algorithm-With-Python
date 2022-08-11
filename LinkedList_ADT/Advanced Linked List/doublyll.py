# Implementation of the doubly linked list
class DoublyLinkedList:
    """creates an empty doubly linked list"""
    def __init__(self):
        self.head = None
        self.tail = None
        self.probe = None   # will be used for searching


# Private storage class for our doubly linked list
class _DlistNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
