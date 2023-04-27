import requests
from bs4 import BeautifulSoup

res = requests.get("https://finance.naver.com/sise/sise_quant.naver") #네이버 페이지 크롤링 해보기
print(res.encoding) #페이지 인코딩 정보
soup = BeautifulSoup(res.content, 'html.parser', from_encoding='euc-kr') #크롤링시 인코딩 명시하기

tab_python = soup.find('table', class_='type_2')

if res.status_code == 200:
  for tag in tab_python.find_all(class_='no'):
    print("번호 :", tag.string) #번호 
    print("이름 :", tag.next_sibling.next_sibling.string) #이름
    print("가격 :", tag.next_sibling.next_sibling.next_sibling.next_sibling.string) #가격
    print("-" * 80)
else:
  print("연결 실패")