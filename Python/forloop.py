'''
Definite Interation - # of iterations determined before hand. Indefininite Iteration - code executes until 
some condition is met
- Collection Based or Iterator Based Iteration
for <var> in <iterable>: # Loop variable <var> takes on next value in <iterable> on each iteration.
    <statement(s)>
- Iterable : an object that can be used in iteration. Ex: String, List, Set, Dict, Tuple, file, Frozenset
- Non-iterables: Int, float, functions
- Iterable objects can can converted to an interator with: iter(<object>) <- returns an iterator object
- Iterator yeilds next values with function: >>> next(<iterator object>)
Ex:
a = ['foo', 'bar', 'baz']   # a is iterable
itr = iter(a)    
itr                         # itr is associated iterator with iterable list a
                            # <list_iterator object at 0x031EFD10>
next(itr)                   # Each call to next obtains the next value from itr
- When next() runs out of values to return it raises a StopIteration exception
- Convert iterator to a list, set, tuple with list(<itr>), set(<itr>), tuple(<itr>)
** For Loops in Python **
Ex:
a = ['foo', 'bar', 'baz']
for i in a:
    print(i)
1) Calls iter(a) to obtain iterator for a
2) Calls next() repeatedly to obtain each element from iterator.
3) Terminates loop when next() raises StopIteration exception.

- Standard Library module called itertools exists containing many functions that return iterables.
- User defined objects with OOP can be made iterable.
- Generators make creating an iterator simple. Covered in generators.py
*** Dictionaries 
    1)for a in dict           # Will iterate through keys in dict.
    2)for a in dict.values()  # Will iterate through dicts values
    3)for i, j in [(1, 2), (3, 4), (5, 6)]: # on each iteration i,j assigned values from the tuples.
         print(i, j) # will print 1 2/3 4/5 6
    
    d = {'foo': 1, 'bar': 2, 'baz': 3}
    d.items() # returns dict_items([('foo', 1), ('bar', 2), ('baz', 3)]), dict.items() returns a list of tuples.
    - So to iterate key/val in dic, create list of tuples from dict with .items() and use #3 above.
*** range() function -> returns an interable which yeilds a sequence of ints
x = range(0, 5) # type(x) = <class 'range'> Note, it returns an object of class range, not a list/tuple/etc. But object range is an iterable.
- Like iterators, range objects are lazy(don't generate values until requeted)
- Format: range(<begin>, <end>, <stride>). If stride omitted, defaults to 1. If just one # input, begin = 0, end = the number.
** Else clause for "for loops"
for i in range(5):/n print(i) /n Else: /n print("Done")
The else clause will be executed if the loop terminates through exhaustion of the iterable, but not if terminated with "break".

