# Chapter 5, Problem 13: Given a positive integer, find the number of partitions 
# this integer. 

# Recursive Definition of P(m,n). P(m,n) is the number of different
# ways to express m as the sum of positive integers not exceeding n. 
# Of note, P(m) = P(m,m)
# Def:
# P(m,n) = 1)1 if m = 1, 2)1 if n = 1, 3)P(m,m) if m < n, 
# 4)1 + P(m,m−1) if m = n > 1, 5)P(m,n−1) + P(m−n,n) if m > n > 1.

def main():
    # Input: Enter value for m and n. m is the number for which you want to find the
    # number of partitions as the sum of positive ints not exceeding n.
    m = 20
    n = 20

    # Output
    print(partitions(m,n))

def partitions(m,n):
    # Def:
    # P(m,n) = 1)1 if m = 1, 2)1 if n = 1, 3)P(m,m) if m < n, 
    # 4)1 + P(m,m−1) if m = n > 1, 5)P(m,n−1) + P(m−n,n) if m > n > 1.
    # Input checking:
    if (m < 1):
        return None # You can't write zero as the sum of positive ints.
    elif (n < 1):
        return None # You can't parition a positive int into ints equaling 0.
    # Recursive Base Cases:
    if (m == 1) or (n == 1):
        return 1
    # Recursive Cases:
    if (m < n):
        return partitions(m,m)
    elif (m == n): # m = n > 1
        return 1 + partitions(m, m - 1)
    else: # m > n > 1
        return partitions(m, n-1) + partitions(m-n,n)

 

if __name__ == "__main__":
    main()