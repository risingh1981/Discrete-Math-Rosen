# Chapter 9, Computer Project 7: Given a positive integer n, display all the 
# equivalence relationson the set of the n smallest positive integers {1,2,...,n}.
# Math Foundation: An equivalence relation is a relation that is reflexive, symmetric, 
# and transitive.
# In previous programs, I have already written function which generate all possible
# relations, test for reflexivity, symmetry and transitivity. I will use them here.
from DiscreteMathRosen.Chapter9.transitiveCount95 import generateAllRelations, transitive
from DiscreteMathRosen.Chapter9.symmetric92 import symmetric
from DiscreteMathRosen.Chapter9.reflexive91 import reflexive
from time import perf_counter_ns

def main():
    # Input
    # Bell Numbers: 1,2,5,15,52,203,877,4140
    n = 4
    inputSet = [x for x in range(1, n + 1)]
    generateAllEquivRel(inputSet)
    
    '''
    Total Rels Generated:65536  in 0.3001236 seconds.
    Total relations: 65536
    Time(s) for timeER:0.0635196  timeRef:0.0336878, timeSym:0.0567236, timeTrans:1.4653186  
    Counts:   Ref:4096   Sym:1024  Trans:3994  ER: 15
    '''


def generateAllEquivRel(inputSet):
    allRel = generateAllRelations(inputSet)
    allER = []
    # Will check in order: Symmetric, Reflexive, Trans because time to check each is
    # in that order least to most.
    for relation in allRel:
        if symmetric(relation) and reflexive(relation) and transitive(relation):
            allER.append(relation)


if __name__ == "__main__":
    main()