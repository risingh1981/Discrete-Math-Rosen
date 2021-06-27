# Chapter 6, Program 1: Given a positive integer n and a nonnegative integer not
# exceeding n, find the number of r-permutations and r-combinations
# of a set with n elements.
# Formulas for r-permutations(P(n,r)) and r-combinations(C(n,r)):
# P(n,r) = n!/(n-r)!
# C(n,r) = n!/(r!*(n-r)!)

def main():
    # Input: Enter values for n and r
    n = 10
    r = 10

    # Output:
    print(f"P({n},{r}) = {permutations(n,r)}")
    print(f"C({n},{r}) = {combinations(n,r)}")

def permutations(n,r):
    return int(factorial(n)/factorial(n-r))

def combinations(n,r):
    return int(factorial(n)/(factorial(r)*factorial(n-r)))

def factorial(n):
    if ((n == 0) or (n == 1)):
        return 1
    fact = 1
    for i in range(2,n + 1):
        fact = fact * i
    return fact
    


if __name__ == "__main__":
    main()