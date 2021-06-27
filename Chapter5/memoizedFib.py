# Will create a program to determine the nth fibonacci number using memoization - similar to
# recursion, except it uses a lookup table before computing solutions.
# Will also do timing comparisons between the three fib functions: recursive, iterative and memoized.
from iterativeFibonacci511 import iterativeFibonacci
from recursiveFibonacci512 import recursiveFibonacci
from time import perf_counter_ns




def main():

    # Timing Tests
    lookup = [None] * 21
    
    for n in range(0,21):
        start = perf_counter_ns()
        valDP = fibDP(n)
        end = perf_counter_ns()
        timeDP = end - start

        start = perf_counter_ns()
        valIF = iterativeFibonacci(n)
        end = perf_counter_ns()
        timeIF = end - start
    
        start = perf_counter_ns()
        valRF = recursiveFibonacci(n)
        end = perf_counter_ns()
        timeRF = end - start
    
        print(f"n = {n}  Dynamic Fib: {timeDP} ns.  Iterative Fib: {timeIF} ns  Recursive Fib: {timeRF}")


def fibDP(n, lookup = None, is_first = True):
    if is_first:
        lookup = [None] * (n+1)
    # Basecase:
    if ((n == 0) or (n == 1)):
        lookup[n] = n

    # Recursive Case:
    if (lookup[n] == None):
        lookup[n] = fibDP(n-1, lookup, is_first = False) + fibDP(n-2, lookup, is_first = False)

    return lookup[n]

if __name__ == "__main__":
    main()
