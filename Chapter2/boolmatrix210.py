# Chapter 2, Computer Project 10: Given two m × n Boolean matrices(0/1 Matrices), find their meet(conjunction
# of entries in respective locations) and join(disjunction of entries in respective locations). 

def main():
    # Input 2 Matrices
    # 3x3 matrix
    A = [[1,0,0],
         [1,1,1],
         [0,1,0]]

    # 3x4 matrix
    B = [[0,0,1],
         [1,1,1],
         [1,1,1]]



    # Output:
    print(A)
    print(B)
    # Meet Function Test:
    print(meet(A,B))
    # Join Function Test:
    print(join(A,B))

def meet(A,B):
    dim = len(A)
    result = [[None for i in range(dim)] for j in range(dim)]
        
    for row in range(0,dim):
        for col in range(0,dim):
            result[row][col] = (A[row][col] & B[row][col])
    return result

def join(A,B):
    dim = len(A)
    result = [[None for i in range(dim)] for j in range(dim)]
        
    for row in range(0,dim):
        for col in range(0,dim):
            result[row][col] = (A[row][col] | B[row][col])
    return result


if __name__ == "__main__":
    main()