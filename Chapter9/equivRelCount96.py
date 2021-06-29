# Chapter 9, Computer Project 6: Given a positive integer n, determine the number 
# of equivalence relations on a set with n elements.

# Math Foundation: The number of equivalence relations on a set A is equal to the
# number of partitions of the set.
# Bells Number(Bₙ) = the number of partitions of a Set A with n elements.
# Bₘ=∑(from n = 1 to m) of S(m,n)
# S(m,n) := Sterling Number of the Second Kind, counts number of ways to partition
# a set with m elements into k non-empty subsets
# S(m,n) =(1/n!)∑(from k=0 to n) of (−1)^k*C(n,k)*(n−k)^m
# or defined recursively: S(n, k) = k* S(n-1, k) + S(n-1, k-1)
# I will just use sympy's bell function to calculate bell numbers. In previous 
# programs, I have already created functions for combinations, factorial, and power
# which could be used here but its more convienient to just use the Sympy Library.

from sympy import bell

def main():
    # Input value for number of elements in set:
    n = 8
    # Output
    print(partitions(n))

def partitions(n):
    return bell(n)


if __name__ == "__main__":
    main()
