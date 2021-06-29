# Chapter 9, Computer Project 2: Given the matrix representing a relation on a 
# finite set, determine whether the relation is symmetric and/or antisymmetric.
# Definitions: A relation R on set S is:
# 1) Symmetric - for all a,b in S, if R(a, b) , then R(b, a)
# 2) Antisymmetric - for all a,b in S, if R(a, b) with a != b then !R(b, a).
#    equivalently, if R(a, b) and R(b, a), then a = b.
def main():
    # Inputs:
    A = [[1,0,1,1],[0,1,0,1],[1,0,0,0],[1,1,0,1]] # Symmetric:True, AS: False
    B = [[1,0,1,1],[0,1,0,1],[1,0,0,0],[1,0,0,1]] # Symmetric: False, AS: False
    C = [[1,0,1,0],[0,1,0,1],[1,0,0,0],[1,1,0,1]] # Symmetric: False, AS: False
    D = [[1,0,0,0],[0,1,0,1],[1,0,0,0],[1,0,0,1]] # Symmetric: False, AS: True
    # Outputs:
    print(f"Relation A- symmetric:{symmetric(A)}")
    print(f"Relation B- symmetric:{symmetric(B)}")
    print(f"Relation C- symmetric:{symmetric(C)}")
    print(f"Relation D- symmetric:{symmetric(D)}")
    print(f"Relation A- antisymmetric:{antisymmetric(A)}")
    print(f"Relation B- antisymmetric:{antisymmetric(B)}")
    print(f"Relation C- antisymmetric:{antisymmetric(C)}")
    print(f"Relation D- antisymmetric:{antisymmetric(D)}")


def symmetric(relation):
    dim = len(relation)
    for row in range(0, dim):
        for col in range(0, dim):
            if relation[row][col] != relation[col][row]:
                return False
    return True
    

def antisymmetric(relation):
    dim = len(relation)
    for row in range(0, dim):
        for col in range(0, dim):
            if (row != col) and (relation[row][col] ==  1) and (relation[col][row] == 1):
                return False
    return True


if __name__ == "__main__":
    main()