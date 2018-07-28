class LinkedStack:

    class _Node:
        #streamline memory usage
        __slots__ = '_element', '_next'

        #intialize node variables
        def __init__(self, element, next):
            self._element = element
            self._next = next

    #initialize class list
    def __init__(self):
        self._head = None
        self._size = 0

    #return lenght of the list
    def __len__(self):
        return self._size

    #return True or False whether list is empty
    def is_empty(self):
        return self._size == 0

    #add element to the top or end of the list, increase lenght by one
    def push(self, e):
        self._head = self._Node(e, self._head)
        self._size += 1
        return e
    
    #return the bottom or first element without removing
    def top(self):
        if self.is_empty():
            raise Empty( Stack is empty )
        return self._head._element

    #return the top or last element and remove from list, decrease length by one or raise Error if list is empty
    def pop(self):
        if self.is_empty():
            raise Empty( Stack is empty )
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer

#initialize list
ls = LinkedStack()
print("LinkedStack is empty? {}, Len:{}".format(ls.is_empty(),len(ls),))

#get user input to add a number to the stack and check functions
ls.push(int(input('Enter a number to push onto the stack: ')))
print("LinkedStack is empty? {}, Top:{}, Len:{}, Pop:".format(ls.is_empty(),ls.top(),len(ls)), ls.pop())

#push elements to list and run functions to display results
print("Push:",ls.push(10))
print("Push:",ls.push(20))
print("Push:",ls.push(30))
print("LinkedStack is empty? {}, Top:{}, Len:{}, Pop:".format(ls.is_empty(),ls.top(),len(ls)), ls.pop())
