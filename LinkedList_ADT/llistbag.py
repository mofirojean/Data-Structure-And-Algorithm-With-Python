# Implementation of the Bag ADT using a singly linked list

class Bag:
    """ Constructs an empty bag"""
    def __init__(self):
        self._head = None
        self._size = 0

    # Returns the number of items in the bag
    def __len__(self):
        return self._size

    # Determines if an item is contain in the bag
    def __contains__(self, item):
        curNode = self._head
        while curNode is not None and curNode.data != item:
            curNode = curNode.next
        return curNode is not None

    # Adds a new item to the bag
    def add(self, item):
        newNode = _BagListNode(item)
        newNode.next = self._head
        self._head = newNode
        self._size += 1


# Defines a private storage class for creating list nodes
class _BagListNode:
    def __init__(self, item):
        self._item = item
        self.next = None
