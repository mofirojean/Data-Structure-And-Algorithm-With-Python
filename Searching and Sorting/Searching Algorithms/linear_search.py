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


# Finds the smallest value in an unsorted list
def findSmallest(theValues):
    n = len(theValues)
    # Assume the first item is the smallest
    smallest = theValues[0]
    # Determine if any other item in the sequence is smaller
    for i in range(1, n):
        if theValues[i] < smallest:
            smallest = theValues[i]

    return smallest     # Return the smallest found


# Finds the greatest value in an unsorted list
def findGreatest(theValues):
    n = len(theValues)
    # Assume the first item is the greatest value
    greatest = theValues[0]
    # Determine if any other item in the sequence is greater
    for i in range(1, n):
        if theValues[i] > greatest:
            greatest = theValues[i]

    return greatest     # Returns the greatest found


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

    print("\n\nFinding the smallest value in the list")
    print("The smallest value is:", findSmallest(theArray))

    print("\n\nFinding the greatest value in the list")
    print("The greatest value is:", findGreatest(theArray))
