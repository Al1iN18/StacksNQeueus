from node import Node

class Stack():
    def __init__(self):
        self.top = None

    def __str__(self):
        string = "TOP Of StACK \n"
        traverser = self.top
        while traverser != None:
            string += str(traverser.data)+ "\n" 
            traverser = traverser.next
        string += "-----Bottom of Stack-----"
        return string
    


    def push(self, data):
        temp = Node(data)
        temp.next = self.top
        self.top = temp

    def pop(self):
        if self.top == None:
            print ("Empty stack")
        else:
            temp = self.top
            self.top = self.top.next
            return temp.data
        
