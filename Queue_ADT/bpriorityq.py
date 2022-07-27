# Implementation of the Bounded Priority QUEUE ADT using an array of
# queues in which queues are implemented using a linked list.
from queue_array import Array
from llqueue import Queue


class BPriorityQueue:
    """ Creates an empty bounded priority queue"""
    def __init__(self, numLevels):
        self._qSize = 0
        self._qLevels = Array(numLevels)
        for i in range(numLevels):
            self._qLevels = Queue()

    # Returns True if the queue is empty
    def isEmpty(self):
        return self._qSize == 0

    # Returns the number of items in the queue
    def __len__(self):
        return self._qSize

    # Adds the given items in the queue
    def enqueue(self, item, priority):
        if 0 <= priority < len(self._qLevels):
            self._qLevels[priority].enqueue(item)
        else:
            print("Invalid priority level")

    # Removes and returns the next item in the queue
    def dequeue(self):
        """makes sure the queue is not empty"""
        if not self.isEmpty():
            """find the first empty queue"""
            i = 0
            p = len(self._qLevels)
            while i < p and self._qLevels[i].isEmpty():
                i += 1
            """We know the queue is not empty so we dequeue from ith queue"""
            return self._qLevels[i].dequeue()
