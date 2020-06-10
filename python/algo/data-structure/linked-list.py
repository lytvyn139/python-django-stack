class Node:
    def __init__(self, valueInput):
        self.value = valueInput
        self.next = None

class SLL:
    def __init__(self):
        self.head = None
    
    def addfrond(self, valueInput):
        newnode = Node(valueInput)
        newnode.next = self.head
        self.head = newnode
        return self

    def display(self):
        runner = self.head
        while runner != None:
            print(runner.value)
            runner = runner.next
        return self
    
    def contains(self, valueInput):
        runner = self.head
        while runner != None:
            #print(runner)
            #print(valueInput)
            if runner.value == valueInput:
                return True
            runner = runner.next
        return False


sll1 = SLL()
print(sll1.addfrond(5).addfrond(8).addfrond(15).display().contains(23))


