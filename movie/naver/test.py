import requests
from bs4 import BeautifulSoup

cnt = 0
page = 1
compare_writer = ''


url = 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=191436&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page=1'
resp = requests.get(url)

if resp.status_code != 200:
    print('존재하지 않는 URL')

soup = BeautifulSoup(resp.text, 'html.parser')
reply_list = soup.select('div.score_result li')

for i, reply in enumerate(reply_list):
    previous_writer = reply.select('div.score_reple a > span')[0].text.strip()
    cut_index = previous_writer.find('(')  # 작성자에 닉네임만 추출하기 위한 index번호 계산

    '''
    네이버 영화댓글의 작성자는 닉네임(아이디) 구조
    ex) 초롱이(cow****) -> 닉네임만 추출(그러나 닉네임이 없는 경우도 있음)
    닉네임이 없는 경우 ()안의 아이디를 사용하는 코드 작성
    '''
    if cut_index > 0:
        writer = previous_writer.index('(')
    else:
        writer = previous_writer

    writer = reply.select('div.score_reple a > span')[0].text.strip()[:cut_index]  # 작성자
    grade = reply.select('div.star_score > em')[0].text.strip()  # 평점
    review = reply.select('span#_filtered_ment_{}'.format(cnt))[0].text.strip()  # 내용

    ''' 방법 1
    for i, reply in enumerate(reply_list):
        review = reply.select('span#_filtered_ment_'+str(i))[0].text.strip()

        방법2 (추천)
    for reply in reply_list:
        review = reply.select('div.score_reple > p > span')
    '''

    reg_dt = reply.select('div.score_reple em')[1].text.strip()[:10]  # 작성일자

    '''
    네이버 영화 댓글 수집 페이지의 마지막 페이지를 계산하는 코드
    네이버는 1명의 작성자가 1개의 댓글만 작성할 수 있음
    매 페이지의 첫번쨰 게시글의 작성자를 compare_writer에 저장하고
    매 페이지의 첫번째 게시글 작성자와 compare_writer를 비교해서 비교해서 같으면 중복페이지 -> 수집종료
    '''
    if i == 0:
        if compare_writer == writer:
            print('Finished Collect:)')
            break
        else:
            compare_writer = writer

    cnt += 1

    print('작성자 : ', writer)
    print('평점 : ', grade)
    print('리뷰 : ', review)
    print('등록일 : ', reg_dt)
    print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
    print('총 {} 건의 리뷰를 수집하였습니다.'.format(cnt))
    print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
page += 1