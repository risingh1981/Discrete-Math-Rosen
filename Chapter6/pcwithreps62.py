# Chapter 6, Program 2: Given positive integers n and r, find the number of
# r-permutations when repetition is allowed and r-combinations
# when repetition is allowed of a set with n elements.
# P(n,r) w/ repetitions = n^r
# C(n,r)w/ repetitions  = C(n+r-1,r)
from permscombs61 import combinations

def main():
    # Input: Enter values for n and r
    n = 10
    r = 3

    # Output:
    print(f"P({n},{r}) w/ repetitions = {permreps(n,r)}")
    print(f"C({n},{r}) w/ repetitions= {combreps(n,r)}")

def permreps(n,r):
    return pow(n,r)

def combreps(n,r):
    return combinations(n+r-1,r)


if __name__ == "__main__":
    main()