import math
from rational import *

# Display a matrix
def display(mat):
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            print(f"{mat[i][j]} ", end = "")
        print()

# Finding the RREF of an m by n matrix
def rref(mat):
    m = len(mat)
    n = 0
    if m > 0:
        n = len(mat[0])