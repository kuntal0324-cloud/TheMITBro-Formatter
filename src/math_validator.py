from sympy import Matrix

def trace(matrix):

    return Matrix(matrix).trace()
if __name__ == "__main__":

    A = [
        [2, -1],
        [3, 4]
    ]

    print(trace(A))
