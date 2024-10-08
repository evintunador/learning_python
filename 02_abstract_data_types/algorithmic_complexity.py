# over in stack.py we used lists which can be edited
# here in BadStack we're using tuples where a new tuple has to be created each time
# this means the former uses O(1) operations per .push() and .pop()
# whereas BadStack uses O(n) 
#   because every entry has to be copied again into the new tuple every time

class BadStack:
    def __init__(self):
        self.data = ()

    def push(self, value):
        self.data += (value,)

    def pop(self):
        value = self.data[-1]
        self.data = self.data[:-1]
        return value

    def peek(self):
        return self.data[-1] 
    
# in python, appending to lists is somewhere in-between Stack & BadStack.
# basically a certain amount is pre-allocated, and if you append too many entries
# then the whole list gets copied into a bigger memory slot. This puts it
# in-between O(1) and O(n). Most operations are O(1) but every once in awhile
# we have to do O(n). We say appending an item to a list has an
# "amortised time complexity" of O(1) but a "worst-case time complexity" of O(n).

import sys

def byte_size(n):
    """Print the size in bytes of lists up to length n."""
    data = []
    for i in range(n):
        a = len(data)
        b = sys.getsizeof(data)
        print(f"Length:{a}; Size in bytes:{b}")
        data.append(i)

byte_size(20)

# a queue is like a stack except the only accessible item is the *earliest*
# items get added to the back of the que and taken from the front

# a deque (double-ended queue) is a generalization of queues and stacks that
# permits adding and removing items at either end.
# allocating free memory on both ends of the list that makes up the deque
# would be hella inefficient since we'd have to do the O(n) operation whenever
# only one side fills up. Instead we do what's called a ring buffer where
# as items get appended and prepended, they both take up the same empty space
# and eventually meet in the middle, at which point the O(n) operation of moving
# the list into a larger memory slot is performed