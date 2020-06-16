class Node:
    def __init__(self, valueInput):
        self.value = valueInput
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    #FIFO
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
    
    def front(self):
        if self.head == None:
            return None
        else:
            return self.head.value
    
    #CONTAINS
        #....

    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False

    def size(self):
        count = 0
        runner = self.head
        while runner != None:
            count +=1
            runner = runner.next
        return count


        


# q1 = Queue()
# q1.enqueue(5).dequeue()
# q1.display().

# q1 = Queue
# print(q1)
# q1.enqueue(5).enqueue(8).enqueue(12).dequeue()
# q1.display()

#size
q1 = Queue()
print(q1.enqueue(5).enqueue(8).enqueue(12).size())