def selectionSort(arr) :
    for i in range(len(arr)-1) :
        minIndex = i 
        for j in range(i, len(arr)) :
            if arr[j] < arr[minIndex] :
                minIndex = j
        buf = arr[i]
        arr[i] = arr[minIndex]
        arr[minIndex] = buf
    return arr

def bubbleSort(arr) :
    for i in range(len(arr) - 1, 0, -1) :
        for j in range(i) :
            if arr[j] > arr[j+1] :
                buf = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = buf
    return arr

def insertionSort(arr) :
    for i in range(1, len(arr)) :
        j = i - 1 
        key = array[i]
        while arr[j] > key and j >=0 :
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr


array = [2,5,3,1,6,0]
print(selectionSort(array))
print(bubbleSort(array))
print(insertionSort(array))