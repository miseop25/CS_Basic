# First Class Citizen (일급 객채)

함수형 프로그래밍을 공부하다가 처음 듣게 된 말이다. 그리고 굉장히 자주 나온다.  
First Class Citizen은 다음 조건을 만족하는 객체를 의미한다.  

    1. 변수나 상수에 저장 및 할당 할 수 있어야 한다.  
    2. 파라미터(객체의 인자)로 전달 할 수 있어야 한다.
    3. 함수(객체)에서 return 할 수 있어야 한다.  

글로만 보면 이해가 잘 가질 않으니 코드와 함께 보도록 하겠습니다.    
Swift의 함수는 1급객체임으로 Swift 기반으로 작성하였습니다.  


## 1. 변수나 상수에 저장 및 할당 할 수 있어야 한다. 

```
func firstClassCitizen(test: String) -> String {
    print("1")
    return test
} 

let fcc = firstClassCitizen
```

위처럼 상수에 할당 및 저장될 수 있습니다.  

## 2. 파라미터로 전달 할 수 있어야 한다. 
```
func fccTest(test: String) {
    print("2")
}

fccTest(test: fcc("Hello"))
```
1번에서 선언되어 할당 받은 fcc 자체를 인자로 넘길 수 있습니다. 

## 3. 함수(객체)에서 return 할 수 있어야 한다.  
```
func returnFunc() -> String {
    return firstClassCitizen(test: "3")
}
```
반환 자료형만 일치한다면 반환값에 사용할 수도 았습니다.  




## 일급객체를 공부하면서
일급객체라는 용어가 많이 쓰이고 있는것은 프로그래밍의 패러다임이 함수형 프로그래밍이 주로 이루고 있다고 생각된다.  
아직까지도 함수형 프로그래밍을 100% 알고 사용할 수 있는것은 아니지만 일급객체를 공부하면서 보다 성장한것 같다는 생각이 든다.  


> 내용 출처  
https://medium.com/@lazysoul/functional-programming-에서-1급-객체란-ba1aeb048059   
https://jcsoohwancho.github.io/2019-10-18-1급-객체(first-class-object)이란/


