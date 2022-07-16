# Implementation of the Queue ADT using Python list
class Queue:
    """ Creates an empty queue"""
    def __init__(self):
        self._qList = list()

    def __str__(self):
        lqueue = "["
        for item in self._qList:
            lqueue = lqueue + str(item) + ", "
        lqueue = lqueue + "]"
        return lqueue

    # Returns true if the queue is empty
    def isEmpty(self):
        return len(self._qList) == 0

    # Returns the number of items in the queue
    def __len__(self):
        return len(self._qList)

    # Adds the given item to the queue
    def enqueue(self, item):
        self._qList.append(item)

    # Removes and returns the first item in the queue
    def dequeue(self):
        assert not self.isEmpty(), "Cannot dequeue fro an empty queue"
        return self._qList.pop()

