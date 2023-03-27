##연산자의 우선순위와 종류1##
##산술연산자##
p_a = 7;p_b = 3
print("p_a + p_b의 결과값 :", p_a+p_b) #더하기
print("p_a - p_b의 결과값 :", p_a-p_b) #빼기
print("p_a * p_b의 결과값 :", p_a*p_b) #곱하기
print("p_a / p_b의 결과값 :", p_a/p_b) #나누기
print("p_a // p_b의 결과값 :", p_a//p_b) #몫
print("p_a % p_b의 결과값 :", p_a%p_b) #나머지
print("p_a ** p_b의 결과값 :", p_a**p_b) #제곱
##대입연산자##
p_a = 10; print("p_a = 10의 결과값 :", p_a)
p_a=10; p_a += 5; print("p_a += 5의 결과값 :", p_a) #더하고 저장
p_a=10; p_a -= 5; print("p_a -= 5의 결과값 :", p_a) #빼주고 저장
p_a=10; p_a *= 5; print("p_a *= 5의 결과값 :", p_a) #곱해주고 저장
p_a=10; p_a /= 5; print("p_a /= 5의 결과값 :", p_a) #나눠주고 저장
p_a=10; p_a //= 5; print("p_a //= 5의 결과값 :", p_a) #몫 저장
p_a=10; p_a %= 5; print("p_a %= 5의 결과값 :", p_a) #나머지 저장
p_a=10; p_a **= 5; print("p_a **= 5의 결과값 :", p_a) #제곱 저장
##관계연산자##
p_a = 10
p_b = 20
print("p_a==p_b의 결과값 : ", p_a==p_b) #같다
print("p_a!=p_b의 결과값 : ", p_a!=p_b) #다르다
print(" p_a<p_b의 결과값 : ", p_a<p_b) #작다
print(" p_a>p_b의 결과값 : ", p_a>p_b) #크다
print("p_a<=p_b의 결과값 : ", p_a<=p_b) #작거나같다
print("p_a>=p_b의 결과값 : ", p_a>=p_b) #크거나같다
##논리연산자##
p_a=10; p_b=20; 
print("(p_a==p_b)의 결과값 and (p_a<p_b)의 결과값 : ", (p_a==p_b) and (p_a<p_b)) #두개다
print("(p_a==p_b)의 결과값 or (p_a<p_b)의 결과값 : ", (p_a==p_b) or (p_a<p_b)) #하나만
print("not (p_a==p_b)의 결과값 : ", not (p_a==p_b)) #같지 않을때
##비트연산자##
p_a=3; p_b=2
print("(p_a&p_b)의 결과값 : ", (p_a&p_b)) #비트 AND
print("(p_a|p_b)의 결과값 : ", (p_a|p_b)) #비트 OR
print("(p_a^p_b)의 결과값 : ", (p_a^p_b)) #비트 XOR
print("(~p_a)의 결과값 : ", (~p_a)) #비트 NOT
print("(p_a<<p_b)의 결과값 : ", (p_a<<p_b)) #시프트 좌 이동
print("(p_a>>p_b)의 결과값 : ", (p_a>>p_b)) #시프트 우 이동