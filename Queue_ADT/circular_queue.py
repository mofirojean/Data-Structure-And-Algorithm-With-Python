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

    # Returns the number of items in the queue.
    def __len__(self):
        return self._count

    # Adds the given item to the queue
    def enqueue(self, item):
        if not self.isFull():
            maxSize = len(self._qArray)
            self._back = (self._back + 1) % maxSize
            self._qArray[self._back] = item
            self._count += 1
        else:
            print("Cannot enqueue to a full queue")

    # Removes and returns the first item in the queue
    def dequeue(self):
        if not self.isEmpty():
            item = self._qArray[self._front]
            maxSize = len(self._qArray)
            self._front = (self._front + 1) % maxSize
            self._count -= 1
            return item
        else:
            print("Cannot dequeue from an empty queue")


# Driver method
if __name__ == "__main__":
    myQ = Queue(5)
    myQ.enqueue("Mary")
    myQ.enqueue("John")
    myQ.enqueue("Jean")
    myQ.enqueue("Peter")
    print(myQ)
