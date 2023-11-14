#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared_matrix = []

    for row in matrix:
        squared_row = []

        for element in row:
            squared_row.append(element ** 2)

        squared_matrix.append(squared_row)

    return squared_matrix

if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    new_matrix = square_matrix_simple(matrix)
    print(new_matrix)
    print(matrix)
