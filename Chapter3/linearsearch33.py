# Chapter 3, Computer Problem 3: Given a list of n distinct integers, determine the position
# of an integer in the list using a linear search.
from random import shuffle

def main():
    # Input range of ints to generate:
    n = 100
    # Input the number you would like  to determine index of
    p = 49
    # Generate List of numbers 1 through n and shuffle.
    ints = list(range(1,n+1))
    shuffle(ints) # Shuffles list ints in place. Sample generates a new shuffled list.
    # Call function linearsearch(<list>,p)
    index = linearsearch(ints,p)
    # Output
    print(f"Per linear search function, the index of {p} in generated list is:{index}")
    print(f"Per Pythons built-in index function, the index of {p} is {ints.index(p)}.")
    


# Function returns index of int p in list ints. If p is not found, it returns None.
def linearsearch(ints,p):
    for i in range(len(ints)):
        if (ints[i] == p):
            return i
    return None

    

if __name__ == "__main__":
    main()