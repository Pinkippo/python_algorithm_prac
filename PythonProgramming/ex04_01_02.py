## 한승완_컴퓨터시스템과_3학년_201945004_파이선 4장과제물 (1)
print("-" * 50) #50개 반환(2)
print("##한승완_컴퓨터시스템과_3학년_201945004_파이선 4장과제물##") #(3)
print("=" * 50) #50개 반환 (4)
a = 9 #(5)
b = 2 #(6)
print("a = 9, a= 2 일때 a//b의 결과값 : ", a // b) #(7)
print("a = 9, a= 2 일때 -a//b의 결과값 : ", -a // b) 
print("My name's Han Seung Wan") #(8)
c = "My name is Han Seung Wan"
print('c = "My name is Han Seung Wan" 일때 s의 개수 : ', c.count("s")) #(10)
d = "Bythom Programing" 
print('d = "Bythom Programing" 일때 수정 결과 : ',
"P" + d[1:5] + "n " + d[7:14] + "m" + d[14:]) #(10)
e = "inha"
print('e = "inha" 일때 inha를 대문자로 변환 결과 : ', e.upper()) #(11)
f = "I like INHA"
print('f = "I like INHA" 일때 like를 love로 바꾼 결과 : ', f.replace("like", "love")) #(12)
g = "20250401Monday" #(13)
year = g[:4]
month = g[4:6]
day = g[6:8]
week = g[8:]
print('g = "20250401Monday" 일때 : ', year + "년 " + month + "월 " + day + "일 " + week) #(14)