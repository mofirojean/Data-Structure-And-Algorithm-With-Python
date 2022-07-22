# Implementation of a sorted linked list
class SortedLinkedList:
    """ Constructs an empty linked list"""
    def __init__(self):
        self._head = None

    # Inserts an item to its exact position in the sorted list
    def insert(self, item):
        """Finds the insertion point for the new value"""
        predNode = None
        curNode = self._head
        while curNode is not None and item > curNode.data:
            predNode = curNode
            curNode = curNode.next

        # creates the new node for the item
        newNode = _ListNode(item)
        newNode.next = curNode
        # link the new node into the list
        if curNode is self._head:
            head = newNode
        else:
            predNode.next = newNode

    # deletes the instance of the node containing the item
    def delete(self, item):
        predNode = None
        curNode = self._head
        while curNode is not None and item > curNode.data:
            predNode = curNode
            curNode = curNode.next

        # Unlike the node containing the item
        if curNode is not None:
            if curNode is self._head:
                head = curNode.next
            else:
                predNode.next = curNode.next

    # search for an item in the sorted list
    def sortedSearch(self, item):
        curNode = self._head
        while curNode is not None and curNode.data < item:
            if curNode.data == item:
                return True
            else:
                curNode = curNode.next
        return False


# Defines a private storage class for creating list nodes
class _ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
