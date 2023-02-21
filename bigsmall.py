def solution(s):
    
    v = list(map(int,s.split(' ')))
    v.sort()
    return '{0} {1}'.format(v[0],v[-1])

print(solution("-1 -2 -3 -4"))