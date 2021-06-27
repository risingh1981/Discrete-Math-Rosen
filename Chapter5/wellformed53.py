# Chapter 5, Computer Project 3: Generate all well-formed formulae for 
# propositions with n or fewer symbols where each symbol is T, F, one of
# the propositional variables p and q, or an operator from {¬,∨,∧,→,↔}.


from math import log2
from itertools import combinations_with_replacement
from time import perf_counter_ns


def main():
    # T, F, one of
    # the propositional variables p and q, or an operator from {¬,∨,∧,→,↔}.
    wff =["T","F", "P", "Q"]
    ops = ["∨","∧","→","↔"]
    # "¬" will not be handled with the other operations(ops). It will be handled by a "notadder" function.
    n = 3

    start = perf_counter_ns()
    answer = wellFormed2(wff,ops,n)
    end = perf_counter_ns()    
    count = elecount(answer)
    print(f"Time for n = {n} symbols is: {end - start} ns. WFF Count: {count}")
    
    
    
# Function to count elements in final dictionary of WFFs that is generated.
def elecount(answer):
    total = 0
    for key in answer:
        total = total + len(answer[key])
    return total


# Function to add "¬" infront of WFF to create a WFF with length 1 greater.
def notAdder(A):
    newWFFs = set()
    for wff in A:
            if (wff[0] == "¬"):
                newWFF1 = "¬(" + wff + ")"
            else: 
                newWFF1 = "¬" + wff
            newWFFs.add(newWFF1)
    return list(newWFFs)

# Function wffGenerator takes 2 arrays of WFF as input and returns an array of
# those WFF in both arrays combined.
def wffGenerator(A,B,ops):
    newWFFs = set()
    if (A != B):
        for first in A:
            for second in B:
                for op in ops:
                    # In the case of the "→" operator  P → Q is different from Q → P
                    if (op == "→"):
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
                second = B[j]
                for op in ops:
                    # In the case of the "→" operator  P → Q is different from Q → P
                    if (op == "→"):
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
            
            if (pair == (-1,-1)):
                newWWFs = notAdder(result[key-1])
            else:
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
    # Find max odd value for dictionary key based on value of n. If n odd, max value = n
    # if n even, max value = n - 1
    maxOddVal = n if (n % 2 != 0) else (n-1)
    combos2 = {}
    for tuple in combos:
        sum1 = sum(list(tuple)) + 1
        if (sum1 <= n + 1):
            combos2[(sum1 - 1)] = [(-1,-1)] # Even key in combos2 contain a tuple with touple of (-1,-1) without any other tuples.
        if (sum1 <= maxOddVal):
            if (sum1 in combos2):
                combos2[sum1].append(tuple)
            else:
                combos2[sum1] = [tuple]
            combos2[sum1].append((-1,-1)) # To indicate, not operation needs to be done for this level too.
   
    result = combinor(combos2, result, ops)
    return result

      
if __name__ == "__main__":
    main()