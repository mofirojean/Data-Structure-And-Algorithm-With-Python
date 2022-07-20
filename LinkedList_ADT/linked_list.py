from linkedlist import LinkedList


# traversal for our linked list
def traversal(head):
    curNode = head
    while curNode is not None:
        print(curNode.data)
        curNode = curNode.next


# reverse our linked list
def reversal(head):
    curNode = head
    prevNode = None
    while curNode is not None:
        revNode = prevNode
        prevNode = curNode
        curNode = curNode.next
        prevNode.next = revNode


myList = LinkedList()
myList.insert("jean")
myList.insert("jean")
myList.insert("jean")
print(myList)

