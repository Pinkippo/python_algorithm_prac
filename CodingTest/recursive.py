#재귀 = 자기 자신을 호출 하는 것 
#재귀 함수 = 자기 자신을 호출하는 함수 -> 끝나는 조건(탈출조건)이 꼭 필요함

arr = [8,3,2,9,11,22,55,66,100]

#pop() 
#상태가 변한것을 다시 호출 하는것이 재귀의 기본


def sum(arr, accu): #재귀 1번
    if (len(arr) == 0): return accu
    last = arr.pop()
    xxx = last
    
    return sum(arr, accu + xxx)

def sum2(arr, accu): #재귀 구조 간소화 2번
    if(len(arr)== 0): return accu
    return sum(arr, accu + arr.pop())
    

print(sum2(arr,0))