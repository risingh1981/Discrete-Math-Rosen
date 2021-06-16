# Chapter 1 Computer Project 1: Given the truth values of the propositions 
# p and q, find the truth values of the conjunction, disjunction, 
# exclusive or, conditional statement, and biconditional of these propositions.
import distutils.core

def main():
    # Get user input.
    p , q = getinput()
    
    # Output conjunction of p and q: (p ^ q)
    print(f"Truth value of conjunction of p and q ({p} ^ {q}) is: {p and q}.")
    # Output disjunction of p and q: (p || q)
    print(f"Truth value of disunction of p and q ({p} || {q}) is: {p or q}.")
    # Output exclusive or of p and q: (p ⊕ q)
    print(f"Truth value of exclusive or of p and q ({p} ⊕  {q}) is: {p != q}.")
    # Output value of conditional p implies q: (p -> q)
    print(f"Truth value of conditional  p -> q ({p} -> {q}) is: {not(p) or q}.")
    # Output value of biconditional p iff q: (p <-> q)
    print(f"Truth value of biconditional p iff q ({p} <-> {q}) is: {not(p!=q)}.")

# Gets input for p and q. Returns bool values for p and q.
def getinput():
    # Get input
    while(True):
        p = input("Enter truth value for proposition p (T for True or F for False): ").upper()
        if (p in {"T","F"}):
            break
        else:
            print("Format of input for p in correct. Please re-try.")
    while(True):
        q = input("Enter truth value for proposition q (T for True or F for False): ").upper()
        if (q in {"T","F"}):
            break
        else:
            print("Format of input for q in correct. Please re-try.")
    return bool(distutils.util.strtobool(p)), bool(distutils.util.strtobool(q))

if __name__ == "__main__":
    main()