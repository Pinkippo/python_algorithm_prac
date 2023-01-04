#가장 안좋은 입력에 대한 기본 연산 횟수 측정 = worstcase time.complexity
# => 어떤 입력에 대해서도 w.t.c보다 수행시간이 크지 않다

#알고리즘 수행시간 = 최악의 입력에 대한 기본 연산횟수 정의

x = [5, 6, 7, 3, 1, 5, 7, 11, 33, 55, 3, 2, 1, 30,60]

def am(a):        #2n-1
    c_m = a[0]
    for i in range(0,len(a)):
        if c_m < a[i]:
            c_m = a[i]
    return c_m

print(am(x))

def sum1(b):  #4n+1
    sum = 0
    for i in range(0,len(b)):
        if b[i] % 2 == 0:
            sum += b[i]
    return sum
