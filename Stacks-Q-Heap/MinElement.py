# Find the minimum element in a stack in O(1) time

class minStackElement():
    def __init__(self, value, minElement):
        self.value = value
        self.minElement = minElement

class Stack:
     def __init__(self):
         self.items = []

     def push(self, item):
         if self.items == []:
             self.items.append(minStackElement(item,item))
         else:
             if self.items[len(self.items)-1].minElement > item:
                 self.items.append(minStackElement(item,item))
             else:
                 self.items.append(minStackElement(item,self.items[len(self.items)-1].minElement))

     def pop(self):
         return self.items.pop()

     def minElement(self):
         return self.items[len(self.items)-1].minElement

s = Stack()
for i in range(5,10):
    s.push(i)
print s.minElement()
s.push(1)
s.push(1)
s.push(3)
s.pop()
s.pop()
print s.minElement()
