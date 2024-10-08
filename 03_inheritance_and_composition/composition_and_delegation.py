# an example from group theory

class Element:
    """An element of the specified group"""
    def __init__(self, group, value):
        self.group = group
        self.value = value

        # "delegating" the job of making sure that value is a valid item in
        # the group to the actual group class which we've yet to write
        group._validate(value)

    def __mul__(self, other):
        assert isinstance(other, Element)
        return Element(self.group, self.group.operation(self.value, other.value))
    
    def __str__(self):
        return f"{self.value}_{self.group}"
    
class CyclicGroup:
    """AKA addition modulo group order"""
    def __init__(self, order):
        self.order = order

    def _validate(self, value): # leading underscore indicates internal use only
        if not (isinstance(value, int) and 0 <= value < self.order):
            raise ValueError("Element value must be an integer"
                             f" in the range [0, {self.order})")
        
    def operation(self, a, b):
        return (a+b) % self.order
    
    def __call__(self, value):
        # "composition" of these two classes: you never need to actually
        # directly use the Element class bc CyclicGroup calls & uses it for you
        return Element(self, value)
    
    def __str__(self):
        return f"C{self.order}"
    
if __name__ == "__main__":
    C = CyclicGroup(5)
    print(C)
    print(C(3) * C(4))
    print(C(1.5))