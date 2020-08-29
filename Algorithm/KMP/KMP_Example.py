def simpleCompare(original, search) :
    for i in range(len(original)- len(search)) :
        flag = True
        for j in range(len(search)) :
            if original[i+j] != search[j] :
                flag = False
                break
        if flag :
            return i
    return -1

def makeFailureFunctionTable(word) :
    # j = 0, i = 1 부터 비교를 진행해 줍니다. ->KMP 알고리즘은 2글자 이상의 문자열에서만 적용됩니다.
    j = 0 
    table = [0]*len(word)   # 반환할 Table을 생성해줍니다.
    for i in range(1, len(word)) :
        while j > 0 and word[i] != word[j] :
            j = table[j-1] 
        if word[j] == word[i] :
            j += 1
            table[i] = j
    return table

def KMP(original, search) :
    table = makeFailureFunctionTable(search)
    j = 0
    for i in range(len(original)) :
        while j > 0 and search[j] != original[i] :
            j = table[j-1]
        if search[j] == original[i] :
            if j == len(search) -1 :
                print(i - len(search) + 1, "번째 인덱스에서부터 일치합니다.")
                j = table[j-1]
            j += 1

print(simpleCompare("abcdef", "cd"))
print(KMP("ababacabacaabacaaba", "abacaaba"))
