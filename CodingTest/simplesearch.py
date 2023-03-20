#단순 탐색 = 앞에서부터 하나하나 찾는다
#장점 = 만들기 쉽다 / 정렬이 안되어 있어도 된다
#단점 = 느리다 => 0(n)
#대안 = 이진탐색(Binary search) => 0(log n)

arr =[1,2,3,4,5,6,8,9,10,11]

#입력받은 숫자가 몇번째 인덱스에 있는지 찾는 func

def search(arr, num):
    for i in range(0,len(arr)):
        if(arr[i] == num):
            return i
        return -1

print(search(arr,int(input())))