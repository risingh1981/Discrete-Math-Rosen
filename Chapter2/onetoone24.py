# Chapter 2, Computer Project 4: Given a function f from {1, 2, . . . , n} to the set of integers,
# determine whether f is one-to-one.
import ast
from math import *

def main():
    # Input value of n for domain of function f(x) from 1 to n to the integers.
    n = 100
    # Input function in terms of x in between quotes using proper Python syntax. No need to type math.*
    function = "1/(1 - x)"

    # Determine if One-To-One(Injective). Method onetoone() returns a string stating if function is one-to-one
    # or if not, the reason for not being so.
    truthvalue, reason = onetoone(function,n)
    print(f"One-to-One: {truthvalue}. {reason}")
    
def onetoone(function, n):
    values = {}
    a= ""
    code = ast.parse(function, mode='eval')
    for x in range(1, n+1):
        try: 
            y = eval(compile(code, '', mode='eval'))
            if (y != int(y)):
                return False, f"The function f(x) = {function} does not map to the integers. Its value for f({x}) is {y}."
                break
            elif (y not in values):
                values[y] = x
            elif (y in values):
                return False, f"f(x) = {function} is not one-to-one. f({values[y]}) = f({x}) = {y}."
        except Exception as e:
            a = str(e)
            if (a == "division by zero"):
                return False, f"f(x) = {function} is not a function as it is not defined for all values in domain. Leading to {a} error for f({x})."
            else:
                return None, f"The function f(x) = {function} is leading to some error. Cannot determine if it is one-to-one."
    return True, f"Function f(x) = {function} is one-to-one."

    


if __name__ == "__main__":
    main()