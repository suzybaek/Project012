import requests
import pprint
import json
import pandas as pd
import sqlite3
import re

url = 'http://api.koreafilm.or.kr/openapi-data2/wisenut/search_api/search_json2.jsp?collection=kmdb_new2&ServiceKey=3H0FW57G94948YJ89Z2G'
response = requests.get(url)
contents = response.text

title = [] ; plotText = []
r = requests.post(url, data={'title':title,'plotText':plotText})
pp = pprint.PrettyPrinter(indent=4)

print(pp.pprint(contents)) #contents 확인

json_ob = json.loads(contents)
print(type(json_ob)) #json타입 확인


data=r.json()
for h in data['Data'][0]['Result']:
    print(h['title'],h['plots'],h['posters']) #title , plots, posters 프린트


data3= []
for h in data['Data'][0]['Result']:
    data3.append((h['title'],h['plots'],h['posters'])) #data3 에 리스트 추가
print(data3)

title= []
for h in data['Data'][0]['Result']:
     title.append(h['title'])
print(title)

plots= []
for h in data['Data'][0]['Result']:
     plots.append(h['plots'])
print(plots)

title1= json.dumps(title,ensure_ascii=False)
plots1=json.dumps(plots,ensure_ascii=False)
data1=json.dumps(data3,ensure_ascii=False)


#title dataframe
realtitle=pd.DataFrame(title)
realtitle.rename(columns= {0:"title"}, inplace = True)
print(realtitle)

#특수문자제외 - plot 분리
def clean_text(inputString):
    text_rmv = re.sub('[-=+#/\?:^\{\}@*\"※~ㆍ!』‘|\(\)`\]\'…》\”\“\’·\,]', ' ', inputString)
    text_rmv = ' '.join(text_rmv.split())
    return text_rmv


#plot dataframe
cleanplot = clean_text(plots1)
import re
dat = re.sub("plot","",cleanplot)
dat1 = re.sub("Lang","",dat)
dat2 = re.sub("Text","",dat1)
dat3 = re.sub("한국어","",dat2)
dat4 = re.sub("영어","",dat3)
mydataframe= pd.DataFrame(dat4.split('['))
plotdata=mydataframe.shift(-2)
plotdata.rename(columns= {0:"plot"}, inplace = True)
print(plotdata)

#dataframe 결합
realmoviedata = pd.concat([realtitle,plotdata],axis=1)

realmoviedata.to_csv('data/kmdb_movie.csv')