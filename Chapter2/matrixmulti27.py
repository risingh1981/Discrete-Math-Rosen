# Chapter 2, Computer Project 7: Given an m × k matrix A and a k × n matrix B, find AB.
# Directly applying the mathematical definition of matrix multiplication gives an 
# algorithm that takes time on the order of n^3 field operations to multiply two 
# n × n matrices over that field.(O(n^3) time)
# Strassen’s algorithm runs in O(n^2.81) time. But For small matrices, the cost of the additional 
# additions of matrix blocks outweighs the savings in the number of multiplications.

def main():
    # Input: 2 Matrices A & B. A is m x k and B is k x n.
    # Test input:
    # 3x3 matrix
    A = [[12,7,3],
        [4 ,5,6],
        [7 ,8,9]]

    # 3x4 matrix
    B = [[5,8,1,2],
        [6,7,3,0],
        [4,5,9,1]]
    
    # Output: Product of A*B
    AB = matrixproduct(A, B)
    print(AB)

def matrixproduct(A,B):
    # A = m x n  B = p x q. To multiply A*B, we need n(cols of A) to equal p(rows of B)
    if (len(A[0]) != len(B)):
        print(f"Unable to multiply matrix A*B as the dimensions are not appropriate.")
        return None
    # Initialize Product Matrix C to zeros.
    C = [[0 for y in range(len(B[0]))] for x in range(len(A))]
    # Calculate dimensions of resultant product matrix C (rowsA x colsB)
    rowsA = len(A)
    colsB = len(B[0])
    sm = len(B) # Shared dimension between A & B(aka colsA or rowsB)
    
    #Loop
    for cr in range(0, rowsA):
        for cc in range(0, colsB):
            for sd in range(0, sm):
                C[cr][cc] = C[cr][cc] + (A[cr][sd]*B[sd][cc])
                
    return C



if __name__ == "__main__":
    main()