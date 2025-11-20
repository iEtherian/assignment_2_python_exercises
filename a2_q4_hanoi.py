"""
Assignment 2 - Question 4
Solve the Tower of Hanoi puzzle using a recursive approach.
"""

def hanoi(n, source, target, temp):
    """Return a list of moves to solve the Tower of Hanoi for n discs."""

    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    
    if not all(rod in ("A", "B", "C") for rod in (source, target, temp)):
        raise ValueError("Rods must be 'A', 'B', or 'C'.")
    
    # Base case: move on disc directly
    if n == 1:
        return [(source, target)]
    
    # Recursive case: move n-1 discs out of the way, move the largest disc,
    # then move the n-1 discs back on top.
    moves = hanoi(n - 1, source, temp, target)
    moves.append((source, target))
    moves.extend(hanoi(n - 1, temp, target, source))

    return moves

# Solve the Tower of Hanoi for 3 discs
try:
    n = 3
    source_rod = 'A'
    target_rod = 'C'
    temp_rod = 'B'

    steps = hanoi(n, source_rod, target_rod, temp_rod)

    for i, move in enumerate(steps, start=1):
        print(f"{i}: {move[0]} to {move[1]}")

except ValueError as e:
    print(e)