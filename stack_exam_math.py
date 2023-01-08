# infix 수식 -> postfix 수식
# (1) = 괄호 치기
# (2) = 연산자의 오른쪽 괄호 다음으로 연산자 이동
# (3) = 괄호 지우기

#입력 -> infix 수식
#출력 -> postfix 수식

class stack:
    def __init__(self): # 매개변수는 언제든지 추가할 수 있다
        self.items = [] 

    def push(self, val):
        self.items.append(val) #수행시간 - 상수시간
    
    def pop(self):
        try:                               #파이썬 예외 처리
            return self.items.pop() #수행시간 - 상수시간
        except IndexError:                   #처리해줄 익셉션 종류
            print("스택이 비었습니다.")
    
    def top(self):
        try:
            return self.items[-1] #수행시간 - 상수시간
        except:
            print("스택이 비었습니다")
        
    def __len__(self): #스페셜 메소드 -> 이름을 다르게
        return len(self.items) #수행시간 - 상수시간

x = list(input().split())
y = []
z = stack()

for i in range(0,len(x)):
    if x[i].isdigit():
        y.append(x[i])
    else:
        if (x[i] == '*' or '/') and (stack.top(z) == '+' or '-'): 
            if stack.__len__(z) ==0: stack.push(z,x[i])
            else:  
                stack.push(z,x[i])
                y.append(stack.pop(z))
        else:
            stack.push(z,x[i])
            
while(stack.__len__(z) != 0):
    y.append(stack.pop(z))

print(y)
