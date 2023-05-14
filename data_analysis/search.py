import requests
import pprint
import json
import pandas as pd
import sqlite3
import dataname
import re
import moviedata
movie = pd.read_csv('data/movie.csv')


df = pd.DataFrame(columns=['title','plot'])
movie_data = dataname.data
kmdb_data = moviedata.realmoviedata

realreal = []
for i in range(len(kmdb_data['title'])):
    movie_title = movie_data['movie'][i]
    kmdb_title = kmdb_data['title'][i]
    plot = kmdb_data['plot'][i]
    if movie_title == kmdb_title :
        realreal.append(kmdb_data[i])

print(realreal)
hey = pd.DataFrame(realreal)
hey.to_csv('data/real_movie.csv')

