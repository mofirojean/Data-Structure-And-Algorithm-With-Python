# prints numbers from 1 to n in reverse order
def printRev(n):
    if n > 0:
        print(n)
        printRev(n - 1)


# Prints numbers from 1 to n in ascending order
def printInAscOrder(n):
    if n > 0:
        printRev(n - 1)
        print(n)


# Driver Method
def main():
    print("Function prints numbers in reverse order")
    printRev(4)
    print("Function prints numbers in ascending order")
    printInAscOrder(4)


if __name__ == "__main__":
    main()