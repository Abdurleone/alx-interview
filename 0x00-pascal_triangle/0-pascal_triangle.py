#!/usr/bin/python3
"""Writing a function for Pascal's Triangle"""

def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to the nth row.

    Parameters:
    n (int): Number of rows of Pascal's Triangle to generate.

    Returns:
    List[List[int]]: A list of lists of integers representing Pascal's Triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) != n:
        previous = triangle[-1]
        current = [1]
        for i in range(len(previous) - 1):
            current.append(previous[i] + previous[i + 1])
        current.append(1)
        triangle.append(current)
    

    return triangle
