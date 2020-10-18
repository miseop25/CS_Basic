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

class makeQueueWithStack :
    def __init__(self):
        self.a_Stack = []
        self.b_Stack = []
    
    def enQueue(self, data) :
        self.a_Stack.append(data)
    
    def deQueue(self) :
        if self.b_Stack :
            return self.b_Stack.pop()
        while self.a_Stack :
            self.b_Stack.append(self.a_Stack.pop())

        if not self.b_Stack :
            return "deQueue 할 수 없습니다."

        return self.b_Stack.pop()


if __name__ == "__main__":
    l = LinkedQue()
    l.enQueue(Node(1))
    l.enQueue(Node(2))
    l.print()
    l.deQueue()
    l.print()

    # 스택 2개로 큐 만들기 
    print("=======================")
    st = makeQueueWithStack()
    st.enQueue(1)
    st.enQueue(2)
    print(st.deQueue())
    print(st.deQueue())
    print(st.deQueue())
