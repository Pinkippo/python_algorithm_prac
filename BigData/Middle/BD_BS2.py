import requests
from bs4 import BeautifulSoup

res = requests.get("https://library.gabia.com/") #가비아 스크랩핑 해보기
soup = BeautifulSoup(res.content, 'html.parser')
if res.status_code == 200:
  for tag in soup.find_all(class_="eg-grant-element-0"):
    print(tag.span.string.strip())
    print(tag.parent.next_sibling.next_sibling.string.strip())
    #print(tag.parent.parent.find_all('div')[-1].string.strip()) 다른 방식
    print("-" * 80)
else:
  print("연결 실패")