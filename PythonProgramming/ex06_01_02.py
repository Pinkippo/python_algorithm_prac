print("=" * 45)
print("■ 컴시과 3학년 A반 9주차 한승완 실습 2")
print("■ 정수, 실수, 문자열을 입력받아")
print("■ 출력 포맷 형식으로 전체 자릿수 지정 프로그램")
print("-" * 45)
jungsu = int(input("정수를 입력하세요! => "))
silsu = float(input("\n실수를 입력하세요! => "))
munja = input("\n문자를 입력하세요! => ")
print("-" * 45)
print(">> 정수 데이터 타입 출력형식")
print("|%d|" % jungsu)
print("|%5d|" % jungsu)
print("|%-5d|" % jungsu)
print("|%+5d|" % jungsu)
print("|%05d|" % jungsu)
print("-" * 45)
print(">> 실수 데이터 타입 출력형식")
print("|%f|" % silsu)
print("|%10.1f|" % silsu)
print("|%10.3f|" % silsu)
print("|%-10.3f|" % silsu)
print("|%+10.3f|" % silsu)
print("|%010.3f|" % silsu)
print("-" * 45)
print(">> 문자열 데이터 타입 출력형식")
print("|%s|" % munja)
print("|%8s|" % munja)
print("|%-8s|" % munja)
print("=" * 45)