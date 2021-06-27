# Chapter 5, Problem 12: Given a nonnegative integer n, find the nth Fibonacci
# number using recursion. Will also do a version of the fib function with dynamic programming.
from time import perf_counter_ns
from iterativeFibonacci511 import iterativeFibonacci

def main():
    # Input: Enter value for n. Program will print out fibonacci numbers upto 
    # the nth fibonacci number.
    n = 20

    for i in range(0,21):
        print(f"F({i}): {recursiveFibonacci(i)}")


    
# Functions returns nth Fibonacci number
def recursiveFibonacci(n):
    # Recursive Base Case
    fnMinusTwo = 0
    fnMinusOne = 1
    # If n = 0, returns fnMinusTwo = 0 or if n = 1, returns fnMinusOne = 1
    if (n == 0):
        return fnMinusTwo
    elif (n == 1):
        return fnMinusOne
    # Recursive calls
    return recursiveFibonacci(n - 1) + recursiveFibonacci(n - 2)

if __name__ == "__main__":
    main()