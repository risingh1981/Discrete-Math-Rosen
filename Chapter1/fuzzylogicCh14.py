# Chapter 1, Computer Project 4: Given the truth values of the propositions p and q in
# fuzzy logic, find the truth value of the disjunction and
# the conjunction of p and q.

# Fuzzy logic is used in artificial intelligence. In fuzzy logic, a
# proposition has a truth value that is a number between 0 and 1,
# inclusive.Aproposition with a truth value of 0 is false and one
# with a truth value of 1 is true. Truth values that are between 0
# and 1 indicate varying degrees of truth. For instance, the truth
# value 0.8 can be assigned to the statement “Fred is happy,”
# because Fred is happy most of the time, and the truth value
# 0.4 can be assigned to the statement “John is happy,” because
# John is happy slightly less than half the time.
# The truth value of the conjunction of two propositions in
# fuzzy logic is the minimum of the truth values of the two
# propositions. The truth value of the disjunction of two propositions in
# fuzzy logic is the maximum of the truth values of the two
# propositions.

def main():
    # Input Truth Values
    p = 0.8
    q = 0.5

    # Output for Truth Values of Conjunction/Disjunction of p and q.
    print(f"Truth value of p || q: {disjunctionValue(p,q)}")
    print(f"Truth value of p & q: {conjunctionValue(p,q)}")

def disjunctionValue(a,b):
    return(max(a,b))

def conjunctionValue(a,b):
    return(min(a,b))

if __name__ == "__main__":
    main()