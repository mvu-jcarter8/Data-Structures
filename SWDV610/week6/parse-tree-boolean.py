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
    print(fpexp)
    fplist = fpexp.split()
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree
    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i not in ['+', '-', '*', '/', ')', '<', '>', '<=','>=','==','!=']:
            currentTree.setRootVal(int(i))
            parent = pStack.pop()
            currentTree = parent
        elif i in ['+', '-', '*', '/', '<', '>', '<=','>=','==','!=']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ')':
            currentTree = pStack.pop()
        else:
            raise ValueError
    return eTree

def evaluate(parseTree):
    opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv, '<':operator.lt, '>':operator.gt,  '<=':operator.le, '>=':operator.ge, '==':operator.eq, '!=':operator.ne}

    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()

    if leftC and rightC:
        fn = opers[parseTree.getRootVal()]
        return fn(evaluate(leftC),evaluate(rightC))
    else:
        return parseTree.getRootVal()

pt = buildParseTree(" ( 50 < 40 ) ")
print(evaluate(pt))
pt = buildParseTree(" ( 50 > 40 ) ")
print(evaluate(pt))
pt = buildParseTree(" ( 50 <= 40 ) ")
print(evaluate(pt))
pt = buildParseTree(" ( 50 >= 40 ) ")
print(evaluate(pt))
