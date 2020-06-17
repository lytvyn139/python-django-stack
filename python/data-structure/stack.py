class Node:
    def __init__(self, valueInput):
        self.value = valueInput
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, valueInput):
        newnode = Node(valueInput)
        if self.top == None:
            self.top = newnode
        else:
            newnode.next = self.top
            self.top = newnode
        return self

    #another implementation of push
    def push2(self, valueInput):
        newnode = Node(valueInput)
        temp = self.top
        self.top = newnode
        self.top.next = temp
        return self

    def display(self):
        runner = self.top
        # print(runner)
        while runner != None:
            print(runner.value)
            runner = runner.next
        return self

newstk = Stack()
newstk.push(5).push(15).display()
