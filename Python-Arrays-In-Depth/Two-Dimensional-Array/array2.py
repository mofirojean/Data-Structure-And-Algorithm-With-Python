import ctypes


class Array:
    # initialising our class attributes
    def __init__(self, size):
        # testing our size
        assert size > 0, "Array size is invalid!"

        ArrayPythonType = ctypes.py_object * size
        self._element = ArrayPythonType()

        self.clear(None)

    # methods of our class
    def length(self):
        return len(self._element)

    def getitem(self, index):
        assert index >= 0 or index < self.length(), "Array index out of bounds"
        return self._element[index]

    def setitem(self, index, value):
        assert index >= 0 or index < self.length(), "Array index out of bounds"
        self._element[index] = value

    def clear(self, value):
        for i in range(self.length()):
            self._element[i] = value

    def snapshot(self):
        arraylist = []
        for item in self._element:
            arraylist.append(item)
        print("Array: ", arraylist)


kelly = Array(5)
kelly.snapshot()
kelly.setitem(0, "KB")
kelly.setitem(2, "Kelly Bright")
kelly.setitem(4, "KELLY")
kelly.snapshot()
print(kelly.getitem(2))
