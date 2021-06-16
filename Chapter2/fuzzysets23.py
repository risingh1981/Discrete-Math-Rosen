# Chapter 2, Computer Project 3: 
# Given fuzzy sets A and B, find A, A ∪ B, and A ∩ B.
# Fuzzy sets are used in artificial intelligence. Each element
# in the universal set U has a degree of membership, which
# is a real number between 0 and 1 (including 0 and 1), in a
# fuzzy set S. The fuzzy set S is denoted by listing the elements
# with their degrees of membership (elements with 0 degree of
# membership are not listed). For instance, we write {0.6 Alice,
# 0.9 Brian, 0.4 Fred, 0.1 Oscar, 0.5 Rita} for the set F (of famous
# people) to indicate that Alice has a 0.6 degree of membership
# in F, Brian has a 0.9 degree of membership in F, Fred
# has a 0.4 degree of membership in F, Oscar has a 0.1 degree
# of membership in F, and Rita has a 0.5 degree of membership
# in F (so that Brian is the most famous and Oscar is the least
# famous of these people). 
# The complement of a fuzzy set S is the set ~S, with the
# degree of the membership of an element in ~S equal to
# 1 minus the degree of membership of this element in S.
# The union of two fuzzy sets S and T is the fuzzy set
# S ∪ T , where the degree of membership of an element in
# S ∪ T is the maximum of the degrees of membership of
# this element in S and in T.
# The intersection of two fuzzy sets S and T is the fuzzy
# set S ∩ T , where the degree of membership of an element
# in S ∩ T is the minimum of the degrees of membership
# of this element in S and in T .

def main():
    # Input 2 Fuzzy Sets.
    # Format: Enter into Dictionaries with the keys as element of set and respective value
    # of degree of memberships(d) where 0 < d <=1.
    P = {"Alice":0.4 , "Brian":0.8 , "Fred": 0.2, "Oscar": 0.9, "Rita":0.7, "Abby":1.0}
    Q = {"Alice":0.6 , "Brian":0.9 , "Fred": 0.4, "Oscar": 0.1 , "Rita": 0.5, "Frank":0.5}
    # Universal Fuzzy Set:
    U = {"Alice":1.0 , "Brian":1.0 , "Fred":1.0, "Oscar":1.0 , "Rita":1.0, "Frank":1.0, "Abby":1.0}
    


    # Output:
    print(f"Fuzzy Set P:{P}")
    print(f"Fuzzy Set Q:{Q}")
    # Complement of P (~P) relative to Universal Set U
    print("Complement of P: ", complement(P,U))
    # P ∪ Q
    print("P ∪ Q: ", union(P,Q))
    # P ∩ Q
    print("P ∩ Q: ", intersection(P,Q))
    
# Complement of Fuzzy Set P
def complement(P, U):
    R = {}
    for key in U:
        if (key in P) and (P[key] != 1):
            R[key] = round(1 - P[key],1)
        elif (key not in P):
            R[key] = U[key]
    return R



# Union of Fuzzy Sets P and Q
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

# Intersection of Fuzzy Sets P and Q
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