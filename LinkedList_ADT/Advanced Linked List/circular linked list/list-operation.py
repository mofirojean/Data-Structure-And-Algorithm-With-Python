# Implementation of the single version circular linked list

class CircularLinkedList:
    """Creates an empty circular linked list"""
    def __init__(self):
        self.head = None
        self.tail = None
    
    # Inserts an item into the list
    def insert(self, data):
        newNode = CListNode(data)
        if self.tail is None:           # for an empty list
            self.tail = newNode
            newNode.next = self.head
        elif data < self.tail.data:     # Insert in front
            newNode.next = self.tail.next
            self.tail.next = newNode
        elif data > self.tail.data:     # Insert in Back
            newNode.next = self.tail.next
            self.tail.next = newNode
            self.tail = newNode
        else:                           # insert in the middle
            """position the two pointer"""
            preNode = None
            curNode = self.tail
            done = self.tail is None
            while not done:
                preNode = curNode
                curNode = curNode.next
                done = curNode is self.tail or curNode.data > data
            # Adjust links to insert Node
            newNode.next = curNode
            preNode.next = newNode

    # removing an item in a circular linked list


        

# Private class for storing the values of each node
class CListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

