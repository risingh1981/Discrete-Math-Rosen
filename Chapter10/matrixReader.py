# Program to read in values for adjacency matrix and create lists out of the values as formatted on
# website http://funkybee.narod.ru/graphs.htm
from copy import deepcopy
def main():

    trialDict = dictGraphs(4)
    for key in trialDict:
        print(trialDict[key])


# n is number of graphs to extract 
def dictGraphs(n):
    file = open("graphIsomorphism.txt", "r")
    counter = 1
    start = 0
    end = 20
    size = 3
    numGraphs = 0
    dictOfMatrices = {}
    printIndex = 0
    for line in file:
        if len(line) == 3 or len(line) == 2:
            size = int(line.strip())
            start = counter + 1
            end = counter + (2*size) + 1
            matrixOfGraph = [([0] * size) for _ in range(size)]
            firstOrSecond = 1
            indexDecrement = start
        if (counter == start + size) or (counter == end + 1):
            if f"{size}.F.2" in dictOfMatrices:
                dictOfMatrices[f"{size}.{'G'}.{firstOrSecond}"] = deepcopy(matrixOfGraph)
            elif f"{size}.E.2" in dictOfMatrices:
                dictOfMatrices[f"{size}.{'F'}.{firstOrSecond}"] = deepcopy(matrixOfGraph)
            elif f"{size}.D.2" in dictOfMatrices:
                dictOfMatrices[f"{size}.{'E'}.{firstOrSecond}"] = deepcopy(matrixOfGraph)
            elif f"{size}.C.2" in dictOfMatrices:
                dictOfMatrices[f"{size}.{'D'}.{firstOrSecond}"] = deepcopy(matrixOfGraph)
            elif f"{size}.B.2" in dictOfMatrices:
                dictOfMatrices[f"{size}.{'C'}.{firstOrSecond}"] = deepcopy(matrixOfGraph)
            elif f"{size}.A.2" in dictOfMatrices:
                dictOfMatrices[f"{size}.{'B'}.{firstOrSecond}"] = deepcopy(matrixOfGraph)
            elif f"{size}.2" in dictOfMatrices:
                dictOfMatrices[f"{size}.{'A'}.{firstOrSecond}"] = deepcopy(matrixOfGraph)
            else:
                dictOfMatrices[f"{size}.{firstOrSecond}"] = deepcopy(matrixOfGraph)
            numGraphs += 1
            firstOrSecond = 2
            indexDecrement = counter + 1
        if (numGraphs == n):
            return dictOfMatrices
        if (counter >= start) and (counter <= end) and (line.strip() != ""):
            index = counter - indexDecrement
            addLineToMatrix(matrixOfGraph, line,index)
        counter += 1
        
def addLineToMatrix(matrixOfGraph, line, index):
    for pos, char in enumerate(line.strip()):
        matrixOfGraph[index][pos] = int(char)

if __name__ == "__main__":
    main()