# 이분탐색 (Binary Search)

이번 포스팅에서는 이분탐색에 대하여 알아보고자 합니다. 이분탐색은 특정 값을 찾기위한 알고리즘 중 하나입니다.    
이분탐색의 다음 문장으로 표현할 수 있습니다.   

    이분탐섹
    데이터가 정렬되어 있는 상황에서 특정 데이터를 찾기위해 범위를 절반씩 줄여가며 탐색하는 방법

데이터가 정렬되어 있기 때문에 탐색하고자 하는 데이터가 어디에 있을지 추측할 수 있기 때문에  
범위를 절반씩 줄여나아가면서 탐색할 수 있습니다. 

## 이분탐색의 구현   

이분탐색의 구현은 굉장히 간단합니다. 먼저 어떤 식으로 알고리즘이 진행되는지 한번 살퍄보도록 하겠습니다.    

이분탐색 알고리즘 (a : 정렬되어 있는 배열, target : 내가 찾고자 하는 값)

1. Left, Right, Mid 세개의 변수가를 다음과 같이 초기화 시켜줍니다.       
    Left = 0    
    Rifgt = a 의 길이 - 1 (마지막 인덱스 값을 가리킵니다.)   
    Mid = (Left + Right) / 2     

2. a[Mid] 값과 target 값을 비교합니다.   
    - a[Mid] == target -------> 값을 찾았습니다. 해당 Mid 값을 반환합니다.
    - a[Mid] > target --------> Right = Mid - 1 
    - a[Mid] < target --------> Left = Mid - 1   
    
    비교한 후 값이 크거나 작을때 Mid 값에서 1을 더하거나 빼는 과정을 진행하게 됩니다.   
    그 이유는 어차피 값이 크거나 작기 때문에 Mid 값은 포함되지 않기 때문입니다.   

3. Mid 값을 새롭게 Update 합니다.   
    Mid = (Left + Right) / 2   

4. Left > Right 가 참이 될때까지 2~3번 과정을 반복해 줍니다.  

이러한 과정을 그대로 코드로 작성해주면 이분탐색을 진행할 수 있습니다.    

다음은 Python으로 작성한 이분탐색의 예시 코드 입니다.  

```
def binarySearch(array, target) :
    left = 0
    right = len(array) - 1
    mid = (left + right)//2

    while left < right :
        if array[mid] == target :
            return mid
        elif array[mid] > target :
            right = mid - 1
        else :
            left = mid + 1
        mid = (left + right)//2

    if array[mid] == target :
        return mid
    else :
        return -1
```



## 정리하면서   

이분탐색 알고리즘을 수업때 잠깐 배우고 계속 머릿속으로만 계산하면서 사용해 왔었다.   
그러다보니 위에 써놓은 알고리즘 2번과정에서 실수가 계속 되었었다. 이렇게 정리하면서 한번 더 되새길 수 있어 기쁘다.   
아무리 쉽고 자주 쓰이는 알고리즘, 지식이라도 자만하지 않고 계속 공부해야겠다.   

> 참고한 자료   
https://wootool.tistory.com/62   
http://blog.naver.com/PostView.nhn?blogId=ndb796&logNo=221275413971&parentCategoryNo=&categoryNo=128&viewDate=&isShowPopularPosts=false&from=postView   

