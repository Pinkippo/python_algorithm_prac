#7주차 커피빈

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"]) #옵션

wd = webdriver.Chrome(options=options)  #셀레니움 크롭 연결
wd.get('https://www.coffeebeankorea.com/store/store.asp')        #크롬 연결
wd.execute_script("storePop2(333)")                              #자바 스크립트 실행
time.sleep(2)           #연결 대기

soup = BeautifulSoup(wd.page_source, 'html.parser')              #뷰티풀 soup으로 크롤링
wd.quit()

selector = '#matizCoverLayer0Content > div > div > div.store_txt' #개발자모드에서 우클릭 copy -> selector 한 값
store_txt = soup.select_one(selector) # 그 값을 beatiful soup의 selector로 찾기
print(store_txt.h2.string) #지점 찾아오기
for store in store_txt.select('table tr'):
    print(f"{store.th.string}: {store.td.get_text()}") # 정보 받아오기



