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

    # Removes an instance of the item from the bag
    def remove(self, item):
        predNode = None
        curNode = self._head
        while curNode is not None and curNode.data != item:
            predNode = curNode
            curNode = curNode.next

        # The item has to be in the bag to remove it
        if curNode is not None:
            self._size -= 1
            if curNode is self._head:
                self._head = curNode.next
            else:
                predNode.next = curNode.next
            return curNode.item
        else:
            print(f"{item} not found in the bag")

    # Returns and iterator for traversing the list of items
    def __iter__(self):
        return _LinkedListIterator(self._head)


# Defines a private storage class for creating list nodes
class _BagListNode:
    def __init__(self, item):
        self._item = item
        self.next = None


# Defines a linked list iterator
class _LinkedListIterator:
    def __init__(self, listHead):
        self._curNode = listHead

    def __iter__(self):
        return self

    def next(self):
        if self._curNode is None:
            raise StopIteration
        else:
            item = self._curNode.next
            self._curNode = self._curNode.next
            return item

