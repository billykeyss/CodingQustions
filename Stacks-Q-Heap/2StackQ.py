# HARD: Implement a queue using 2 stacks

class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self,item):
        self.stack1.append(item)

    def dequeue(self):
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        popped = self.stack2.pop()

        while self.stack2:
            self.stack1.append(self.stack2.pop())
        return popped



s = Queue()
for i in range(1,10):
    s.enqueue(i)
print s.dequeue()
print s.dequeue()
print s.dequeue()
