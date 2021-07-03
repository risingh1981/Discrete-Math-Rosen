# There are 80 graph matrices in graph isomorphism.
from DiscreteMathRosen.Chapter10.mGraphColor import graphColor
from DiscreteMathRosen.Chapter10.matrixReader import dictGraphs


def read78(n):
    trialDict = dictGraphs(n)
    return trialDict

def individualTrial(trialKey, m, trialDict, errorCheck = False):
    trial = trialKey
    # Result stores the generated m-coloring of trialDict[trial]
    result = graphColor(trialDict[trial],m)
    
    matrix = trialDict[trial].copy()
    count = 1
    countDict ={}
    for ele in result:
        if ele in countDict:
            countDict[ele].append(count)
        else:
            countDict[ele] = [count]
        count += 1
    
    if errorCheck:
        errorChecker(countDict, matrix)

def errorChecker(countDict, matrix):
    errors = []
    for key in countDict:
        for num in countDict[key]:
            for num2 in countDict[key]:
                if matrix[num - 1][num2 - 1] == 1:
                    errors.append((num,num2))

    return errors
# Pass in list of trial keys to print in format that can be entered into Graph Online website.
def printMatrix(trialKeys, trialDict):
    for key in trialKeys:
        print(f"Graph for {key}")
        print()
        for line in trialDict[key]:
            print(*line, sep=",", end="")
            print()
        print()
# m is the max m to check upto
def determineM(trialDict, m = 10):
    for key in trialDict:
        for i in range(1,m):
            if graphColor(trialDict[key],i):
                print(f"Graph {key} is {i}-colorable")
                break
            
    