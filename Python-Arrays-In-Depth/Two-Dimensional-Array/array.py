# Implements the Array ADT using array capabilities of the ctypes module
import ctypes


class Array:
    """Creates an array with size element"""
    def __init__(self, size):
        assert size > 0, "Array size must be > 0"
        self._size = size
        # Create the array structure using the ctypes module.
        PyArrayType = ctypes.py_object * size
        self._elements = PyArrayType()
        # Initialize each element.
        self.clear(None)  # the initialisation of this array is done by calling the clear method

    # Returns the size of the array.array2d.clear(7)
    def __len__(self):
        return self._size

    # Gets the contents of the index element
    def __getitem__(self, index):
        assert (0 <= index < len(self)), "Array subscript out of range"
        return self._elements[index]

    # Puts the value in the array element at the index position.
    def __setitem__(self, index, value):
        assert (0 <= index < len(self)), "Array subscript out of range"
        self._elements[index] = value

    # Clears the array by setting each element to a given value
    def clear(self, value):
        for i in range(len(self)):
            self._elements[i] = value

    # Returns the array's iterator for traversing the elements.
    def __iter__(self):
        return _ArrayIterator(self._elements)


# An iterator for the Array ADT.
class _ArrayIterator:
    def __init__(self, theArray):
        self._arrayRef = theArray
        self._curNdx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._curNdx < len(self._arrayRef):
            entry = self._arrayRef[self._curNdx]
            self._curNdx += 1
            return entry
        else:
            raise StopIteration


# Implementation of the Array2D ADT using arrays of arrays
class Array2D:
    """ Creates a 2-D array of size numRows x numCols"""
    def __init__(self, numRows, numCols):
        # Creates a 1-D to store an array reference for each row.
        self._theRows = Array(numRows)

        # Create the 1-D arrays for each row of the 2-D array.
        for i in range(numRows):
            self._theRows[i] = Array(numCols)

    # Returns the number of rows in the 2-D array.
    def numRows(self):
        return len(self._theRows)

    # Returns the number of columns in the 2-D array.
    def numCols(self):
        return len(self._theRows[0])

    # Clears the array by setting every element to the given value.
    def clear(self, value):
        for row in self._theRows:
            row.clear(value)

    # Gets the content of the elements at the position  [i, j]
    def __getitem__(self, ndxTuple):
        assert len(ndxTuple) == 2, "Invalid number of array subscript"
        row = ndxTuple[0]
        col = ndxTuple[1]
        assert (0 <= row < self.numRows()) and (0 <= col < self.numCols()), "Array subscripts out of range"
        theIdArray = self._theRows[row]
        return theIdArray[col]

    # Set the contents of the element at position [i, j] to value.
    def __setitem__(self, ndxTuple, value):
        assert len(ndxTuple) == 2, "Invalid number of array subscript"
        row = ndxTuple[0]
        col = ndxTuple[1]
        assert (0 <= row < self.numRows()) and (0 <= col < self.numCols()), "Array subscripts out of range"
        theIdArray = self._theRows[row]
        theIdArray[col] = value

    # the snapshot function displays the structure of the array stored in a list
    def snapshot(self):
        arrayItems = []
        for row in self._theRows:
            for i in row:
                arrayItems.append(i)
        print(arrayItems)
