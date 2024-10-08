# Starting from the first link in a list, it is possible to move along 
# the list by following the references to successive further links. 
# A new item can be inserted at the current point in the list by 
# creating a new link, pointing the link reference of the new link to 
# the next link, and pointing the link reference of the current link to the new link.
# A doubly linked list differs from a singly linked list in that each 
# link contains links both to the next link and to the previous one. 
# This enables the list to be traversed both forwards and backwards.

class Link:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

    def insert(self, new_link):
        '''Insert a new link after the current one.'''
        new_link.next = self.next
        new_link.prev = self
        if self.next:
            self.next.prev = new_link
        self.next = new_link

# Test the doubly linked list
if __name__ == "__main__":
    # Create the initial link
    head = Link(1)
    
    # Insert more links
    head.insert(Link(2))
    head.insert(Link(3))
    head.next.insert(Link(4))
    
    # Traverse forward
    print("Forward traversal:")
    current = head
    while current:
        print(current.value, end=" ")
        current = current.next
    print()
    
    # Traverse backward
    print("Backward traversal:")
    current = head
    while current.next:
        current = current.next
    while current:
        print(current.value, end=" ")
        current = current.prev
    print()