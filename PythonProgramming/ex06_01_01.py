## 본인의 체질량지수 (BMI)를 산출하는 프로그램## 
print("=" * 45)
print(" ■ 201945004 컴시과 3학년 A반 한승완 실습 1")
print(" ■ 본인의 체질량지수(BMI)를 산출하는 프로그램")
print("-" * 45)
height = eval(input(" >> 키 입력(m)     : "))
weight = eval(input(" >> 체중 입력(kg)  : "))
result = weight / (height * height)
print("-" * 45)
print(" >> 본인의 BMI     : %.2f " % result)
print("=" * 45)