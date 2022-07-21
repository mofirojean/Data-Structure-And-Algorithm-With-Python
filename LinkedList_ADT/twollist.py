# implementation of a two reference linked list
class LinkedList:
    """ Constructs an empty list"""
    def __init__(self):
        self._head = None
        self._tail = None

    # Produces a string representation of our list
    def __str__(self):
        if self._head is None:
            return "[]"
        else:
            ll_str = "["
            curNode = self._head
            while curNode is not self._tail.next:
                ll_str = ll_str + str(curNode.data) + " -> "
                curNode = curNode.next
            ll_str = ll_str + "None]"
            return ll_str

    # Inserts a new item in our linked list
    def insert(self, item):
        newNode = _ListNode(item)
        if self._head is None:
            self._head = newNode
        else:
            self._tail.next = newNode
        self._tail = newNode

    # Removes target item from the list
    def remove(self, item):
        predNode = None
        curNode = self._head
        while curNode is not None and curNode.data != item:
            predNode = curNode
            curNode = curNode.next

        if curNode is not None:
            if curNode is self._head:
                head = curNode.next
            else:
                predNode = curNode.next
            if curNode is self._tail:
                self._tail = predNode


# Defines a private storage class for creating list nodes
class _ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
