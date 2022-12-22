#버블 정렬
#알고리즘에서 가장 첫번째로 나오는 알고리즘

'''
핵심 로직 : 첫번째꺼랑 두번재꺼랑 비교해서 두번째가 더 작으면
첫번째꺼랑 자리를 바꾼다.
n, n+1
'''

numbers = [50, 7, 3, 2, 9, 10, 2, 4, 11, 40]

#자리 바꾸기
'''
first = numbers[0]
second = numbers[1]

temp = first
first = second
second = temp
'''

def bubble_1(array): #수업 듣기전에 연습해보기 = 단순하게 n, n+1 만 한번씩 훑으면서 지나가도록 설계했음
    if len(array) < 2:
        return array
    else:
        for i in range(1,len(array)):
            if(array[i-1] > array[i]):
                temp = array[i-1]
                array[i-1] = array[i]
                array[i] = temp
        return array

def bubble_2(array): #혼자 해본 버블 정렬 설계 / 중첩 for문 적용
    if len(array) < 2:
        return array
    else:
        for i in range(len(array)):
            for j in range(1,len(array)-i):
                if(array[j-1] > array[j]):
                    temp = array[j-1]
                    array[j-1] = array[j]
                    array[j] = temp
        return array

def bubble_3(array): #수업에서 진행하는 버블 정렬 설계
    if len(array) <2:
        return array
    else:
        for front_index in range(0,len(array)-1):
            for index in range(front_index + 1, len(array)):
                if array[front_index] > array[index]:
                    temp = array[front_index]
                    array[front_index] = array[index]
                    array[index] = temp
        return array


result = bubble_3(numbers)
print(result)