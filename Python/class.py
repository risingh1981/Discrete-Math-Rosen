class Complex:
    def __init__(self):
        self.r = 10
        self.i = 60
    def changeR(self, newval):
        self.r = newval

def main():
    x = Complex()
    y = Complex()
    print(x)
    print("X vals:",x.r, x.i)
    print("Y vals:", y.r, y.i)
    x.changeR(100)
    print("New X vals:",x.r, x.i)
    print("New Y vals:",y.r, y.i)


main()
