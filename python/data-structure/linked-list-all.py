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
        
    
    #Given a pointer to the first node in a list, remove the head node and return the new list head node. If list is empty, return null.”
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

    #Create a function that creates a ListNode with given value and inserts it at end of a linked list.”
    #each node have node.next
    #find which node didn't have Next (next == none)
    #insert new node
    def create_node_at_end(self, valueInput): 
        #your code here
        #create new node
        newnode = Node(valueInput)
        if self.head == None:
            self.head = newnode
        else:
            runner = self.head
            while runner.next != None:
                #increment runner
                runner = runner.next
            # print(runner.value)
            runner.next = newnode
            # return self



    # def removeBack(self):
    #     if self.head == None:
    #         print("nothing to return fam")
    #         return self
    #     runner = self.head
    #     if runner.next == None:
    #         self.head = None
    #         return self
    #     while runner.next.next != None:
    #         runner = runner.next
    #     # print(runner.value)
    #     runner.next = None
    #     return self

    #standalone method
    def removeBack(SLLInput):
            if SLLInput.head == None:
                print("nothing to return fam")
                return SLLInput
            runner = SLLInput.head
            if runner.next == None:
                SLLInput.head = None
                return SLLInput
            while runner.next.next != None:
                runner = runner.next
            # print(runner.value)
            runner.next = None
            return SLLInput



##  display
# sll3 = SLL()
# sll3.remove_first().display()

## contains
#sll = SLL()
#print(sll.addfrond(5).addfrond(8).addfrond(15).display().contains(23))

## remove 
# sll2 = SLL()
# #created with self.head = None
# print(sll2.addfrond(5).addfrond(3).addfrond(12).remove_first().display())

#crete node at end
# sll = SLL()
# print(sll.addfrond(5).addfrond(3).addfrond(8).create_node_at_end(4).display())



#removeBack
sll1 = SLL()
# sll1.addback(5).addback(8).addback(12).addback(13).addback(15).display()
sll1.addback(5).addback(12).addback(18)

removeBack(sll1)
sll1.display()










