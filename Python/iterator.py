# Defining your own iterator. Create class for iterator.
class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)
    
    def __iter__(self):
        return self
        
    
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]
    

def main():
    name = "Rick"
    new = Reverse(name)
    print(new)
    
    it1 = iter(name)# Regular Iter() function defined for certain object types
    it2 = iter(new)# Class Reverse redefines iterator function to go in reverse
    print("Next ele with next on regular iterator:",next(it1))
    print("Next ele with next on reverse class iterator:",next(it2))
  




if __name__ == "__main__":
    main()