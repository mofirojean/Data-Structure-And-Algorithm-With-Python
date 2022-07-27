# implementation of the linear search algorithm
def linearSearch(theValues, target):
    n = len(theValues)
    for i in range(n):
        """ If target is in the ith element, return True"""
        if theValues[i] == target:
            return True

    return False  # If not, return False


def sortedLinearSearch(theValue, item):
    n = len(theValue)
    for i in range(n):
        """If target is found in the ith element, return True"""
        if theValue[i] == item:
            return True
        # If target is larger than the ith element, it's not in the sequence.
        elif theValue[i] > item:
            return False

    return False    # The item is not in the sequence


# Driver Method
if __name__ == "__main__":
    theArray = [10, 51, 2, 18, 4, 31, 13, 5, 23, 64, 29]
    print("Linear Search on an unsorted list")
    print("Searching for 31:", linearSearch(theArray, 31))
    print("Searching for 8:", linearSearch(theArray, 8))

    print("\n\nLinear Search on a sorted list")
    sortedArray = sorted(theArray)
    print("Searching for 3:", sortedLinearSearch(sortedArray, 3))
    print("Searching for 4:", sortedLinearSearch(sortedArray, 4))
