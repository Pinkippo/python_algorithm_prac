# 괄호가 바르게 짝지어졌다는 것은 '(' 문자로 열렸으면 반드시 짝지어서 ')' 문자로 닫혀야 한다는 뜻입니다.

# "()()" 또는 "(())()" 는 올바른 괄호입니다.
# ")()(" 또는 "(()(" 는 올바르지 않은 괄호입니다.
# '(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때, 문자열 s가 올바른 괄호이면 true를 return 하고
# 올바르지 않은 괄호이면 false를 return 하는 solution 함수를 완성해 주세요.


#시간 초과 해결 완료

def solution(s): 
    test = 0
    for word in s: #문자열에서 하나씩 읽는다
        if test < 0: #만약 괄호 순서가 맞지 않으면 False
            return False
        
        if word == "(": #열린괄호는 +1
            test += 1 
        if word == ")": #닫힌 괄호는 -1
            test -= 1
        
    return test == 0 #괄호 개수가 맞으면 True 

print(solution("()()()"))