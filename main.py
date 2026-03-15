import math
from rational import *

def validate_same_size(matrix1, matrix2):
    # idk assuming all matrix 
    return (len(matrix1) == len(matrix2)) and (len(matrix1[0]) == len(matrix2[0]))

#add function 
def add(matrix1, matrix2):
    # check for the same size!!!
    if (not validate_same_size(matrix1, matrix2)):
        print("You can't add matrices of different sizes!!!")
        return []

    m = len(matrix1)
    n = len(matrix1[0])

    result_matrix = []

    for i in range(m):
        column = [] 
        for j in range(n):
            column.append(matrix1[i][j] + matrix2[i][j])
        
        result_matrix.append(column)
    
    return result_matrix

# multiply
def multiply(matrix1, matrix2):
    if (not len(matrix1[0]) == len(matrix2)):
        print("not a valid matrix")
    
    result_matrix = []

    m = len(matrix1)
    n = len(matrix2[0])
    shared_term = len(matrix1[0])

    for i in range(m):
        column = []
        for j in range(n):
            sum = 0
            for k in range(shared_term):
                sum += matrix1[i][k]*matrix2[k][j]
            column.append(sum)
        result_matrix.append(column)
    
    return result_matrix



# Display a matrix
def display(mat):
    try:
        mat[0][0]
        len(mat)
    except:
        print("bro thats not a matrix prob cuz error somewhere else")

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