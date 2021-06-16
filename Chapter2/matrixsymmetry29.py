# Given a square matrix, determine whether it is symmetric.

def main():
    # Input: Square matrix A
    # Example of Asymmetric Matrix
    A = [[1, 2, 3, 4, 5],
         [2, 6, 7, 8, 9],
         [3, 7,10,11,12],
         [4, 8,11,13,14],
         [5, 9,12,13,15]]
    # Example of Symmetric Matrix
    B = [[1, 2, 3, 4, 5],
         [2, 6, 7, 8, 9],
         [3, 7,10,11,12],
         [4, 8,11,13,14],
         [5, 9,12,14,15]]
    # Output:
    print(issymmetric(A)) # Symmetric: False
    print(issymmetric(B)) # Symmetric: True


def issymmetric(A):
    dim = len(A)
    for row in range(1,dim):
        for col in range(0,row):
            if A[row][col] != A[col][row]:
                return False
    return True


if __name__ == "__main__":
    main()