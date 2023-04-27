
# n명의 사람이 끝말잇기를 할때다
# 집합 리스트에 추가하며 숫자가 늘지 않았을때의 숫자를 확인

def solution(n, words):
    for i in range(1, len(words)):
        if words[i][0] != words[i-1][-1] or words[i] in words[:i] :
            return [(i%n)+1, (i//n)+1]
    else:
        return [0,0]

print(solution(2,["hello", "one", "even", "never", "now", "world", "draw"]))