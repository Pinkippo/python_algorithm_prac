
def one(): #1000까지 돌면서 3으로 나눴을때 나머지 x
    result = 0
    i = 1
    for i in range(1,1001):
        if i % 3 == 0:
            result += i
            i += 1
    return result

def two_change(): #for loop 변환
    [print("*"*i) for i in range(1,6) ]
  

def two(): #for loop + for loop 변환
    for i in range(1,6):
        print()
        for j in range(i):
            print('*', end = '')


def is_odd(number): #주어진 수 홀수 짝수 확인
    return number % 2 == 1

def avg_nums(*args): #가변인자 연습
    result = 0
    for i in args:
        result += i
    return result / len(args)

print(avg_nums(1,2,3,4,5,6,50))