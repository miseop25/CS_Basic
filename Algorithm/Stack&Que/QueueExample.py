class Node(object) :
    def __init__(self, data) :
        self.data = data
        self.next = None

class LinkedQue(object) :
    def __init__(self) :
        self.top = None
        self.rear = None
    
    def enQueue(self, node) :
        if self.rear == None :
            self.top = node
            self.rear = node
        else :
            self.top.next = node
            self.top = self.top.next
    
    def deQueue(self) :
        if self.rear == None : 
            return False
        
        v= self.rear.data
        self.rear = self.rear.next

        if self.rear == None :
            self.top = None
        return v 

    def print(self) :
        temp = self.rear
        result = ""
        while temp :
            result += str(temp.data)
            if temp.next :
                result += " "
            temp = temp.next
        print(result)


if __name__ == "__main__":
    l = LinkedQue()
    l.enQueue(Node(1))
    l.enQueue(Node(2))
    l.print()
    l.deQueue()
    l.print()
