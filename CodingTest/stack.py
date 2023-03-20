#파이썬으로 스택 자료구조 구현

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

#전체 시간이 상수시간으로 들어가는 자료구조 생성완료

