# Implement n! using recursion

def fact(n):
    if n >= 0:
        if n < 2:
            return 1
        else:
            return n * fact(n - 1)
    else:
        return "Factorial not defined for negative values"


# Driver method
def main():
    n = 10
    print(f"{n}! = {fact(n)}")


if __name__ == "__main__":
    main()
