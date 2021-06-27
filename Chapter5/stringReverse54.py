# chapter 5, Problem 4: Given a string, find its reversal.

def main():
    # Input
    test = "Apple"
    

    # Output
    print(reverse(test))


def reverse(toReverse):
    reversal =""
    for char in toReverse:
        reversal = char + reversal
    return reversal

if __name__ == "__main__":
    main()