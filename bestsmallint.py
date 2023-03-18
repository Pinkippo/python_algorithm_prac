def solution(arr):
    small = arr[0]
    small_index = 0
    for i, v in enumerate(arr):
        if v < small:
            small = v
            small_index = i
    arr.pop(small_index)
    if len(arr) == 0:
        return [-1]
    else:
        return arr