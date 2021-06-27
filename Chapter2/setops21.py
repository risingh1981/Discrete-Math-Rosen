# Chapter 2, Computer Project 1: Given subsets A and B of a set with n elements, use bit
# strings to find A, A ∪ B, A ∩ B, A − B, and A ⊕ B.


def main():
    # Input
    # For a set with n elements, numbered 1 through n.
    # Input subsets A and B as a bit string a(n)..a(2)a(1) where 
    # a(i) = 1 if the ith element is in subset and a(i) = 0
    # if ith element is not in subset.

    A = "00110"
    B = "01101"
    
    # Output:
    # A ∪ B
    print("Union(A ∪ B):",union(A,B))
    # A ∩ B
    print("Intersection(A ∩ B):",intersection(A,B))
    # A − B
    print("Set Difference(A − B):",setdifference(A,B))
    # A ⊕ B
    print("Symmetric Difference(A ⊕  B):", symmetricdifference(A,B))
    

    
# Set Union
def union(A,B):
    return padding(bin(int(A,2) | int(B,2)), len(A))
# Set Intersection
def intersection(A,B):
    return padding(bin(int(A,2) & int(B,2)), len(A))
# Set Difference
def setdifference(A,B):
    aList = list(A)
    for i in range(0,len(A)):
        if (A[i] == "1"):
            digit = str(int(A[i]) - int(B[i]))
            aList[i] = digit
    A = "".join(aList)
    return A
# Set Symmetric Difference
def symmetricdifference(A,B):
    return padding(bin((int(A,2) ^ int(B,2))),len(A))
# Pads final bit string with leading 0s, if necessary.
def padding(bitstring, chars):
    bitstring = bitstring[2:]
    if (chars > len(bitstring)):
        bitstring = "0" * (chars - len(bitstring)) + bitstring
    return bitstring


if __name__ == "__main__":
    main()