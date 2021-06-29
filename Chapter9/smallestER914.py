# Chapter 9, Computer Project 14: Given the matrix representing a relation on a 
# finite set, find the matrix representing the smallest equivalence relation
# containing this relation.
# Math Foundation: The transitive closure of the symmetric closure of the reflexive 
# closure of a relation R is the smallest equivalence relation that contains R.
from DiscreteMathRosen.Chapter9.reflexiveClosure910 import reflexiveClosure
from DiscreteMathRosen.Chapter9.symmClosure911 import symmetricClosure
from DiscreteMathRosen.Chapter9.warshallsTC913 import warshalls
from DiscreteMathRosen.Chapter9.transitive93 import transitive
from DiscreteMathRosen.Chapter9.symmetric92 import symmetric
from DiscreteMathRosen.Chapter9.reflexive91 import reflexive

def main():
    # Input
    inputMatrix = [[0, 0, 0, 1], [1, 0, 1, 0], [1, 0, 0, 1], [0, 0, 1, 0]]

    # Output
    output = warshalls(symmetricClosure(reflexiveClosure(inputMatrix)))

    print(f"Test Matrix: {inputMatrix}")
    print(f"Equivalence Closure(EC) of Test Matrix: {output}")
    print(f"Is Test Matrix an ER:{reflexive(inputMatrix) and transitive(inputMatrix) and symmetric(inputMatrix)}. Is output an ER:{reflexive(output) and transitive(output) and symmetric(output)}.")


if __name__ == "__main__":
    main()