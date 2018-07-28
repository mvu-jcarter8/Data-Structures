class LinkedQueue:

    class _Node:
        #streamline memory usage
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    #intialize LinkedQueue class variables
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    #return length of the list
    def __len__(self):
        return self._size
    
    #return True or False whether list is empty 
    def is_empty(self):
        return self._size == 0

    #function returns first element without removing it
    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._head._element

    #function returns first element from the list, reduces length by one or raises Empty error
    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return answer

    #function adds element to the last of the list and increases the length by one
    def enqueue(self, e):
        newest = self._Node(e, None)
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1
        return e

lq = LinkedQueue()
#testing usage of functions to add elements to the list and display results
print("LinkedQueue is empty? {}, Len:{}".format(lq.is_empty(),len(lq),))
print("Enqueue:",lq.enqueue(10))
print("Return first:",lq.first())

#add elements to the list by using enqueue functions
print("Enqueue:",lq.enqueue(20))
print("Enqueue:",lq.enqueue(30))
print("Enqueue:",lq.enqueue(40))
print("Enqueue:",lq.enqueue(50))
print("LinkedQueue is empty? {}, Len:{}".format(lq.is_empty(),len(lq),))

#remove elements from list using dequeue functions
print("Dequeue:",lq.dequeue())
print("Dequeue:",lq.dequeue())
print("Dequeue:",lq.dequeue())
print("Dequeue:",lq.dequeue())
print("Dequeue:",lq.dequeue())
print("LinkedQueue is empty? {}, Len:{}".format(lq.is_empty(),len(lq),))
