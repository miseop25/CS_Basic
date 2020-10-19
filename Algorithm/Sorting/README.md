# 정렬 (Sorting)

정렬은 가장 기초적이면서도 많이 사용하는 알고리즘 입니다.  
이미 좋은 정렬 함수들이 많이 존재하고 있어서 직접 만들어서 사용한 경우는 적은 편 입니다.  
가장 기초적인만큼 어떤 정렬 알고리즘이 있는지 알고 넘어가면 좋을 것 같습니다.  
이번 포스팅에서는 기초적인 알고리즘 3가지를 알아보도록 하겠습니다.  

1. 선택정렬(Selection Sort)
2. 버블정렬(Bubble Sort)
3. 삽입정렬(Insertion Sort)

*** 

## 선택정렬 (Selection Sort)

선택정렬은 자리를 선택한 후 해당 자리에 올 요소를 집어넣는 경우입니다.  
오름차순으로 정렬을 잰행한다면 첫번째 인덱스에는 가장 작은수를 찾아서 넣고, 두번째 인덱스도 두번째 인덱스부터 가장 작은 수를 찾아서 정렬합니다.      

    선택정렬의 시간복잡도    
    최선 : O(N^2)
    평균 : O(N^2)
    최악 : O(N^2)   


다음 그림을 보면 이해가 쉬울 것이라 생각됩니다.   

![스크린샷 2020-08-19 오후 9 45 48](https://user-images.githubusercontent.com/44546283/90636311-5ee71c00-e265-11ea-9dc5-4250a0462b94.png)

**다음은 선택정렬의 Python Code 입니다.**
```
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
```

*** 
  
## 버블정렬(Bubble Sort)

버블정렬은 서로 인접한 두 원소를 비교하면서 정렬하는 알고리즘입니다.  
선택정렬은 앞에서부터 정렬이 이루어진 반면 버블정렬은 뒤에서부터 정렬이 이루어집니다.(1회전 시)

    버블 정렬의 시간복잡도   
    최선 : O(N^2)
    평균 : O(N^2)
    최악 : O(N^2)

버블정렬은 다음과 같은 과정을 통해서 이루어집니다.   

![스크린샷 2020-08-19 오후 11 25 30](https://user-images.githubusercontent.com/44546283/90647466-4d0c7580-e273-11ea-876a-448bc9b52a28.png)
**다음은 버블정렬의 Python Code 입니다.**
```
def bubbleSort(arr) :
    for i in range(len(arr) - 1, 0, -1) :
        for j in range(i) :
            if arr[j] > arr[j+1] :
                buf = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = buf
    return arr
```
***

## 삽입정렬(Insertion Sort)  

삽입정렬은 삽입하고자 하는 앞의 배열을 탐색하면서 들어갈 위치를 찾는 것 입니다.   
2번째 요소부터 시작하여 자신의 위치를 찾는 것 입니다.   

    삽입정렬의 시간복잡도 
    최선 : O(N)
    평균 : O(N^2)
    최악 : O(N^2)

삽입정렬은 다음과 같은 과정을 통해서 이루어집니다.   

![스크린샷 2020-08-20 오전 12 13 03](https://user-images.githubusercontent.com/44546283/90653282-f35b7980-e279-11ea-905f-ae499f0f6f65.png)

![스크린샷 2020-08-20 오전 12 13 10](https://user-images.githubusercontent.com/44546283/90653293-f5253d00-e279-11ea-97a4-3137d499e8f8.png)

위 그림과 같은 방식으로 움직일 요소를 Key에 저장한 후 들어갈 위치를 하나씩 찾으면서 정렬을 진행합니다.    

**다음은 삽입정렬의 Python Code 입니다.**
```
def insertionSort(arr) :
    for i in range(1, len(arr)) :
        j = i - 1 
        key = array[i]
        while arr[j] > key and j >=0 :
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr
```



> 참고페이지    
https://reakwon.tistory.com/37   
https://gmlwjd9405.github.io/2018/05/06/algorithm-bubble-sort.html   
