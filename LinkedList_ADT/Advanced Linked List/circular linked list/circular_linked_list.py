# Implementation of the single version circular linked list

class CircularLinkedList:
    """Creates an empty circular linked list"""

    def __init__(self):
        self.head = None
        self.tail = None

    # created a display for our list
    def __str__(self):
        if self.tail is None:
            return "[]"
        else:
            string = "["
            curNode = self.tail
            done = self.tail is None
            while not done:
                curNode = curNode.next
                string = string + " <---> " + f"{curNode.item}"
                done = curNode is self.tail
            string = string + "]"
            return string

    # Inserts an item into the list
    def insert(self, value):
        newNode = CListNode(value)
        if self.tail is None:  # for an empty list
            self.tail = newNode
            newNode.next = self.head
        elif value < self.tail.item:  # Insert in front
            newNode.next = self.tail.next
            self.tail.next = newNode
        elif value > self.tail.item:  # Insert in Back
            newNode.next = self.tail.next
            self.tail.next = newNode
            self.tail = newNode
        else:  # insert in the middle
            """position the two pointer"""
            preNode = None
            curNode = self.tail
            done = self.tail is None
            while not done:
                preNode = curNode
                curNode = curNode.next
                done = curNode is self.tail or curNode.item > value
            # Adjust links to insert Node
            newNode.next = curNode
            preNode.next = newNode

    # removing an item in a circular linked list


# Private class for storing the values of each node
class CListNode:
    def __init__(self, item):
        self.item = item
        self.next = None


# Driver method
cll = CircularLinkedList()
cll.insert(12)
cll.insert(14)
cll.insert(11)
cll.insert(13)
print(cll)
