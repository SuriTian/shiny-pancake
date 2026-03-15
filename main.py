import math

def validate_size(matrix1, matrix2):
    # idk assuming all matrix 
    return (len(matrix1) == len(matrix2)) and (len(matrix1[0]) == len(matrix2[0]))

def add(matrix1, matrix2):
    # check for the same size!!!
    validate_size(matrix1, matrix2)
    m = len(matrix1)
    n = len(matrix1[0])

    result_matrix = []

    for i in range(m):
        column = [] 
        for j in range(n):
            column.append(matrix1[j] + matrix2[j])
        
        result_matrix.append(column)
    
    return result_matrix
