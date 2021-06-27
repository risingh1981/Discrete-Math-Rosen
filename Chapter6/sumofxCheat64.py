from itertools import combinations_with_replacement
# Chapter 6, Program 4: Given an equation x1 + x2 +· · ·+xn = C, where C is a
# constant, and x1, x2, . . . , xn are nonnegative integers, list
# all the solutions.
# This solutions uses too many features of python and its time complexity is exponential. Will 
# redo with dymnamic programming.



def main():
    # Input n
    n = 20

    generate(n)
    

    



def generate(n):
    nArr = [x for x in range(1,n)]
    print(nArr)
    validcombs = []
    validcombs.append([n])
    #print(validcombs)
    combinationsChecked = 0
    for i in range(2,n):
        #print(f"i = {i}")
        combsArr = combs(nArr,i)
        #print(combsArr)
        for combtuple in combsArr:
            combinationsChecked += 1
            tot = sum(combtuple)
            if (tot == n):
                validcombs.append(sorted(list(combtuple)))
    validcombs.append([1 for i in range(0,n)])
    print(validcombs)
    print("Combinations Checked:",combinationsChecked)
    


def combs(nArr,y):
    combsx = combinations_with_replacement(nArr,y)
    #print(list(combsx))
    combsArr = list(combsx).copy()
    #print(combsArr)
    #print(combsArr[0])
    return combsArr


if __name__ == "__main__":
    main()
