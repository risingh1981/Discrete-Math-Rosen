# Chapter 2, Computer Project 11: Given an m × k Boolean matrix A and a k × n Boolean
# matrix B, find the Boolean product of A and B.

def main():
    # Input:
    A = [[1,0,1],
         [1,1,0],
         [0,0,1]]
    B = [[0,1,1],[1,0,1],[1,0,1]]
    print(booleanproduct(A,B))
    # Expected Output: [[1,1,1],[1,1,1],[1,0,1]]

def booleanproduct(A,B):
    # A = m x n  B = p x q. To find bool product A and B, we need n(cols of A) to equal p(rows of B)
    if (len(A[0]) != len(B)):
        print(f"Unable to calculate boolean product of A and B as the dimensions are not appropriate.")
        return None
    # Initialize Boolean Product Matrix C to zeros.
    C = [[None for y in range(len(B[0]))] for x in range(len(A))]
    # Calculate dimensions of resultant product matrix C (rowsA x colsB)
    rowsA = len(A)
    colsB = len(B[0])
    sm = len(B) # Shared dimension between A & B(aka colsA or rowsB)
    
    #Loop
    for cr in range(0, rowsA):
        for cc in range(0, colsB):
            for sd in range(0, sm):
                if C[cr][cc] == 1:
                    break
                C[cr][cc] = (A[cr][sd] & B[sd][cc])
                
    return C

if __name__ == "__main__":
    main()