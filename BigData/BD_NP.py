import numpy as np

#넘파이를 이용하여 배열 사용
ar1 = np.array([1,2,3,4,5])

#ar2
ar2 = np.array([[1,2,3],[1,2,3]])

#1에서 11까지 2를 증가시키면서 배열 생성 
ar3 = np.arange(1, 11, 2)

#배열 생성 -> X행 X열로 변환 가능
ar4 = np.array([1,2,3,4,5,6]).reshape((3,2))

# X행 X열을 0으로 채워서 형태로 저장
ar5 = np.zeros((2,3))

# X행 X열로 슬라이싱 해주겠다
ar6 = ar5[0:2, 0:2]

# 각 원소마다 값을 더한다
ar8 = ar1 + 10
# = 사칙연산이 모두 가능하다

#넘파이 행렬 곱 연산 == a의 열의 개수와 b의 행의 개수가 같아야하다
ar9 = np.dot(ar2,ar4)
print(ar9)
