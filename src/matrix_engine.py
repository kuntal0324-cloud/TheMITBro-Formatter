from sympy import Matrix

# -----------------------------------
# Matrix Engine
# -----------------------------------

def trace(matrix):
    return Matrix(matrix).trace()
    
def determinant(matrix):
    return Matrix(matrix).det()

def rank(matrix):
    return Matrix(matrix).rank()

def norm(matrix):
    return Matrix(matrix).norm()

def matrix_power(matrix, power):
    return Matrix(matrix) ** power

def multiply(A, B):
    return Matrix(A) * Matrix(B)

def add(A, B):
    return Matrix(A) + Matrix(B)

def subtract(A, B):
    return Matrix(A) - Matrix(B)

def transpose(matrix):
    return Matrix(matrix).T

def inverse(matrix):
    return Matrix(matrix).inv()

def rref(matrix):
    return Matrix(matrix).rref()[0]

def nullspace(matrix):
    return Matrix(matrix).nullspace()

def column_space(matrix):
    return Matrix(matrix).columnspace()

def eigenvalues(matrix):
    return Matrix(matrix).eigenvals()

def eigenvectors(matrix):
    return Matrix(matrix).eigenvects()

def characteristic_polynomial(matrix):
    return Matrix(matrix).charpoly().as_expr()
