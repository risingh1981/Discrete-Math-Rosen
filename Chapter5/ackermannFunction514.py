# Chapter 5, Problem 14: Given positive integersmand n, find A(m, n), the value of
# Ackermann’s function at the pair (m, n). 

# Ackermann’s function plays an important role in the theory of recursive 
# functions and in the study of the complexity of certain algorithms involving 
# set unions. 
# Definition of Ackermann's function:
# A(m, n) = 1) 2n if m = 0, 2) 0 if m ≥ 1 and n = 0, 3) 2 if m ≥ 1 and n = 1
# 4) A(m − 1, A(m, n − 1)) if m ≥ 1 and n ≥ 2

def main():
    # Input: Enter value for m and n for which you would like to evaluate
    # Ackermann function A(m,n)
    m = 3
    n = 3
    # Don't try (m,n) = (3,4). You will exceed makimum recursion depth.
    # The answer for A(3,4) is 2^2^2^...^2, 65535 times. Extremely large.

    # Output
    print(ackermann(m,n))

def ackermann(m,n):
    # Def:
    # A(m, n) = 1) 2n if m = 0, 2) 0 if m ≥ 1 and n = 0, 3) 2 if m ≥ 1 and n = 1
    # 4) A(m − 1, A(m, n − 1)) if m ≥ 1 and n ≥ 2
    #input(f"ackermann({m},{n})")
    # Recursive Base Cases:
    if (m == 0):
        return 2 * n
    elif ((m >= 1) and (n == 0)):
        return 0
    elif ((m >= 1) and (n == 1)):
        return 2

    # Recursive Case:
    return ackermann(m - 1, ackermann(m, n - 1))

 

if __name__ == "__main__":
    main()