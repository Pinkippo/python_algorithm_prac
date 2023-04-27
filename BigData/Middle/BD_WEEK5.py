import requests #리퀘스트 입포트
from bs4 import BeautifulSoup #뷰티풀숩 임포트

res = requests.get("https://blog.replit.com/") #HTTP 객체 받기
if res.status_code == 200: #만약 연결이 잘 되었으면
    soup = BeautifulSoup(res.content,'html.parser') #스크랩핑
    for tag in soup.find_all(class_='post-title'): #FOR LOOP -> 기사 제목
        print('\033[1m' + tag.a.string.strip()) # 제목 표시
        print(tag.parent.h3.string.strip()) #날짜 표시
        print("---------------------------------------------------")