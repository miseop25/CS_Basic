class Sort :
    def __init__(self, array):
        self.array = array
    
    def quickSort(self, st, ed) :
        if st >= ed :
            return
        
        pivot = st
        small = st + 1
        big = ed
        temp = 0
        while small <= big :
            while small <= ed and self.array[small] <= self.array[pivot] :
                small += 1
            
            while big > st and self.array[big] >= self.array[pivot] :
                big -= 1
            if small > big :
                temp = self.array[big]
                self.array[big] = self.array[pivot]
                self.array[pivot] = temp
            else :
                temp = self.array[small]
                self.array[small] = self.array[big]
                self.array[big] = temp

        self.quickSort(st, big-1)
        self.quickSort(big+1 , ed)
    

if __name__ == "__main__":
    test = [3,7,8,1,5,9,6,10,2,4]
    s = Sort(test)
    s.quickSort(0, len(test)-1)
    print(s.array)