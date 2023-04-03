# --------------------------- #
# 기본형 데이터 타입 예제 소스 #
# --------------------------- #
a = "Python Programming"
print('a = "Python Programming" 일때 a[:2] : ', a[:2])
print('a = "Python Programming" 일때 a[:3] : ', a[3:])
print('a = "Python Programming" 일때 a[:5] : ', a[:5])
print('a = "Python Programming" 일때 a[:] : ', a[:])
a = "20330518Monday"
year = a[:4]
print('a="20330518Monday" 일때 a[:4]의 결과: ', year)
month = a[4:6]
print('a="20330518Monday" 일때 a[4:6]의 결과 : ', month)
day = a[6:8]
print('a="20330518Monday" 일때 a[6:8]의 결과 : ', day)
week = a[8:]
print('a="20330518Monday" 일때 a[8:]의 결과 : ', week)
print('a="20330518Monday" 일때 슬라이싱 합쳐서 출력한 결과 : ',
year + "년 " + month + "월 " + day + "일 " + week)
a = "Sprce"
print('a="Sprce" 일때 a[:2]의 결과 : ', a[:2])
print('a="Sprce" 일때 a[3:]의 결과 : ', a[3:])
print("Scpre 오타 수정한 결과 : ", a[:2] + 'a' + a[3:])
a = "Spacezone"
print('a = "Spacezone" 일때 a의 개수 : ', a.count('a'))
a = "I can do it"
print('a = "I can do it" 일때 a의 인덱스 번호 : ', a.find('a'))
print('a = "I can do it" 일때 do의 인덱스 번호 : ', a.find('do'))
print('a = "I can do it" 일때 s의 인덱스 번호 : ', a.find('s'))
a = "Have a good time"
print('a = "Have a good time" 일때 a의 인덱스 번호 : ', a.index('a'))
print('a = "Have a good time" 일때 me의 인덱스 번호:', a.index('me'))
a = " power "
print('a = " power " 일때 양쪽 공백 제거 : ', a.strip())
print('a = " power " 일때 왼쪽 공백 제거 : ', a.lstrip())
print('a = " power " 일때 오른쪽 공백 제거 : ', a.rstrip())
a = "Speed Zone"
print('a = "Speed Zone" 일때 대문자로 바꾼 결과 : ', a.upper())
print('a = "Speed Zone" 일때 소문자로 바꾼 결과 : ', a.lower())
a = " / "
print('a = " / "일때 "/" 삽입하기 : ', a.join('asdf'))
a = " or "
print('a = " or " 일때 "or" 삽입하기 : ', a.join('asdf'))
a = "speed zone"
print('a = "speed zone" 일때 "speed"를 "power"로 대체한 결과 : ',
a.replace("speed", "power"))
a = "One Two Three"
print('a = "One Two Three" 일때 공백을 기준으로 문자열 나눈 결과 : ', a.split())
a = "spring:summer:fall:winter"
print('a = "spring:summer:fall:winter"일때 " : " 기준 문자열 나눈 결과 : ', 
a.split(':'))
