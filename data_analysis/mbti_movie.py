import pandas as pd

data = pd.read_csv('data/mbti.csv', encoding='utf-8')
movieList = pd.read_csv('data/movie_list.csv', encoding='utf-8')
df = pd.DataFrame(columns=['mbti', 'movie'])
df.index.name = 'index'
df.reset_index()

# mbti_key = ['ENFP', 'INFP', 'ESFP', 'ISFP',
#             'ENTP', 'INTP', 'ENFJ', 'INFJ',
#             'ESTP', 'ISTP', 'ESTJ', 'ISTJ',
#             'ESFJ', 'ISFJ', 'ENTJ', 'INTJ']

idx = 0
for m in movieList['movie']:
    mbti = ''
    tmp = data[data['movie']==m]
    
    for i in range(len(tmp['role'])):
        mbti += tmp.iloc[i]['role'] + '(' + tmp.iloc[i]['mbti'] + ')'
        mbti += ','
    
    df.loc[idx] = [mbti, m]
    idx += 1

df.to_csv('data/mbti_movie.csv', encoding='utf-8')
df.to_json('data/mbti_movie.json', orient='table')