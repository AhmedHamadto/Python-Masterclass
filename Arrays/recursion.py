# This is a program to explain recursion.

# A recursive function is a function that calls itself.


# This is a recursive function to find the factorial of an integer:
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)