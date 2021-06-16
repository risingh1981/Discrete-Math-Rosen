# Chapter 2, Computer Project 2: Given multisets A and B from the same universal set, find
# A ∪ B, A ∩ B, A − B, and A + B 
# The notation {m1 · a1, m2 · a2, . . . , mr · ar }
# denotes the multiset with element a1 occurring m1 times, element
# a2 occurring m2 times, and so on.
# The union of the multisets P and Q is the multiset where the multiplicity of an element is
# the maximum of its multiplicities in P and Q. 
# The intersection of P and Q is the multiset where the multiplicity of an
# element is the minimum of its multiplicities in P and Q. 
# The difference of P and Q is the multiset where the multiplicity
# of an element is the multiplicity of the element in P less its
# multiplicity in Q unless this difference is negative, in which
# case the multiplicity is 0. 
# The sum of P and Q is the multiset where the multiplicity of an element is the sum of multiplicities
# in P and Q. The union, intersection, and difference of
# P and Q are denoted by P ∪ Q, P ∩ Q, and P − Q, respectively
# (where these operations should not be confused with
# the analogous operations for sets). The sum of P and Q is
# denoted by P + Q.

def main():
    # Input 2 Multisets from Universal Set with elements numbered 1 through n: U = {1,2,3,...,n}
    # Format: Into Dictionaries with the keys as element number and value for each key as its multiplicity.
    #
    P = {6:3, 2:3, 5:3, 7:2}
    Q = {1:2, 2:3, 5:4, 7:1}


    # Output:
    print(f"MultiSet P:{P}  Q:{Q}")
    # P ∪ Q
    print("P ∪ Q: ", union(P,Q))
    # P ∩ Q
    print("P ∩ Q: ", intersection(P,Q))
    # P − Q
    print("P − Q: ", difference(P,Q))
    # P + Q
    print("P + Q: ", sum(P,Q))

# Union of Multisets P and Q
def union(P,Q):
    R = {}
    for key in (set(P) & set(Q)):
        R[key] = max(P[key],Q[key])
    for key in (set(P) ^ set(Q)):
        if key in P:
            R[key] = P[key]
        else:
            R[key] = Q[key]
    return R

# Intersection of Multisets P and Q
def intersection(P,Q):
    R = {}
    for key in (set(P) & set(Q)):
        R[key] = min(P[key],Q[key])
    return R

# Difference of Multisets P and Q
def difference(P,Q):
    R = {}
    for key in P:
        if (key not in Q):
            R[key] = P[key]
        elif ((key in Q) and (P[key] - Q[key] > 0)):
            R[key] = P[key] - Q[key]
    return R

# Sum of Multisets P and Q
def sum(P,Q):
    R = {}
    for key in (set(P) & set(Q)):
        R[key] = P[key] + Q[key]
    for key in (set(P) ^ set(Q)):
        if key in P:
            R[key] = P[key]
        else:
            R[key] = Q[key]
    return R
    

if __name__ == "__main__":
    main()