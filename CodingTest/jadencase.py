#JadenCase란 모든 단어의 첫 문자가 대문자이고, 그 외의 알파벳은 소문자인 문자열입니다.
#단, 첫 문자가 알파벳이 아닐 때에는 이어지는 알파벳은 소문자로 쓰면 됩니다.
#(첫 번째 입출력 예 참고) 문자열 s가 주어졌을 때,
#s를 JadenCase로 바꾼 문자열을 리턴하는 함수, solution을 완성해주세요.

def solution(s):
    title_s = s.title() #제목 형식으로 바꿔주는 메서드
    words = title_s.split(" ")
    for i in range(len(words)):
        if len(words[i]) != 0 and words[i][0].isdigit():
            words[i] = words[i].lower()

    return " ".join(words)
print(solution("3people unFollowed me"))