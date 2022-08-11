# Implementation of the doubly linked list
class SortedDoublyLinkedList:
    """creates an empty doubly linked list"""
    def __init__(self):
        self.head = None
        self.tail = None
        self.probe = None   # will be used for searching

    # creates the display for our list
    def __str__(self):
        if self.head is None:
            return "[]"
        else:
            string = "["
            curNode = self.head
            while curNode is not None:
                string = string + str(curNode.data) + " <---> "
                curNode = curNode.next
            string = string + "None]"
            return string

    # function inserts an item in a sorted doubly linked list
    def insert(self, value):
        newNode = _DlistNode(value)
        # insert for an empty list
        if self.head is None:
            self.head = newNode
            self.tail = self.head

        # Insert before head
        elif value < self.head.data:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode

        # Insert after the tail
        elif value > self.tail.data:
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode

        else:
            curNode = self.head
            # Traverse through the list and find the node
            # whose data is less than our value
            while curNode is not None and curNode.data < value:
                curNode = curNode.next

            newNode.next = curNode
            newNode.prev = curNode.prev
            curNode.prev.next = newNode
            curNode.prev = newNode

    # function removes an element in the sorted list
    def remove(self, target):
        predNode = None
        curNode = self.head

        # locates our item and stores it inside the curNode
        while curNode is not None and curNode.data != target:
            predNode = curNode
            curNode = curNode.next

        # item has to be in the list to be removed
        if curNode is not None:
            if curNode is self.head:
                self.head = curNode.next
                curNode.next.prev = self.head
            elif curNode is self.tail:
                predNode.next = curNode.next
                self.tail = predNode
            else:
                predNode.next = curNode.next
                curNode.next.prev = predNode
        else:
            print("You can remove an item from an empty list")


# Private storage class for our doubly linked list
class _DlistNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


# Driver Method
dll = SortedDoublyLinkedList()
dll.insert(15)
dll.insert(12)
dll.insert(13)
dll.remove(15)
dll.insert(14)
dll.insert(16)
dll.insert(18)
dll.insert(10)
dll.remove(20)
dll.remove(16)
dll.remove(10)
print(dll)
