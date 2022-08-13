# Implementation of various operations that can be performed on a circular linked list

# Traversing a circular linked list
def Traversal(listRef):
    curNode = listRef
    done = listRef is None
    while not done:
        curNode = curNode.next
        print(curNode.data)
        done = curNode is listRef


# Searching a circular linked list
def searchCircularList(listRef, target):
    curNode = listRef
    done = listRef is None
    while not done:
        curNode = curNode.next
        if curNode.data == target:
            return True
        else:
            done = curNode is listRef or curNode.data > target
    return False

