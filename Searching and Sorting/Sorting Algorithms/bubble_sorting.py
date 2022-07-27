# Sorts a sequence in ascending order using the bubble sort algorithm
def bubbleSort(theSeq):
    n = len(theSeq)
    # Perform n-1 bubble operation on the sequence
    for i in range(n):
        """Bubble the largest item to the end"""
        for j in range(0, n - i - 1):
            if theSeq[j] > theSeq[j + 1]:   # swap the j and j+1
                tmp = theSeq[j]
                theSeq[j + 1] = tmp
    return theSeq


# Driver method
if __name__ == "__main__":
    data = [-2, 45, 0, 11, -9]
    print("Unsorted array:", data)
    print("Sorted array:", bubbleSort(data))
