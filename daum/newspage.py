# 다음에서 뉴스 여러페이지 내에서의 기사와 내용을 수집

import requests
from bs4 import BeautifulSoup

cnt = 0
for i in range(1, 4):
    url = 'https://news.daum.net/breakingnews/digital?page={}'.format(i)
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')

    url_list = soup.select('ul.list_news2.list_allnews a.link_txt')
    for j in url_list:
        cnt += 1
        url = j['href']
        resp = requests.get(url)
        soup = BeautifulSoup(resp.text, 'html.parser')
        title = soup.select('h3.tit_view')
        contents = soup.select('div#harmonyContainer p')

        text = ''
        for k in contents:
            text += k.text
        print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
        print(title[0].text)
        print("=======================================================================================================")
        print(text)

print('▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶')
print('{}건의 뉴스기사를 수집하였습니다.'.format(cnt))
print('▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶')