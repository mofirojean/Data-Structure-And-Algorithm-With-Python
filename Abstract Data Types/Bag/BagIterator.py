# An iterator for the Bag ADT implemented as a Python list.
class _BagIterator:
    def __init__(self, theList):
        self._bagItems = theList
        self._curItem = 0

    # The __iter__ method simply returns a reference to the object itself
    def __iter__(self):
        return self

    # Its called to return the next item in the container
    def __next__(self):
        if self._curItem < len(self._bagItems):
            item = self._bagItems[self._curItem]  # save the reference to the current item
            self._curItem += 1
            return item
        else:
            raise StopIteration
