#프그래머스_최소직사각형

def solution(sizes):
    big = 0
    small = 0
    for i in sizes:
        if i[0] >= i[1]:
            if i[0] > big:
                big = i[0]
            if i[1] > small:
                small = i[1]
        else:
            if i[1] > big:
                big =i[1]
            if i[0] > small:
                small = i[0]
    answer = big * small
    return answer