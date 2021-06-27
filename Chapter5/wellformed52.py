# Chapter 5, Computer Project 2: Generate all well-formed formulae for expressions involving
# the variables x, y, and z and the operators
# {+, ∗, /, −} with n or fewer symbols.

from math import log2
from itertools import combinations_with_replacement
from time import perf_counter_ns

def main():
    wff =["X","Y", "Z"]
    ops = ["+","-","*","/"]
    n = 13
    
    for i in range(1,n):
        start = perf_counter_ns()
        answer = wellFormed2(wff,ops,i)
        end = perf_counter_ns()    
        print(f"Time for n = {i} symbols is: {end - start} ns. WFF Count: {elecount(answer)}")
    
# Function to count elements in final dictionary of WFFs that is generated.
def elecount(answer):
    total = 0
    for key in answer:
        total = total + len(answer[key])
    return total

# Function wffGenerator takes 2 arrays of WFF as input and returns an array of
# those WFF in both arrays combined.
def wffGenerator(A,B,ops):
    newWFFs = set()
    if (A != B):
        for first in A:
            for second in B:
                for op in ops:
                    # In the case of the "-" or "/" operator X - Y is different from Y - X
                    if ((op == "-") or op == "/"):
                        newWFF1 = "(" + first + " " + op + " " + second + ")"
                        newWFF2 = "(" + second + " " + op + " " + first + ")"
                        newWFFs.add(newWFF1)
                        newWFFs.add(newWFF2)
                    else:
                        newWFF1 = "(" + first + " " + op + " " + second + ")"
                        newWFFs.add(newWFF1)
    else:
        for i in range(len(A)):
            first = A[i]
            for j in range(i,len(B)):
                second = A[j]
                for op in ops:
                    # In the case of the "-" or "/" operator X - Y is different from Y - X
                    if ((op == "-") or op == "/"):
                        newWFF1 = "(" + first + " " + op + " " + second + ")"
                        newWFF2 = "(" + second + " " + op + " " + first + ")"
                        newWFFs.add(newWFF1)
                        newWFFs.add(newWFF2)
                    else:
                        newWFF1 = "(" + first + " " + op + " " + second + ")"
                        newWFFs.add(newWFF1)

    # Convert set to List before returning
    return list(newWFFs)

# Will return dictionary that has to be appeneded to get final result to result
def combinor(combos2, result, ops):
    for key in combos2:
        for pair in combos2[key]:
            newWWFs = wffGenerator(result[pair[0]],result[pair[1]],ops)
            if key in result: 
                result[key] = result[key] + newWWFs
            else:
                result[key] = newWWFs
    return result

def wellFormed2(wff, ops, n):
    one = wff.copy()
    result = {1:one}
    oddUpToN = list(range(1,n+1, 2))
    combos = list(combinations_with_replacement(oddUpToN, 2))
    # Find max value for dictionary key based on value of n. If n odd, max value = n
    # if n even, max value = n - 1
    maxVal = n if (n % 2 != 0) else (n-1)
    combos2 = {}
    for tuple in combos:
        sum1 = sum(list(tuple)) + 1
        if (sum1 <= maxVal):
            if (sum1 in combos2):
                combos2[sum1].append(tuple)
            else:
                combos2[sum1] = [tuple]
    result = combinor(combos2, result, ops)
    return result

      
if __name__ == "__main__":
    main()