"""
Assignment 2 - Question 2
Compute the greatest common divisor (GCD) of two integers using the Euclidean
algorithm.
"""

def gcd(n, m):
    """Return the greatest common divisor of n and m."""
    if not (isinstance(n, int) and isinstance(m, int)):
        raise TypeError("Both inputs must be integers")
    
    n, m = abs(n), abs(m)

    if m == 0:
        return n
    return gcd(m, n % m)

# Get and validate first number
while True:
    n1 = input("Enter the first integer: ")
    try:
        num1 = int(n1)
        break
    except ValueError:
        print("Please enter a valid integer")

# Get and validate second number
while True:
    n2 = input("Enter the second integer: ")
    try:
        num2 = int(n2)
        break
    except ValueError:
        print("Please enter a valid integer")

result = gcd(num1, num2)
print(f"The greatest common divisor of {num1} and {num2} is {result}")