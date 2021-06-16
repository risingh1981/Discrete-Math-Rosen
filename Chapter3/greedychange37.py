# Chapter 3, Computer Project 7: Given an integer n, use the greedy algorithm to find the
# change for n cents using quarters, dimes, nickels, and pennies.

def main():
    # Input: Enter dollar amount to convert to change as value for n. ie. $1 and 61 cents = 1.61
    n = 10.49
    # Convert dollar and cent amount to just cents.
    cents = n * 100
    # Calculations:
    quarters = cents // 25
    cents = cents - (quarters * 25)
    dimes = cents // 10
    cents = cents - (dimes * 10)
    nickels = cents // 5
    cents = cents - (nickels * 5)

    # Output
    print(f"The change for ${round(n,2)} is {int(quarters)} quarters, {int(dimes)} dimes, {int(nickels)} nickels, and {int(cents)} pennies.")


if __name__ == "__main__":
    main()
