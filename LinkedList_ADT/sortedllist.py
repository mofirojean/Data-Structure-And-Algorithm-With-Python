# Implementation of a sorted linked list
class SortedLinkedList:
    """ Constructs an empty linked list"""
    def __init__(self):
        self._head = None

    # Produces a string representation of our linked list
    def __str__(self):
        if self._head is None:
            return "[]"
        else:
            ll_str = "["
            curr = self._head
            while curr is not None:
                ll_str = ll_str + str(curr.data) + " -> "
                curr = curr.next
            ll_str = ll_str + "None]"
            return ll_str

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
            self._head = newNode
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
                self._head = curNode.next
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


# Driver Method
mylist = SortedLinkedList()
mylist.insert(10)
mylist.insert(13)
mylist.insert(12)
mylist.insert(18)
print(mylist)
mylist.delete(12)
print(mylist)
