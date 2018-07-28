class _DoublyLinkedBase:

    class _Node:
        #streamine memory usage
        __slots__ = '_element', '_prev', '_next'
        
        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next
            
    #initialize _DoublyLinkedBase elements    
    def __init__(self):
        self._header = self._Node(None,None,None)
        self._trailer = self._Node(None,None,None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0
    
    #return the length of the list at a given time
    def __len__(self):
        return self._size
    
    #function returns True or False if list is empty
    def is_empty(self):
        return self._size == 0

    #function inserts elements between others in the list
    def _insert_between(self, e, predecessor, successor):
        newest = self._Node(e, predecessor, successor)
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest
    
    #function deletes elements from the list
    def _delete_node(self, node):
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element
        node._prev = node._next = node._element = None
        return element 

#LinkedDeque class inherits functions from _DoublyLinkedBase
class LinkedDeque(_DoublyLinkedBase):
    
    class _Node:
        __slots__ = '_element', '_prev', '_next'
    
        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next
            
    #function to return the first element from the list or raise Empty error
    def first(self):
        if self.is_empty():
            raise Empty( Deque is empty )
        return self._header._next._element
    
    #function to return the last element in the list or raise Empty error
    def last(self):
        if self.is_empty():
            raise Empty( Deque is empty )
        return self._trailer._prev._element
    
    #function to insert elements at the beginning of the list in the first position
    def insert_first(self,e):
        self._insert_between(e, self._header, self._header._next)
    
    #function inserts elements at the end of the list
    def insert_last(self,e):
        self._insert_between(e, self._trailer._prev, self._trailer)
    
    #function deletes first element from the list or raise Empty error
    def delete_first(self):
        if self.is_empty():
            raise Empty( Deque is empty )
        return self._delete_node(self._header._next)
    
    #function deletes last element from the list or raise Empty error
    def delete_last(self):
        if self.is_empty():
            raise Empty( Deque is empty )
        return self._delete_node(self._trailer._prev)

#initialize list
ld = LinkedDeque()

#display process of adding elements, display length, and removing from beginning and end of the list
print("Adding '10'", ld.insert_first(10))
print("Len:", len(ld))
print("First:", ld.first())
print("Last:", ld.last())
print("Insert '20' to last")
ld.insert_last(20)
print("Len:", len(ld))
print("First:", ld.first())
print("Last:", ld.last())
print("Insert '30' to last")
ld.insert_last(30)
print("Adding '1' to first")
ld.insert_first(1)
print("Len:", len(ld))
print("First:", ld.first())
print("Last:", ld.last())
print("Delete first '1'")
ld.delete_first()
print("First:", ld.first())
print("Delete last '30'")
ld.delete_last()
print("Last:", ld.last())
