#정렬 - 버블, 선택, 삽입, 병합, 퀵, 퀵정렬
#재귀를 이용해서 남은 애들을 계속 함수를 태웁니다.

numbers = [40, 35, 20, 60, 75, 44 ,20 ,10 , 5, 3, 222, 100]

def quickSort(array): # 퀵정렬 = 반으로 줄이고 반으로 줄이고 이어 나가면서 정렬을 한다. 
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [number for number in array[1:] if number <= pivot ]
        greater = [number for number in array[1:] if number > pivot ]
        return quickSort(less) + [pivot] + quickSort(greater)


result = quickSort(numbers)
print(result)