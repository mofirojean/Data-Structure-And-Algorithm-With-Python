# Implements the Bag ADT container using a Python list.
from BagIterator import _BagIterator


class Bag:
    """Constructs an empty bag"""

    def __init__(self):
        self._theItems = list()

    # Return the number of items in the bag.
    def __len__(self):
        return len(self._theItems)

    # Determines if an item is contained in the bag
    def __contains__(self, item):
        return item in self._theItems

    # Adds a bew item to the bag
    def add(self, item):
        self._theItems.append(item)

    # Removes and returns an instance of the item from the bag
    def remove(self, item):
        assert item in self._theItems, "The item must be in the bag"
        ndx = self._theItems.index(item)
        return self._theItems.pop(ndx)

    # Returns an iterator for traversing the list of items
    def __iter__(self):
        return _BagIterator(self._theItems)


myBag = Bag()
myBag.add("clothes")
myBag.add("clothes")
myBag.add("clothes")
myBag.__iter__()

