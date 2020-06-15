class Node:
    def __init__(self, valueInput):
        self.value = valueInput
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

# clinkscale enqueue
# def enqueue(self, valueInput):
#     if self.head == None:
#         self.head = Node(valueInput)
#         self.tail = Node(valueInput)
#         return self
#     else:
#         newnode = Node(valueInput)
#         runner = self.head
#         while runner.next != None:
#             runner = runner.next
#         runner.next = newnode
#         self.tail = runner.next
#         return self

    def enqueue(self, valueInput):
        newnode = Node(valueInput)
        if self.head == None:
            self.head = newnode
            self.tail = newnode
        else:
            self.tail.next = newnode
            self.tail = self.tail.next
        return self

    def dequeue(self):
        if self.head == None:
            print("nothing to remove fam")
            return self
        else:
            temp = self.headvalue
            self.head = self.head.next
            return temp


    def display(self):
        runner = self.head
        # print(runner)
        while runner != None:

            runner = runner.next
        return self


q1 = Queue()
q1.enqueue(5).dequeue()
q1.display().

q1 = Queue
print(q1)
q1.enqueue(5).enqueue(8).enqueue(12).dequeue()
q1.display()