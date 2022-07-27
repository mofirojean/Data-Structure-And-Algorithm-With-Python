# Sorts a sequence in ascending order using the selection sort algorithm
def selectionSort(theSeq):
    n = len(theSeq)
    for i in range(n - 1):
        """Assumes the ith element is the smallest"""
        smallNdx = i
        # Determine if any other element contains the smaller value
        for j in range(i + 1, n):
            if theSeq[j] < theSeq[smallNdx]:
                smallNdx = j

        """Swap the ith value and the smallNdx value only if the smallest 
            value is not already in its proper position. Some implementations
            omit testing the condition and always swap the two values"""
        if smallNdx != i:
            (theSeq[i], theSeq[smallNdx]) = (theSeq[smallNdx], theSeq[i])
    return theSeq


# Driver Method
if __name__ == "__main__":
    data = [-2, 45, 0, 11, -9]
    print("Unsorted list:", data)
    print("Sorted list using selection sort:", selectionSort(data))
