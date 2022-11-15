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

    # calling the function to get determinant value of given matrix.
    det_coefficient = determinant_of_matrix(mat)

    # printing the determinant value of given matrix.
    print("The determinant of the coefficient matrix is: ", det_coefficient)

    # Exit the program if determinant is zero.
    if det_coefficient == 0:
        print("The coefficient matrix is singular.")
        exit()
    else:
        print("The coefficient matrix is non-singular.")

    # Enter the solution matrix.
    print("Enter the elements of solution matrix: ")
    solution_matrix = []
    for i in range(rows):
        solution_matrix.append(int(input()))

    # print the solution matrix.
    print("The solution matrix is: ", solution_matrix)

    # Use cramer's rule to solve the system of linear equations.
    for i in range(rows):
        # initialize the matrix to get the minor matrix.
        minor_matrix = [[0] * rows for i in range(rows)]

        # get the minor matrix.
        for j in range(rows):
            for k in range(rows):
                if j == i:
                    minor_matrix[k][j] = solution_matrix[k]
                else:
                    minor_matrix[k][j] = mat[k][j]

        # calculate the determinant of minor matrix.
        det_minor_matrix = determinant_of_matrix(minor_matrix)

        # Exit the program if determinant is zero.
        if det_minor_matrix == 0:
            print("The system has infinitely many solutions.")
            exit()

        # calculate the value of x.
        x = det_minor_matrix / det_coefficient

        # print the value of x.
        print("The value of x", i + 1, "is: ", x)
