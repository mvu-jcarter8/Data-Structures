class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

from binarytree import BinaryTree
import operator

def buildParseTree(fpexp):
    #remove any white spaces
    fpexp = fpexp.replace(' ', '')
    #replace left parenthesis with space after
    fpexp = fpexp.replace('(','( ')
    #replace right parenthesis with space before
    fpexp = fpexp.replace(')',' )')
    #replace operators with spaces before and after
    fpexp = fpexp.replace('+',' + ')
    fpexp = fpexp.replace('-',' - ')
    fpexp = fpexp.replace('*',' * ')
    fpexp = fpexp.replace('/',' / ')
    
    fplist = fpexp.split()
    print("String before processing: {}".format(fplist))
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree
    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i not in ['+', '-', '*', '/', ')']:
            currentTree.setRootVal(int(i))
            parent = pStack.pop()
            currentTree = parent
        elif i in ['+', '-', '*', '/']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ')':
            currentTree = pStack.pop()
        else:
            raise ValueError
    return eTree
        
#pt = buildParseTree("( ( 20 + 10 ) * 3 )")
pt = buildParseTree("((20+50)*3)") #no spaces expressions
pt.postorder()
