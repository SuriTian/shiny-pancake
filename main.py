import math

# Display a matrix
def display(mat):
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            print(f"{mat[i][j]} ", end = "")
        print()

sample = [[1, 2, 3]]

# Finding the RREF of an m by n matrix
def rref(mat):
    m = len(mat)
    n = len(mat[0])
    for i in range(2):
        lst = []
        for j in range(2):
            lst.append(i+j)
        sample.append(lst)