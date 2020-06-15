import sys

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

    def remove_first(self): 
        # print(f"self.head: {self.head}") #12
        # print(f"self.head.next: {self.head.next} ") #3
        # print(f"self.head.next.value {self.head.next.value}") #3
        # self.head = self.head.next
        # return self

        if self.head == None:
            print('nothing to remove')
            return None
        else:
            self.head = self.head.next
        return self





#sll = SLL()
#print(sll.addfrond(5).addfrond(8).addfrond(15).display().contains(23))

sll2 = SLL()
#created with self.head = None
print(sll2.addfrond(5).addfrond(3).addfrond(12).remove_first().display())

sll3 = SLL()
sll3.remove_first().display()






