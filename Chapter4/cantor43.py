# Program will output Cantor Expansion for given integer.
# Cantor expansion is a(n)*n! + a(n-1)*(n-1)! + ... + a(2)*2! + a(1)*1!
# where each 0<=a(i)<=i for i = 1,2,3,...,n
def main():
    # Enter value for which you want to find the Cantor Expansion:
    c = 1000000
    print(f"Cantor Expansion of {c} is: ", cantor(c))

def cantor(x):
    maxfact = maxfactor(x)
    cantorstring = ""
    ai = 0 # Value of coefficient for the ith factorial
    if (x == 0):
        return "0*1!"
    for i in range(maxfact, 0, -1):
        ai = int(x / factorial(i))
        x = x - (ai * factorial(i))
        if (i == maxfact):
            cantorstring = cantorstring + str(ai) + f"*{i}!"
        else:
            cantorstring = cantorstring + " + " + str(ai) + f"*{i}!"
    return cantorstring
        

def maxfactor(x):
    maxfact = 1
    while (x >= factorial(maxfact)):
        maxfact += 1
    return maxfact - 1

def factorial(x):
    if (x == 0):
        return 1
    return x * factorial(x-1)





if __name__ == "__main__":
    main()
