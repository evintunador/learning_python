class Link:
    """a linked list that only goes forward unlike in linked_list.py"""
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def insert(self, link):
        '''Insert a new link after the current one.'''

        link.next = self.next
        self.next = link

    def __iter__(self):
        return LinkIterator(self)

# an iterator
class LinkIterator:
    def __init__(self, link):
        self.here = link

    def __iter__(self):
        # all iterators must have __iter__ which usually just returns self
        return self
    
    def __next__(self):
        # __next__ is the part that actually tells python what to return at each it
        if self.here:
            next = self.here
            self.here = self.here.next
            return next.value
        else:
            raise StopIteration
        
if __name__ == "__main__":
    linked_list = Link(1, Link(2, Link(3)))
    for l in linked_list:
        print(l)