from collections import deque
stack = deque();
print(deque)

stack.append('www.cnn.com')
stack.append('www.cnn.com/world')
stack.append('www.cnn.com/india')
stack.append('www.cnn.com/china')
print(f'{stack} \n')

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self,val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return self.container[-1]
    
    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)
    
    s = Stack()
    s.push(5)
    s.peek()