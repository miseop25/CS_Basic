# DFS and BFS

그래프에서 탐색을 하는 알고리즘 중에 가장 기본적이면서도 대표적인 DFS와 BFS에 대해서 알아보도록 하겠습니다.    
DFS, BFS는 다양한 알고리즘의 기반이 되기도 하기 때문에 잘 알아두는 것이 좋습니다. 

## DFS(Deep First Search) 
우리말로는 깊이 우선 탐색인 DFS는 말 그대로 깊이있는 것 부터 우선적으로 탐색을 진행하는 알고리즘입니다.    

![스크린샷 2020-09-17 오전 12 36 46](https://user-images.githubusercontent.com/44546283/93359909-116ac880-f87e-11ea-80f7-a69a7a34a9fe.png)   

위 그래프에서 1번 정점에서부터 깊이 우선 탐색을 진행한다면 다음과 같이 나옵니다.  

    DFS 탐색 결과 : 1 -> 2 -> 4 -> 5 -> 3 -> 6 -> 7

깊이 우선 탐색은 통상적으로 Stack을 통해서 구현됩니다.   
하지만 Stack을 사용하지 않고서도 재귀함수를 통해서 구현 할 수 있습니다.    
이는 컴퓨터는 구조적으로 항상 Stack의 원리를 사용하기 때문입니다.   
본 포스팅에서는 Stack을 통한 구현을 중점적으로 살펴보도록 하겠습니다.  

### DFS의 구현

DFS 는 다음과 같은 알고리즘을 통해서 간단하게 구현할 수 있습니다.    

    1. Stack에 탐색할 노드를 삽입한 후 방문했다는 표시를 합니다. 
    2. Stack의 최상단 노드와 연결된 인접 노드를 확인합니다. 
    3. 방문하지 않은 노드가 있다면 그 노드를 Stack에 삽입한 후 방문했다는 표시를 합니다. 
        만약 모든 인접노드를 방문했었다면 Stack에서 최상단 노드를 제거합니다. 
    4. Stack이 빌때까지 2~3번 작업을 반복합니다.   

보다 쉬운 이해를 위해서 그림으로 표현해 보면 다음과 같습니다.   

![스크린샷 2020-09-17 오전 1 15 06](https://user-images.githubusercontent.com/44546283/93364260-4b8a9900-f883-11ea-9448-afc7b397368a.png)
![스크린샷 2020-09-17 오전 1 15 13](https://user-images.githubusercontent.com/44546283/93364264-4cbbc600-f883-11ea-8a95-bd6a09829d27.png)


깊이 우선 탬색의 원리와 방법을 이했다면 이를 그대로 코드로 작성하면 됩니다.  
다음은 Python 을 통해 구현한 Stack 을 사용한 깊이 우선 탐색 코드입니다.   

```
    def DFS_Use_Stack(self, target) :
        stack = []
        checkRoot = [0 for _ in range(self.N+1)]
        result = []
        stack.append(target.data) 
        checkRoot[target.data] = 1
        result.append(target.data)

        while stack :
            target.child = sorted(target.child)
            flag = True
            for i in target.child :
                if checkRoot[i] == 0 :
                    target = self.nodeDict[i]
                    stack.append(target.data)
                    result.append(i)
                    checkRoot[i] = 1
                    flag = False
                    break
            if flag :
                target = self.nodeDict[stack.pop()]
        return result
```

Stack 을 사용해서 DFS를 구현하기는 했지만 프로그래밍 대회나 코딩테스트 같은 곳에서는 재귀함수를 통하여    
DFS를 구현하는 편입니다. 다음은 재귀함수를 통한 DFS의 Python 코드입니다.   

```
    def DFS(self, target) :
        self.reslutDFS.append(str(target.data))
        self.checkDFS[target.data] = 1
        target.child = sorted(target.child)
        for i in target.child :
            if self.checkDFS[i] == 0 :
                self.DFS(self.nodeDict[i])
```


## BFS(Breadth First Search)

우리말로는 너비 우선 탐색이라고도 합니다. 시작점과 가까운 정점부터 탐색을 진행합니다.   
주로 최단길이, 최단 경로, 미로찾기 등을 구하고자 할때 많이 사용되고 있습니다.    

먼저 BFS가 왜 너비 우선 탐색인지 예시를 보면서 살펴보도록 하겠습니다.    
![스크린샷 2020-09-17 오전 12 36 46](https://user-images.githubusercontent.com/44546283/93359909-116ac880-f87e-11ea-80f7-a69a7a34a9fe.png)   

위 그래프에서 1번 노드부터 BFS 탐색을 실시했다고 한다면 다음과 같은 결과가 나옵니다.

    BFS 탐색 결과 : 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7



### BFS의 구현   

BFS는 Queue(큐) 자료구조를 통해서 구현할 수 있으며 다음과 같은 간단한 알고리즘을 통해서 구현할 수 있습니다.    

    1. 시작할 노드를 큐에 삽입한 후 방문체크를 해줍니다.   
    2. 큐에서 노드 하나를 추출합니다.   
    3. 추출된 노드의 인접 노드를 확인한 후 방문하지 않았다면 큐에 추가하고 방문 체크를 해줍니다. 
    4. 큐가 빌때까지 2~3번 과정을 반복합니다.    

보다 쉬운 이해를 위해서 그림으로 과정을 표현하면 다음과 같습니다.    

![스크린샷 2020-09-18 오후 9 43 57](https://user-images.githubusercontent.com/44546283/93598754-1b183b80-f9f8-11ea-8940-dec0f9836133.png)


너비 우선 탐색의 방법을 이해했다면 코드로 그대로 구현하면 됩니다.  

다음은 Python으로 구현한 BFS 코드 예시입니다.

```
    def BFS(self, target) :
        que = deque([])
        que.append(target)
        self.checkBFS[target.data] = 1
        while que :
            n = que.popleft()
            self.reslutBFS.append(str(n.data))
            c = sorted(n.child)
            for i in c :
                if self.checkBFS[i] == 0 :
                    que.append(self.nodeDict[i])
                    self.checkBFS[i] = 1
```

이번 포스팅에서 작성한 코드는 Back Joon 1260번 DFS와 BFS를 풀이에 기반을 두어 작성되었습니다.[문제보기](https://www.acmicpc.net/problem/1260)    

DFS와 BFS를 이해하기에 가장 기본적인 문제이니 공부를 하고 계신분이라면 한번쯤 풀어보시면 좋을 것 같습니다.  

백준 1260번에 대한 전체 코드는 다음 링크에 있습니다. [백준 1260번 코드보기](https://github.com/miseop25/Back_Jun_Code_Study/blob/1d1ec37ada9dc4905d3a6d6ac6e110146f7855ca/back_joon/너비우선탐색_BFS/back_joon_1260_DFSBFS/back_joon_1260_ver1.py)

****


## 정리하면서   

DFS와 BFS에 대해서 단순히 사용하는 방법만 알고 있었을 뿐 알고리즘을 어떻게 작동하는지 모르고 있었다.   
이번 기회에 확실하게 알고가는 것 같아 기분이 좋았고 앞으로도 더 많은 공부를 진행해야겠다.    

>  참고한 자료  
https://yunyoung1819.tistory.com/86   
https://m.blog.naver.com/PostView.nhn?blogId=ndb796&logNo=221230945092&proxyReferer=https:%2F%2Fwww.google.com%2F  



