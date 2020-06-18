import requests
from bs4 import BeautifulSoup

url = 'https://news.naver.com/main/read.nhn?mode=LS2D&mid=shm&sid1=105&sid2=230&oid=030&aid=0002887934'
# url사이트에 get방식으로 requests를 하면
# return으로 사이트의 html code를 전달
resp = requests.get(url)

if resp.status_code==200:
    resp.headers
else:
    print('잘못된 URL입니다. 다시 입력해 주세요')


soup = BeautifulSoup(resp.text, 'html.parser')
title = soup.find('h3', id='articleTitle')
contents = soup.find('div', id='articleBodyContents')
print(title.text)
print('|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')
print(contents.text.strip())  #strip 여백 제거

