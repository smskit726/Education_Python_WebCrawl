import requests
from bs4 import BeautifulSoup

url = 'https://news.v.daum.net/v/20200615030609070'
resp = requests.get(url)

if resp.status_code==200:
    resp.headers
else:
    print('잘못된 URL입니다. 다시 입력해 주세요')


soup = BeautifulSoup(resp.text, 'html.parser')
title = soup.find('h3', 'tit_view')
contents = soup.find('div', 'news_view')
print(title.text)
print('|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')
print(contents.text.strip())

