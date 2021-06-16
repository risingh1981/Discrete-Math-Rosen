def main():
    print(gcd(325,26))
    #1,234,567 and 7,654,321.




def gcd(a,b):
    print(f"a: {a} b: {b}")
    if (a<b):
        a,b = b,a
    if (a % b == 0):
        return b

    return gcd(b, a % b)


if __name__ == "__main__":
    main()