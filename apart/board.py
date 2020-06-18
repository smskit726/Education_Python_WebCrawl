# 제목
# 내용
# 작성일자
# 작성자

import requests
from bs4 import BeautifulSoup

url = 'http://mnews.sarangbang.com/talk/bbs/free/163894'

resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'html.parser')

if resp.status_code != 200:
    print('WARNING : 잘못된 URL 접근')

title = soup.select('h3.tit_view')[0].text.strip()
writer = soup.select('a.name_more')[0].text.strip()
reg_dt = soup.select('div.poll_date')[0].text.strip()
contents = soup.select('div.article_body p')
# contents = soup.select('div.article_view')


print('TITLE ▶▶▶▶▶▶▶', title)
print('WRITER ▶▶▶▶▶▶▶', writer)
print('REGDATE ▶▶▶▶▶▶▶', reg_dt)
content = ''
for i in contents:
    content += i.text.strip()
print('CONTENT ▶▶▶▶▶▶▶', content)