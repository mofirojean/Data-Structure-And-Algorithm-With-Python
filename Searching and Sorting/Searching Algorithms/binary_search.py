# Implementation of the binary search algorithm
def binarySearch(theValues, target):
    """Start with the entire sequence of elements"""
    low = 0
    high = len(theValues) - 1

    # Repeatedly subdivide the sequence until the target is found
    while low <= high:
        """Find the midpoint in the sequence"""
        mid = (high + low) // 2
        # Does the midpoint contain the target
        if theValues[mid] == target:
            return True
        # or does the target precedes the midpoint
        elif target < theValues[mid]:
            high = mid - 1
        # or does it follow the midpoint ?
        else:
            low = mid + 1

    # If the sequence can not be subdivided further, we're done
    return False


# Driver Method
if __name__ == "__main__":
    theArray = [2, 4, 5, 10, 13, 18, 23, 29, 31, 51, 64]
    print("Binary search for 5:", binarySearch(theArray, 5))
    print("Binary search for 30:", binarySearch(theArray, 30))
