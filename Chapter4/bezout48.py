def main():
    a = int(input("Enter first integer:"))
    b = int(input("Enter second integer:"))
    s,t, gcd, outputA, outputB = bezout(a,b)
    print(f"GCD({outputA},{outputB}) = {gcd}")
    print(f"The Bezout identity is {gcd} = ({s})({outputA}) + ({t})({outputB})")

def bezout(a,b):
    returnA = a
    returnB = b
    if (a<b):
        a,b = b,a
        returnA, returnB = returnB, returnA

    r = 1
    coA2orig = 1
    coB2orig = 0
    coA3 = 0
    coB3 = 1
    while(True):
        q = int(a/b)
        r = a % b
        if (r == 0):
            break
        coA1 = coA2orig
        coB1 = coB2orig
        coA2orig = coA3
        coB2orig = coB3
        coA2 = q * coA3
        coB2 = q * coB3
        coA3 = coA1 - coA2
        coB3 = coB1 - coB2

        a = b
        b = r

        #print(f"A1: {coA1} B1: {coB1}  A2: {coA2}  B2: {coB2}  A3: {coA3}  B3: {coB3}  r: {r}")
    return coA3, coB3, b, returnA, returnB

if __name__ == "__main__":
    main()