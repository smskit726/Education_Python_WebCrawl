import requests
from bs4 import BeautifulSoup

import requests
from bs4 import BeautifulSoup

cnt = 0
for page in range(1,6):
    list_url = 'http://news.sarangbang.com/bbs.html?tab=story&p={}'.format(page)
    resp = requests.get(list_url)

    if resp.status_code != 200:
        print('WARNING : 잘못된 URL 접근!!')

    soup = BeautifulSoup(resp.text,'html.parser')
    board_list = soup.select('tbody#bbsResult > tr > td > a:not(.name_more)')  # 작성자는 빼고 긁어온다

    for i, href in enumerate(board_list):

        cnt += 1
        url = 'http://news.sarangbang.com'+ href['href'] # href['href'] 만 작성 시 주소 앞부분을 잘라버림

        resp = requests.get(url)
        soup = BeautifulSoup(resp.text, 'html.parser')

        if resp.status_code != 200:
            print('WARNING : 잘못된 URL 접근')

        title = soup.select('h3.tit_view')[0].text.strip()
        writer = soup.select('a.name_more')[0].text.strip()
        reg_dt = soup.select('span.tit_cat')[1].text.strip()
        contents = soup.select('div.bbs_view p')

        content = ''
        for i in contents:
            content += i.text.strip()

        print('TITLE ▶▶▶▶▶▶▶', title)
        print('WRITER ▶▶▶▶▶▶▶', writer)
        print('REGDATE ▶▶▶▶▶▶▶', reg_dt)
        print('CONTENT ▶▶▶▶▶▶▶', content)
        print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
print('사랑방 부동산에서 {}건의 게시글을 수집하였습니다.'.format(cnt))
