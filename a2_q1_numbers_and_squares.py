"""
Assignment 2 - Question 1
Print the numbers 11 through 20 on one line, and their squares on the next.
"""

# Print numbers 11 to 20
for i in range(11, 21):
    print(f"{i:>4}", end= " ")
print()                         # New line after the first row

# Print the squares of the numbers
for i in range(11, 21):
    print(f"{i*i:>4}", end= " ")