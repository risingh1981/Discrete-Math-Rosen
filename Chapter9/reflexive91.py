# Chapter 9, Computer Project 1: Given the matrix representing a relation on a 
# finite set, determine whether the relation is reflexive and/or irreflexive.

def main():
    # Input:
    A = [[1,0,0],[0,1,0],[0,0,1]] # Reflexive
    B = [[0,1,0],[0,1,0],[0,0,1]] # Neither
    C = [[0,1,1],[1,0,1],[1,1,0]] # Irreflexive

    # Output
    print("Reflexive or Irreflexive or Neither")
    print(f"Relation A:{A} is {reflexiveOrIrreflexive(A)}")
    print(f"Relation B:{B} is {reflexiveOrIrreflexive(B)}")
    print(f"Relation C:{C} is {reflexiveOrIrreflexive(C)}")

# Function returns "Reflexive" if matrix representing relation is Reflexive. "Irreflexive"
# if irreflexive, or "Neither" is not reflexive and not irrefelexive.
def reflexiveOrIrreflexive(arr):
    dim = len(arr)
    count = 0
    for i in range(0,dim):
        if (arr[i][i] == 1):
            count += 1
    if (count == dim):
        return "Reflexive"
    elif (count == 0):
        return "Irreflexive"
    else:
        return "Neither"

def reflexive(arr):
    dim = len(arr)
    for i in range(0,dim):
        if (arr[i][i] != 1):
            return False
    return True


if __name__ == "__main__":
    main()