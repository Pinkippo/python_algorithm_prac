list = [9,22,3,7,25,5]

def solution(list):
    
    result = list[0]
    for num in list[1:]:
        if result < num:
            result = num


    return result


def solution2(list):
    result = list[0]
    for i in range(1, len(list)):
        if list[i] > result:
            result = list[i]
    return result


print('=>',solution2(list))