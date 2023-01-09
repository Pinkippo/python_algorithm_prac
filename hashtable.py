#해시 테이블 : 매우 빠른 평균 삽입, 삭제, 탐색 => 연산 제공
#충돌 -> collision / 충돌했을때 -> collision resolution method

# 해시테이블 중요한거 3가지 -> list / Hash function / Colision resolution method


# Division hash func = 해쉬함수로 나머지 이용

# Perfect hash func = key <-> slot = 1대1 -> 비현실적
# universal hash func = Pr(f(x) == f(y)) = 1/m -> 이상적인 해시함수
# c-universal hash func => c/m

# 좋은 해시 => 
# (1) = less collision
# (2) = fast cornpution