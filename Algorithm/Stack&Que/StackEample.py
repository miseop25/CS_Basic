stack = [None]*10
top = 0

def stackPush(data) :
    global top
    if top < 10 :
        stack[top] = data
        top += 1
        return True
    return False

def stackPop() :
    global top
    if top > 0 :
        top -= 1
        result = stack[top] 
        stack[top] = None
        return result
    return None


while True :
    print("Stack으로 어떤 작업을 할 것인지 선택하세요")
    print("1. Push, 2. Pop, 3. stack 보기, 4. 종료")
    cmd = input().rstrip()
    if cmd == "1" :
        print("적재할 숫자를 입력해 주세요")
        data = input().rstrip()
        result = stackPush(data)
        if result :
            print(data, " 가 정상적으로 입력되었습니다.")
        else :
            print("스택이 가득 찼습니다.")
    elif cmd == "2" :
        result = stackPop()
        if result != None :
            print("삭제한 데이터는 ", result, " 입니다.")
        else :
            print("삭제할 데이터가 없습니다.")
    elif cmd == "3" :
        print(stack)
    elif cmd == "4" :
        break
    else :
        print("1,2,3,4 중에 하나만 입력해 주세요!!")
