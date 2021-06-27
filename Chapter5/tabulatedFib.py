# Tabulation (Bottom Up): The tabulated program for a given problem builds a table in bottom up fashion and 
# returns the last entry from table. For example, for the same Fibonacci number, we first calculate fib(0) 
# then fib(1) then fib(2) then fib(3) and so on. So literally, we are building the solutions of subproblems 
# bottom-up. The other way is Memoization which it Top Down and uses look-up table
def main():
    # Test
    print(fibDPTabulated(20))

    

def fibDPTabulated(n):
    # Array Declaration:
    fib = [0] * (n+1)
    # Base case:
    fib[1] = 1
    # Calculating the fib numbers and storing values:
    for i in range(2,n+1):
        fib[i] = fib[i-1] + fib[i-2]
    # Return final value 
    return fib[n]

    

if __name__ == "__main__":
    main()
