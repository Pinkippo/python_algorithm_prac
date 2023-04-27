import requests
from bs4 import BeautifulSoup

res = requests.get("https://webhosting.gabia.com/container/service") #가비아 컨테이너 스크랩핑 해보기
soup = BeautifulSoup(res.content, 'html.parser')
tab_python = soup.find('div', id='_tab1-2')
if res.status_code == 200:
  for tag in tab_python.find_all(class_="brick-plan-prod__name python"):
    print(tag.string)
    print("-" * 80)
else:
  print("연결 실패")