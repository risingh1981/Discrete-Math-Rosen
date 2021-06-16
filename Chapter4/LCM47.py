def main():
    a = int(input("Enter first number to find LCM of: "))
    b = int(input("Enter second number:"))
    lcm(a,b)

def lcm(a,b):
    if (a>b):
        start = a
    else:
        start = b
    for i in range(start, a*b + 1):
        if (i % a == 0) and (i % b == 0):
            print(f"The LCM of {a} and {b} is: {i}")
            break
if __name__ == "__main__":
    main()