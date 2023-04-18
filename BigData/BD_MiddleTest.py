import requests
from bs4 import BeautifulSoup

res = requests.get("https://google.com") #request.get 스크래핑
soup = BeautifulSoup(res.content,'html.parser')

soup.title #<title>The Dormouse's story</title>
soup.title.name # 'title'
soup.title.string # 'The Dormouse's story'

soup.find_all('a')
#리스트로 나온다
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]


for link in soup.find_all('a'):
    print(link.get('href'))
# http://example.com/elsie
# http://example.com/lacie
# http://example.com/tillie