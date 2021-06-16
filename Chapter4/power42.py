def main():
    # Given the positive integers a, b, and m with m > 1, find a^b mod m.
    # Enter values of a, b, and m.
    a = 6
    b = 5
    m = 7

    ans = (a ** b) % m

    print(f"{a}^{b} mod {m} = ", ans)

if __name__ == "__main__":
    main()