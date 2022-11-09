# determinant of matrix.

# defining a function to get the minor matrix after excluding i-th row and j-th column.


def get_cofactor(m, i, j):
    return [row[: j] + row[j + 1:] for row in (m[: i] + m[i + 1:])]


# defining the function to calculate determinant value of given matrix a.


def determinant_of_matrix(mat):
    # if given matrix is of order 2*2 then simply return det value by cross multiplying elements of matrix.
    if len(mat) == 2:
        value = mat[0][0] * mat[1][1] - mat[1][0] * mat[0][1]
        return value

    # initialize Sum to zero
    Sum = 0

    # loop to traverse each column of matrix a.
    for current_column in range(len(mat)):
        # calculating the sign corresponding to co-factor of that sub matrix.
        sign = (-1) ** current_column

        # calling the function recursively to get determinant value of sub matrix obtained.
        sub_det = determinant_of_matrix(get_cofactor(mat, 0, current_column))

        # adding the calculated determinant value of particular column matrix to total Sum.
        Sum += (sign * mat[0][current_column] * sub_det)

    # returning the final Sum
    return Sum


# Driver code
if __name__ == '__main__':

    # input the number of rows
    rows = int(input("Enter the number of rows and columns: "))

    # initialize matrix
    mat = [[0] * rows for i in range(rows)]

    # input the elements of matrix
    print("Enter the elements of matrix: ")
    for i in range(rows):
        print("Enter the elements of row", i + 1)
        for j in range(rows):
            mat[i][j] = int(input())

    # declaring the matrix.
    # mat = [[1, 0, 0],
    #        [0, 1, 0],
    #        [0, 0, 1]]

    # printing determinant value by function call
    print('Determinant of the matrix is :', determinant_of_matrix(mat))
