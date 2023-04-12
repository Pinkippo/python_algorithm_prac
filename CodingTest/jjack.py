# 문제 설명
# 짝지어 제거하기는, 알파벳 소문자로 이루어진 문자열을 가지고 시작합니다.
# 먼저 문자열에서 같은 알파벳이 2개 붙어 있는 짝을 찾습니다.
# 그다음, 그 둘을 제거한 뒤, 앞뒤로 문자열을 이어 붙입니다.
# 이 과정을 반복해서 문자열을 모두 제거한다면 짝지어 제거하기가 종료됩니다.
# 문자열 S가 주어졌을 때, 짝지어 제거하기를 성공적으로 수행할 수 있는지 반환하는 함수를 완성해 주세요.
# 성공적으로 수행할 수 있으면 1을, 아닐 경우 0을 리턴해주면 됩니다.

def solution(s): #효율성 때문에 스택 이용
    stack = []
    for word in s:
        if len(stack) == 0: stack.append(word)
        elif stack[-1] == word : stack.pop()
        else: stack.append(word)
    if len(stack) == 0: return 1
    else: return 0 


print(solution('ddaaaa'))