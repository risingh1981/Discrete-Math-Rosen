# Generators are a simple for creating iterators.
"""
def reverse(data):
    for index in range(len(data)-1, -1, -1): # index decreases from max to min
        print(f"In Reverse Generator at index:{index}.")
        yield data[index] # yield keyword returns a generator object
# Testing to see if returning a file just returns first line. Reality: it returns a file object.
def returntest():
    return open("C:/Users/ricky/Desktop/Programming/Discrete Math Rosen/Chapter2/test3.py", "r")

#They are written like regular functions but use the yield statement whenever they want to return data.
gen = reverse("golf") # Creates a generator object because yield was used, its like an iterator object
                      # on which you can call next
print(gen)
print(next(gen)) # Will print first char in generator gen, but thats actually last char in string used for
                 # creating the generator
# Since the yield in the reverse function returns 

# Using yield will result in a generator object. 
# Using return will result in the first line of the file only. (dont get what they meant by first line)
file = returntest() # returntest returns a file object which you can iterator over with next().
print(file) # return used to return file object
print(next(file)) # next interator will return next line in file, which at this time is first line in file.

** Creating Generators:
>>> nums_squared_lc = [num**2 for num in range(5)]  # Creates a list: [0,1,4,9,16]
>>> nums_squared_gc = (num**2 for num in range(5))  # Creates a generator: <generator object <genexpr> at 0x107fbbc78>
- Generators help keep mem usage low. A list of squares 0-10000 is 87624 bytes, a generator object is 120 bytes.
-  Generators are slower than list comprehension.
    If speed is an issue and memory isn’t, then a list comprehension is likely a better tool for the job.
** Yield Keyword
- Generators based on yield functionality.
- You can use multiple yields within a function. The function will pause at first yield till next is called.
** Advanced Generator Methods: send(), close(), throw()
