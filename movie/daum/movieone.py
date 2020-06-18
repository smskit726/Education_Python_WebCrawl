import requests
from bs4 import BeautifulSoup
import movie.persistence.MongoDAO as DAO

# 객체생성
mDao = DAO.MongoDAO()

cnt = 0
page = 1
while(True):
    url = 'https://movie.daum.net/moviedb/grade?movieId=126335&type=netizen&page={}'.format(page)

    resp = requests.get(url)
    soup = BeautifulSoup(resp.text,'html.parser')

    if resp.status_code != 200:
        print('WARNING : 잘못된 URL 접근')

    reply_list = soup.select('div.review_info')

    if len(reply_list)==0:
        print('마지막 페이지입니다.')
        print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
        break


    for reply in reply_list:
        cnt += 1
        writer = reply.select('em.link_profile')[0].text.strip()
        grade = reply.select('em.emph_grade')[0].text.strip()
        review = reply.select('p.desc_review')[0].text.strip()
        reg_dt = reply.select('span.info_append')[0].text.strip()#[:10]


        print('작성자 : ', writer)
        print('평점 : ', grade)
        print('리뷰 : ', review)
        print('등록일 : ', reg_dt)

        #
        index_val = reg_dt.index(',')
        print('등록일 : ', reg_dt[:index_val])

        print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')

        # MongoDB에 저장하기 위해 Dict Type으로 변환:
        data = {'review': review,
                'write': writer,
                'grade': grade,
                'reg_dt': reg_dt}

        # 내용, 작성자, 평점, 작성일자 MongoDB에 Save
        mDao.mongo_write(data)

    page+=1
print("수집한 영화댓글은 총 {}건입니다.".format(cnt))