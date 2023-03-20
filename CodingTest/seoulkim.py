def solution(seoul):
    for i, v in enumerate(seoul):
        if v == "Kim":
            index = i
            break
    return ("김서방은 {}에 있다".format(index))
