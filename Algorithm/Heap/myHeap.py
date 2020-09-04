class MyMaxHeap :
    def __init__(self) :
        self.heap = [None]*100
        self.size = 0 
    
    def push(self, data) :
        self.size += 1
        self.heap[self.size] = data
        i = self.size
        while i > 1 :
            if self.heap[int(i//2)] < self.heap[i] :
                temp = self.heap[int(i//2)]
                self.heap[int(i//2)] = self.heap[i]
                self.heap[i] = temp
            else :
                break
            i = int(i//2)
    
    def pop(self) :
        if self.isEmpty() :
            return None
        result = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.heap[self.size] = None
        self.size -= 1
        
        i = 1
        while i < (self.size//2 ) : 
            if (self.heap[i] > self.heap[i*2]) and (self.heap[i] > self.heap[i*2 + 1]) :
                break
            elif self.heap[i] < self.heap[i*2] :
                temp = self.heap[i]
                self.heap[i] = self.heap[i*2]
                self.heap[i*2] = temp
                i *= 2
            else :
                temp = self.heap[i]
                self.heap[i] = self.heap[(i*2) +1]
                self.heap[(i*2) + 1] = temp
                i = i*2 + 1
        return result

    def isEmpty(self) :
        if self.size == 0 : 
            return True
        else :
            return False

h = MyMaxHeap()
h.push(1)
h.push(2)
h.push(10)
h.push(3)
h.push(-2)

for _ in range(5) :
    print(h.pop())

