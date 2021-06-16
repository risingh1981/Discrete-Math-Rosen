# Chapter 4, Copmuter Project 11: Given a positive integer N, a modulus m, a multiplier a, an
# increment c, and a seed x0, where 0 ≤ a < m, 0 ≤ c < m,
# and 0 ≤ x0 < m, generate the sequence of N pseudorandom
# numbers using the linear congruential generator
# xn+1 = (axn + c) mod m.

def main():
    # Input values for Psuedorandom Generator(N - # of values to generate, m - modulus, a - multiplier, 
    # c - increment, and x0 - seed with 0 ≤ a < m, 0 ≤ c < m, and 0 ≤ x0 < m ):
    N = 50
    m = 11
    a = 4
    c = 5
    x0 = 7

    # Loop to generate and print out values.
    print(f"Seed: {x0}")
    xn = x0
    for i in range(0, N):
        xn = generate(xn, m, a, c)
        print(f"Value {i+1}: {xn}")

# Function to Generate Values
def generate(xn, m, a, c):
    nextX = (a*xn + c) % m
    return nextX

if __name__ == "__main__":
    main()