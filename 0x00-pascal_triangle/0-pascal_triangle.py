#!/usr/bin/python3
''' Pascal's Triangle '''


def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        row = [1]  # Every row starts with 1
        if i > 0:  # For rows beyond the first
            last_row = triangle[-1]  # Get the last row
            for j in range(1, i):
                row.append(last_row[j-1] + last_row[j])  # Compute the values
            row.append(1)  # Every row ends with 1

        triangle.append(row)

    return triangle
