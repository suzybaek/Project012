import requests
import pandas as pd
import search_query
import re

client_id = "mIi3pzvEmKNwGSH54RZS"
client_secret = "Gk_CbiaUFu"
df = pd.DataFrame(columns=['movie_index', 'code', 'mbti', 'title', 'subtitle', 'link', 'image', 'pubDate', 'director', 'actors', 'rating'])
movie_data = search_query.data
index = 0

def remove_html(sentence):
    sentence = re.sub('(<([^>]+)>)', '', sentence)
    return sentence

for j in range(len(movie_data['index'])):
# for j in range(50):
    mbti = movie_data['mbti'][j]
    movie_index = movie_data['index'][j]
    movie = movie_data['movie'][j]
    temp = movie.split('(')
    if len(temp) == 2:
        movie_year = movie.split('(')[1].rstrip(')').strip()
    else:
        movie_year = 'None'
    movie_title = movie.split('(')[0].strip()
    
    if movie_year.isdigit():
        yearfrom = movie_year
        yearto = movie_year
    else:
        yearfrom = 1900
        yearto = 2021

    header_params = {"X-Naver-Client-Id":client_id, "X-Naver-Client-Secret":client_secret}
    url = f"https://openapi.naver.com/v1/search/movie.json?query={movie_title}&yearfrom={yearfrom}&yearto={yearto}"
    res = requests.get(url, headers=header_params)
    data = res.json()
    
    if 'items' not in data:
        print(movie_index, movie, movie_title, yearfrom, yearto)
        continue

    for i in range(len(data['items'])):
        index += 1

        title = remove_html(data['items'][i]['title'])
        subtitle = remove_html(data['items'][i]['subtitle'])
        link = data['items'][i]['link']
        code = link.split('=')[1]
        image = data['items'][i]['image']
        date = data['items'][i]['pubDate']
        director = data['items'][i]['director'].split('|')[0]
        actors = data['items'][i]['actor'].split('|')[:-1]
        rating = float(data['items'][i]['userRating'])
        
        if image and date and director and actors and rating:
            if rating != 10.0 and rating != 0.0:
                df.loc[index] = [movie_index, code, mbti, title, subtitle, link, image, date, director, actors, rating]

        # # curl 요청
        # os.system("curl " + image + " > img/poster" +
        #           str(movie_index) + str(i) + ".jpg")

df.to_csv('data/naver_movie.csv', encoding='utf-8')
df.to_json('data/naver_movie.json', orient='table')