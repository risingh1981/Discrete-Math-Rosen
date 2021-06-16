# Given a function f from {1, 2, . . . , n} to itself, determine
# whether f is onto.
import ast
from math import *
from onetoone24 import onetoone

def main():
    # Input value of n for domain of function f(x) from 1 to n to the integers.
    n = 100
    # Input function in terms of x in between quotes using proper Python syntax. No need to type math.*
    function = "1/(1 - x)"

    # Determine if function is Onto(Surjective). Method onto() returns true/false.
    truthvalue = onto(function,n)
    print(f"Onto: {truthvalue}.")

# Since the function is from {1,2,...,n} to itself. If it it not one-to-one, then it is not onto. Importing
# onetoone function from 2.4OneToOne.py.
def onto(function,n):
    truthval, reason = onetoone(function,n)
    return truthval


if __name__ == "__main__":
    main()