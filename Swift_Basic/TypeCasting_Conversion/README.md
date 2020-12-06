# Type Conversion 과 Type Casting

Type Conversion, Casting 모두 우리말로 하면 형변환이다

하지만 Swift 에서는 두개의 개념이 완전히 다르다. 

결론부터 말하자면 Type Conversion은 메모리에 저장된 값은 완전히 다른 값으로 바꿔서 새로운 값을 생성한다. 

Type Casting은 메모리에 저장된 값을 그대로 두고 compiler가 다른 형식으로 처리하도록 지시한다. 


## Type Conversion

    문법 : Type(value) 
    Ex) Int(2.0)

Type Conversion 할 형태 안에 값을 넣어준다. 

성공한다면 변환된 값을 반환 할 것이고 실패할 경우 error 또는 nil 값이 반환된다. 

에러가 되는 경우 : 값을 저장할 경우가 충분하지 않다면 Error 가 발생함( 큰 자료형 -> 작은 자료형으로 갈때 조심)

Nil 이 되는 경우 : 아에 변환이 안될 경우 ( "abc" -> int로 바꾼다면 아에 안되기 때문에 nil 이 리턴)


## Type Casting

Type Casting 에는 두가지 연산자가 있음 

    Is 연산자    
    문법 : Expression is Type   
        Ex) 2 is Int   
    연산의 결과 : 형식이 동일하다면 True가 리턴  
        동일한 상속 계층 오른쪽이 Super 클래스라면 True가 리턴
        나머지 경우에는 False 가 리턴된다. 
 
<!--  -->

    As 연산자 
    문법 : Expression as Type. 
    *** 새로운 인스턴스가 리턴 되는 것이 아니라 이미 존재하는 인스턴스에서 
    오른쪽 타입에서만 접근할 수 있는 임시 인스턴스가 생성된다. 

크게 2가지 형태를 가지고 있다. 

1. Compile Time Cast   
	그냥 as 만 사용하는 경우이다.   
	서로 호환되는 casting을 진행하는 것을 Bridging 이라고 함, 주로 이때 사용한다.    
	캐스팅에 실패할 경우 컴파일 에러가 발생한다.   


2. Runtime Cast (as?, as!)    
	결과를 알 수 없다. -> 실제 코드가 동작되었을때 작동하기 때문에    
As? : 성공하면 해당하는 인스턴스를 리턴 실패하면 nil을 리턴   
As! : 강제 추출 연산, 실패하면 크러시가 발생한다. (아에 앱이 죽어버림)

다운 캐스팅을 진행할 때에는 타입캐스팅(컨디션털)이랑 옵셔널 바인딩을 함께 사용하는 것이 보다 효율적이다.(실패할 가능성이 있기 때문!)   
업캐스팅이 진행되면 업캐스팅 된 프로퍼티와 매소드만 사용이 가능하다.

다운캐스팅과 업케스팅에 관련해서는 다른 포스팅으로 진행하도록 하겠습니다.  

> 참조   
https://docs.swift.org/swift-book/LanguageGuide/TypeCasting.html   






















