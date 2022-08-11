# Implementation of the various processes that can be done with a doublyll


# Implementation of the traversal method
# with the tail reference
def revTraversal(tail):
    curNode = tail
    elements = []
    while curNode is not None:
        elements.append(curNode.data)
        curNode = curNode.prev
    return elements


# Traversal using the head reference
def Traversal(head):
    curNode = head
    elements = []
    while curNode is not None:
        elements.append(curNode.data)
        curNode = curNode.next
    return elements


# Searching for an element in our List gib=ven the head,tail and probe references
def search(head, probe, target):
    """make sure the list is not empty"""
    if head is None:
        return False
    # if probe is null initialise it to the first node
    elif probe is None:
        probe = head

    """
        if target comes before the probe node, we traverse backward
        otherwise we traverse forward
    """
    if target < probe.data:
        while probe is not None and target <= probe.data:
            if target == probe.data:
                return True
            else:
                probe = probe.prev
    else:
        while probe is not None and target >= probe.data:
            if target == probe.data:
                return True
            else:
                probe = probe.next

    # If the target is not found in the list return  false
    return False

