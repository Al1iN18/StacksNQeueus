from node import Node

class Queue():
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        temp = Node(data)
        if self.rear == None:
            self.front = self.rear = temp
        else:
            self.rear.next = temp
            self.rear = temp
    
    def dequeue(self):
        if self.front == None:
            print("Empty queue")
        else:
            temp = self.front
            self.front = temp.next
            return temp.data
        
    def __str__(self):
        string = "Front of Q:  "
        traverser = self.front
        while traverser != None:
            string += str(traverser.data) + " | "
            traverser = traverser.next
        string += "Rear of Q  "

        return string

