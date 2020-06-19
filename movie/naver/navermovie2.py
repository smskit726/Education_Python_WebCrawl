import requests
from bs4 import BeautifulSoup
import movie.persistence.MongoDAO as DAO

mDao = DAO.MongoDAO()

page = 1
cnt = 0
page_cut = 5

while(True):
    url = 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=182835&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page={}'.format(page)
    resp = requests.get(url)

    if resp.status_code != 200:
        print('존재하지않는 URL')

    soup = BeautifulSoup(resp.text, 'html.parser')
    reply_list = soup.select('div.score_result li')

    for i, reply in enumerate(reply_list):
        previous_writer = reply.select('div.score_reple a > span')[0].text.strip()
        cut_index = previous_writer.find('(')

        if cut_index > 0:
            writer = previous_writer.index('(')
        else:
            writer = previous_writer

        writer = reply.select('div.score_reple a > span')[0].text.strip()[:cut_index]
        grade = reply.select('div.star_score > em')[0].text.strip()
        review = reply.select('div.score_reple > p > span')

        if len(review) > 1:
            review = reply.select('div.score_reple > p > span')[0].text.strip() +\
                     " ) " +\
                     reply.select('div.score_reple > p > span')[1].text.strip()
        else:
            review = reply.select('div.score_reple > p > span')[0].text.strip()

        reg_dt = reply.select('div.score_reple em')[1].text.strip()[11:17]

        cnt += 1
        print('■■■■■■■■게시글{} ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■'.format(cnt))
        print('작성자: ', writer)
        print('평점: ', grade)
        print('리뷰: ', review)
        print('등록일: ', reg_dt)


        data = {'review': review,
                'write': writer,
                'grade': grade,
                'reg_dt': reg_dt}

        mDao.mongo_write(data)

    if page == page_cut:
        break

    page += 1

print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
print('네이버 영화 리뷰 총 {} 건을 수집하였습니다.'.format(cnt))
