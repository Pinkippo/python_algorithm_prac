#이진 탐색 = 탐색 범위를 절반씩 줄여 나가면서 찾는다
#장점 = 빠르다 / 실제로 쓰인다
#단점 = 정렬이 되어 있어야 한다. / 만들기 어렵다 

# 핵심 로직
# 중간 인덱스 값을 구해서 반씩 나눠가며 탐색

arr = [1,2,3,5,6,7,8,9,10,11]

def bisearch(arr,num):

    start = 0
    end = len(arr) -1

    midindex = len(arr) // 2
    indexv = arr[midindex]
    if indexv == num:
        return midindex
    elif indexv < num:
        start = midindex +1
    elif indexv > num:
        end = midindex -1


    return -1