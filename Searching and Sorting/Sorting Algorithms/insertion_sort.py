# Sorts a sequence in ascending order using insertion sort algorithm
def insertionSort(theSeq):
    n = len(theSeq)
    # Starts with the first item as the only sorted entry
    for i in range(1, n):
        """Save the value to be positioned"""
        value = theSeq[i]
        # Find the position where the value fits in the ordered part of the list.
        pos = i
        while pos > 0 and value < theSeq[pos - 1]:
            """Shift the items to the right during the search"""
            theSeq[pos] = theSeq[pos - 1]
            pos -= 1

        # Puts the saved value into the open slot
        theSeq[pos] = value

    return theSeq


# Driver method
if __name__ == "__main__":
    data = [-2, 45, 0, 11, -9]
    print("Unsorted list:", data)
    print("Sorted list using insertion sort:", insertionSort(data))

