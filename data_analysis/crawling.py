import re
import os
from random import randrange

import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlretrieve

data = pd.read_csv('data/naver_movie.csv', encoding='utf-8')
df = pd.DataFrame(columns=['movie_index', 'code', 'mbti', 'title', 'subtitle', 'genre', 'story', 'image', 'pubDate', 'director', 'actors', 'rating', 'rtime'])
genre_store = []
story_store = []
rtime_store = []

# 특수문자 제거 위한 함수
def cleanText(readData):
    # 텍스트에 포함되어 있는 특수 문자 제거
    text = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》 ]', '', readData)
    return text

def isNone(readData):
    if readData:
        data_str = ' '.join(readData)
    else:
        data_str = 'None'
        
    return data_str


def crawling():
    try:
        # HTML 파싱
        # 저장 된 영화와 포스터의 행을 맞추기 위한 정수 j
        j = 0
        # 네이버영화의 영화 코드 지정
        print(len(data['code']))
        for i in range(len(data['code'])):
        # for i in range(10):
            movie_code = str(data['code'][i])

            raw = requests.get("https://movie.naver.com/movie/bi/mi/basic.nhn?code=" + movie_code)
            html = bs(raw.text, 'html.parser')

            # 전체 컨테이너
            movie = html.select("div.article")

            # 영화 정보
            for a, m in enumerate(movie):

                # 영화 장르
                genre = m.select("dl.info_spec dd p span:nth-of-type(1) a")
                
                # 영화줄거리
                story = m.select("div.story_area p.con_tx")

                # 영화 상영시간
                rtime = m.select_one("dl.info_spec dd p span:nth-of-type(3)")

                genre_list = [g.text for g in genre]
                genre_str = isNone(genre_list)
                    
                story_list = [s.text for s in story]
                story_str = isNone(story_list)
                    
                if rtime:
                    rtime_str = rtime.text
                else:
                    rtime_str = 'None'
                    
            if story_str != 'None':
                df.loc[i] = [data['movie_index'][i], data['code'][i], data['mbti'][i], data['title'][i], data['subtitle'][i], genre_str, story_str, data['image'][i], data['pubDate'][i], data['director'][i], data['actors'][i], data['rating'][i], rtime_str]

            # print(len(data['code']), " 중 ", i, "번째")

    except Exception as ex:
        print("에러발생", ex)
    finally:
        print("완료")
    
    # data['genre'] = genre_store
    # data['story'] = story_store
    # data['runTime'] = rtime_store
    df.to_csv('data/naver_movie_story.csv', encoding='utf-8')
    df.to_json('data/naver_movie_story.json', orient='table')