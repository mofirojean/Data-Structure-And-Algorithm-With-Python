# Compute the nth number in the Fibonacci sequence

def fib(n):
    if n >= 1:
        if n < 3:
            return n - 1
        else:
            return fib(n - 1) + fib(n - 2)
    else:
        return "Fibonacci not defined for n < 1"


# Driver Method
if __name__ == "__main__":
    print(fib(10))
