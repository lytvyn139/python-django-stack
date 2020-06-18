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

    def display(self):
        runner = self.top
        # print(runner)
        while runner != None:
            print(runner.value)
            runner = runner.next
        return self

    def return_top(self):
        if self.top == None:
            print ('stack is empty')
            return self
        else:
            print(self.top.value)
            return self.top.value

    def is_empty(self):
        if self.top == None:
            return True
        else:
            return False

    #pop stack
    def pop(self):
        if self.top != None:
            temp_value = self.top.value
            self.top = self.top.next
            return temp_value
        else:
            print('no top to pop')
            return self


# return top stack
new_stack = Stack()
new_stack.push(5).push(15).push(25).return_top()
# return top but the stack is empty
empty_stack = Stack()
empty_stack.return_top()

# check if the stack is empty
new_stack2 = Stack()
print(new_stack2.push(5).push(15).push(25).is_empty())

#pop stack
pop_stack = Stack()
pop_stack.push(5).push(15).push(25).pop()
pop_stack.display()