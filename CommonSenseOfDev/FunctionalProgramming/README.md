# Functional Programming(함수형 프로그래밍)

## Functional Programming을 공부하기에 앞서

함수형프로그래밍을 공부하기 전에는 그저 함수를 이용한 프로그래밍 정도라고만 생각했다.  
그저 자주 사용하는 기능들을 함수로 만들어 사용하는 정도로 말이다.  
일부는 맞을수도 있지만 함수형프로그래밍은 내가 이전에 해왔던 함수를 사용하면서 프로그래밍하기는 아닌것 같다.  
함수형 프로그래밍을 이해하기 위해서 그 이전에 해오던 것이 어떤건지부터 살펴봐야겠다.  
  

프로그래밍 패러다임을 찾아보니 크게 함수형과 명령형 프로그래밍으로 나뉘는것 같다.  
먼저 함수형과 명령형 프로그래밍의 차이점을 살펴보자! 

## 명령형 프로그래밍 vs 선언형 프로그래밍  

두 프로그래밍의 차이를 한문장으로 말하면 다음과 같을것 같습니다.  

    어떻게(How)프로그래밍 할것인가? 와 무엇(What)을 프로그래밍 할 것인가?

즉 다음과 같이 표련을 할 수 있을것 같습니다. 

    명령형 프로그래밍 : 알고리즘을 명시하지만 목적을 명시하진 않습니다.    
    - 객체지향 프로그래밍, 절차지향 프로그래밍

     선언형 프로그랴밍 : 목적을 명시하지만 알고리즘을 설명하진 않습니다.   
    - 함수형 프로그래밍


### 명령형 프로그래밍은 어떻게(How) 프로그래밍 할지 고민하는것!  

내가 지금까지 해오던 대부분의 프로그래밍은 명령형 프로그래밍이었다. 대부분 문제를 어떻게 해결해야 하는지를 고민했다.  
주로 프로그래밍에서 변수를 선언하고 상태 변화에 따라서 프로그래밍 했었다.  
즉, 명령형 프로그래밍은 어떻게 상태를 바꾸고, 문제를 해결해 나아가는 것이다.

### 선언형 프로그래밍은 무엇(What)을  프로그래밍할지 정하는것!

프로그램이 어떻게 만들어지는지를 하기보다는 무엇을 하는지에 초점을 둔 프로그래밍을 말한다.  
가령 어플을 개발한다고 할때, 버튼, 이미지 표현, 텍스트 표시 등 우리가 도트를 찍어가며 프로그래밍 하는 것이 아니라  
목적에 맞는 함수들을 호출하여 사용한다. (이게 정확히 맞는 비유인지를 잘 모르겠다... )

보다 쉬운 이해를 위해 다음 예시를 참조하면 좋을것 같다.  

    명령형   
    - 죽전성당앞사거리에서 "용구대로" 방면으로 좌회전
    - 492m 후 농수산물센터 사거리에서 '서울, 수서. 농수산물유통센터' 방면으로 좌회전   
    - 940m 후 경기고속삼거리에서 'KINSTOWER, 성남 아트센터' 방면으로 진입   
    - 1.2km 후 '안양, 분당구청, 분당제생병원' 방면 오른쪽 방향   
    - 137m 후 '정자3동, KT본사, 분당노인종합복지관' 방면으로 우회전   
    - 59m 후 정자일로1사거리에서 '금곡동'방면으로 우회전  
    - 12m 후 우회전
    - NAVER 그린팩토리

    함수형   
    - 출발 : 죽전성당  
    - 도착 : NAVER 그린팩토리

이처럼 명령형은 어떻게 목적지까지 도착할지를 설명하고 있습니다. 반면 선언형은 무엇을 할 갓인지 정의합니다.   

## 함수형 프로그래밍

간략하게 함수형 프로그래밍의 뚜렷한 특징을 살펴보면 다음과 같은 것들이 있습니다.

- Input과 Output이 있다.   
- 외부 환경으로부터 철저히 독립적입니다.  
    해당 함수 내부에서 외부의 변수나 상태를 변경시키지 않고 주어진 작업만 실행합니다.
- 같은 Input에 대해서는 언제나 동일한 Output을 출력해 냅니다.  
    외부 환경으로부터 독립적이니 시간, 다른 변수에 영향을 받지 않고 오직 주어진 입력값에만 반응합니다.

이러한 특징들 덕분에 아주 강력한 장점이 생겨납니다!!      

    부작용(Side Effect)에 대한 문제로부터 보다 자유롭다.

함수형 프로그래밍에서 해당 함수가 동작하면서 외부의 상태를 변경시키지 않고 들어온 입력을 복사해서 사용하기 때문에  
스레드, 프로세스간에 충돌등을 방지 할 수 있기 때문입니다.  




ps. 아직 함수형 프로그래밍을 직접 해보지 않아 정확히 어떠한 방식으로 작동되는지는 더 공부후 공유하도록 하겠습니다. ㅜㅜ


> 참고 페이지  
> - https://velog.io/@kyusung/함수형-프로그래밍-요약   
> - https://medium.com/@hongseongho/선언형-프로그래밍-알아보기-1d8247342f17
> - https://ko.wikipedia.org/wiki/선언형_프로그래밍
> - https://www.youtube.com/watch?v=jVG5jvOzu9Y




        


