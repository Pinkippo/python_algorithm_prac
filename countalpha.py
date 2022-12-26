word = "tesdfsafdasdfsdafsadddssssdddddd"

def highFrequencyLettterCount(word): #내가 설계한 함수
    count = []
    for i in word:
        count.append(word.count(i))
    count.sort(reverse=True)
    return count[0]

def high(word): #수업을 들으며 설계한 함수
    map ={}
    for i in word:
        if map.get(i) == None:
            map[i]=1
        else:
            map[i]+=1
    return max(map.values())


print(high(word))