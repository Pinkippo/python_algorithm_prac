#프로그래머스_모의고사
def solution(answers):
    list1 = [1,2,3,4,5]
    list2 = [2,1,2,3,2,4,2,5]
    list3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0,0,0]
    answer = []
    
    for idx, x in enumerate(answers):
        if x == list1[idx%len(list1)]:
            score[0] += 1
        if x == list2[idx%len(list2)]:
            score[1] += 1
        if x == list3[idx%len(list3)]:
            score[2] += 1
            
    for idx, x in enumerate(score):
        if x == max(score):
            answer.append(idx+1)
    return answer