# Implementation of the unbounded Priority Queue ADT using a python list
# with new items appended to the end
class PriorityQueue:
    """ Creates an empty unbounded priority queue"""
    def __init__(self):
        self._qList = list()

    # Returns true if queue is empty.
    def isEmpty(self):
        return len(self._qList) == 0

    # Returns the number of items in the queue
    def __len__(self):
        return len(self._qList)

    # Adds a given item to he queue
    def enqueue(self, data_item, priority):
        """Creates a new instance of the storage class and append it to the list"""
        entry = _PriorityQEntry(data_item, priority)
        self._qList.append(entry)

    # Removes and returns the first item in the queue
    def dequeue(self):
        if not self.isEmpty():
            """finds the with the highest priority"""
            highest = self._qList[0].priority
            index = 0
            for i in range(len(self)):
                """see if the ith entry contains a higher priority (smaller integer)"""
                if self._qList[i].priority < highest:
                    highest = self._qList[i].priority
                    high = self._qList[i]
                    index = self._qList.index(high)
            """Remove the entry with the highest priority and return the item"""
            entry = self._qList.pop(index)
            return entry.item
        else:
            print("You cannot dequeue from an empty queue")


# Private storage class for associating queue items with their priority
class _PriorityQEntry(object):
    def __init__(self, item, priority):
        self.item = item
        self.priority = priority


# Driver Method
if __name__ == "__main__":
    myQ = PriorityQueue()
    myQ.enqueue("purple", 5)
    myQ.enqueue("black", 1)
    myQ.enqueue("orange", 3)
    myQ.enqueue("white", 0)
    myQ.enqueue("green", 1)
    myQ.enqueue("yellow", 5)
    # prints all the items in the queue
    while not myQ.isEmpty():
        item = myQ.dequeue()
        print(item)

