import requests
from bs4 import BeautifulSoup

import movie.persistence.MongoDAO as DAO

mDao = DAO.MongoDAO()

cnt = 0
page = 1
compare_writer = ''

for page in range(1, 6):
    url = 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=169647&type=after&onlyActualPointYn=N&onlySpoilerPointYn=N&order=newest&page={}'.format(
        page)
    resp = requests.get(url)

    if resp.status_code != 200:
        print('Wrong URL')

    soup = BeautifulSoup(resp.text, 'html.parser')
    reply_list = soup.select('div.score_result li ')

    for i, reply in enumerate(reply_list):
        cnt += 1
        previous_writer = reply.select('div.score_reple a > span')[0].text.strip()
        content = reply.select('div.score_reple > p > span')[0].text.strip()
        cut_index = previous_writer.find('(')
        score = reply.select('div.star_score > em')[0].text.strip()
        reg_date = reply.select('div.score_reple em')[1].text.strip()[11:]

        if cut_index > 0:
            writer = previous_writer[:cut_index]
        else:
            writer = previous_writer

        print('■■■■■■■■ 게시글 {} ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■'.format(cnt))
        print('게시글 ', cnt)
        print('작성자', writer)
        print('내용', content)
        print('평점', score)
        print('작성일자', reg_date)

        data = {'content': content, 'writer': writer, 'score': score, 'reg_date': reg_date}
        # mDao.mongo_write(data)

        page += 1
print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
print('수집한 영화댓글은 총{}건입니다.'.format(cnt))










