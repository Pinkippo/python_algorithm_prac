#6주차

import requests
from bs4 import BeautifulSoup

i = 0

while True:
    i += 1
    res = requests.get(f"https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={i}&sido=&gugun=&store=")
    soup = BeautifulSoup(res.content, 'html.parser', from_encoding='euc-kr') #크롤링시 인코딩 명시하기
    if soup.find('td').string == '등록된 지점이 없습니다.':
        break
    else:
        for line in soup.find_all(class_="noline center_t"):
            print("지역 : " , line.string)
            print("매장 : ", line.next_sibling.next_sibling.string)
            print("현황 : ", line.next_sibling.next_sibling.next_sibling.next_sibling.string)
            print("현황 : ", line.next_sibling.next_sibling.next_sibling.next_sibling.string)
            print("주소 : ", line.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.string)
            print("전화번호 : ", line.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.string)
            print("-" * 50)