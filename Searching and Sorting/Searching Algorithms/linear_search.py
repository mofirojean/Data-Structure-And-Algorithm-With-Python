# implementation of the linear search algorithm
def linearSearch(theValues, target):
    n = len(theValues)
    for i in range(n):
        """ If target is in the ith element, return True"""
        if theValues[i] == target:
            return True

    return False  # If not, return False


# Driver Method
if __name__ == "__main__":
    theArray = [10, 51, 2, 18, 4, 31, 13, 5, 23, 64, 29]
    print(" Searching for 31:", linearSearch(theArray, 31))
    print(" Searching for 8:", linearSearch(theArray, 8))
