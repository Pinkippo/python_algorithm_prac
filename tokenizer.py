#스트링토크나이저 만들기
#토큰이란 프로그램에서 다루는 최소 단위
#Tokenizer = 가장 작은 단위로 나누어 주는 일을 하는 것
#왜 나누느냐? = 나눠서 처리 해야 하기 때문
#StringTokenizer = 스트링을 나누어 주는 로직
string = "12+2*(3-4)"
def StringTokenizer(string, deli):
    result = []
    accu = ""
    for char in string:
        if char in deli:
            if(accu != ""): result.append(accu) 
            result.append(char)
            accu=""
        else:
            accu += char
    return result

print(StringTokenizer(string,"+-*/(){}[]"))