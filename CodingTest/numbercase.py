# Finn은 요즘 수학공부에 빠져 있습니다. 
# 수학 공부를 하던 Finn은 자연수 n을 연속한 자연수들로 표현 하는 방법이 여러개라는 사실을 알게 되었습니다.
# 예를들어 15는 다음과 같이 4가지로 표현 할 수 있습니다.

# 1 + 2 + 3 + 4 + 5 = 15
# 4 + 5 + 6 = 15
# 7 + 8 = 15
# 15 = 15

# 자연수 n이 매개변수로 주어질 때, 연속된 자연수들로 n을 표현하는 방법의 수를 return하는
# solution를 완성해주세요.


#생각 동기화 - 이중 for문 사용(완전탐색) -> 값이 동일해질 경우 정답 개수를 늘리고 break
#해당 숫자 -> 위로 하나씩 더해가면서 값이 같아지면 +1 -> 커지면 break


def solution(n):
    answer = 0
    for i in range(1,n+1): #1에서부터 n까지 for 
        sum = 0
        for j in range(i,n+1): #고른 숫자부터 n까지 더한다
            sum += j
            if sum == n: #값이 나올경우 +1 -> break
                answer += 1
                break
            elif sum > n: #같지않고 커지면 -> break
                break

    return answer


print(solution(15))