## Zip() function
# Returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument 
# sequences or iterables. The iterator stops when the shortest input iterable is exhausted. 
# With a single iterable argument, it returns an iterator of 1-tuples. With no arguments, it returns an 
# empty iterator. 
# If you’re going to use the Python zip() function with unordered iterables like sets, tuples returned by 
# zip() will have elements that are paired up randomly.


a = [1,2,3,4]
b = ["a","b","c","d","e"]
e = [5.6,6.7,7.8,8.9] # you can use zip with 3 iterables to generate an iterator of 3-tuples.

c = zip(a,b) # c is iterator of tuples of respective elements from a and b. 
print(c) # <zip object at 0x01098748>
print(next(c)) # (1, 'a')
print(dict(c)) # {2: 'b', 3: 'c', 4: 'd'} # Since we had already iterated over (1, 'a')
print(list(c)) # []  # Since iterator c had nothing left.
d = zip(a,b)
print(list(d)) # [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')] # a 1D-array of the tuples as elements
# print(dict(zip(a,b,e))) # ValueError: dictionary update sequence element #0 has length 3; 2 is required
print(list(zip(a,b,e))) # [(1, 'a', 5.6), (2, 'b', 6.7), (3, 'c', 7.8), (4, 'd', 8.9)]

## Unpacking operator.
# If you have a list with tuples, you can "unpack" the tuples into a tuple for each element in original tuples.
pairs = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
numbers, letters = zip(*pairs)
print(numbers) # (1, 2, 3, 4)
print(letters) # ('a', 'b', 'c', 'd')
