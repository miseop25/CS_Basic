class Sort :
    def __init__(self, array):
        self.array = array
    
    def quickSort(self, st, ed) :
        if st >= ed :
            return
        
        pivot = st
        i = st + 1
        j = ed
        temp = 0
        while i <= j :
            while i <= ed and self.array[i] <= self.array[pivot] :
                i += 1
            
            while j > st and self.array[j] >= self.array[pivot] :
                j -= 1
            if i > j :
                temp = self.array[j]
                self.array[j] = self.array[pivot]
                self.array[pivot] = temp
            else :
                temp = self.array[i]
                self.array[i] = self.array[j]
                self.array[j] = temp
        self.quickSort(st, j-1)
        self.quickSort(j+1 , ed)
    

if __name__ == "__main__":
    test = [2,4,6,4,1,23,6,8,8,213,4]
    s = Sort(test)
    s.quickSort(0, len(test)-1)
    print(s.array)