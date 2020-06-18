import requests
from bs4 import BeautifulSoup

# 제목
# 내용
# 작성일자
# 작성자

import requests
from bs4 import BeautifulSoup

cnt = 0
list_url = 'http://news.sarangbang.com/bbs.html?tab=story&p=2'
resp = requests.get(list_url)

if resp.status_code != 200:
    print('WARNING : 잘못된 URL 접근!!')

soup = BeautifulSoup(resp.text,'html.parser')
board_list = soup.select('tbody#bbsResult > tr > td > a')
#print(board_list)

for i, href in enumerate(board_list):
    #print(i, href)
    if(i%2==0):
        cnt += 1
        # 1건의 게시글의 제목, 내용, 작성자, 작성일자 수집하는 코드
        url = 'http://news.sarangbang.com'+ href['href'] # href['href'] 만 작성 시 주소 앞부분을 잘라버림

        resp = requests.get(url)
        soup = BeautifulSoup(resp.text, 'html.parser')

        if resp.status_code != 200:
            print('WARNING : 잘못된 URL 접근')

        title = soup.select('h3.tit_view')[0].text.strip()
        writer = soup.select('a.name_more')[0].text.strip()
        reg_dt = soup.select('span.tit_cat')[1].text.strip()
        contents = soup.select('div.bbs_view p')

        print('TITLE ▶▶▶▶▶▶▶', title)
        print('WRITER ▶▶▶▶▶▶▶', writer)
        print('REGDATE ▶▶▶▶▶▶▶', reg_dt)

        content = ''
        for i in contents:
            content += i.text.strip()
        print('CONTENT ▶▶▶▶▶▶▶', content)

print('사랑방 부동산에서 {}건의 게시글을 수집하였습니다.'.format(cnt))