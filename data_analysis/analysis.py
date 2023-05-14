import sys
import os
from collections import Counter
from konlpy.tag import *
import numpy as np
import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer
from PIL import Image
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt

mbti_key = ['ENFP', 'INFP', 'ESFP', 'ISFP',
            'ENTP', 'INTP', 'ENFJ', 'INFJ',
            'ESTP', 'ISTP', 'ESTJ', 'ISTJ',
            'ESFJ', 'ISFJ', 'ENTJ', 'INTJ']

# POS tag a sentence
data = pd.read_csv('data/naver_movie_story.csv')
df = pd.DataFrame(columns=[])

"""한글, 숫자, 영어 빼고 전부 제거"""
def sub_special(s):
  return re.sub(r'[^ㄱ-ㅎㅏ-ㅣ가-힣0-9a-zA-Z ]','',s)

STOP_WORDS = ['의','가','이','은','로','에게',
              '것','들','는','좀','잘','걍','과',
              '도','을','를','으로','자','에','와',
              '한','하다','되다','후','줄','에서',
              '에서는','에도','다','한다','된다',
              '있다','싶다','위해','로부터','않다','되어다']

def morph_and_stopword(s, freq):
  token_ls = []
  #형태소 분석
  s = sub_special(s)
  words = Okt().pos(s, norm=True, stem=True)
  tmp = [x for x, y in words if y in ['Noun', 'Verb', 'Adjective']]
  # tmp = Okt().nouns(s)
  # words = Kkma().pos(s)
  
  #불용어 처리
  for token in tmp:
    if token not in STOP_WORDS:
      token_ls.append(token)
  
  if freq:
    for i, v in enumerate(token_ls):
      if len(v)<2:
        token_ls.pop(i)
    
    count = Counter(token_ls)
    noun_list = count.most_common(300)
    return noun_list

  return token_ls


def withFreq(s):
  return sum(s, [])
  

def drawWordCloud(freq):
  for i in range(16):
    # mbti 별 top10 줄거리 가져오기
    mbti_movie = data['mbti'].str.contains(mbti_key[i])
    set_mbti = data[mbti_movie]
    top10 = set_mbti.nlargest(10, 'rating', keep='all')
    
    # top = top10.iloc[0]['image']
    # curl 요청
    # os.system("curl " + top + " > src/poster" + mbti_key[i] + ".jpg")
    # print(top)
    
    # 형태소 분석 및 count
    if freq:
      total_story = []
      for s in top10['story']:
        wordList = morph_and_stopword(s, freq)
        total_story.append(wordList)
    else:
      total_story = ''
      for s in top10['story']:
        wordList = morph_and_stopword(s, freq)
        total_story += ' '.join(wordList)
        total_story += ' '
    
    # faltten / tf-idf
    if (freq):
      words = withFreq(total_story)
    else:
      vectorizer = CountVectorizer(min_df=1)
      bow = vectorizer.fit_transform([total_story])
      
      transformer = TfidfTransformer()
      tfidf = transformer.fit_transform(bow.toarray())
      words = zip(vectorizer.get_feature_names(),tfidf.toarray()[0])
      # print(tfidf.shape)

    # draw wordcloud & save img
    img = Image.open('src/posterESFP.jpg')
    img = img.resize((2048, 2048))
    img_array = np.array(img)
    mask = Image.open('src/6.jpg')
    mask = mask.resize((2048, 2048))
    mask = np.array(mask)
    
    wordcloud = WordCloud(font_path=r'.\fonts\PoorStory-Regular.ttf', background_color='black', mask=mask)
    image = wordcloud.generate_from_frequencies(dict(words))
    image_colors = ImageColorGenerator(img_array)
    image.recolor(color_func=image_colors)
    image.to_image().save("img/wordcloud_" + mbti_key[i] + ".jpg")
    
    

if __name__ == '__main__':
  arguments = sys.argv
  
  # 단어 빈도수 이용
  if arguments[1] == '-f' or arguments[1] == '-F':
    drawWordCloud(True)
  # tf-idf 이용
  elif arguments[1] == '-t' or arguments[1] == '-T':
    drawWordCloud(False)
  else:
    print("두 가지 옵션 중 한 가지를 선택하여 실행해주세요. (-f | -t")