# Implementation of the Queue ADT using a circular array
from queue_array import Array


class Queue:
    """Creates an empty queue"""
    def __init__(self, maxSize):
        self._count = 0
        self._front = 0
        self._back = maxSize - 1
        self._qArray = Array(maxSize)

    # Returns True if the queue is empty
    def isEmpty(self):
        return self._count == 0

    # Returns True if the queue is full
    def isFull(self):
        return self._count == len(self._qArray)

