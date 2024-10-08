import numpy as np

from composition_and_delegation import Element

# now for different types of groups, we can start with a base Group class
class Group:
    def __init__(self, n):
        self.n = n

    def __call__(self, value):
        return Element(self, value)
    
    def __str__(self):
        # we don't expect Group itself to ever be instantiated and we'll be
        # defining .symbol in an inherited classes, so this will work at runtime
        return f"{self.symbol}{self.n}"
    
class CyclicGroup(Group): # <- the inheritance part
    symbol = "C" 
    # by defining this here instead of inside a __init__, that makes symbol
    # the same across all CyclicGroup objects that get created
    # good to do this when you won't need to change the value

    def _validate(self, value):
        if not (isinstance(value, int) and 0 <= value < self.n):
            raise ValueError("Element value must be an integer"
                             f" in the range [0, {self.n})")
        
    def operation(self, a, b):
        return (a+b) % self.n
    
class GeneralLinearGroup(Group):
    """general linear group represented by n x n matrices"""
    symbol = "G"

    def _validate(self, value):
        value = np.asarray(value)
        if not (value.shape == (self.n, self.n)):
            raise ValueError("Element value must be a "
                             f"{self.n} x {self.n} square array")
        
    def operation(self, a, b):
        return a @ b
    
cyc = CyclicGroup(5)
lin = GeneralLinearGroup(2)
print(cyc)
print(lin)
    
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
    def __repr__(self):
        return f"{type(self).__name__}({self.length, self.width!r})"
    
class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)
        # using super() avoids having to override methods from Rectangle 
        # as we're instead passing in inputs.

    def __repr__(self):
        return f"{type(self).__name__}({self.length!r})"
    
sq = Square(2)
print(sq.width, sq.length, sq.area())